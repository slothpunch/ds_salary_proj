# -*- coding: utf-8 -*-
"""
Created on Sat May 23 22:24:19 2020

@author: GIS
"""

import glassdoor_scraper_No_Head_Comp as gs
import pandas as pd

path = "D:/Kaggle/0. Data_Science_Salaries/ds_salary_proj/chromedriver"

df = gs.get_jobs("data scientist", 1000, False, path, 15)

df.to_csv('1000_glassdoor_jobs.csv', index=False)