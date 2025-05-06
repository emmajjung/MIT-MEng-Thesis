DIABETIC_DIAGNOSIS_CODE = "E11"

KIDNEY_TRANSPLANT_DIAGNOSIS_CODES = {"Z94.0", "V42.0"}  # ICD 9 + 10 code
KIDNEY_TRANSPLANT_PROCEDURE_CODES = {"0TY00Z0", "0TY10Z0", "0TY10Z1", "0TY00Z1", "0TY10Z2", "0TY00Z2", "70536003", "313030004", "6471000179103", "175902000", "1008098", "1008099", "50300", "50320", "1008104", "50327", "50328", "50329", "1008109", "50360", "50365", "50323", "50325", "50340", "50370", "50380", "55.69", "55.6" } #ICD 10, SNOMED, CPT

# RxNorm codes
ALBIGLUTIDE_CODE = 1534763
DULAGLUTIDE_CODE = 1551291
EXENATIDE_CODE = 60548
LIRAGLUTIDE_CODE = 475968
LIXISENATIDE_CODE = 1440051
SEMAGLUTIDE_CODE = 1991302
MEDICATION_CODES = {ALBIGLUTIDE_CODE,
                    DULAGLUTIDE_CODE,
                    EXENATIDE_CODE,
                    LIRAGLUTIDE_CODE,
                    LIXISENATIDE_CODE,
                    SEMAGLUTIDE_CODE}


ORIGINAL_USERS = "glp1_users/patient.csv"
USERS_DIAGNOSIS = "glp1_users/diagnosis.csv"
USERS_PROCEDURE = "glp1_users/procedure.csv"
USERS_LAB_RESULTS = "glp1_users/lab_result.csv"
USERS_VITAL_SIGNS = "glp1_users/vitals_signs.csv"
USERS_MEDICATION = "glp1_users/medication_ingredient.csv"

USERS = "csv_files/glp1_users.csv"
USERS_MOST_RECENT = "csv_files/most_recent_date_users.csv"
DEMOGRAPHICS_PROPENSITY_USERS = "csv_files/demographics_propensity_users.csv"
DIAGNOSIS_PROPENSITY_USERS = "csv_files/diagnosis_propensity_users.csv"
MEDICATION_PROPENSITY_USERS = "csv_files/medication_propensity_users.csv"
LAB_RESULTS_PROPENSITY_USERS = "csv_files/lab_results_propensity_users.csv"

ORIGINAL_NONUSERS = "glp1_nonusers/patient.csv"
NONUSERS_DIAGNOSIS = "glp1_nonusers/diagnosis.csv"
NONUSERS_PROCEDURE = "glp1_nonusers/procedure.csv"
NONUSERS_LAB_RESULTS = "glp1_nonusers/lab_result.csv"
NONUSERS_VITAL_SIGNS = "glp1_nonusers/vitals_signs.csv"
NONUSERS_MEDICATION = "glp1_nonusers/medication_ingredient.csv"

NONUSERS = "csv_files/glp1_nonusers.csv"
NONUSERS_MOST_RECENT = "csv_files/most_recent_date_nonusers.csv"
MATCHED_NONUSERS = "csv_files/matched_glp1_nonusers.csv"
MATCHED_NONUSERS_W_LIMIT = "csv_files/matched_glp1_nonusers_with_limit.csv"
