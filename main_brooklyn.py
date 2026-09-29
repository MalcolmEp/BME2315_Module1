from patient_brooklyn import *

import matplotlib.pyplot as plt # Importing from README file from dog data
from scipy import stats
import numpy as np
import statistics 
import pandas as pd

with open("/Users/brook/OneDrive/Desktop/COMP/Mod 1/BME2315_Module1/BME2315_Module1/Metadata and Protein Data for Module 1.csv", newline="") as f:  # Opens data file
        reader = csv.reader(f)
        headers = next(reader) # First row of data set, this is where the headers are
        for h in headers:
            print(h)

# Initializing our own test patients
Patient_Object1 = Patient_Objects(90,7.7,137.9865,"H19.33.004","Female")
Patient_Object2 = Patient_Objects(88,8.2,241.264,"H20.33.005","Male")
Patient_Object3 = Patient_Objects(95,7.1,319.95,"H19.33.006","Female")
Patient_Object4 = Patient_Objects(77,7.5,94.12345,"H20.33.005","Female")
Patient_Object5 = Patient_Objects(74,8.1,333.1675,"H20.33.007","Male")

print(Patient_Object1)
print(Patient_Object2)
print(Patient_Object3)
print(Patient_Object4)
print(Patient_Object5)
print()

sorted_patients = sorted(Patient_Objects.all_patients, key = Patient_Objects.get_age_at_death) # Sorts patients by thier age of death

for patient in sorted_patients:
    print(patient) 
print()


Patient_Objects.print_based_on_aad_sex() # Any patients above a given age of death and sex are called to print , this example is given from the 5 test patients above
print()
print(Patient_Objects.get_age_at_death2(88))  # The first patient that died at 88 



Patient_Objects.instantiate_from_csv("/Users/brook/OneDrive/Desktop/COMP/Mod 1/Module_1_Patient_Practice/Metadata and Protein Data for Module 1.csv") # Instantiating patients from the data file
age_at_death_male = [] # Initializing age at death lists for each sex
age_at_death_female = []

for patient in Patient_Objects.filter(Patient_Objects.all_patients, sex = "Male"): # Adding each patient age at death to the lists given above depending on their sex
    age_at_death_male.append(patient.age_at_death)
for patient in Patient_Objects.filter(Patient_Objects.all_patients, sex = "Female"):
    age_at_death_female.append(patient.age_at_death)


x_male_bar = (statistics.mean(age_at_death_male))  # each bar height is the mean age of death for each sex
x_female_bar = (statistics.mean(age_at_death_female))
age_at_death_male_stdev = (statistics.stdev(age_at_death_male))  # Standard deviations set as SD for male and female age of deaths
age_at_death_female_stdev = (statistics.stdev(age_at_death_female))

print(f'x_male_bar = {x_male_bar}, ge_at_death_male_stdev {age_at_death_male_stdev}') # Standard deviations of bars set to the SD's
print(f'x_female_bar = {x_female_bar}, ge_at_death_female_stdev {age_at_death_female_stdev}')

patient_sex_cols = ['Male', 'Female'] # Column headers
mean_sex = [x_male_bar, x_female_bar]
stdev_sex = [age_at_death_male_stdev, age_at_death_female_stdev]
yerr = [np.zeros(len(mean_sex)), stdev_sex]

t_stat, p_val = stats.ttest_ind(age_at_death_male, age_at_death_female)
print(f't_stat = {t_stat}, p_val = {p_val}') 

plt.bar(patient_sex_cols, mean_sex, yerr=yerr, capsize=10, color=["blue", "orange"]) # Colors and chart titles
plt.title("Age at Death by Sex")
plt.xlabel("Sex")
plt.ylabel("Age at Death")
plt.show()

brain_ph = []  # Initializing brain pH and tau lists 
tTau_pg_ug = []

for patient in Patient_Objects.all_patients:  # If a patient has a ph > 5 and a tau < 5000) the tau and pH data are added to their lists
    if patient.brain_ph > 5 and patient.tTau_pg_ug < 5000:
        brain_ph.append(patient.brain_ph)
        tTau_pg_ug.append(patient.tTau_pg_ug)

X = brain_ph # X is ph and y is tau
y = tTau_pg_ug

plt.scatter(X, y, color='blue') # Prints scatter plot and sets colors / titles
plt.xlabel('Brain pH')
plt.ylabel('tTAU pg/ag')
plt.title('Scatter Plot of Brain pH vs tTAU pg/ag')
plt.show()