# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from __future__ import division

sns.set_palette(['#00A99D', '#F5CA0C', '#B6129F', '#76620C', '#095C57'])
np.version.full_version


#%% Data

#We use a fictional data set of 10000 averge number of Facebook friends.
facebook_mu = 190.0
facebook_sigma = 36.0
facebook_friends = np.random.normal(facebook_mu, facebook_sigma, 10000)

# show first 12 samples
facebook_friends[:12]

# First take a look at the pdf and especially the green area under
# the curve containing the probability of 227 Facebook friends or less.
x = 227.0
sns.distplot(facebook_friends, label='Facebook friends', kde=False, 
             fit=stats.norm, color='y')
plt.text(x+5, .0003, '$x$='+str(x))
x_plot = np.linspace(min(facebook_friends), x, 1000)
y_plot = stats.norm.pdf(x_plot, facebook_mu, facebook_sigma)
plt.fill_between(x_plot,  y_plot)
c=plt.legend()


# To calculate the probability, we need the z score.
zscore = (x - facebook_mu) / facebook_sigma
zscore
# Calculate the probability by calling stats.norm.cdf
# This is a computational z table lookup
p = stats.norm.cdf(zscore)
p

# Probability of having a value more than 227
1 - p


#%% From probability back to the actual value
 # Let's assume we have a 21% chance of having a certain number of Facebook 
 # friends or more. What is the minimum number of Facebook friends 
 # we have in this case?
 
 # We use the ppf function (inverse cdf) - from probability to z score
p = 1 - .21
z = stats.norm.ppf(p)
z

# From z score to number of Facebook friends
x = z * facebook_sigma + facebook_mu

# The green area under the curve containing the probability 
# of (roughly) 206 Facebook friends or more.
sns.distplot(facebook_friends, label='Facebook friends', kde=False, 
             fit=stats.norm, color='y')
plt.text(x+5, .0003, '$x$='+str(int(x)))
x_plot = np.linspace(x, max(facebook_friends), 1000)
y_plot = stats.norm.pdf(x_plot, facebook_mu, facebook_sigma)
plt.fill_between(x_plot,  y_plot)
c=plt.legend()

#%% Calculate probability in between two values
# We want to know the proportion of the green area under the curve.
x1 = 120.0
x2 = 170.0
sns.distplot(facebook_friends, label='Facebook friends', kde=False, 
             fit=stats.norm, color='w')
plt.text(x1+5, .0003, '$x_1$='+str(x1))
plt.text(x2+5, .0003, '$x_2$='+str(x2))
x_plot = np.linspace(x1, x2, 1000)
y_plot = stats.norm.pdf(x_plot, facebook_mu, facebook_sigma)
plt.fill_between(x_plot,  y_plot)
c=plt.legend()

# First we need the z score of x1
z1 = (x1 - facebook_mu) / facebook_sigma
z1

# Then we calculate the probability for value x1 or less
p1 = stats.norm.cdf(z1)
p1


# Now we calculate the z score for x2
z2 = (x2 - facebook_mu) / facebook_sigma
z2

# and agian the probabilty for value x2 or less
p2 = stats.norm.cdf(z2)
p2

# So the probability of having between x1 and x2 Facebook friends is
# the probability having x2 minus the probability having x1
p2 - p1





