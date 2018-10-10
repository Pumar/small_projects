import math as mt
import pandas as pd

x=[]
y=[]
for i in range(0,10000):
    x.append(i)
    y.append(mt.exp(-x[i])*mt.cos(x[i]))

d = {'a' : x, 'b' : y}
df = pd.DataFrame(d,columns=['x','y'])

plot1 = df.plot(x=x,y=y,kind='scatter')
fig1 = plot1.get_figure()
fig1.savefig('exp.png')
