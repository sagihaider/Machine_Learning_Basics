import pandas as pd
import numpy as np
from scipy import stats

# Constructing a beer sales DataFrame
df = pd.DataFrame({'Billy Beer': [13884, 23008, 17883, 24435, 49938],
                   'Lucky Lager': [34565, 83938, 59437, 28843, 48285],
                   'Triple Bock': [39987, 35512, 23542, 37729, 36647]})
df


# Quick insights / descriptive statistics
df. describe()

# Computing the mean sales for each brand
df.mean()


# Calculate the 75% quartile
df.quantile(q=.75)

# Calculate the sample standard deviation
df.std()

# Calculate the population standard deviation
df.std(ddof=0)

#%% Using apply or Lambda Expression

# The same as calling .mean on the DataFrame
df.apply(np.mean)

np.mean(df)

# Specify a function to apply to the DataFrame
def zscore(series):
    result = (series - series.mean()) / series.std()
    return result

# Call Apply on the highest function
df.apply(zscore)



# The same result values as using scipy stats zscore with
# a dynamic degrees of freedom of 1 
stats.zscore(df, ddof=1)

# Calculate inter quartile range with a lambda expression
df.apply(lambda x: x.quantile(q=.75) - x.quantile(q=.25))