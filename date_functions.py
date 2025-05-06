import csv
from datetime import timedelta
import pandas as pd

from constant import *

def find_earliest_transplant(patient_file, diagnosis_file, procedure_file, output_file, chunksize=10000):
    # Read patient IDs
    patient_ids = set(pd.read_csv(patient_file)['patient_id'])

    # Initialize dictionary to store earliest transplant dates
    earliest_transplants = {pid: None for pid in patient_ids}

    # Process diagnosis file
    for chunk in pd.read_csv(diagnosis_file, chunksize=chunksize):
        chunk['date'] = pd.to_datetime(chunk['date'], format='%Y%m%d')
        for _, row in chunk[chunk['patient_id'].isin(patient_ids)].iterrows():
            if row['code'] in KIDNEY_TRANSPLANT_DIAGNOSIS_CODES:
                if earliest_transplants[row['patient_id']] is None or row['date'] < earliest_transplants[row['patient_id']]:
                    earliest_transplants[row['patient_id']] = row['date']

    # Process procedure file
    for chunk in pd.read_csv(procedure_file, chunksize=chunksize):
        chunk['date'] = pd.to_datetime(chunk['date'], format='%Y%m%d')
        for _, row in chunk[chunk['patient_id'].isin(patient_ids)].iterrows():
            if row['code'] in KIDNEY_TRANSPLANT_PROCEDURE_CODES:
                if earliest_transplants[row['patient_id']] is None or row['date'] < earliest_transplants[row['patient_id']]:
                    earliest_transplants[row['patient_id']] = row['date']

    # Write results to output file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['patient_id', 'first_kidney_transplant_date'])
        for patient_id, transplant_date in earliest_transplants.items():
            if transplant_date:
                writer.writerow([patient_id, transplant_date.strftime('%Y%m%d')]) 
    
    print(f"Output written to {output_file}")

def find_earliest_medication(patient_file, medication_file, output_file, chunksize=10000):
    # Read patient IDs
    patient_df = pd.read_csv(patient_file)
    patient_ids = set(patient_df['patient_id'])

    # Initialize dictionary to store earliest medication dates
    earliest_medication = {}

    included = set()

    # Process medication file
    for chunk in pd.read_csv(medication_file, chunksize=chunksize):
        # Filter relevant rows
        mask = (chunk['patient_id'].isin(patient_ids)) & (chunk['code'].isin(MEDICATION_CODES))
        relevant_chunk = chunk[mask].copy()

        # Convert date
        relevant_chunk['date'] = pd.to_datetime(relevant_chunk['start_date'], format='%Y%m%d')

        # Group by patient_id and find the earliest date
        chunk_earliest = relevant_chunk.groupby('patient_id')['date'].min()

        # Update earliest_medication
        for pid, date in chunk_earliest.items():
            if pid not in earliest_medication or date < earliest_medication[pid]:
                earliest_medication[pid] = date
                included.add(pid)

    patient_df= patient_df[patient_df['patient_id'].isin(included)]
    # Add first_glp1_date to patient_df
    patient_df['first_glp1_date'] = patient_df['patient_id'].map(lambda x: earliest_medication.get(x).strftime('%Y%m%d') if x in earliest_medication else '')

    # Write results to output file
    patient_df.to_csv(output_file, index=False)
    print(f"Output written to {output_file}")

def find_day_difference(patient_file):
    # Read the patient file into a DataFrame
    df = pd.read_csv(patient_file)

    # Convert the date columns to datetime objects
    df['first_kidney_transplant_date'] = pd.to_datetime(df['first_kidney_transplant_date'], format='%Y%m%d')
    df['first_glp1_date'] = pd.to_datetime(df['first_glp1_date'], format='%Y%m%d')

    # Calculate the difference in days and add a new column
    df['day_difference'] = (df['first_glp1_date'] - df['first_kidney_transplant_date']).dt.days
    df['first_kidney_transplant_date'] = df['first_kidney_transplant_date'].dt.strftime('%Y%m%d')
    df['first_glp1_date'] = df['first_glp1_date'].dt.strftime('%Y%m%d')

    # Save the modified DataFrame back to the same file
    df.to_csv(patient_file, index=False)
    print(f"Output written to {patient_file}")

def latest_date(patient_file, diagnosis_file, procedure_file, medication_file, lab_result_file, output_file, chunksize=10000):
    # Read patient file
    patients = pd.read_csv(patient_file) 
    patient_ids = set(patients['patient_id'])
        
    # Initialize a dictionary to store the most recent date for each patient
    most_recent_dates = {}
    
    for file, key in [(diagnosis_file, 'Diagnosis'), (medication_file, 'Medication'), (procedure_file, 'Procedure'), (lab_result_file, 'Laboratory')]:
        print(key)
        for chunk in pd.read_csv(file, chunksize=chunksize):
            if key == 'Medication':
                chunk['date'] = pd.to_datetime(chunk['start_date'], format='%Y%m%d')
            else:
                chunk['date'] = pd.to_datetime(chunk['date'], format='%Y%m%d')
            
            # Update most recent dates
            for index, row in chunk.iterrows():
                if row['patient_id'] not in most_recent_dates or row['date'] > most_recent_dates[row['patient_id']]:
                    most_recent_dates[row['patient_id']] = row['date']

        
    # Write output file
    output = pd.DataFrame(list(most_recent_dates.items()), columns=['patient_id', 'most_recent_date'])

    merged_df = pd.merge(patients, output[['patient_id', 'most_recent_date']], on='patient_id', how='left')
    merged_df['most_recent_date'] = merged_df['most_recent_date'].dt.strftime('%Y%m%d')

    merged_df[['patient_id', 'most_recent_date']].to_csv(output_file, index=False)
    print(f"Written to {output_file}")

