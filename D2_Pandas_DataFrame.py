import pandas as pd
import numpy as np
import datetime

# turn of data table rendering (of the 90s)
pd.set_option('display.notebook_repr_html', False)

#%% Creating a DataFrame

# Collection of data columns
s1 = np.random.randn(5)
s2 = [True, True, False, True, False]
s3 = ['Apple', 'Banana', 'Tomato', 'Bean', 'Rice']

# Dict with added column names
data = {'Randnum': s1, 'IsBool': s2, 'Name': s3}
df=pd.DataFrame(data)

# Create a new column and assign it all 127
df['New'] = 127
df

# Select the first three rows
df[:3]

# Select the second row
df.ix[1]


# Select the Randnum value of the second row
df.ix[1, 2] # or
df.ix[1, 'Randnum']

# Select specific row and column
df.ix[1:3,0:3]

# Selecting specific rows and columns
df.ix[[0, 2, 6], ['Name', 'Randnum', 'Unknown']]

#%% Conditions

# Retrieve boolean Series, True if Randnum is smaller than zero
belowzero = df.Randnum < 0
belowzero

# Selects all rows meeting the belowzero condition
df[belowzero]

# Retrieve boolean Series, True if Randnum is smaller than zero
isapple = df['Name'] == 'Apple'
isapple

# Select belowzero AND isapple conditions
df[belowzero & isapple]

#%% Date range as an index

# Set the index to a date range
df.index = pd.date_range('1-1-2015', periods=5, freq='m')
df.index.name = 'Date'
df


#%% Nested Dictornary to DataFrame


# Create a nested dictionary of equal inner value-count
data = {'Paris': {'N': 1.2, 'E': 4, 'S': 2.9, 'W': 0.8},
        'Amsterdam': {'N': 2.3, 'E': 1.7, 'S': 2.1, 'W': 7.2},
        'London': {'N': 9.7, 'E': 3.1, 'S': 7.2, 'W': 2}}

df2 = pd.DataFrame(data)
df2






















