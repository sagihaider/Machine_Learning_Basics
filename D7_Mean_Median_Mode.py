# -*- coding: utf-8 -*-
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# turn of data table rendering
pd.set_option('display.notebook_repr_html', False)
plt.style.use('ggplot')
pd.__version__

#%%  Load Data

# Load 248 days of step data and vivofit goals
data = pd.read_csv('Data/garmin-vivofit.csv', index_col='date')
data.head()

#%% Plot the steps and goal data
data.steps.plot(kind='area', figsize=(8,5),color='green',alpha=0.5)
data.goal.plot()
plt.ylabel('steps per day')
plt.legend(loc='upper left')

#%% Calculate mean

x,n=0.0,0

for number_of_steps in data.steps:
    x=x+number_of_steps
    
n=len(data.steps)    
mean=x/n
mean

# We can also let pandas use NumPy's mean function to do the job
data.steps.mean()

# use numpy to get the mean
np.mean(data.steps)

# use pandas to get the mean
data.mean()

# Plot the mean, togehter with the steps and goal data
data.steps.plot(kind='area', color='#00A99D', alpha=.5, figsize=(8,5))
data.goal.plot(legend=True)
plt.plot([0, len(data.steps)],[mean, mean])
plt.ylabel('steps per day')
plt.text(25, mean-1200, r'$\mu=' + str(int(math.floor(mean))) + '$', fontsize=14)
plt.legend(loc='upper left')


#%% MEDIAN 

median, n = 0.0, 0

# Get the number of observations
n = len(data.steps)
    
# order the data
ordered_data = data.steps.order()

if n % 2 == 0:
    # n is even
    m1 = ordered_data.ix[(n - 2) / 2]
    m2 = ordered_data.ix[(n / 2)]
    median = (m1 + m2) / 2.0
else:
    # n is odd
    median = ordered_data.ix[(n - 2) / 2.0]

median

# Again, we can let pandas use NumPy's median function to do the job
data.steps.median()

# Or we can call NumPy's median function ourselves
np.median(data.steps)

# Use pandas to get the median for all columns at ones
data.median()

#%% MODE
# Let's create a lambda that assigns a bucket of size 1000 steps
# to each of the step count in the data set
bucket_size = 1000
bucket_calculator = lambda x: int(x) / bucket_size * bucket_size

data['bucket'] = data.steps.apply(bucket_calculator)
bucket_min = data.bucket.min()
bucket_max = data.bucket.max()
bins = (bucket_max-bucket_min)/bucket_size

data.bucket.hist(color='#00A99D', alpha=.5, bins=int(bins), figsize=(8,5))
