import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import math
from __future__ import division

# turn of data table rendering
pd.set_option('display.notebook_repr_html', False)

sns.set_palette(['#00A99D', '#F5CA0C', '#B6129F', '#76620C', '#095C57'])
np.version.full_version
#%%  Data
# Load the data from a csv file
data = pd.read_csv('data/klout-scores.csv', header=None, names=['scores'])
data.head()

p=sns.distplot(data.scores)

# Sample size
n = data.scores.count()

# The confidence coefficient
confidence_coef = .95

# The alpha level
alpha = 1. - confidence_coef

# First we need our sample mean
# This is called the point estimate
klout_xbar = data.scores.mean()
klout_xbar


# We also need the standard error of the sample
# Since our sample size is large (> 30) we can use
# the sample standard deviation as an approximation of sigma
klout_s = data.scores.std()
klout_s

# The we need to find the z score to calculate the
# lower and upper bound of our confidence interval
# This is called the critical value
critical_value = stats.norm.ppf(alpha / 2) * -1.
critical_value

# An easier way to get the critical values calling scipy.stats
# interval function. The alpha .95 being a littbe bit misleading since
# it is not our alpha but our confidence coefficient
zscore_interval = stats.norm.interval(alpha=confidence_coef)
zscore_interval


# We need the standard error to calculate the bounds
klout_SE = klout_s / math.sqrt(n)
klout_SE


# Calculate the lower and upper bound Klout Score 
# for the confidence interval
klout_CI_mean_lower = klout_xbar - critical_value * klout_SE
klout_CI_mean_upper = klout_xbar + critical_value * klout_SE
klout_CI_mean_lower, klout_CI_mean_upper

#%% THE EFFECT OF SAMPLE SIZE
# Let's create a sample of 50 random Klout Scores
n_50 = 50
data_50 = data.ix[np.random.choice(data.index, n_50)]
data_50.head()

# Plot the sample and note a similar bimodal distribution shape
p=sns.distplot(data_50.scores)

# Get the point estimate
klout_50_xbar = data_50.scores.mean()
klout_50_xbar

# Get the sample standard deviation as an approximation of sigma
klout_50_s = data_50.scores.std()
klout_50_s

# Calculate the standard error for this sample size
klout_50_SE = klout_50_s / math.sqrt(n_50)
klout_50_SE


# Calculate the lower and upper bound Klout Score 
# for the confidence interval of our sample of n=50
klout_50_CI_mean_lower = klout_50_xbar - critical_value * klout_50_SE
klout_50_CI_mean_upper = klout_50_xbar + critical_value * klout_50_SE
klout_50_CI_mean_lower, klout_50_CI_mean_upper