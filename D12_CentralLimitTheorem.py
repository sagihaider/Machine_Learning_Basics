# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from __future__ import division

# turn of data table rendering
pd.set_option('display.notebook_repr_html', False)

sns.set_palette(['#00A99D', '#F5CA0C', '#B6129F', '#76620C', '#095C57'])
np.version.full_version

#%% DATA

# One throw leads to one of four outcomes
data = np.array([1.0, 2.0, 3.0, 4.0])
data

# Our data has a perfect uniform distribution
p=sns.barplot(data=data)

# Calculate the population mean
population_mu = data.mean()
population_mu

# Calculate the standard deviation of the population
population_sigma = data.std(ddof=0)
population_sigma

#%% Illustration of Cnetral Limit Theorem

# Let's find out the number of possible outcomes with a sample size 2
possible_outcomes = 4**2
possible_outcomes

# Create a dataframe with the mean of all possible outcomes
mean_outcome_matrix = pd.DataFrame(index=data, dtype='float64', columns=data )

for x in data:
    for y in data:
        mean_outcome_matrix[x][y]=np.mean([x,y])
        
p=sns.heatmap(mean_outcome_matrix, annot=True)


# Now get the mean of all possible mean outcomes
sample_mean = mean_outcome_matrix.mean().mean()
sample_mean


# Note the mean of all possible mean outcomes 
# is exactly the same as the population mean!
population_mu == sample_mean


# Below a plot the sampling distribution of all possible mean outcomes
# Note that it's perfectly normal
diff_val_count = mean_outcome_matrix.stack().value_counts().count()
p=sns.distplot(mean_outcome_matrix.stack(), bins=diff_val_count)


#%% Standord error

# The standard deviation of the sampling distribution is called the standard Error (SE).
# Calculate the standard error (SE) of all possible mean outcomes
mean_outcomes_SE = mean_outcome_matrix.stack().std(ddof=0)
mean_outcomes_SE

# If we now calculate the ratio of sigma to SE
# we see it is the square root of 2
ratio_sigma_SE = population_sigma / mean_outcomes_SE
ratio_sigma_SE


# So if we square this ratio we get... our sample size (approximately)
ratio_sigma_SE ** 2

#%% Increasing the sample size

# When we take a larger sample to calculate the sampling mean, the resulting
# distribution will become more normal and skinny. Also, the mean of the sampling 
# distribution will match up more with the population mean. This effect is 
# illustrated in the example below.

# Let's simulate a population of a 1000 throws with a weighted 
# tetrahedral die (with a 40% chance of throwing a 4)
# The result is a negatively skewed distribution
non_normal_data = np.random.choice(data, 1000, p=[0.10, .20, .30, .4])
a = ['1', '2', '3', '4']
p=sns.barplot(non_normal_data)


# In this example we plot four sampling distributions of different
# sizes to show the effect of the increasing sample size.
# Note thst the distribution is getting more normal and skinny
# with an increased sample size.
f, (ax1, ax2) = plt.subplots(2, 2, sharex=True)
axes = [ax1[0], ax1[1], ax2[0], ax2[1]]
ax = 0

for sample_size in [2,5,20,100]:
    sampling_distribution = []
    for i in range(100):
        mean_sample = np.random.choice(non_normal_data, sample_size).mean()
        sampling_distribution.append(mean_sample)

    p=sns.distplot(sampling_distribution, ax=axes[ax], 
                   axlabel=str(sample_size) + ' samples, $\\bar{x}=$' + 
                   str(np.mean(sampling_distribution)))
    ax += 1
