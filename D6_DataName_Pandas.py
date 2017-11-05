import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# turn of data table rendering
pd.set_option('display.notebook_repr_html', False)
plt.style.use('ggplot')
pd.__version__

#%%  READ DATA from CSV file
# Reading stock data from csv. Used in a pandas tutorial by Wes McKinney. 
names_df = pd.read_csv('Data/baby-names2.csv')
names_df.head() # see the header of the data frame


#%%   Explore the data

# Get popular names for 1969
names_df[names_df.year == 1969].tail()

# Separate the boys from the girls
boys_df=names_df[names_df.sex=='boy'] # get boys into a new data frame
girls_df=names_df[names_df.sex=='girl'] # get girls into a new data frame
boys_df.head() # get header of boys
girls_df.head() # get header of girls

# Get the number of boy baby name rows per year (showing first 5)
boys_df.groupby('year').size()

# Get the hierarchical index of baby name rows per year 
# grouped by gender for the year 1969
names_df.groupby(['year','sex']).size().ix[1969]

# Get the most popular boy name for the year 1969
rowid_b = boys_df[boys_df.year == 1969].prop.idxmax()
rowid_g = girls_df[girls_df.year == 1969].prop.idxmax()
boys_df.ix[rowid_b]
girls_df.ix[rowid_g]

# Apply the get_max_proportion to the whole dataframe
# to get the most popular name for each year (showing first 5)
def get_max_proportion(group):
    return group.ix[group.prop.idxmax()]

popular_boys_df=boys_df.groupby('year').apply(get_max_proportion)
popular_boys_df.tail()


#%% PLOT the proportion of the most popoular boy name per year
# may be showing more diversity in chosen boy names over time

popular_boys_df.prop.plot(legend=True, title='Proportion most boy name', kind='area')
