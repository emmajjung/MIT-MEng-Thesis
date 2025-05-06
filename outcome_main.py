from constant import *
from outcome_functions import *

prior_outcomes(USERS,
                ORIGINAL_USERS,
                USERS_DIAGNOSIS,
                USERS_PROCEDURE,
                USERS_MEDICATION,
                USERS_LAB_RESULTS,
                'csv_files/prior_outcome_users.csv',
                'first_kidney_transplant_date')

prior_outcomes(NONUSERS,
                ORIGINAL_NONUSERS,
                NONUSERS_DIAGNOSIS,
                NONUSERS_PROCEDURE,
                NONUSERS_MEDICATION,
                NONUSERS_LAB_RESULTS,
                'csv_files/prior_outcome_nonusers.csv',
                'first_kidney_transplant_date')

prior_outcomes('csv_files/matched_users.csv',
                ORIGINAL_USERS,
                USERS_DIAGNOSIS,
                USERS_PROCEDURE,
                USERS_MEDICATION,
                USERS_LAB_RESULTS,
                'csv_files/prior_outcome_matched_users.csv',
                'first_glp1_date')

prior_outcomes('csv_files/matched_nonusers.csv',
                ORIGINAL_NONUSERS,
                NONUSERS_DIAGNOSIS,
                NONUSERS_PROCEDURE,
                NONUSERS_MEDICATION,
                NONUSERS_LAB_RESULTS,
                'csv_files/prior_outcome_matched_nonusers.csv',
                'first_glp1_date')

days_to_outcome('csv_files/matched_users.csv',
                ORIGINAL_USERS,
                USERS_DIAGNOSIS,
                USERS_PROCEDURE,
                USERS_MEDICATION,
                USERS_LAB_RESULTS,
                'csv_files/days_to_outcome_users.csv')

days_to_outcome('csv_files/matched_nonusers.csv',
                ORIGINAL_NONUSERS,
                NONUSERS_DIAGNOSIS,
                NONUSERS_PROCEDURE,
                NONUSERS_MEDICATION,
                NONUSERS_LAB_RESULTS,
                'csv_files/days_to_outcome_nonusers.csv')

calculate_survival_probabilities('csv_files/days_to_outcome_users.csv',
                                 'user_survival_prob.csv')

calculate_survival_probabilities('csv_files/days_to_outcome_nonusers.csv',
                                 'nonuser_survival_prob.csv')

calculate_hazard_ratios('csv_files/days_to_outcome_users.csv',
                        'csv_files/days_to_outcome_nonusers.csv',
                        'csv_files/hazard_ratios.csv')

# Merge log of propensity score for aHR calculation
days_to_outcome_users = pd.read_csv('csv_files/days_to_outcome_users.csv')
days_to_outcome_users['user'] = 1
matched_users_and_nonusers = pd.read_csv('csv_files/matched_users_and_nonusers.csv')

merged_df = pd.merge(days_to_outcome_users, matched_users_and_nonusers[['patient_id', 'user', 'propensity_score']], on=['patient_id', 'user'], how='left')

merged_df.to_csv('csv_files/days_to_outcome_users.csv', index=False)

days_to_outcome_nonusers = pd.read_csv('csv_files/days_to_outcome_nonusers.csv')
days_to_outcome_nonusers['user'] = 0

merged_df = pd.merge(days_to_outcome_nonusers, matched_users_and_nonusers[['patient_id', 'user', 'propensity_score']], on=['patient_id', 'user'], how='left')

merged_df.to_csv('csv_files/days_to_outcome_nonusers.csv', index=False)

calculate_hazard_ratios('csv_files/days_to_outcome_users.csv',
                        'csv_files/days_to_outcome_nonusers.csv',
                        'csv_files/adjusted_hazard_ratios.csv',
                        True)
