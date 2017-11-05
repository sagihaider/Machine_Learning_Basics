import pandas as pd
import numpy as np

## turn of data table rendering
#pd.set_option('display.notebook_repr_html', False) 
#
## This function is to show two data structures side by side
## Used in Web McKinney's presentations: http://www.youtube.com/watch?v=w26x-z-BdWQ
#def side_by_side(*objs, **kwds):
#    from pandas.core.common import adjoin
#    space = kwds.get('space', 4)
#    reprs = [repr(obj).split('\n') for obj in objs]
#    print(adjoin(space, *reprs))
    

# Reading stock data from csv. Used in a pandas tutorial by Wes McKinney. 
df = pd.read_csv('../data/stock_data.csv', index_col=0, parse_dates=True)

# Take a look at the last 5 rows
df.tail()

# Query the number of rows
len(df)

# Slices of the DataFrame of IBM stock
s1=df.IBM[10:20]
s2=df.IBM[5:15]    
print(s1.head)
print(s2.head)

# Union (of the index) and sum where both values are not NaN
print(s1 + s2)

# Same thing but now stripped of the NaN values
print((s1 + s2).dropna())

#%% Allign

# Align s1 and s2 with an outer join = default
a, b = s1.align(s2, join='outer')

# Align s1 and s2 with an inner join
a, b = s1.align(s2, join='inner')

# Align s1 and s2 with a left join
a, b = s1.align(s2, join='left')