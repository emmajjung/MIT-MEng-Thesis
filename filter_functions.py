import csv
from datetime import timedelta
import pandas as pd

def exclude_dead_patients(patient_file, demographics_file, most_recent_file, output_file, user=True):
    # Read patient file
    patients_df = pd.read_csv(patient_file)
    patients_df['first_kidney_transplant_date'] = pd.to_datetime(patients_df['first_kidney_transplant_date'], format='%Y%m%d')
    if user:
        patients_df['first_glp1_date'] = pd.to_datetime(patients_df['first_glp1_date'], format='%Y%m%d')
    patients_df = pd.read_csv(patient_file)
    patients_df['first_kidney_transplant_date'] = pd.to_datetime(patients_df['first_kidney_transplant_date'], format='%Y%m%d')

    # Read demographics file
    demographics_df = pd.read_csv(demographics_file)
    demographics_df['month_year_death'] = pd.to_datetime(demographics_df['month_year_death'], format='%Y%m', errors='coerce')
    
    most_recent_df = pd.read_csv(most_recent_file)
    most_recent_df['most_recent_date'] = pd.to_datetime(most_recent_df['most_recent_date'], format='%Y%m%d', errors='coerce')

    # Merge patients_df with demographics_df
    merged = pd.merge(patients_df, demographics_df[['patient_id', 'month_year_death']], on='patient_id', how='left')

    merged = pd.merge(merged, most_recent_df[['patient_id', 'most_recent_date']], on='patient_id', how='left')

    # Identify patients to exclude
    to_exclude = merged[
        ((merged['month_year_death'].notna()) &
        ((merged['month_year_death'] < merged['first_kidney_transplant_date'])
        | (merged['month_year_death'] <= merged['first_kidney_transplant_date'] + pd.Timedelta(days=90))
        | (merged['month_year_death'] + pd.Timedelta(days=31) < merged['most_recent_date'])))
    ]['patient_id']

    # Filter out excluded patients
    patients_df_filtered = merged[~merged['patient_id'].isin(to_exclude)]

    patients_df_filtered['first_kidney_transplant_date'] = patients_df_filtered['first_kidney_transplant_date'].dt.strftime('%Y%m%d')
    patients_df_filtered['month_year_death'] = patients_df_filtered['month_year_death'].dt.strftime('%Y%m')
    patients_df_filtered['most_recent_date'] = patients_df_filtered['most_recent_date'].dt.strftime('%Y%m%d')

    if user:
        patients_df_filtered['first_glp1_date'] = pd.to_datetime(patients_df_filtered['first_glp1_date'], format='%Y%m%d')
        patients_df_filtered['first_glp1_date'] = patients_df_filtered['first_glp1_date'].dt.strftime('%Y%m%d')

    # Write the filtered dataframe to the output file
    patients_df_filtered.to_csv(output_file, index=False)

    print(f"Excluded {len(to_exclude)} patients. Remaining patients: {len(patients_df_filtered)}")

