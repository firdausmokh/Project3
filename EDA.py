# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:36:28 2024

@author: Firdaus Mokhtar
"""

import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#load data into python
data = pd.read_excel(r"C:\Users\Firdaus Mokhtar\OneDrive\360TMG\Project 3\clean data.xlsx")
data.info()

### Break the table into 2 main column ######

turbine_failure = data[(data['Failure_status'] == 'Failure')]
turbine_failure.info

no_turbine_failure = data[(data['Failure_status'] == 'No_failure')]
no_turbine_failure.info

##### Drop Date and Failure status column ##############

turbine_failure = turbine_failure.drop('date', axis = 1)
turbine_failure = turbine_failure.drop('Failure_status', axis = 1)

no_turbine_failure = no_turbine_failure.drop('date', axis = 1)
no_turbine_failure = no_turbine_failure.drop('Failure_status', axis = 1)

###### Find the outlier from each column ##############

# Turbine failure

for column in turbine_failure.columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(turbine_failure[column])
    plt.title(f'Boxplot of {column}')
    plt.show()
    
# No Turbine Failure

for column in no_turbine_failure.columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(no_turbine_failure[column])
    plt.title(f'Boxplot of {column}')
    plt.show()
    
######## Check the normal distribution ###########

sns.histplot(turbine_failure['Wind_speed'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Wind_speed'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Power'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Power'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Nacelle_ambient_temperature'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Nacelle_ambient_temperature'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Generator_bearing_temperature'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Generator_bearing_temperature'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Gear_oil_temperature'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Gear_oil_temperature'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Ambient_temperature'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Ambient_temperature'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Rotor_Speed'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Rotor_Speed'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Nacelle_temperature'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Nacelle_temperature'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Bearing_temperature)'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Bearing_temperature)'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Generator_speed'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Generator_speed'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Yaw_angle'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Yaw_angle'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Wind_direction'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Wind_direction'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Wheel_hub_temperature'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Wheel_hub_temperature'], kde=True, color='orange', label='No Fail', alpha=0.5) 

sns.histplot(turbine_failure['Gear_box_inlet_temperature'], kde=True, color='blue', label= 'Fail', alpha=0.5)
sns.histplot(no_turbine_failure['Gear_box_inlet_temperature'], kde=True, color='orange', label='No Fail', alpha=0.5) 

############## Statistical Analysis (EDA) ###########################

#### TURBINE FAILURE DATA #####
# 1st moment / measures for central tendency
# mean, median, and mode

for column in turbine_failure.columns:
    mean_value = turbine_failure[column].mean()
    print(f'The mean value of {column} is {mean_value}')
    
for column in turbine_failure.columns:
    median_value = turbine_failure[column].median()
    print(f'The median value of {column} is {median_value}')

for column in turbine_failure.columns:
    mode_value = turbine_failure[column].mode()
    print(f'The mode value of {column} is {mode_value}')

# 2nd moment / measures of dispersion
# variance, standard deviation, and range (max and min)

for column in turbine_failure.columns:
    var_value = turbine_failure[column].var()
    print(f'The variance value of {column} is {var_value}')
    
for column in turbine_failure.columns:
    std_value = turbine_failure[column].std()
    print(f'The standard deviation value of {column} is {std_value}')

for column in turbine_failure.columns:
    range_value = turbine_failure[column].max() - turbine_failure[column].min()
    print(f'The range value of {column} is {range_value}')

# 3rd moment / skewness

for column in turbine_failure.columns:
    skew_value = turbine_failure[column].skew()
    print(f'The skewness value of {column} is {skew_value}')
    
# 4th moment / kurtosis

for column in turbine_failure.columns:
    kurt_value = turbine_failure[column].kurt()
    print(f'The kurtosis value of {column} is {kurt_value}')
    
#### NO TURBINE FAILURE DATA #####
# 1st moment / measures for central tendency
# mean, median, and mode

for column in no_turbine_failure.columns:
    mean1_value = no_turbine_failure[column].mean()
    print(f'The mean value of {column} is {mean1_value}')
    
for column in no_turbine_failure.columns:
    median1_value = no_turbine_failure[column].median()
    print(f'The median value of {column} is {median1_value}')

for column in turbine_failure.columns:
    mode1_value = turbine_failure[column].mode()
    print(f'The mode value of {column} is {mode1_value}')

# 2nd moment / measures of dispersion
# variance, standard deviation, and range (max and min)

for column in no_turbine_failure.columns:
    var1_value = no_turbine_failure[column].var()
    print(f'The variance value of {column} is {var1_value}')
    
for column in no_turbine_failure.columns:
    std_value = no_turbine_failure[column].std()
    print(f'The standard deviation value of {column} is {std_value}')

for column in no_turbine_failure.columns:
    range1_value = no_turbine_failure[column].max() - no_turbine_failure[column].min()
    print(f'The range value of {column} is {range1_value}')

# 3rd moment / skewness

for column in no_turbine_failure.columns:
    skew1_value = no_turbine_failure[column].skew()
    print(f'The skewness value of {column} is {skew1_value}')
    
# 4th moment / kurtosis

for column in no_turbine_failure.columns:
    kurt1_value = no_turbine_failure[column].kurt()
    print(f'The kurtosis value of {column} is {kurt1_value}')
    
########## Hypothesis Testing ##################

# Chiq Squared test
from scipy.stats import chi2_contingency

data1= pd.read_excel(r"C:\Users\Firdaus Mokhtar\OneDrive\360TMG\Project 3\binned data.xlsx")

# 1. Create a contingency table
contingency_table = pd.crosstab(data1['Binned_WindSpeed'], data1['Failure_status'])

# 2. Perform the Chi-Square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# 3. Output results
print(f"Chi-Square Statistic: {chi2}")
print(f"P-value: {p}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

# 4. Interpret the result
if p < 0.05:
    print("Reject the null hypothesis. There is a significant relationship between wind speed and turbine failure.")
else:
    print("Fail to reject the null hypothesis. There is no significant relationship between wind speed and turbine failure.")

# Loop over each columns
for column in data1.columns:
    print(f"\nAnalyzing factor: {column}")
    
    # 1. Create a contingency table
    contingency_table = pd.crosstab(data1[column], data1['Failure_status'])
    
    # 2. Perform the Chi-Square test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    # 3. Output results
    print(f"Chi-Square Statistic: {chi2}")
    print(f"P-value: {p}")
    print(f"Degrees of Freedom: {dof}")
    print("Expected Frequencies:")
    print(expected)
    
    # 4. Interpret the result
    if p < 0.05:
        print(f"Reject the null hypothesis. There is a significant relationship between {column} and turbine failure.")
    else:
        print(f"Fail to reject the null hypothesis. There is no significant relationship between {column} and turbine failure.")




