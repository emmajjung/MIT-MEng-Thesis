import pandas as pd

from constant import *
from propensity_functions import *

# for USERS
demographics_characteristics(USERS,
                             ORIGINAL_USERS,
                             'csv_files/propensity_files/demographics_propensity_users.csv')

diagnosis_characteristics(USERS,
                          USERS_DIAGNOSIS,
                          'csv_files/propensity_files/diagnosis_propensity_users.csv')

medication_characteristics(USERS,
                           USERS_MEDICATION,
                           'csv_files/propensity_files/medication_propensity_users.csv')

lab_results_characteristics(USERS,
                            USERS_LAB_RESULTS,
                            USERS_VITAL_SIGNS,
                            'csv_files/propensity_files/lab_results_propensity_users.csv')

# for NONUSERS
demographics_characteristics(NONUSERS,
                             ORIGINAL_NONUSERS,
                             'csv_files/propensity_files/demographics_propensity_nonusers.csv')

diagnosis_characteristics(NONUSERS,
                          NONUSERS_DIAGNOSIS,
                          'csv_files/propensity_files/diagnosis_propensity_nonusers.csv')

medication_characteristics(NONUSERS,
                           NONUSERS_MEDICATION,
                           'csv_files/propensity_files/medication_propensity_nonusers.csv')

lab_results_characteristics(NONUSERS,
                            NONUSERS_LAB_RESULTS,
                            NONUSERS_VITAL_SIGNS,
                            'csv_files/propensity_files/lab_results_propensity_nonusers.csv')

# Read the CSV files for propensity users
demographics_users = pd.read_csv('csv_files/propensity_files/demographics_propensity_users.csv')
diagnosis_users = pd.read_csv('csv_files/propensity_files/diagnosis_propensity_users.csv')
medication_users = pd.read_csv('csv_files/propensity_files/medication_propensity_users.csv')
lab_results_users = pd.read_csv('csv_files/propensity_files/lab_results_propensity_users.csv')

# Join the dataframes on patient_id
joined_users = demographics_users.merge(diagnosis_users, on='patient_id', how='outer')
joined_users = joined_users.merge(medication_users, on='patient_id', how='outer')
joined_users = joined_users.merge(lab_results_users, on='patient_id', how='outer')

# Add a new column 'user' set to 1
joined_users['user'] = 1

# Read the CSV files for propensity nonusers
demographics_nonusers = pd.read_csv('csv_files/propensity_files/demographics_propensity_nonusers.csv')
diagnosis_nonusers = pd.read_csv('csv_files/propensity_files/diagnosis_propensity_nonusers.csv')
medication_nonusers = pd.read_csv('csv_files/propensity_files/medication_propensity_nonusers.csv')
lab_results_nonusers = pd.read_csv('csv_files/propensity_files/lab_results_propensity_nonusers.csv')

# Join the dataframes on patient_id
joined_nonusers = demographics_nonusers.merge(diagnosis_nonusers, on='patient_id', how='outer')
joined_nonusers = joined_nonusers.merge(medication_nonusers, on='patient_id', how='outer')
joined_nonusers = joined_nonusers.merge(lab_results_nonusers, on='patient_id', how='outer')

# Add a new column 'user' set to 0
joined_nonusers['user'] = 0

# Concatenate the dataframes
concatenated_df = pd.concat([joined_users, joined_nonusers])

concatenated_df = concatenated_df.dropna()

# Write the concatenated dataframe to a new CSV file
concatenated_df.to_csv('csv_files/propensity_files/prematched_propensity_characteristics.csv', index=False)

generate_propensity_score('csv_files/propensity_files/prematched_propensity_characteristics.csv',
                          'csv_files/propensity_files/propensity_scores.csv')

propensity_score_matching(USERS,
                          'csv_files/kidney_matches/0_day_user_to_nonusers.csv',
                          'csv_files/propensity_files/propensity_scores.csv',
                          'csv_files/matched_users_and_nonusers_wout_limit.csv',
                          None)

propensity_score_matching(USERS,
                          'csv_files/kidney_matches/0_day_user_to_nonusers.csv',
                          'csv_files/propensity_files/propensity_scores.csv',
                          'csv_files/matched_users_and_nonusers.csv')

matched_data = pd.read_csv('csv_files/matched_users_and_nonusers.csv')
glp1_users = pd.read_csv(USERS)
glp1_users['most_recent_date'] = pd.to_datetime(glp1_users['most_recent_date'], format='%Y%m%d')
users = matched_data[matched_data['user'] == 1] 
merged_users = pd.merge(users, glp1_users[['patient_id', 'most_recent_date']], on='patient_id', how='left')
merged_users['most_recent_date'] = pd.to_datetime(merged_users['most_recent_date']).dt.strftime('%Y%m%d')
merged_users.to_csv('csv_files/matched_users.csv', index=False)

glp1_nonusers = pd.read_csv(NONUSERS)
glp1_nonusers['most_recent_date'] = pd.to_datetime(glp1_nonusers['most_recent_date'], format='%Y%m%d')
nonusers = matched_data[matched_data['user'] == 0]
merged_nonusers = pd.merge(nonusers, glp1_nonusers, on='patient_id', how='left')
merged_nonusers['most_recent_date'] = pd.to_datetime(merged_nonusers['most_recent_date']).dt.strftime('%Y%m%d')
merged_nonusers.to_csv('csv_files/matched_nonusers.csv', index=False)
prematched_df = pd.read_csv('csv_files/propensity_files/prematched_propensity_characteristics.csv')
matched_df = pd.read_csv('csv_files/matched_users_and_nonusers.csv')

# Filter the prematched_df to get rows corresponding to matched_patient_ids
filtered_prematched_df = pd.merge(prematched_df, matched_df[['patient_id', 'user']],  on=['patient_id', 'user'], how='inner')

# Write the filtered dataframe to the postmatched_propensity_characteristics.csv file
filtered_prematched_df.to_csv('csv_files/propensity_files/postmatched_propensity_characteristics.csv', index=False)
