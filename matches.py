import pandas as pd
import csv
from datetime import datetime

def match_based_on_date(users_file, nonusers_file, output_file, days):
    # Read the users and nonusers files
    users_df = pd.read_csv(users_file)
    nonusers_df = pd.read_csv(nonusers_file)

    # Convert date columns to datetime format
    users_df['first_kidney_transplant_date'] = pd.to_datetime(users_df['first_kidney_transplant_date'], format='%Y%m%d')
    users_df['first_glp1_date'] = pd.to_datetime(users_df['first_glp1_date'], format='%Y%m%d')

    nonusers_df['first_kidney_transplant_date'] = pd.to_datetime(nonusers_df['first_kidney_transplant_date'], format='%Y%m%d')
    nonusers_df['most_recent_date'] = pd.to_datetime(nonusers_df['most_recent_date'], format='%Y%m%d')
    nonusers_df['month_year_death'] = pd.to_datetime(nonusers_df['month_year_death'], format='%Y%m', errors='coerce')

    # Initialize an empty list to store the matches
    matches = []

    # Iterate over each user
    for index, user in users_df.iterrows():
        matched_nonusers = []

        # Iterate over each nonuser
        for _, nonuser in nonusers_df.iterrows():
            # Check if the nonuser's transplant date is within the specified range
            if (user['first_kidney_transplant_date'] - pd.Timedelta(days=days)) <= nonuser['first_kidney_transplant_date'] <= (user['first_kidney_transplant_date'] + pd.Timedelta(days=days)):
                # Check if the nonuser's death date is after the user's first GLP1 date or if death date is missing
                if pd.isnull(nonuser['month_year_death']) or nonuser['month_year_death'] > user['first_glp1_date']:
                    # Check if nonsuser most recent date is after user first GLP1 date 
                    if user['first_glp1_date'] <= nonuser['most_recent_date']:
                        matched_nonusers.append(nonuser['patient_id'])

        # Append the user and their matches to the list
        # print(user['patient_id'], matched_nonusers)
        matches.append({
            'user_patient_id': user['patient_id'],
            'matched_nonuser_patient_ids': ','.join(map(str, matched_nonusers))
        })

        print(user['patient_id'], len(matched_nonusers))

    # Convert the matches list to a DataFrame and write it to the output file
    matches_df = pd.DataFrame(matches)
    matches_df.to_csv(output_file, index=False)

def generate_nonuser_file(matched_file, user_file, nonuser_file, output_file):
    # Load the files into DataFrames
    matched_df = pd.read_csv(matched_file)
    user_df = pd.read_csv(user_file)
    user_df['first_glp1_date'] = pd.to_datetime(user_df['first_glp1_date'], format='%Y%m%d')

    nonuser_df = pd.read_csv(nonuser_file)
    nonuser_df['first_kidney_transplant_date'] = pd.to_datetime(nonuser_df['first_kidney_transplant_date'], format='%Y%m%d')
    nonuser_df['most_recent_date'] = pd.to_datetime(nonuser_df['most_recent_date'], format='%Y%m%d')

    # Merge matched_df with user_df to get first_glp1_date
    merged_user_df = pd.merge(matched_df[['user_id', 'matched_id']], user_df[['patient_id', 'first_glp1_date']], left_on='user_id', right_on='patient_id', how='left')
    
    # Merge merged_user_df with nonuser_df to get first_kidney_transplant_date and most_recent_date
    merged_df = pd.merge(merged_user_df, nonuser_df[['patient_id', 'first_kidney_transplant_date', 'most_recent_date']], left_on='matched_id', right_on='patient_id', how='left')

    # Rename columns to match output requirements
    merged_df = merged_df.rename(columns={'matched_id': 'patient_id', 'first_glp1_date': 'first_glp1_date', 'first_kidney_transplant_date': 'first_kidney_transplant_date', 'most_recent_date': 'most_recent_date'})

    # Select required columns for output
    output_df = merged_df[['patient_id', 'first_kidney_transplant_date', 'first_glp1_date', 'most_recent_date']]
    output_df['first_kidney_transplant_date'] = output_df['first_kidney_transplant_date'].dt.strftime('%Y%m%d')
    output_df['first_glp1_date'] = output_df['first_glp1_date'].dt.strftime('%Y%m%d')
    output_df['most_recent_date'] = output_df['most_recent_date'].dt.strftime('%Y%m%d')

    # Save output to file
    output_df.to_csv(output_file, index=False)
    print(f"Written to {output_file}")

match_based_on_date('../glp1_users.csv',
                    '../glp1_nonusers.csv', 
                    '0_day_user_to_nonusers.csv',
                    0)
