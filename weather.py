import pandas as pd

df = pd.read_csv('weather.dat', sep='\s+')
df[['MxT', 'MnT']] = df[['MxT', 'MnT']].apply(lambda x: x.str[:2].astype(int))
a = df.MxT - df.MnT
b = a.index[a==max(a)].tolist()
print df.loc[b][['Dy', 'MxT', 'MnT']].unstack().tolist()

