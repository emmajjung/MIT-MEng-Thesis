import pandas as pd
from datetime import datetime, timedelta
import numpy as np
from lifelines import KaplanMeierFitter
from lifelines import CoxPHFitter

from outcome_constant import * 
import warnings

# Suppress FutureWarning about downcasting
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('future.no_silent_downcasting', True)

def prior_outcomes(patient_file, demographics_file, diagnosis_file,
procedure_file, medication_file, lab_result_file, output_file, column, chunksize=10000, lab_value=14.00):
    # Read patient file
    patients = pd.read_csv(patient_file, usecols=['patient_id', column]) 
    patients[column] = pd.to_datetime(patients[column], format='%Y%m%d')
    patient_ids = set(patients['patient_id'])
        
    # Merge with demographics for death date (optional)
    demographics = pd.read_csv(demographics_file)
    demographics['month_year_death'] = pd.to_datetime(demographics['month_year_death'], format='%Y%m')
    merged = patients.merge(demographics[['patient_id', 'month_year_death']], on='patient_id', how='left')

    # Initialize output dataframe
    output = patients[['patient_id']].copy()

    for outcome, criteria in OUTCOME_CODES.items():
        print(outcome)
        
        output[outcome] = 0

        # Check for death within timeframe (if applicable)
        if 'Demographics' in criteria and 'Deceased' in criteria['Demographics']:
            mask = (merged[column] > merged['month_year_death'])
            output.loc[output['patient_id'].isin(merged.loc[mask,'patient_id']), outcome] = 1
        
        for file, key in [(diagnosis_file, 'Diagnosis'), (procedure_file, 'Procedure'), (lab_result_file, 'Laboratory')]:

            if key not in criteria:
                continue

            for chunk in pd.read_csv(file, chunksize=chunksize):
                chunk['date'] = pd.to_datetime(chunk['date'], format='%Y%m%d')

                merged_chunk = patients.merge(chunk, on='patient_id', how='left')

                if key == 'Diagnosis':
                    code_mask = merged_chunk['code'].str.startswith(tuple(criteria[key]))
                elif key == 'Procedure':
                    code_mask = merged_chunk['code'].isin(criteria[key])
                else:  # Laboratory
                    code_mask = (merged_chunk['code'].isin(criteria[key])) & (merged_chunk['lab_result_num_val'] <= lab_value)
                  
                mask = (merged_chunk[column] > merged_chunk['date'])
                code_mask = (mask) & (code_mask.fillna(False).infer_objects(copy=False))
                
                # Update output based on the mask
                for idx in merged_chunk.loc[code_mask, 'patient_id']:
                    output.loc[output['patient_id'] == idx, outcome] = 1

    # Write output file
    output.to_csv(output_file, index=False)
    print(f"Written to {output_file}")

def days_to_outcome(patient_file, demographics_file, diagnosis_file, procedure_file, medication_file, lab_result_file, output_file, outcome_type=0, chunksize=10000, lab_value=14.00):
    # Read patient file
    patients = pd.read_csv(patient_file, usecols=['patient_id', 'first_glp1_date', 'most_recent_date'])
    patients['first_glp1_date'] = pd.to_datetime(patients['first_glp1_date'], format='%Y%m%d')
    patients['most_recent_date'] = pd.to_datetime(patients['most_recent_date'], format='%Y%m%d')
    patient_ids = set(patients['patient_id'])
        
    # Merge with demographics for death date (optional)
    demographics = pd.read_csv(demographics_file)
    demographics['month_year_death'] = pd.to_datetime(demographics['month_year_death'], format='%Y%m')
    merged = patients.merge(demographics[['patient_id', 'month_year_death']], on='patient_id', how='left')

    # Initialize output dataframe
    output = patients[['patient_id']].copy()

    # Initialize a dictionary to store the most recent date for each patient
    most_recent_dates = {}
    for index, row in patients.iterrows():
        most_recent_dates[row['patient_id']] = row['most_recent_date']

    codes = OUTCOME_CODES
    if outcome_type == 1:
        codes = MACE_OUTCOME_CODES
    elif outcome_type == 2:
        codes = OTHER_OUTCOME_CODES

    for outcome, criteria in codes.items():
        seen = set()
        print(outcome)
        
        # Initialize outcome and days_to columns
        output[outcome] = 0
        output[f"days_to_{outcome}"] = (patients['most_recent_date'] - patients['first_glp1_date']).dt.days + 1

        # Check for death within timeframe (if applicable)
        if 'Demographics' in criteria and 'Deceased' in criteria['Demographics']:
            mask = (merged['first_glp1_date'] <= merged['month_year_death'])
            output.loc[output['patient_id'].isin(merged.loc[mask,'patient_id']), outcome] = 1
            output.loc[output['patient_id'].isin(merged.loc[mask, 'patient_id']), f"days_to_{outcome}"] = (merged.loc[mask, 'month_year_death'] - merged.loc[mask, 'first_glp1_date']).dt.days + 1
        
        for file, key in [(diagnosis_file, 'Diagnosis'), (procedure_file, 'Procedure'), (lab_result_file, 'Laboratory')]:

            if key not in criteria:
                continue

            for chunk in pd.read_csv(file, chunksize=chunksize):
                chunk['date'] = pd.to_datetime(chunk['date'], format='%Y%m%d')

                merged_chunk = patients.merge(chunk, on='patient_id', how='left')

                if key == 'Diagnosis':
                    code_mask = merged_chunk['code'].str.startswith(tuple(criteria[key]))
                elif key == 'Procedure':
                    code_mask = merged_chunk['code'].isin(criteria[key])
                else:  # Laboratory
                    code_mask = (merged_chunk['code'].isin(criteria[key])) & (merged_chunk['lab_result_num_val'] <= lab_value)
                  
                mask = (merged_chunk['first_glp1_date'] <= merged_chunk['date'])
                code_mask = (mask) & (code_mask.fillna(False).infer_objects(copy=False))
                merged_chunk.loc[code_mask, 'days'] = (merged_chunk.loc[code_mask, 'date'] - merged_chunk.loc[code_mask, 'first_glp1_date']).dt.days + 1

                merged_min = merged_chunk.groupby('patient_id')['days'].min()

                output_subset = output.set_index('patient_id')
                common_index = merged_min.index.intersection(output_subset.index)

                # Ensure both Series are indexed on common_index without duplicates
                merged_min_aligned = merged_min.loc[common_index]
                # Remove duplicates from output_subset_aligned by taking the first value for each index
                output_subset_aligned = output_subset.loc[common_index, f"days_to_{outcome}"].drop_duplicates()

                # Ensure alignment by merging on the index
                aligned_data = pd.merge(
                    merged_min_aligned.to_frame('min_days'),
                    output_subset_aligned.to_frame(f"days_to_{outcome}"),
                    left_index=True,
                    right_index=True,
                    how='inner'
                )

                # Perform comparison on aligned data
                mask = (aligned_data['min_days'].notna()) & (aligned_data[f"days_to_{outcome}"].isna() | (aligned_data['min_days'] < aligned_data[f"days_to_{outcome}"]))

                # Update output_subset based on the mask
                for idx in aligned_data.index[mask]:
                    output_subset.loc[idx, f"days_to_{outcome}"] = merged_min.loc[idx]
                    output_subset.loc[idx, outcome] = 1
                    seen.add(idx)

                output = output_subset.reset_index()

        # Update days_to_outcome if no valid instance
        for patient_id in patients['patient_id']:
            if patient_id in seen:
                continue

            if most_recent_dates.get(patient_id) and pd.isna(output.loc[output['patient_id'] == patient_id, f"days_to_{outcome}"].values[0]):
                if output.loc[output['patient_id'] == patient_id, {outcome}.values[0]] == 0: 
                    output.loc[output['patient_id'] == patient_id, f"days_to_{outcome}"] = (most_recent_dates[patient_id] - patients.loc[patients['patient_id'] == patient_id, 'first_glp1_date'].values[0]).days + 1

    # Write output file
    output.to_csv(output_file, index=False)
    print(f"Written to {output_file}")

def calculate_survival_probabilities(outcome_file, output_file):
    # Read CSV files into DataFrames
    users = pd.read_csv(outcome_file)

    # Create a dictionary to store survival probabilities for each outcome
    survival_probabilities_dict = {}

    for outcome in MACE_OUTCOME_CODES.keys():
        try:
            # Extract relevant columns for the current outcome
            users_outcome = users[['patient_id', f"{outcome}", f"days_to_{outcome}"]]

            # Fit Kaplan-Meier models
            kmf_users = KaplanMeierFitter()
            
            kmf_users.fit(users_outcome[f"days_to_{outcome}"], event_observed=users_outcome[f"{outcome}"])
            
            # Get survival probabilities at specific time points
            time_points = np.arange(1, max(users_outcome[f"days_to_{outcome}"])+ 1)
            
            survival_users = kmf_users.predict(time_points)
            
            # Store survival probabilities in the dictionary
            survival_probabilities_dict[outcome] = pd.DataFrame({
                'Time': time_points,
                'Survival Probability': survival_users
            })

        except:
            print(f'skip {outcome}')

    # Write survival probabilities for each outcome to separate CSV files
    for outcome, df in survival_probabilities_dict.items():
        df.to_csv(f"{outcome}_{output_file}", index=False)
        print(f"Survival probabilities for {outcome} written to {outcome}_{output_file}")


def calculate_hazard_ratios(user_days_to_outcome_file, nonusers_days_to_outcome_file, output_file, outcome_type=0, adjusted=False, days=None):
    # Read CSV files into DataFrames
    users = pd.read_csv(user_days_to_outcome_file)
    nonusers = pd.read_csv(nonusers_days_to_outcome_file)

    # Create a dictionary to store hazard ratios for each outcome
    hazard_ratios_dict = {}

    codes = OUTCOME_CODES
    if outcome_type == 1:
        codes = MACE_OUTCOME_CODES
    elif outcome_type == 2:
        codes = OTHER_OUTCOME_CODES

    for outcome in codes.keys():
        try:
            if outcome not in users.columns or outcome not in nonusers.columns:
                continue

            # Extract relevant columns for the current outcome
            cols = ['patient_id', f"{outcome}", f"days_to_{outcome}"]
            if adjusted:
                cols.append('propensity_score')

            users_outcome = users[cols]
            nonusers_outcome = nonusers[cols]
            if days is not None:
                users_outcome.loc[users_outcome[f"days_to_{outcome}"] > days, outcome] = 0
                nonusers_outcome.loc[nonusers_outcome[f"days_to_{outcome}"] >  days, outcome] = 0

            # Combine users and nonusers into a single DataFrame
            combined = pd.concat([users_outcome, nonusers_outcome], ignore_index=True)

            # Add a column to indicate whether the patient is a user or nonuser
            combined['user'] = np.where(combined.index < len(users_outcome), 1, 0)

            if adjusted:
                combined['log_propensity'] = np.log(combined['propensity_score'])

            model_columns = ['user', f"days_to_{outcome}", f"{outcome}"]
            if adjusted:
                model_columns.insert(1, 'log_propensity')  # Insert after 'user'

            # Fit Cox proportional hazards model
            cph = CoxPHFitter()
            cph.fit(combined[model_columns],
                    duration_col=f"days_to_{outcome}",
                    event_col=f"{outcome}")
            

            # Get hazard ratio
            hazard_ratio = cph.summary.loc['user', 'exp(coef)']
            lower_95 = cph.summary.loc['user', 'exp(coef) lower 95%']
            upper_95 = cph.summary.loc['user', 'exp(coef) upper 95%']
            p_value = cph.summary.loc['user', 'p']

            # Store hazard ratio in the dictionary
            hazard_ratios_dict[outcome] = {
              'hazard_ratio': hazard_ratio,
              'lower_95': lower_95,
              'upper_95': upper_95,
              'p_value': p_value
            }

        except:
            print(f'Cannot {outcome}')

    # Write hazard ratios to a CSV file
    hazard_ratios_df = pd.DataFrame({
        'Outcome': list(hazard_ratios_dict.keys()),
        'Hazard Ratio': [v['hazard_ratio'] for v in hazard_ratios_dict.values()],
        'Lower 95% CI': [v['lower_95'] for v in hazard_ratios_dict.values()],
        'Upper 95% CI': [v['upper_95'] for v in hazard_ratios_dict.values()],
        'P-Value': [v['p_value'] for v in hazard_ratios_dict.values()]
    })
    hazard_ratios_df.to_csv(output_file, index=False)
    print(f"Hazard ratios written to {output_file}")

