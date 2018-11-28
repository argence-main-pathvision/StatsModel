import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

#split Filename
file = "housing.csv"
filetype = file.split(".")[1]
print('File Type:',filetype)


#File Path 
import os
import os.path
os.chdir( "/home/Desktop/ZEUS")#Path for the file directory


#Read File
def read_file(filetype):
    if filetype=='csv':
        data=pd.read_csv(file)#Read CSV file.
    elif filetype=='xls':
        data=pd.read_excel(file)#Read excel file.
    elif filetype=='xlsx':
        data=pd.read_excel(file)#Read excel file.
    elif filetype=='json':
        data=pd.read_json(file)#Read json file.
    else:
        print('file not found') 
    return data


data=read_file(filetype)
print(data.head(5))

#Missing Values
missing_value=data.isnull().sum()
print('Total missing values in dataset:')
print(missing_value)

##Visualization of missing value
import seaborn as sns
sns.heatmap(data.isnull(), yticklabels=False, cmap='viridis')
plt.show()

#Drop The Missing Value Rows
data=data.dropna()

#Find Catagorical Values
cols = data.columns
num_cols = data._get_numeric_data().columns#list of numarical variables
#print('Numaric Data columns:',num_cols)
cat_cols=list(set(cols) - set(num_cols))#List of categorical variables
#print('Categorial Data Columns:',cat_cols)

for i in cat_cols:
     data[i] = pd.Categorical(data[i])#Convert Object Type to Categorical.

print('Info:',data.info())





#How to check a variable is continuous or discrete?
   #Values are integers: +.7
   #Values are floats: +.8
   #Values are normally distributed: +.3
   #Values not contain a relatively small number of unique values: +.3
   #Values aren't all the same number of characters: +.1
   #Values don't contain leading zeros: +.1

#Conert Numarical to Categorical Type

def Read_cat(data):
    col_names=data.columns.tolist()
    threshold=0
    cat_var= []
    for i in col_names:
        if data[i].dtype=='int64':
            #print(i)
            threshold = threshold + 0.7
            #from scipy import stats
            #p=stats.shapiro(data[i])[1]
            #if p < 0.05:
             #   threshold = threshold + 0.3
            if len(set(data[i])) > 10:
                threshold = threshold + 0.3
            #print(f'Threshold for {i} is {threshold}')
            if(threshold<=0.7):
                cat_var.append(i)
            threshold = 0
    return cat_var

Numaric_to_Categorical = Read_cat(data)
print('New Categorical variable:',Numaric_to_Categorical)
#Convert Datatype name to categorical
for i in Numaric_to_Categorical:
    data[i] = pd.Categorical(data[i])

#Find Final Number of Catagorical Values
num_cols = data._get_numeric_data().columns#list of numarical variables
print('Numaric Data columns:',num_cols)
cat_cols=list(set(cols) - set(num_cols))#List of categorical variables
print('Categorial Data Columns:',cat_cols)


#Generate discriptive Staistics:Mean Standard_Deviation Range Count
print(data.describe())


#Mean(dataframes)
data_mean= data.mean()
Data_mean = pd.DataFrame(data_mean)

#Median(dataframes)
data_median=data.median()
Data_median=pd.DataFrame(data_median)

#print mean and median for numarical values
for i in num_cols:
    m=Data_mean.loc[i].tolist()
    print("Mean for {0} is {1}.".format(i, m))
    n=Data_median.loc[i].tolist()
    print("Median for {0} is {1}.".format(i, n))    
    

#DataFrame for modes    
data_Mode=data.mode()
data_Mode=data_Mode.T
Data_Mode=pd.DataFrame(data_Mode)
Data_Mode=Data_Mode.iloc[:,0:1]
#print mode for all the dataset variablesDData_Mode=Data_Mode.iloc[:,0:1]ata_Mode=Data_Mode.iloc[:,0:1]
for i in cat_cols:
    z=Data_Mode.loc[i].tolist()
    print("Mode for {0} is {1}.".format(i, z))  

#Visulization
#Box_plot:- Numarical Values
for i in num_cols:
    print('Variable_name:',i)
    #Histogram Plot
    data[i].hist()
    plt.show()
    #Box Plot
    data[i].plot(kind='box', subplots=True, layout=(1,2), sharex=False, sharey=False)
    plt.show()
    #Density Plot:-Numarical Values
    data[i].plot.kde()
    plt.show()
    #Scatter Matrix Plot 
    scatter_matrix(data, alpha=0.2, figsize=(16, 16), diagonal='kde')
    plt.show()
#Bar_plot:-Categorical values
for i in cat_cols:
    print('Variable_name:',i)
    data[i].value_counts().head(10).plot.bar()
    plt.show()




