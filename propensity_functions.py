import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from propensity_constant import *

def demographics_characteristics(patient_file, demographics_file, output_file):
    # Read demographics file
    demographics = pd.read_csv(demographics_file)
    demographics.set_index('patient_id', inplace=True)

    # Read patient file
    patients = pd.read_csv(patient_file)
    patients = patients.dropna(subset=['first_kidney_transplant_date'])
    patients['first_kidney_transplant_date'] = pd.to_datetime(patients['first_kidney_transplant_date'].astype(int), format='%Y%m%d')


    # Open output file
    with open(output_file, 'w') as out:
        # Write header
        out.write('patient_id,male,hispanic,white,age_at_index\n')

        # Process each patient
        for _, row in patients.iterrows():
            patient_id = row['patient_id']
            first_kidney_transplant_date = row['first_kidney_transplant_date']

            # Get demographic data for this patient
            demo = demographics.loc[patient_id]

            # Calculate values
            if pd.isna(demo['sex']) or pd.isna(demo['year_of_birth']):
                continue

            male = 1 if demo['sex'] == 'M' else 0
            hispanic = 1 if demo['ethnicity'] == 'Hispanic or Latino' else 0
            white = 1 if demo['race'] == 'White' else 0
            
            # Calculate age at index
            birth_year = demo['year_of_birth']
            age_at_index = first_kidney_transplant_date.year - birth_year

            # Write to output file
            out.write(f'{patient_id},{male},{hispanic},{white},{age_at_index}\n')

    print(f"Written to {output_file}")

def diagnosis_characteristics(patient_file, diagnosis_file, output_file, chunksize=10000):
    # Read patient file
    patients = pd.read_csv(patient_file, usecols=['patient_id', 'first_kidney_transplant_date'])
    patients['first_kidney_transplant_date'] = pd.to_datetime(patients['first_kidney_transplant_date'], format='%Y%m%d')

    # Initialize result dataframe
    result = patients[['patient_id']].copy()
    for code_name in DIAGNOSIS_CODES.keys():
        result[code_name] = 0

    # Process diagnosis file in chunks
    for chunk in pd.read_csv(diagnosis_file, chunksize=chunksize):
        chunk['date'] = pd.to_datetime(chunk['date'], format='%Y%m%d')
        
        # Merge with patients and filter dates
        merged = pd.merge(chunk, patients, on='patient_id')
        merged = merged[
            (merged['date'] >= merged['first_kidney_transplant_date'] - timedelta(days=365)) &
            (merged['date'] < merged['first_kidney_transplant_date'])
        ]

        # Check for each diagnosis code
        for code_name, code_value in DIAGNOSIS_CODES.items():
            if isinstance(code_value, str):
                mask = merged['code'].str.startswith(code_value)
            else:  # Set of codes
                mask = merged['code'].str.startswith(tuple(code_value))
            
            diagnosed_patients = merged[mask]['patient_id'].unique()
            result.loc[result['patient_id'].isin(diagnosed_patients), code_name] = 1

    # Write results to output file
    result.to_csv(output_file, index=False)
    print(f"Written to {output_file}")

def medication_characteristics(patient_file, medication_file, output_file, chunksize=10000):
    # Read patient file
    patients = pd.read_csv(patient_file, usecols=['patient_id', 'first_kidney_transplant_date'])
    patients['first_kidney_transplant_date'] = pd.to_datetime(patients['first_kidney_transplant_date'], format='%Y%m%d')

    # Initialize result dataframe
    result = patients[['patient_id']].copy()
    for med_group in MEDICATION_CODES.keys():
        result[med_group] = 0

    # Process medication file in chunks
    for chunk in pd.read_csv(medication_file, chunksize=chunksize):
        chunk['start_date'] = pd.to_datetime(chunk['start_date'], format='%Y%m%d')
        
        # Merge with patients and filter dates
        merged = pd.merge(chunk, patients, on='patient_id')
        merged = merged[
            (merged['start_date'] >= merged['first_kidney_transplant_date'] - timedelta(days=365)) &
            (merged['start_date'] < merged['first_kidney_transplant_date'])
        ]

        # Check for each medication group
        for med_group, codes in MEDICATION_CODES.items():
            mask = merged['code'].isin(codes)
            prescribed_patients = merged[mask]['patient_id'].unique()
            result.loc[result['patient_id'].isin(prescribed_patients), med_group] = 1

    # Write results to output file
    result.to_csv(output_file, index=False)
    print(f"Written to {output_file}")

def lab_results_characteristics(patient_file, lab_result_file, vital_sign_lab, output_file, chunksize=10000):
    PERCENTILE_RANGES = {
        'blood_pressure_diastolic': (19, 113),
        'blood_pressure_systolic': (37, 193),
        'body_mass_index': (17, 45.0268),
        'potassium': (3, 6.1),
        'sodium': (126, 147),
        'triglyceride': (40, 603),
        'cholesterol_hdl': (2.7, 111),
        'hemoglobin_a1c': (4.3, 13.1),
        'alanine_aminotransferase': (5, 500),
        'aspartate_aminotransferase': (8, 511),
        'bilirubin_total': (0.2, 17.6),
        'natriuretic_peptide_b': (8, 17098.76),
        'glomerular_filtration_rate': (1.1008, 135.6007)
    }
    
    # Read patient file
    patients = pd.read_csv(patient_file, usecols=['patient_id', 'first_kidney_transplant_date'])
    patients['first_kidney_transplant_date'] = pd.to_datetime(patients['first_kidney_transplant_date'], format='%Y%m%d')

    # Initialize result dataframe
    result = patients.set_index('patient_id')[['first_kidney_transplant_date']].copy()
    for lab_code in LAB_RESULT_CODES.keys():
        result[lab_code] = -1.0 

    # Process lab result file in chunks
    for chunk in pd.read_csv(lab_result_file, chunksize=chunksize):
        chunk['date'] = pd.to_datetime(chunk['date'], format='%Y%m%d')
        chunk = chunk.dropna(subset=['lab_result_num_val'])

        # Merge with patients and filter dates
        merged = pd.merge(chunk, patients, on='patient_id')
        merged = merged[
            (merged['date'] >= merged['first_kidney_transplant_date'] - timedelta(days=365)) &
            (merged['date'] < merged['first_kidney_transplant_date']) 
        ]

        # Check for each lab result  
        for lab_group, codes in LAB_RESULT_CODES.items():
            mask = merged['code'].isin(codes)
            filtered_merged = merged[mask]

            low, high = PERCENTILE_RANGES[lab_group]
            filtered_merged = filtered_merged[
                (filtered_merged['lab_result_num_val'].astype(float) >= low) &
                (filtered_merged['lab_result_num_val'].astype(float) <= high)
            ]
            
            latest_results = filtered_merged.sort_values('date', ascending=False).drop_duplicates('patient_id', keep='first')
            if not latest_results.empty:
                result.loc[latest_results['patient_id'], lab_group] = latest_results['lab_result_num_val'].astype(float).values[0]
    
    # Process vital sign lab file in chunks
    for chunk in pd.read_csv(vital_sign_lab, chunksize=chunksize):
        chunk['date'] = pd.to_datetime(chunk['date'], format='%Y%m%d')
        chunk = chunk.dropna(subset=['value'])

        # Merge with patients and filter dates
        merged = pd.merge(chunk, patients, on='patient_id')
        merged = merged[
            (merged['date'] >= merged['first_kidney_transplant_date'] - timedelta(days=365)) &
            (merged['date'] < merged['first_kidney_transplant_date'])
        ]

        # Check for each vital sign result  
        for lab_group, codes in LAB_RESULT_CODES.items():
            mask = merged['code'].isin(codes)
            filtered_merged = merged[mask]

            low, high = PERCENTILE_RANGES[lab_group]
            filtered_merged = filtered_merged[
                (filtered_merged['value'].astype(float) >= low) &
                (filtered_merged['value'].astype(float) <= high)
            ]

            latest_results = filtered_merged.sort_values('date', ascending=False).drop_duplicates('patient_id', keep='first')
            if not latest_results.empty:
                result.loc[latest_results['patient_id'], lab_group] = latest_results['value'].astype(float).values[0]

    # Reset index and write results to output file
    result = result.reset_index().drop(columns=['first_kidney_transplant_date'])
    result.to_csv(output_file, index=False)
    print(f"Written to {output_file}")

def generate_propensity_score(filename, output_file):
    # Load the data
    df = pd.read_csv(filename)

    # Separate the target variable and features
    X = df.drop(['patient_id', 'user'], axis=1)  # Features
    y = df['user']  # Target variable

    # Fit a logistic regression model to estimate propensity scores
    model = LogisticRegression(max_iter=10000)
    model.fit(X, y)

    # Print covariate weights (added section)
    print("\nCovariate Weights:")
    weights = pd.DataFrame({
        'Feature': X.columns,
        'Weight': model.coef_[0]
    }).sort_values(by='Weight', ascending=False)
    print(weights.to_string(index=False))


    print("\nOdds Ratio:")
    weights = pd.DataFrame({
        'Feature': X.columns,
        'Weight': np.exp(model.coef_[0])
    }).sort_values(by='Weight', ascending=False)
    print(weights.to_string(index=False))

    # Predict propensity scores
    propensity_scores = model.predict_proba(X)[:, 1]

    # Create a new DataFrame with the results
    result_df = pd.DataFrame({
        'patient_id': df['patient_id'],
        'user': df['user'],
        'propensity_score': propensity_scores
    })

    # Save the results to the output directory
    result_df.to_csv(output_file, index=False)
    print(f"Written to {output_file}")

def propensity_score_matching(users_file, matches_file, propensity_scores_file, output_file, caliper_limit=0.05):
    # Load users data
    users_data = pd.read_csv(users_file)
    users_data['first_glp1_date'] = pd.to_datetime(users_data['first_glp1_date'], format='%Y%m%d')

    # Load matches data
    matches_data = pd.read_csv(matches_file)
    matches_data['matched_nonuser_patient_ids'] = matches_data['matched_nonuser_patient_ids'].astype(str)

    # Load propensity scores data
    propensity_scores = pd.read_csv(propensity_scores_file)

    # Initialize output list
    matched_ids = []
    used_nonusers = set()  # Keep track of used nonusers

    # Iterate over each user in matches_data
    for index, row in matches_data.iterrows():
        user_patient_id = row['user_patient_id']
        matched_nonuser_patient_ids = row['matched_nonuser_patient_ids'].split(',')

        # Find the user's row in users_data
        user_row = users_data[users_data['patient_id'] == user_patient_id]
        if user_row.empty:
            print(f"No user row found for {user_patient_id}. Skipping...")
            continue

        first_glp1_date = user_row['first_glp1_date'].dt.strftime('%Y%m%d').values[0]

        # Find the user's row in propensity_scores_file
        user_row = propensity_scores[(propensity_scores['patient_id'] == user_patient_id) & (propensity_scores['user'] == 1)]
        if user_row.empty:
            print(f"No user row found for {user_patient_id} in propensity scores. Skipping...")
            continue

        user_score = user_row['propensity_score'].values[0]

        # Filter non-users data to exclude used matches and ensure user value is 0
        eligible_nonusers = propensity_scores[propensity_scores['user'] == 0]
        available_nonusers = eligible_nonusers[~eligible_nonusers['patient_id'].isin(used_nonusers)]

        # Filter available nonusers based on matched_nonuser_patient_ids
        available_nonusers = available_nonusers[available_nonusers['patient_id'].isin(matched_nonuser_patient_ids)]

        # Apply caliper limit if specified
        if caliper_limit is not None:
            available_nonusers = available_nonusers[(available_nonusers['propensity_score'] - user_score).abs() <= caliper_limit]

        if available_nonusers.empty:
            print(f"No available nonusers for {user_patient_id}. Skipping...")
            continue

        # Find the closest propensity score among available nonusers
        closest_match = available_nonusers.loc[available_nonusers['propensity_score'].sub(user_score).abs().idxmin()]
        matched_id = closest_match['patient_id']
        matched_score = closest_match['propensity_score']

        # Add the matched ID to the used set
        used_nonusers.add(matched_id)

        # Append the matched ID and its propensity score to the output list
        matched_ids.append({
            'patient_id': user_patient_id,
            'user': 1,
            'propensity_score': user_score,
            'first_glp1_date': first_glp1_date
        })

        # Also add the matched nonuser to the output list
        matched_ids.append({
            'patient_id': matched_id,
            'user': 0,
            'propensity_score': matched_score,
            'first_glp1_date': first_glp1_date
        })

        print(user_patient_id, matched_id)

    # Save the matched IDs to the output file
    matched_df = pd.DataFrame(matched_ids)
    matched_df.to_csv(output_file, index=False)
    print(f"Written to {output_file}")

