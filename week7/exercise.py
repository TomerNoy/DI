import numpy as np

def npf(start, length, stop):
    print(np.arange(0,length)*stop+start)
npf(6, 100, 4)
    

a = np.array([1,2,3,np.nan,5,6,7,np.nan])
a
a = a[~ np.isnan(a)]
a

a = np.random.randint(1, 100, size=(5, 6))
a

x = np.amax(a, 1)
x


import pandas as pd

series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
series

series.unique()
series.value_counts()

series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
series

from dateutil.parser import parse

date_series = series.map(lambda x : parse(x))

for date in date_series:
    print(date.day, date.week, date.day_of_year, date.day_of_week)

url="https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv"
c=pd.read_csv(url)
c

c.dtypes.value_counts()

c.rename(columns= {'Type':'TypeOfCar'})

c.head()

c.isnull().sum()
c.isnull().sum().max()

# c.drop(columns = ['EngineSize', 'Length'], axis = 1)

columns = ['EngineSize', 'Length']
c.drop(columns, inplace=True, axis=1)

# option 2: c = c.drop(columns= columns)

c.isnull().sum()

df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})


df = df1.merge(df2)
df
# not sure i understood the question, would have helped to show the desired output

df = pd.DataFrame(["STD,City\tState",
"33,Kolkata\tWest Bengal",
"44,Chennai\tTamil Nadu",
"40,Hyderabad\tTelengana",
"80,Bangalore\tKarnataka"], columns=['row'])
df

# for x in range(len(df.values)):
#     print(x, df.values[x][0])
col1 =[]
col2 =[]
col3 =[]

for x in df.values:

    col1.append(x[0].split()[0].split(',')[0])
    col2.append(x[0].split()[0].split(',')[1])
    col3.append(x[0].split('\t')[1])


df2 = pd.DataFrame({'col1': col1, 'col2': col2, 'col3': col3})

df2




names = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"]
df_mpg = pd.read_csv("auto-mpg.data", header=None, names=names, delim_whitespace=True)
df_mpg

import matplotlib.pyplot as plt

def scatter_plot(df):
    plt.scatter(df['displacement'],df['acceleration'])

scatter_plot(df_mpg)



def bar_plot(df):
    sorted_By_cyl = df.sort_values('cylinders')
    cylinders = sorted_By_cyl['cylinders'].unique()
    
    list_78_cylinders_count = []
    list_toyota_cylinders_count = []
    
    all_78 = df[(df['model_year'] == 78)]
    toyota = df[df['car_name'].str.contains('toyota')]
    
    for i in cylinders:
        list_78_cylinders_count.append(all_78[all_78['cylinders'] == i].count()['cylinders'])
        list_toyota_cylinders_count.append(toyota[toyota['cylinders'] == i].count()['cylinders'])

    xpos = np.arange(len(list(cylinders)))
    
    plt.bar(xpos, list_78_cylinders_count, label="cars from 1978")
    plt.bar(xpos, list_toyota_cylinders_count, label="Toyota models") 
    plt.ylabel("car count")
    plt.xlabel("cylinders count")
    plt.legend()

bar_plot(df_mpg)


def line_plot(df):
    sorted_By_year = df.sort_values('model_year')
    years = sorted_By_year['model_year'].unique()
    
    toyota = df[df['car_name'].str.contains('toyota')]
    print(len(toyota))
    
    weight_by_year = []
    
    for y in years:
        weight_by_year.append(toyota[toyota['model_year'] == y]['weight'])
        
#     plt.plot(years,weight_by_year)
#     plt.xlabel('Year')
#     plt.ylabel('weight')
#     plt.title('Toyota weight(avg) by year')

        

    
    

line_plot(df_mpg)    
#     toyotas = df[df['car_name'].str.contains('toyota')]

def my_plot(df):
    # shows acceleration & horsepower by year (diffenr units but visually comparible)
    sorted_By_year = df.sort_values('model_year')
    years = sorted_By_year['model_year'].unique()
    
    acceleration_by_year = []
    mpg_by_year = []
    
    for y in years:
        acceleration_by_year.append(df[df['model_year'] == y]['acceleration'].mean())
        mpg_by_year.append(df[df['model_year'] == y]['mpg'].mean())

    plt.plot(years,acceleration_by_year, label = 'acceleration')
    plt.plot(years,mpg_by_year, label = 'mpg')
    plt.xlabel('Year')
    plt.legend(loc='best')
    
my_plot(df_mpg)    


