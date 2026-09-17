from patient_Malcolm import *

import matplotlib.pyplot as plt # Importing all neccesary stuff
from scipy import stats
import numpy as np
import statistics 

with open("/Users/malcolmepstein/Desktop/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv", newline="") as f:  # Opening the data file to read 
        reader = csv.reader(f)
        headers = next(reader) # Get the first row
        for h in headers:
            print(h)

# initializing our own test patients
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

sorted_patients = sorted(Patient_Objects.all_patients, key = Patient_Objects.get_age_at_death) # sorting patients by age at death

for patient in sorted_patients:
    print(patient) 

print()


Patient_Objects.print_based_on_aad_sex()  # calling the method to print any patients above a given age of death of 88 and sex (female) (this is only taken from my created 5 patients)

print()

print(Patient_Objects.get_age_at_death2(88))  # calling the method to print the first patient with an age of death of 88 



Patient_Objects.instantiate_from_csv("/Users/malcolmepstein/Desktop/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv") # making sure patients are instantiated from the data file

age_at_death_male = [] # initializing age at death lists for each sex
age_at_death_female = []

for patient in Patient_Objects.filter(Patient_Objects.all_patients, sex = "Male"): # Adding every patient age at death to the lists
    age_at_death_male.append(patient.age_at_death)

for patient in Patient_Objects.filter(Patient_Objects.all_patients, sex = "Female"):
    age_at_death_female.append(patient.age_at_death)


x_male_bar = (statistics.mean(age_at_death_male))  # setting x and y bar heights as the mean of the age of deaths
x_female_bar = (statistics.mean(age_at_death_female))

age_at_death_male_stdev = (statistics.stdev(age_at_death_male))  # setting the standard deviations as the SD for male and female age of deaths
age_at_death_female_stdev = (statistics.stdev(age_at_death_female))

print(f'x_male_bar = {x_male_bar}, ge_at_death_male_stdev {age_at_death_male_stdev}') # setting standard deviations of bars to the SD's defined one step ago
print(f'x_female_bar = {x_female_bar}, ge_at_death_female_stdev {age_at_death_female_stdev}')

patient_sex_cols = ['Male', 'Female']  # setting column headers
mean_sex = [x_male_bar, x_female_bar]
stdev_sex = [age_at_death_male_stdev, age_at_death_female_stdev]
yerr = [np.zeros(len(mean_sex)), stdev_sex]

plt.bar(patient_sex_cols, mean_sex, yerr=yerr, capsize=10, color=["blue", "orange"]) # setting colors and chart titles
plt.title("Age at Death by Sex")
plt.xlabel("Sex")
plt.ylabel("Age at Death")
plt.show()



brain_ph = []  # initializing brain ph and tau lists 
tTau_pg_ug = []

for patient in Patient_Objects.all_patients:  # if a patient has a ph of above 5 and a tau of below 5000 (to remove crazy outliers), the tau and ph data get addded to their respective lists
    if patient.brain_ph > 5 and patient.tTau_pg_ug < 5000:
        brain_ph.append(patient.brain_ph)
        tTau_pg_ug.append(patient.tTau_pg_ug)

X = brain_ph # setting variables, x to ph and y to tau
y = tTau_pg_ug

plt.scatter(X, y, color='blue') # printing the scatter plot and setting colors / titles
plt.xlabel('Brain pH')
plt.ylabel('tTAU pg/ag')
plt.title('Scatter Plot of Brain pH vs tTAU pg/ag')
plt.show()


# For some reason you have to click run twice, and delete the first bar graph to let both graphs appear at once