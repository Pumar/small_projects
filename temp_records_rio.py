import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d13/570fb18cde0c9766865e6670ce2c11b0562a81415c535e51441176a2.csv')
df = df.set_index('Date').sort_index()


d = {}
for row in df.itertuples():
    if row[0] not in d.keys():
        d[row[0]] = [row[-1]]
    else:
        d[row[0]] += [row[-1]]
date = []
tmax = []
tmin = []
for key in d.keys():
    date.append(key)
    tmax.append(max(d[key]))
    tmin.append(min(d[key]))
observation_dates = list(map(pd.to_datetime,date))
tmax = [float(x)/10 for x in tmax]
tmin = [float(x)/10 for x in tmin]



dtmax = zip(observation_dates,tmax)
dtmin = zip(observation_dates,tmin)

szmax = sorted(dtmax, key=lambda x: x[0])
szmin = sorted(dtmin, key=lambda x: x[0])

szmax = list(zip(*szmax))
szmin = list(zip(*szmin))

sdate = list(szmax[0])
stmax = list(szmax[1])

stmin = list(szmin[1])


records_in_2016 = []

for e in sdate:
    di = sdate.index(e)
    if e.day == 29 and e.month ==2:     
        del sdate[di]
        del stmax[di]
        del stmin[di]

year_max = []
year_min = []
historical_max = []
historical_min = []

for i in range(0,11):
    year_max.append(stmax[i*365:(i+1)*365])
    year_min.append(stmin[i*365:(i+1)*365])
for i in range(0,365):
    daily_max = []
    daily_min = []
    for j in range(0,len(year_max)-1):
        daily_max.append(year_max[j][i])
        daily_min.append(year_min[j][i])
    historical_max.append(max(daily_max))
    historical_min.append(min(daily_min))
    

    


scatter_high = []
scatter_low = []
record_high = year_max[-1]
record_low = year_max[-1]


for t in range(len(record_high)):
    if record_high[t] > historical_max[t]:
        scatter_high.append((record_high[t],sdate[t]))
for t in range(len(record_low)):
    if record_low[t] < historical_min[t]:
        scatter_low.append((record_low[t],sdate[t]))

"""No records for low temperature comparing to previous years """
xaxis = [v for d, v in scatter_high]
yaxis = [d for d, v in scatter_high]

xaxis = dates.date2num(xaxis)

plt.figure()
ax = plt.gca()
hfmt = dates.DateFormatter('%m')
ax.xaxis.set_major_formatter(hfmt)
ax.xaxis_date()

plt.tick_params(
    axis='both',          
    which='both',      
    bottom='off',      
    top='off',         
    labelbottom='on',
    left = 'off')

plt.title('Temperature data around Rio de Janeiro, Brazil.\n Historical highs and lows between 2005-2015')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Month')
ax.set_ylabel('Temperature')
plt.plot(sdate[:364],historical_max[:-1],c='r',alpha=0.8)
plt.plot(sdate[:364],historical_min[:-1],c='b',alpha=0.8)
plt.scatter(xaxis,yaxis,c='k',s=10,label='Temperature records broken in 2016')
plt.gca().fill_between(sdate[:364],
                      historical_min[:-1],historical_max[:-1],
                      facecolor='y',
                      alpha=0.25)

plt.legend(loc=10)
plt.show()