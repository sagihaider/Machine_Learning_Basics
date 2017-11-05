
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

# turn of data table rendering
pd.set_option('display.notebook_repr_html', False)
plt.style.use('ggplot')
pd.__version__

#%% Data

data=pd.DataFrame({'Salaries': [33219, 36254, 38801, 46335, 46840, 
                      47596, 55130, 56863, 78070, 88830]})

data

#%%
data.plot(kind = 'bar', color='red', alpha=0.8)

# To calculate the population variance
n=len(data.Salaries)
mean=data.Salaries.mean()

#sum up the sqaured differnce from the mean
std=0
for v in data.Salaries:
    std += (v - mean) ** 2
    
pop_variance=std/n    
pop_variance

# To calculate the variance if we only have a sample
# First calculate the degrees of freedom (apply Bessel's correction)
dof = n - 1
sample_variance = std / dof
sample_variance


# Of course we can use pandas to let NumPy do the job for us
# The ddof parameter stands for Delta Degrees of Freedom
population_variance = data.Salaries.var(ddof=0)
sample_variance = data.Salaries.var() # ddof=1 by default in pandas
population_variance, sample_variance


# Or call the NumPy var function ourselves
population_variance = np.var(data.Salaries) # ddof=0 by default in NumPy
sample_variance = np.var(data.Salaries, ddof=1)

population_variance, sample_variance


#%%   Calculate the Standard Deviation


# To calculate the population standard deviation
# we first need to calculate the population variance again
n = len(data.Salaries)

# first calculate the mean
mean = data.Salaries.mean()

# Sum up the squared differences from the mean
squared_deviations = 0
for v in data.Salaries:
    squared_deviations += (v - mean) ** 2

population_variance = squared_deviations / n

# Square the variance
population_standard_deviation = math.sqrt(population_variance)
population_standard_deviation


# To calculate the sample standard deviation
# First calculate the degrees of freedom (apply Bessel's correction)
dof = n - 1
sample_variance = squared_deviations / dof

# Square the variance
sample_standard_deviation = math.sqrt(sample_variance)
sample_standard_deviation


# Now let's use pandas to let NumPy do the job for us
population_standard_deviation = data.Salaries.std(ddof=0)
sample_standard_deviation = data.Salaries.std()

population_standard_deviation, sample_standard_deviation


# Or call the NumPy std function ourselves
population_standard_deviation = np.std(data.Salaries)
sample_standard_deviation = np.std(data.Salaries, ddof=1)

population_standard_deviation, sample_standard_deviation
