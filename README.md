# GLP-1RA Thesis Analysis Code

The following code was used to generate results for the GLP-1RA thesis. 

**Only Python code is included in this repository**-no TriNetX datasets are provided due to privacy and security considerations.

---

## Steps to Run the Analysis

1. **Gather Relevant TriNetX Data**  
   Obtain the necessary datasets from TriNetX according to your study requirements.  
   > ⚠️ **Note:** The data itself is not included in this repository.

2. **Run `filter_main.py`**  
   This script filters and preprocesses the raw TriNetX data to prepare it for matching and analysis.

3. **Run `matches.py`**  
   This script performs matching on the filtered dataset to run 1-to-n kidney transplant matching.

4. **Run `propensity_main.py`**  
   This script gathers covariates and calculates propensity scores to ultimately match each user to a nonuser.

5. **Run `outcome_main.py`**  
   This script analyzes the outcomes of interest based on the matched user and nonuser cohorts.

---

Thank you!
