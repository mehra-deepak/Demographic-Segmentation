# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:49:04 2019

@author: Lenovo
"""
# IMPORTING THE OSURCE CODE

# importing the necessary libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# importing the dataset

dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:,1:14].values
y = dataset.iloc[:,13:].values