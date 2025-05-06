# PROPENSITY SCORE: ICD10 CODES
PRIMARY_HYPERTENSION_CODE = 'I10'
DYSLIPIDEMIA_CODE = 'E78'
HEART_FAILURE_CODE = 'I50'
LIVER_DISEASES_CODES = {'K70', 'K71', 'K72', 'K73', 'K74', 'K75', 'K76', 'K77'}
CHRONIC_LOWER_RESPIRATORY_DISEASES_CODES = {'J40', 'J41', 'J42', 'J43', 'J44', 'J45', 'J46', 'J47', 'J4A'}
SYSTEMIC_CONNECTIVE_TISSUE_DISORDERS_CODES = {'M30', 'M31', 'M32', 'M33', 'M34', 'M35', 'M36'}
NEOPLASMS_CODES = {'C', 'D1', 'D2', 'D3', 'D4'}
OVERWEIGHT_AND_OBESITY_CODE = 'E66'
T2DM_COMPLICATIONS_CODE_ONE = 'E11.2'
T2DM_COMPLICATIONS_CODE_TWO = 'E11.3'
T2DM_COMPLICATIONS_CODE_THREE = 'E11.4'
NEPHROTIC_SYNDROME_CODE = 'N04'
CYSTIC_KIDNEY_DISEASE_CODE = 'Q61'
SMOKING_CODE = 'Z72.0'

DIAGNOSIS_CODES = {
    'primary_hypertension': PRIMARY_HYPERTENSION_CODE,
    'dyslipidemia': DYSLIPIDEMIA_CODE,
    'heart_failure': HEART_FAILURE_CODE,
    'liver_diseases': LIVER_DISEASES_CODES,
    'chronic_lower_respiratory_diseases': CHRONIC_LOWER_RESPIRATORY_DISEASES_CODES,
    'systemic_connective_tissue_disorders': SYSTEMIC_CONNECTIVE_TISSUE_DISORDERS_CODES,
    'neoplasms': NEOPLASMS_CODES,
    'overweight_and_obesity': OVERWEIGHT_AND_OBESITY_CODE,
    't2dm_complications_one': T2DM_COMPLICATIONS_CODE_ONE,
    't2dm_complications_two': T2DM_COMPLICATIONS_CODE_TWO,
    't2dm_complications_three': T2DM_COMPLICATIONS_CODE_THREE,
    'nephrotic_syndrome': NEPHROTIC_SYNDROME_CODE,
    'cystic_kidney_disease': CYSTIC_KIDNEY_DISEASE_CODE,
    'smoking': SMOKING_CODE
}


# PROPENSITY SCORE: RXNORM CODES
# H02 codes -> RxNorm codes
TRIAMCINOLONE_CODE = 10759
BETAMETHASONE_CODE = 1514
DEFLAZACORT_CODE = 22396
OSILODROSTAT_CODE = 2286252
VAMOROLONE_CODE = 2669799
CORTISONE_CODE = 2878
DESOXYCORTICOSTERONE_CODE = 3256
DEXAMETHASONE_CODE = 3264
TRILOSTANE_CODE = 38668
FLUDROCORTISONE_CODE = 4452
FLUOCORTOLONE_CODE = 4463
HYDROCORTISONE_CODE = 5492
RIMEXOLONE_CODE = 55681
KETOCONAZOLE_CODE = 6135
METHYLPREDNISOLONE_CODE = 6902
PREDNISOLONE_CODE = 8638
PREDNISONE_CODE = 8640

CORTICOSTEROID_CODES = {TRIAMCINOLONE_CODE,
                        BETAMETHASONE_CODE,
                        DEFLAZACORT_CODE,
                        OSILODROSTAT_CODE,
                        VAMOROLONE_CODE,
                        CORTISONE_CODE,
                        DESOXYCORTICOSTERONE_CODE,
                        DEXAMETHASONE_CODE,
                        TRILOSTANE_CODE,
                        FLUDROCORTISONE_CODE,
                        FLUOCORTOLONE_CODE,
                        HYDROCORTISONE_CODE,
                        RIMEXOLONE_CODE,
                        KETOCONAZOLE_CODE,
                        METHYLPREDNISOLONE_CODE,
                        PREDNISOLONE_CODE,
                        PREDNISONE_CODE} 

# A10A codes -> RxNorm codes
INSULIN_DETEMIR_CODE = 139825
INSULIN_DEGLUDEC_CODE = 1670007
INSULIN_REGULAR_PORK_CODE = 221109
INSULIN_REGULAR_HUMAN_CODE = 253182
INSULIN_GLARGINE_CODE = 274783
INSULIN_GLULISINE_HUMAN_CODE = 400008
INSULIN_ASPART_HUMAN_CODE = 51428
INSULIN_LISPRO_CODE = 86009

INSULIN_CODES = {INSULIN_DETEMIR_CODE,
                 INSULIN_DEGLUDEC_CODE,
                 INSULIN_REGULAR_PORK_CODE,
                 INSULIN_REGULAR_HUMAN_CODE,
                 INSULIN_GLARGINE_CODE,
                 INSULIN_GLULISINE_HUMAN_CODE,
                 INSULIN_ASPART_HUMAN_CODE,
                 INSULIN_LISPRO_CODE}

# A10BA codes -> RxNorm codes
METFORMIN_CODE = 6809

# A10BH codes -> RxNorm codes
LINAGLIPTIN_CODE = 1100699
ALOGLIPTIN_CODE = 1368001
SITAGLIPTIN_CODE = 593411
VILDAGLIPTIN_CODE = 596554
SAXAGLIPTIN_CODE = 857974

DPP4_CODES = {LINAGLIPTIN_CODE,
              ALOGLIPTIN_CODE,
              SITAGLIPTIN_CODE,
              VILDAGLIPTIN_CODE,
              SAXAGLIPTIN_CODE}

# A10BB codes -> RxNorm codes
TOLAZAMIDE_CODE = 10633
TOLBUTAMIDE_CODE = 10635
ACETOHEXAMIDE_CODE = 173
CHLORPROPAMIDE_CODE = 2404
GLIMEPIRIDE_CODE = 25789
GLIQUIDONE_CODE = 25793
GLYBURIDE_CODE = 4815
GLICLAZIDE_CODE = 4816
GLIPIZIDE_CODE = 4821

SULFONYLUREAS_CODES = {TOLAZAMIDE_CODE,
                       TOLBUTAMIDE_CODE,
                       ACETOHEXAMIDE_CODE,
                       CHLORPROPAMIDE_CODE,
                       GLIMEPIRIDE_CODE,
                       GLIQUIDONE_CODE,
                       GLYBURIDE_CODE,
                       GLICLAZIDE_CODE,
                       GLIPIZIDE_CODE}

# A10BG codes -> RxNorm codes
PIOGLITAZONE_CODE = 33738
TROGLITAZONE_CODE = 72610
ROSIGLITAZONE_CODE = 84108

THIAZOLIDINEDIONES_CODES = {PIOGLITAZONE_CODE,
                            TROGLITAZONE_CODE,
                            ROSIGLITAZONE_CODE}

# C07 codes -> RxNorm codes
TIMOLOL_CODE = 10600
ATENOLOL_CODE = 1202
ACEBUTOLOL_CODE = 149
BETAXOLOL_CODE = 1520
BISOPROLOL_CODE = 19484
CARVEDILOL_CODE = 20352
CELIPROLOL_CODE = 20498
CARTEOLOL_CODE = 2116
NEBIVOLOL_CODE = 31555
ESMOLOL_CODE = 49737
LABETALOL_CODE = 6185
METOPROLOL_CODE = 6918
NADOLOL_CODE = 7226
OXPRENOLOL_CODE = 7801
PENBUTOLOL_CODE = 7973
PINDOLOL_CODE = 8332
PROPRANOLOL_CODE = 8787
SOTALOL_CODE = 9947

BETA_BLOCKING_AGENTS_CODES = {TIMOLOL_CODE,
                              ATENOLOL_CODE,
                              ACEBUTOLOL_CODE,
                              BETAXOLOL_CODE,
                              BISOPROLOL_CODE,
                              CARVEDILOL_CODE,
                              CELIPROLOL_CODE,
                              CARTEOLOL_CODE,
                              NEBIVOLOL_CODE,
                              ESMOLOL_CODE,
                              LABETALOL_CODE,
                              METOPROLOL_CODE,
                              NADOLOL_CODE,
                              OXPRENOLOL_CODE,
                              PENBUTOLOL_CODE,
                              PINDOLOL_CODE,
                              PROPRANOLOL_CODE,
                              SOTALOL_CODE}

# C09 codes -> RxNorm codes
AZILSARTAN_CODE = 1091643
SACUBITRIL_CODE = 1656328
BENAZEPRIL_CODE = 18867
CAPTOPRIL_CODE = 1998
CILAZAPRIL_CODE = 21102
CANDESARTAN_CODE = 214354
LISINOPRIL_CODE = 29046
MOEXIPRIL_CODE = 30131
OLMESARTAN_CODE = 321064
ALISKIREN_CODE = 325646
QUINAPRIL_CODE = 35208
RAMIPRIL_CODE = 35296
ENALAPRIL_CODE = 3827
TRANDOLAPRIL_CODE = 38454
ZOFENOPRIL_CODE = 39990
FOSINOPRIL_CODE = 50166
LOSARTAN_CODE = 52175
PERINDOPRIL_CODE = 54552
IMIDAPRIL_CODE = 60245
VALSARTAN_CODE = 69749
TELMISARTAN_CODE = 73494
EPROSARTAN_CODE = 83515
IRBESARTAN_CODE = 83818

RENIN_ANGIOTENSIN_SYSTEM_AGENTS_CODES = {AZILSARTAN_CODE,
                                         SACUBITRIL_CODE,
                                         BENAZEPRIL_CODE,
                                         CAPTOPRIL_CODE,
                                         CILAZAPRIL_CODE,
                                         CANDESARTAN_CODE,
                                         LISINOPRIL_CODE,
                                         MOEXIPRIL_CODE,
                                         OLMESARTAN_CODE,
                                         ALISKIREN_CODE,
                                         QUINAPRIL_CODE,
                                         RAMIPRIL_CODE,
                                         ENALAPRIL_CODE,
                                         TRANDOLAPRIL_CODE,
                                         ZOFENOPRIL_CODE,
                                         FOSINOPRIL_CODE,
                                         LOSARTAN_CODE,
                                         PERINDOPRIL_CODE,
                                         IMIDAPRIL_CODE,
                                         VALSARTAN_CODE,
                                         TELMISARTAN_CODE,
                                         EPROSARTAN_CODE,
                                         IRBESARTAN_CODE}


# C08 codes -> RxNorm codes
VERAPAMIL_CODE = 11170
LERCANIDIPINE_CODE = 135056
BEPRIDIL_CODE = 1436
AMLODIPINE_CODE = 17767
CLEVIDIPINE_CODE = 233603
LEVAMLODIPINE_CODE = 2376944
LACIDIPINE_CODE = 28382
MANIDIPINE_CODE = 29275
ISRADIPINE_CODE = 33910
DILTIAZEM_CODE = 3443
FELODIPINE_CODE = 4316
NICARDIPINE_CODE = 7396
NIFEDIPINE_CODE = 7417
NIMODIPINE_CODE = 7426
NISOLDIPINE_CODE = 7435
NITRENDIPINE_CODE = 7441
PERHEXILINE_CODE = 8050

CALCIUM_CHANNEL_BLOCKERS_CODES = {VERAPAMIL_CODE,
                                  LERCANIDIPINE_CODE,
                                  BEPRIDIL_CODE,
                                  AMLODIPINE_CODE,
                                  CLEVIDIPINE_CODE,
                                  LEVAMLODIPINE_CODE,
                                  LACIDIPINE_CODE,
                                  MANIDIPINE_CODE,
                                  ISRADIPINE_CODE,
                                  DILTIAZEM_CODE,
                                  FELODIPINE_CODE,
                                  NICARDIPINE_CODE,
                                  NIFEDIPINE_CODE,
                                  NIMODIPINE_CODE,
                                  NISOLDIPINE_CODE,
                                  NITRENDIPINE_CODE,
                                  PERHEXILINE_CODE}

# C03 codes -> RxNorm codes
TRIAMTERENE_CODE = 10763
TRICHLORMETHIAZIDE_CODE = 10772
XIPAMIDE_CODE = 11371
BENDROFLUMETHIAZIDE_CODE = 1369
BUMETANIDE_CODE = 1808
CHLOROTHIAZIDE_CODE = 2396
CHLORTHALIDONE_CODE = 2409
FINERENONE_CODE = 2562811
CLOPAMIDE_CODE = 2603
EPLERENONE_CODE = 298869
CYCLOPENTHIAZIDE_CODE = 3000
CONIVAPTAN_CODE = 302285
TOLVAPTAN_CODE = 358257
TORSEMIDE_CODE = 38413
FUROSEMIDE_CODE = 4603
HYDROCHLOROTHIAZIDE_CODE = 5487
HYDROFLUMETHIAZIDE_CODE = 5495
INDAPAMIDE_CODE = 5764
ETHACRYNATE_CODE = 62349
AMILORIDE_CODE = 644
MERSALYL_CODE = 6774
METHYCLOTHIAZIDE_CODE = 6860
METOLAZONE_CODE = 6916
POLYTHIAZIDE_CODE = 8565
POTASSIUM_CODE = 8588
SPIRONOLACTONE_CODE = 9997

DIURETICS_CODES = {TRIAMTERENE_CODE,
                   TRICHLORMETHIAZIDE_CODE,
                   XIPAMIDE_CODE,
                   BENDROFLUMETHIAZIDE_CODE,
                   BUMETANIDE_CODE,
                   CHLOROTHIAZIDE_CODE,
                   CHLORTHALIDONE_CODE,
                   FINERENONE_CODE,
                   CLOPAMIDE_CODE,
                   EPLERENONE_CODE,
                   CYCLOPENTHIAZIDE_CODE,
                   CONIVAPTAN_CODE,
                   TOLVAPTAN_CODE,
                   TORSEMIDE_CODE,
                   FUROSEMIDE_CODE,
                   HYDROCHLOROTHIAZIDE_CODE,
                   HYDROFLUMETHIAZIDE_CODE,
                   INDAPAMIDE_CODE,
                   ETHACRYNATE_CODE,
                   AMILORIDE_CODE,
                   MERSALYL_CODE,
                   METHYCLOTHIAZIDE_CODE,
                   METOLAZONE_CODE,
                   POLYTHIAZIDE_CODE,
                   POTASSIUM_CODE,
                   SPIRONOLACTONE_CODE}

# C10AA codes -> RxNorm codes
CERIVASTATIN_SODIUM_CODE = 221072  # (deprecated 2017)
ROSUVASTATIN_CODE = 301542
SIMVASTATIN_CODE = 36567
FLUVASTATIN_CODE = 41127
PRAVASTATIN_CODE = 42463
CERIVASTATIN_CODE = 596723
LOVASTATIN_CODE = 6472
ATORVASTATIN_CODE = 83367
PITAVASTATIN_CODE = 861634

STATIN_CODES = {CERIVASTATIN_SODIUM_CODE,
                ROSUVASTATIN_CODE,
                SIMVASTATIN_CODE,
                FLUVASTATIN_CODE,
                PRAVASTATIN_CODE,
                CERIVASTATIN_CODE,
                LOVASTATIN_CODE,
                ATORVASTATIN_CODE,
                PITAVASTATIN_CODE}


# A10BK codes -> RxNorm codes
CANAGLIFLOZIN_CODE = 1373458
DAPAGLIFLOZIN_CODE = 1488564
EMPAGLIFLOZIN_CODE = 1545653
ERTUGLIFLOZIN_CODE = 1992672
BEXAGLIFLOZIN_CODE = 2627044
SOTAGLIFLOZIN_CODE = 2638675
SOTAGLIFLOZIN_DEPRECATED_CODE = "OMOP5170634"  # (deprecated 2024)
BEXAGLIFLOZIN_DEPRECATED_CODE = "OMOP5174738"  # (deprecated 2023)

SGLT2_INHIBITOR_CODES = {CANAGLIFLOZIN_CODE,
                         DAPAGLIFLOZIN_CODE,
                         EMPAGLIFLOZIN_CODE,
                         ERTUGLIFLOZIN_CODE,
                         BEXAGLIFLOZIN_CODE,
                         SOTAGLIFLOZIN_CODE,
                         SOTAGLIFLOZIN_DEPRECATED_CODE,
                         BEXAGLIFLOZIN_DEPRECATED_CODE}

MEDICATION_CODES = {
    'sglt2_inhibitors': SGLT2_INHIBITOR_CODES,
    'statins': STATIN_CODES,
    'diuretics': DIURETICS_CODES,
    'calcium_channel_blockers': CALCIUM_CHANNEL_BLOCKERS_CODES,
    'renin_angiotensin_system_agents': RENIN_ANGIOTENSIN_SYSTEM_AGENTS_CODES,
    'beta_blocking_agents': BETA_BLOCKING_AGENTS_CODES,
    'thiazolidinediones': THIAZOLIDINEDIONES_CODES,
    'sulfonylureas': SULFONYLUREAS_CODES,
    'dpp4': DPP4_CODES,
    'metformin': {METFORMIN_CODE},
    'insulin': INSULIN_CODES,
    'corticosteroids': CORTICOSTEROID_CODES
}

# PROPENSITY SCORE: TNX CODES

# 9086 code -> LOINC
BLOOD_PRESSURE_DIASTOILIC = {"8462-4",
                             "76535-4", 
                             "87740-7", 
                             "87736-5",
                             "8453-3", 
                             "8454-1", 
                             "8455-8", 
                             "76213-8"}

# 9085 code -> LOINC
BLOOD_PRESSURE_SYSTOLIC = {"8480-6",
                           "76215-3",
                           "76534-7",
                           "87739-9",
                           "87741-5",
                           "8459-0",
                           "8460-8",
                           "8461-6"}

# 9083 code -> LOINC
BODY_MASS_INDEX = {"39156-5"}

# 9028 code -> LOINC
POTASSIUM = {"2823-3",
             "6298-4",
             "77142-8"}

# 9029 code -> LOINC
SODIUM = {"2947-0",
          "2951-2",
          "77139-4"}

# 9004 code -> LOINC
TRIGLYCERIDE = {"12951-0",
                "2571-8",
                "3043-7"}

# 9001 code -> LOINC
CHOLESTEROL_HDL = {"2085-9",
                   "49130-8"}

# 9037 code -> LOINC
HEMOGLOBIN_A1C = {"17855-8",
                  "17856-6",
                  "4548-4",
                  "4549-2"}

# 9044 code -> LOINC
ALANINE_AMINOTRANSFERASE = {"1742-6",
                            "1743-4",
                            "1744-2",
                            "76625-3",
                            "77144-4"}

# 9047 code -> LOINC
ASPARTATE_AMINOTRANSFERASE = {"1920-8",
                              "30239-8"}

# 9050 code -> LOINC
BILIRUBIN_TOTAL = {"1975-2",
                   "42719-5"}

# 9003 code -> LOINC
NATRIURETIC_PEPTIDE_B = {"30934-4",
                         "42637-9"}

# 8001 code -> LOINC
GLOMERULAR_FILTRATION_RATE = {"33914-3",
                              "48642-3",
                              "48643-1",
                              "50044-7",
                              "69405-9",
                              "76633-7",
                              "77147-7"}

LAB_RESULT_CODES = {
    'blood_pressure_diastolic': BLOOD_PRESSURE_DIASTOILIC,
    'blood_pressure_systolic': BLOOD_PRESSURE_SYSTOLIC,
    'body_mass_index': BODY_MASS_INDEX,
    'potassium': POTASSIUM,
    'sodium': SODIUM,
    'triglyceride': TRIGLYCERIDE,
    'cholesterol_hdl': CHOLESTEROL_HDL,
    'hemoglobin_a1c': HEMOGLOBIN_A1C,
    'alanine_aminotransferase': ALANINE_AMINOTRANSFERASE,
    'aspartate_aminotransferase': ASPARTATE_AMINOTRANSFERASE,
    'bilirubin_total': BILIRUBIN_TOTAL,
    'natriuretic_peptide_b': NATRIURETIC_PEPTIDE_B,
    'glomerular_filtration_rate': GLOMERULAR_FILTRATION_RATE
}

