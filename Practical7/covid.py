import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/zhangxinyao/PYTHON/IBI1_2022-23/Practical7")
#change to the directory where the "full_data.csv" exists
print(os.getcwd())
print(os.listdir())
covid_data = pd.read_csv("full_data.csv")
print(covid_data.head(5))
#show the first five rows in the file
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
#define the new data as the data of new cases and new deaths around the world on 2020-03-31
column = [False,False,True,True,False,False]
print(np.mean(covid_data.loc[covid_data['date']=='2020-03-31',column]))
#the mean number of new cases and new deaths on 31 March 2020
print(37.928205/640.461538)
x=new_data.loc[new_data['location']!='world',"new_cases"]
y=new_data.loc[new_data['location']!='world',"new_deaths"]
plt.boxplot([x,y],vert=True,
            showfliers=False,
            showbox=True,
            showcaps=True,
            notch=False,
            whis=1.5,
            patch_artist=True,meanline=False,labels=["new cases","new deaths"])
plt.title('the new cases and new deaths on March 31th in 2020')
plt.show()
#draw the bloxplot about the new cases and new deaths in the world on 2020-03-31
world_date=covid_data.loc[covid_data['location']=='World',"date"]
world_data1=covid_data.loc[covid_data['location']=='World',"new_cases"]
plt.plot(world_date,world_data1,"c+")
#"b+" represents the color of the plot
world_data2=covid_data.loc[covid_data['location']=='World',"new_deaths"]
plt.plot(world_date,world_data2,"b+")
plt.xticks(world_date.iloc[0:len(world_date):4],rotation=-90)
plt.title('The new cases and new deaths in the world')
plt.xlabel("dates")
plt.ylabel("the number of new cases and deaths")
plt.show()
#xticks only keeps the dates every n days ago,rotation means the angle of the xticks with x axis
#start to answer the question
Australia_data=covid_data.loc[covid_data['location']=='Australia',:]
plt.plot(Australia_data.loc[:,"date"],Australia_data.loc[:,"total_cases"],"bo")
plt.plot(Australia_data.loc[:,"date"],Australia_data.loc[:,"total_deaths"],"ro")
Australia_dates=Australia_data.loc[:,"date"]
plt.xticks(Australia_dates.iloc[0:len(Australia_dates):4],rotation=-90)
plt.yticks([0,2000,4000,6000,8000,10000])
plt.title("Total cases and deaths in Australia")
plt.xlabel('date')
plt.ylabel('number')
plt.show()
