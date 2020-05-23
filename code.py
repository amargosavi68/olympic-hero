# --------------
import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt


#reading data from csv file using path
data = pd.read_csv(path)

data = pd.DataFrame(data)

#Rename the 'Total' column
data.rename(columns={'Total':'Total_Medals'},inplace=True)

#Displaying first 10 records
print(data.head(10))


# --------------
#Code starts here
#Creating new column 'Better_Event' 
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')

data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event'])

# store better event in 'better_event' variable
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here

top_countries = pd.DataFrame(data,columns=['Country_Name','Total_Summer','Total_Winter','Total_Medals'])
last_row = len(top_countries)-1
top_countries.drop(index=last_row,axis=0,inplace=True)

#defining a top_ten() function
def top_ten(top_countries,column_name):
    country_list=[]
    top = top_countries.nlargest(10,column_name)
    country_list = list(top['Country_Name'])
    return country_list

#calling top_ten() for respective columns
top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')

#printing those list
print(top_10_summer)
print(top_10_winter)
print(top_10)

common = list(set(top_10_summer).intersection(top_10_winter).intersection(top_10))
print(common)





# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

plt.figure()
x = summer_df['Country_Name']
y = summer_df['Total_Medals']

plt.bar(x,y)
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.xticks(rotation=90)
plt.show()

plt.figure()
x = winter_df['Country_Name']
y = winter_df['Total_Medals']

plt.bar(x,y)
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.xticks(rotation=90)
plt.show()

plt.figure()
x = top_df['Country_Name']
y = top_df['Total_Medals']

plt.bar(x,y)
plt.xlabel('Country Name')
plt.ylabel('Total Medals')
plt.xticks(rotation=90)
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']

summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold=summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']

winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold=winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']

top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold=top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']




# --------------
#Code starts here
data.drop(index =(len(data)-1),axis=0,inplace=True)
data_1=data

data_1['Total_Points'] = ((data_1['Gold_Total']*3) + (data_1['Silver_Total']*2) + (data_1['Bronze_Total']))
most_points=max(data_1['Total_Points']) 
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']




# --------------
#Code starts here
best=data[data['Country_Name']==best_country]

best=best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


