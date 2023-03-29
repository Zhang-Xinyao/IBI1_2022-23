import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/zhangxinyao/PYTHON/IBI1_2022-23/Practical7")
print(os.getcwd())
print(os.listdir())
covid_data = pd.read_csv("full_data.csv")
print(covid_data.head(5))
print(covid_data.info())
print(covid_data.describe())
print(covid_data.iloc[0,1])
print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
print(covid_data.iloc[0:1001:100,1])
#the code  showing the second column from every 100th row from the first 1000 rows
print(covid_data.iloc[0:3,[0,1,3]])
my_columns = [True, True, False, True, False,False]
print(covid_data.iloc[0:3,my_columns])
print(covid_data.loc[2:4,"date"])
Afghanistan_row=covid_data['location']=='Afghanistan'
#"Afghanistan_row"  shows “total cases” for all rows corresponding to Afghanistan.
print(covid_data.loc[Afghanistan_row])
column = [False,True,True,True,False,False]
print(covid_data.loc[Afghanistan_row,column])
new_data=covid_data.loc[covid_data['date']=='2020-03-31',["location","new_cases","new_deaths"]]
column = [False,False,True,True,False,False]
print(np.mean(covid_data.loc[covid_data['date']=='2020-03-31',column]))
#the mean number of new cases and new deaths on 31 March 2020
print(37.928205/640.461538)
x=covid_data.loc[covid_data['date']=='2020-03-31',"new_cases"]
y=covid_data.loc[covid_data['date']=='2020-03-31',"new_deaths"]
plt.boxplot([x,y],vert=True,showfliers=False,showbox=True,showcaps=True,notch=False,whis=1.5,patch_artist=True,meanline=False,labels=["new cases","new deaths"])
plt.title('the new cases and new deaths on March 31th in 2020')
plt.show()
plt.plot(covid_data.loc[:,"date"],covid_data.loc[:,"new_cases"],"c+")
#"b+" represents the color of the plot
plt.plot(covid_data.loc[:,"date"],covid_data.loc[:,"new_deaths"],"b+")
world_dates=covid_data.loc[:,"date"]
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.title('The new cases and new deaths in the world')
plt.xlabel("dates")
plt.ylabel("the number of new cases and deaths")
plt.show()
#xticks only keeps the dates every n days ago,rotation means the angle of the xticks with x axis
#start to answer the question
Australia_data=covid_data.loc[covid_data['location']=='Australia',:]
plt.plot(Australia_data.loc[:,"date"],Australia_data.loc[:,"total_cases"],"b+")
plt.plot(Australia_data.loc[:,"date"],Australia_data.loc[:,"total_deaths"],"r+")
Australia_dates=Australia_data.loc[:,"date"]
plt.xticks(Australia_dates.iloc[0:len(Australia_dates):4],rotation=-90)
plt.title("Total cases and deaths in Australia")
plt.xlabel('date')
plt.ylabel('number')
plt.show()
