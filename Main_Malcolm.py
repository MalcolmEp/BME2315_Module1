from patient_Malcolm import *

import matplotlib.pyplot as plt # Importing all neccesary stuff
from scipy import stats
import numpy as np
import statistics 
import pandas as pd
from sklearn.linear_model import LinearRegression



Patient_Objects.instantiate_from_csv("/Users/malcolmepstein/Desktop/BME 2315/Module 1/BME2315_Module1/Metadata and Protein Data for Module 1.csv") # making sure patients are instantiated from the data file


# BAR GRAPH

tTau_male_hs = [] # initializing tTau lists for males an females with a high school education
tTau_female_hs = []

for patient in Patient_Objects.filter(Patient_Objects.all_patients, sex = "Male", highest_level_education = "High School"): # Adding every male with a hs education to the list
    tTau_male_hs.append(patient.tTau_pg_ug)

for patient in Patient_Objects.filter(Patient_Objects.all_patients, sex = "Female", highest_level_education = "High School"):
    tTau_female_hs.append(patient.tTau_pg_ug)


x_male_hs_bar = (statistics.mean(tTau_male_hs))  # setting x and y bar heights as the mean of the age of deaths
x_female_hs_bar = (statistics.mean(tTau_female_hs))

tTau_male_hs_stdev = (statistics.stdev(tTau_male_hs))  # setting the standard deviations as the SD for male and female age of deaths
tTau_female_hs_stdev = (statistics.stdev(tTau_female_hs))

print(f'Male (High School) Mean: = {x_male_hs_bar}, Male (High School) Standard Deviation: {tTau_male_hs_stdev}') # Printing means and SD values for both
print(f'Female (High School) Mean: = {x_female_hs_bar}, Male (High School) Standard Deviation: {tTau_female_hs_stdev}')

patient_sex_cols = ['Male (High School)', 'Female (High School)']  # setting column headers
mean_sex = [x_male_hs_bar, x_female_hs_bar]
stdev_sex = [tTau_male_hs_stdev, tTau_female_hs_stdev]
yerr = [np.zeros(len(mean_sex)), stdev_sex]


t_stat, p_val = stats.ttest_ind(tTau_male_hs, tTau_female_hs)
print(f't_statistic bar graph: = {t_stat}, p_value bar graph: = {p_val}')

plt.bar(patient_sex_cols, mean_sex, yerr=yerr, capsize=10, color=["blue", "orange"]) # setting colors and chart titles
plt.title("tTau Levels By Sex (High School)")
plt.xlabel("Sex")
plt.ylabel("tTau")
plt.text(0.05, 0.95, f"p = {p_val:.3f}", transform=plt.gca().transAxes, fontsize=12, verticalalignment='top', horizontalalignment='left')
plt.show()



# SCATTER PLOT

years_of_education = []  # initializing brain ph and tau lists 
tTau_pg_ug = []

# Outlier analysis

all_tTau = []

for patient in Patient_Objects.all_patients: 
    all_tTau.append(patient.tTau_pg_ug)

q1, q3 = np.percentile(all_tTau, [25,75]) # Fetches the 25th and 75th percentile
iqr = q3-q1

lower_fence = q1 - 4.5 * iqr # This is the same as IQR x 3 for only extreme outliers
upper_fence = q1 + 4.5 * iqr

for patient in Patient_Objects.all_patients: 
    if lower_fence < patient.tTau_pg_ug < upper_fence:
        tTau_pg_ug.append(patient.tTau_pg_ug)
        years_of_education.append(patient.years_of_education)

X = years_of_education # setting variables, x to years of educatioon and y to tau
y = tTau_pg_ug

X = np.array(years_of_education).reshape(-1,1)
y = np.array(tTau_pg_ug)

model = LinearRegression()
model.fit(X,y)

slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X,y)

result = stats.linregress(years_of_education, tTau_pg_ug)
print(f'p-value scatter plot: = {result.pvalue:.3f}')

equation = f"y = {slope:.2f}x + {intercept:.2f}\nR^2 = {r2:.5f}"
plt.text(0.05, 0.95, equation, transform=plt.gca().transAxes, color = "black", fontsize = 12, verticalalignment = 'top')

plt.text(0.95, 0.95, f"p = {result.pvalue:.3f}", transform=plt.gca().transAxes, color="black", fontsize=12, verticalalignment='top', horizontalalignment='right')

x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='red', linewidth=2)

plt.scatter(X, y, color='blue') # printing the scatter plot and setting colors / titles
plt.xlabel('Years of Education')
plt.ylabel('tTAU pg/ag')
plt.title('Scatter Plot of Years of Education vs tTAU pg/ag')
plt.show()




# ANOVA

high_school = []
bachelors = []
trade_school = []
graduate = []
professional = []

for patient in Patient_Objects.filter(Patient_Objects.all_patients, highest_level_education = "High School"): 
    if lower_fence < patient.tTau_pg_ug < upper_fence:
        high_school.append(patient.tTau_pg_ug)

for patient in Patient_Objects.filter(Patient_Objects.all_patients, highest_level_education = "Bachelors"): 
    if lower_fence < patient.tTau_pg_ug < upper_fence:
        bachelors.append(patient.tTau_pg_ug)

for patient in Patient_Objects.filter(Patient_Objects.all_patients, highest_level_education = "Trade School/ Tech School"): 
    if lower_fence < patient.tTau_pg_ug < upper_fence:   
        trade_school.append(patient.tTau_pg_ug)

for patient in Patient_Objects.filter(Patient_Objects.all_patients, highest_level_education = "Graduate (PhD/Masters)"): 
    if lower_fence < patient.tTau_pg_ug < upper_fence: # Extreme outlier removal with 3 * IQR
        graduate.append(patient.tTau_pg_ug)

for patient in Patient_Objects.filter(Patient_Objects.all_patients, highest_level_education = "Professional"): 
    if lower_fence < patient.tTau_pg_ug < upper_fence:
        professional.append(patient.tTau_pg_ug)


x_tTau_hs_bar = statistics.mean(high_school)
x_tTau_bachelors_bar = statistics.mean(bachelors)
x_tTau_trade_bar = statistics.mean(trade_school)
x_tTau_graduate_bar = statistics.mean(graduate)
x_tTau_professional_bar = statistics.mean(professional)

x_tTau_hs_stdev = statistics.stdev(high_school)
x_tTau_bachelors_stdev = statistics.stdev(bachelors)
x_tTau_trade_stdev = statistics.stdev(trade_school)
x_tTau_graduate_stdev = statistics.stdev(graduate)
x_tTau_professional_stdev = statistics.stdev(professional)

education_cols = ["High School", "Bachelors", "Trade School", "Graduate", "Professional"]
mean_education_tTau = [x_tTau_hs_bar, x_tTau_bachelors_bar, x_tTau_trade_bar, x_tTau_graduate_bar, x_tTau_professional_bar]
stdev_education_tTau = [x_tTau_hs_stdev, x_tTau_bachelors_stdev, x_tTau_trade_stdev, x_tTau_graduate_stdev, x_tTau_professional_stdev]

f_stat, p_value = stats.f_oneway(high_school, bachelors, trade_school, graduate, professional)
print(f'f_stat ANOVA = {f_stat}, p_value ANOVA = {p_value}')

plt.text(0.5, 0.95, f"One-Way ANOVA: p = {p_value:.3f}", transform=plt.gca().transAxes, ha='right', va='top', fontsize=12)

yerr_education = [np.zeros(len(mean_education_tTau)), stdev_education_tTau]
plt.bar(education_cols, mean_education_tTau, yerr=yerr_education, capsize=10, color=["red", "blue", "pink", "skyblue", "orange"])
plt.title("tTau Levels by Highest Education Level")
plt.xlabel("Education Level")
plt.ylabel("tTau")
plt.show()