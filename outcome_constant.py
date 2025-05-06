# OUTCOME CODES

MORTALITY = {
    "Demographics": {"Deceased"},
    "Diagnosis": {"R99"}
}

MACE = {
    "Demographics": {"Deceased"},
    "Diagnosis": {"R99", "I21", "I46", "I61", "I63"}
}

MAKE = {
    "Demographics": {"Deceased"},
    "Diagnosis": {"R99", "Z99.2"},
    "Procedure": {"90937", "90947", "90945", "1012752", "90935", "302497006", "1012740"},
    "Laboratory": {"33914-3", "48642-3", "48643-1", "50044-7", "69405-9", "76633-7", "77147-7"}
} #if laboratory value is >= 14.00

DKA = {
    "Diagnosis": {"E11.1"}
}


OSTEOPOROTIC_FRACTURE = {
    "Diagnosis": {"M80"}
}

APPENDICITIS = {
    "Diagnosis": {"K35", "K36", "K37"}
}

HEMATOLOGIC_MALIGNANCY = {
    "Diagnosis": {"C81", "C82", "C83", "C84", "C85", "C86", "C87", "C88", "C89", "C90", "C91", "C92", "C93", "C94", "C95", "C96"}
}

COMMON_COLD = {
    "Diagnosis": {"J00"}
}

IRRITABLE_BOWEL_SYNDROME = {
    "Diagnosis": {"K58"}
}

BURN = {
    "Diagnosis": {"T20", "T21", "T22", "T23", "T24", "T25"}
}

SUICIDE_ATTEMPT_AND_IDEATION = {
    "Diagnosis": {"T14.91", "R45.851"}
}

AMI = {
    "Diagnosis": {"I21"}
}

STROKE = {
    "Diagnosis": {"I61", "I63"}
}

INCIDENT_DIALYSIS = {
    "Procedure": {"90937", "90947", "90945", "90935", "1012752", "302497006", "1012740"},
    "Diagnosis": {"Z99.2"}
}

AKI = {
    "Diagnosis": {"N17"}
}

UTI = {
    "Diagnosis": {"N39.0", "N30", "N10"}
}

UROGENITAL_CANDIDIASIS = {
    "Diagnosis": {"B37.3", "B37.4"}
}

OUTCOME_CODES = {
    'mortality': MORTALITY,
    'mace': MACE,
    'make': MAKE,
    'dka': DKA,
    'osteoporotic_fracture': OSTEOPOROTIC_FRACTURE,
    'appendicitis': APPENDICITIS,
    'hematologic_malignancy': HEMATOLOGIC_MALIGNANCY,
    'common_cold': COMMON_COLD,
    'irritable_bowel_syndrome': IRRITABLE_BOWEL_SYNDROME,
    'burn': BURN,
    'suicide_attempt_and_ideation': SUICIDE_ATTEMPT_AND_IDEATION,
    'ami': AMI,
    'stroke': STROKE,
    'incident_dialysis': INCIDENT_DIALYSIS,
    'aki': AKI,
    'uti': UTI,
    'urogenital_candidiasis': UROGENITAL_CANDIDIASIS
}

MACE_OUTCOME_CODES = {
    'mortality': MORTALITY,
    'mace': MACE,
    'ami': AMI,
    'cardiac_arrest': {'Diagnosis': {'I46'}}, 
    'stroke': STROKE
}

OTHER_OUTCOME_CODES = {
    'nausea_and_vomiting': {'Diagnosis' : {'R11'}},
    'diarrhea': {'Diagnosis' : {'R19.7'}},
    'sunburn': {'Diagnosis' : {'L55'}},
    'herniated_disc': {'Diagnosis' : {'M51'}},
    'pneumonia': {'Diagnosis' : {'J18', 'J18.9', 'J12.82', 'J13', 'J14', 'J15.0', 'J15.1',  'J15.2', 'J15.21', 'J15.211', 'J15.212',  'J15.4', 'J15.6', 'J15.8', 'J16'}},
    'diabetic_retinopathy': {'Diagnosis' : {'E11.3', 'E11.31',  'E11.311', 'E11.319', 'E11.32', 'E11.321', 'E11.329', 'E11.33', 'E11.331', 'E11.339', 'E11.34', 'E11.349',  'E11.35', 'E11.351', 'E11.359', 'E11.3593', 'E11.3599'}},
    'depression': {'Diagnosis' : {'F32', 'F32.A'}},
    'hypoglycemia': {'Diagnosis' : {'E16.2'}},
    'pancreatitis': {'Diagnosis' : {'K85'}}
}

