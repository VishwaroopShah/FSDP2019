# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:49:23 2019

@author: TAPAN
"""

"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""



import numpy as np
import matplotlib.pyplot as plt


incomes = np.random.normal(100.0, 20.0, 10000)
plt.hist(incomes,50)

print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

income=np.append(incomes,500)

plt.hist(income,50)

print("Mean value is: ", np.mean(income))
print("Median value is: ", np.median(income))