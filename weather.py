
import pandas as pd
import numpy as np

file_read = 'weather.dat'

# use sep=\s+(regex) to use varying whitespace as the separator 
data = pd.read_table(file_read, sep='\s+')

df = pd.DataFrame(data)

# replace the asterix with an empty space
df = df.replace('\*','',regex=True)

# change to numerals
df = df.apply(pd.to_numeric, errors='coerce')

# get the difference between 'Mxt' and 'Mnt'
df['diff'] = df['MxT'] - df['MnT'] 

# store the maximum spread and the day
max_diff = df['diff'].max()

max_day = df.loc[df['diff'] == max_diff, 'Dy'].iloc[0]

#removing the decimal points.
print '{0:g}'.format(float(max_day)), '{0:g}'.format(float(max_diff))


