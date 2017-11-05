# SETUP
import pandas as pd
import numpy as np 

#%%  SIMPLE SERIES OBJECT
# Data as a list of integers.
data = [101, 4, 23, 8, 27, -3]
s1 = pd.Series(data)
type(s1)
s1

# If we pass values of different datatypes, pandas will upgrade the datatype to the 
# nearest posible type.
data = [101, 4.3, 5]
s1b = pd.Series(data)
s1b 

# The values of the Series.
s1.values
s1b.values

# The indices of the numpy.ndarray.
s1.index
s1b.index

s1[0]# this will return the position of the element
s1[2]

# insert the element into the desired location 
s1[2] = 404

#%% Perform operations

# Calculating the arithmetic average.
s1.mean()

# Calculate the cumulative sum.
s1.cumsum()

# Vector multiplication.
s1 * 3

# Logarithm


#%% Custom indices / labels

# Create custom labels for random values.
index = ['A', 'B', 'C', 'D', 'E', 'F']
data = np.random.randn(6)
data

s2 = pd.Series(data, index)

s2.name='Price'
s2.index.name='Stock'

#%% Series from a dictionary

# Series from dictionary is (of course) not ordered. Keys are used for the index.
d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
s4 = pd.Series(d)
s4

# Slicing based on index
s4[1:3]

# Slicing based on labels
s4['four':'three']

#%% Enumeration

# looping over collection
for i,v in enumerate(s1):
    print(i, v)


# list comprehension
s4b = [x**2 for x in s4]
s4b


#%% DICT LIKE behaviour

# is the key in the series
'four' in s4
'seven' in s4

# custom index retrieval
s4['four']

# custom index assignament
s4['four'] = 999
s4['four']

# Convert Series to a dictionary (looses order).
d4 = s4.to_dict()
d4

# ... and back again (only when found a index mapping - type float!)
s4b = pd.Series(d4, index=['one', 'two', 'three', 'six', 'seven'])
s4b

#%% Munging

s4nan = s4b.isnull()
s4nan

# Extract the NaN's from the Series
s4b[s4nan]

# Drop the NaN's
s4b = s4b.dropna()
s4b


















