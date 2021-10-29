# read from an access.log file in to a dataframe - assuming the delimiter is ''
#  helen o'shea
# 20210318

import pandas as pd
import matplotlib.pyplot as plt

log = '../../../cybersecurity/IDR/Splunk/Splunk/Splunk - tutorialdata/www1/access.log'
names = ['ip', 'dash1', 'userId', 'time', 'url', 'status code', 'size of response', 'referer', 'iser agent', 'dunno' ]
df = pd.read_csv(log, sep=' ', header=None, names =  names )
print(df)

print(df.iloc[0])
df.head()
df.drop(columns = ['dash1', 'userId'], inplace=True)
df['time'].replace(r'\[','', inplace=True, regex=True)
df['time'].replace(r'\]','', inplace=True, regex=True)
print(df['time'].head())
print(df.dtypes)
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')

start_time = pd.to_datetime('2021/02/01 18:22:16')
end_time = pd.to_datetime('2021/02/08 18:20:56')

dfbetween=df.loc[(df['time'] > start_time) & (df['time'] < end_time)]
print(dfbetween['time'].head())
print(dfbetween['time'].tail())

df = df.set_index(['time'])
meanSize = df['size of response'].resample(rule='30Min')
print(meanSize.mean())


plt.title("Mean downloads per 30 minutes")
plt.xlabel("date")
plt.ylabel("mean response size per 30 min")
meanSize.mean().plot()
plt.show()