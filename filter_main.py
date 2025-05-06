from constant import *
from date_functions import *
from filter_functions import *

# for USERS
find_earliest_transplant(ORIGINAL_USERS,
                         USERS_DIAGNOSIS,
                         USERS_PROCEDURE, 
                         USERS) 

find_earliest_medication(USERS,
                         USERS_MEDICATION,
                         USERS) 

latest_date(ORIGINAL_USERS,
            USERS_DIAGNOSIS,
            USERS_PROCEDURE,
            USERS_MEDICATION,
            USERS_LAB_RESULTS,
            USERS_MOST_RECENT)

exclude_dead_patients(USERS,
                      ORIGINAL_USERS,
                      USERS_MOST_RECENT,
                      USERS)


# for NONUSERS
find_earliest_transplant(ORIGINAL_NONUSERS,
                         NONUSERS_DIAGNOSIS,
                         NONUSERS_PROCEDURE,
                         NONUSERS)

latest_date(ORIGINAL_NONUSERS,
            NONUSERS_DIAGNOSIS,
            NONUSERS_PROCEDURE,
            NONUSERS_MEDICATION,
            NONUSERS_LAB_RESULTS,
            NONUSERS_MOST_RECENT)

exclude_dead_patients(NONUSERS,
                      ORIGINAL_NONUSERS,
                      NONUSERS_MOST_RECENT,
                      NONUSERS, 
                      False) 

