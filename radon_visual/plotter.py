import pandas as pd

df = pd.read_table('RAD7 3134 2018-10-10 (Comma Delineated).csv',sep=',', usecols = ['Full Date','Radon'])
df = df.rename(columns={'Full Date' : 'FullDate'})

plot = df.plot(x='FullDate',y='Radon')
fig = plot.get_figure()
fig.savefig('radon.png')
