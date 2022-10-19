2##intro to pandas
##taylor powell
##notes

##-----------------------------------------##
##import
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

size =1
location = ['a','b','c','d','e']
location = location*4
rain = np.random.randint(0,10,len(location))
snow = np.random.randint(0,50,len(location))

##print(location)
##print(rain)
##print(snow)
##

weather = list(zip(location,rain,snow))
weather_f = pd.DataFrame(data=weather,columns=['location','rain','snow'])

print(weather_f)


hail = np.random.randint(0,5,len(location))

weather_f['hail']=hail
weather_f['hail'] += 1

##weather_f.columns = ['m','n','o','p']
##weather_f.index['i','ii','iii','iv']
##print(weather_f.columns[:])

print(weather_f.iloc[3:10])
print(weather_f[['snow','hail']])
print(weather_f.loc[weather_f.index[3:10],['snow','hail']])
newfile = weather_f.loc[weather_f.index[3:10],['snow','hail']]

print(newfile)

print(newfile is weather_f)





##weather_f.to_csv('weatherr.csv',index=True,header=True)
##
##rweather = pd.read_csv('weatherr.csv',names=['location','snow'])
##
##print(rweather)

##sort the snowfall
##sort_weather = weather_f.sort_values(['snow'],ascending=False)
##
##
##
##print(sort_weather.head())
##print(sort_weather.tail())
##print(sort_weather.max())
##print(sort_weather['snow'].max())
##print(sort_weather['location'].unique())
##
####two steps
##gloco = weather_f.groupby('location')
####totals = gloco.sum()
####print(totals)
##
####single step
##totals = weather_f.groupby('location').sum()
##print(totals)
##
##print(weather_f.describe())
##
##sort_weather.plot(x='location',y=['snow','rain'],kind='line',color=['green','blue'])
##
##sort_weather.plot(y='snow',kind='hist', bins=10,color='green')
##
##plt.show()
##
##        
##
