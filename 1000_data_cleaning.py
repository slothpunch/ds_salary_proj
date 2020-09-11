# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:23:44 2020

@author: GIS
"""
import pandas as pd

df = pd.read_csv('1000_glassdoor_jobs.csv')

# 1. salary parsing
# 2. Company name text only
# 3. state field
# 4. age of company
# 5. parsing of job description (Python, etc.)

# 1. salary parsing

# One line if statement
# hourly and employer_provided columns will be created 
# Per Hour or Employer Provided Salary: do not work.. why?
# just putting some part of them like 'per' instead of putting the whole thing 'per hour',works
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

# Call up data not -1 in Salary Estimate
df = df[df['Salary Estimate'] != '-1']
# Delete (Glassdorr est.)
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
# Delete K at the end and $ at the frot of Salary Estimate
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
# Make sure put lower() --> x.lower().replace().replace()
minus_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))
# Make it int. Before putting int(), its dtype = 'O'. After dtype = 'int64'
df['min_salary'] = minus_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2
# Run selection/current line F9
#df['min_salary'].dtype

# 2. Company name text only
# If rating is greather than 0, print Company Name, and also else Company Name. Because of [:-3], ratings at the end of each company name do not show up
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3], axis=1)

# 3. state field
# Chicago, IL x.split(',')[0] --> Chicago, x.split[','][1] --> IL
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])

# square breckets and dots are the same thing, but characters have to be typed, then the only option is using square breckets as we can type characters with a dot
#df.job_city.value_counts()

# Check if the locaiton is the same as the headquarter's location
#df['same_state'] = df.apply(lambda x: 1 if x.Location == x, Headquarters else 0, axis=1)

# 4. age of company
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 -x)

# 5. parsing of job description (Python, etc.)
# Checking descriptions
#df['Job Description'][0]

# Python -- 1 = 197, 0 = 148
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

# R
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() in x.lower() else 0)
df.R_yn.value_counts()

# Excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()

# AWS
df['AWS_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.AWS_yn.value_counts()

# SQL
df['SQL_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df.SQL_yn.value_counts()

#df.columns

#df_out = df.drop(['Unnamed: 0'], axis =1)
#df_out.to_csv('salary_data_cleaned.csv', index = False)

#df.to_csv('1000_salary_data_cleaned.csv', index = False)

#pd.read_csv('1000_salary_data_cleaned.csv')
