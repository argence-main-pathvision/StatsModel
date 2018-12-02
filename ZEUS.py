#Read Different types of File
import pandas as pd #import library read file, 
import matplotlib.pyplot as plt #import library to visualization
from pandas.plotting import scatter_matrix #import library to plot scatter plot

#split Filename
file = "housing.csv" #file name
filetype = file.split(".")[1] #Split filename and take extension
print('File Type:',filetype) #print filename
#File Path 
import os #Import library to acccess os
import os.path #Import library to access path
os.chdir( "/home/shri/Desktop/ZEUS") #Path for the file directory
#Read File
def file_data_read(filetype):#read the file with corresponding with extension
    if filetype=='csv': 
        data=pd.read_csv(file)#Read CSV file.
    elif filetype=='xls':
        data=pd.read_excel(file)#Read excel file.
    elif filetype=='xlsx':
        data=pd.read_excel(file)#Read excel file.
    elif filetype=='json':
        data=pd.read_json(file)#Read json file.
    else:
        print('file not found') #print the file type is not found
    return data #write data into structured format  
data=file_data_read(filetype)#read the function file type read
print(data.head(2))#print data

#Missing Values
missing_value=data.isnull().sum()#calculate total missing values in columns
print(missing_value)#print missing with there column names

#Visualization 
import seaborn as sns #visualization of missing values
sns.heatmap(data.isnull(), yticklabels=False, cmap='viridis') #plot coloured heatmap for missing values
plt.show()#Show the plot
data=data.dropna() #Drop The Missing Value Rows

#Find Catagorical Values
columns = data.columns# total columns names can be extracted
numarical_columns = data._get_numeric_data().columns#list of numarical variables
categorical_columns=list(set(columns) - set(numarical_columns))#List of categorical variables
for i in categorical_columns: #for all categorical columns convert type form object to categorical 
     data[i] = pd.Categorical(data[i])#Convert Object Type to Categorical.

data.info()#print dataset info-shape,type,column name


#How to check a variable is continuous or discrete?
   #Values are integers: +.7
   #Values are floats: +.8
   #Values are normally distributed: +.3
   #Values not contain a relatively small number of unique values: +.3
   #Values aren't all the same number of characters: +.1
   #Values don't contain leading zeros: +.1

#Conert Numarical to Categorical Type
def Read_categorical(data):#read categorical values
    column_names=data.columns.tolist() #list for categorical data can be created
    threshold=0 #Initialuize the threshold
    categorical_variable= [] #Initilize categorical Variable
    for i in column_names: #for each column condition can be checked
        if data[i].dtype=='int64':#Values are integers: +.7
            #print(i)
            threshold = threshold + 0.7#Values are integers: add +.7 in threshold
            #--property not showing the exact values so eliminate this condition and minimize the threshold by 0.3
            #from scipy import stats
            #p=stats.shapiro(data[i])[1]
            #if p < 0.05:
            #   threshold = threshold + 0.3
            
            if len(set(data[i])) > 10:#Values not contain a relatively small number of 10 unique values 
                threshold = threshold + 0.3 #Values not contain a relatively small number of 10 unique values: add +.3
            #print(f'Threshold for {i} is {threshold}')
            if(threshold<=0.7):#If threshold showing lesser value than 0.7 as we elimniate noramilty condition above is consider to bs #categorical
                categorical_variable.append(i) #append list as that column name 
            threshold = 0 
    return categorical_variable #return categorical variable

Numaric_to_Categorical = Read_categorical(data) #store as a numaric values which are showing categorical type of behave 
print(Numaric_to_Categorical)#Print Numarical to categorical variables

for i in Numaric_to_Categorical:#Convert Datatype name to categorical
    data[i] = pd.Categorical(data[i])#data is in categorical form as categorical <- object, categorical

#Find Final Number of Catagorical Values
numaric_columns = data._get_numeric_data().columns#list of numarical variables
print('Numaric Data columns:',numaric_columns)#print Numarical data
categorical_columns=list(set(columns) - set(numaric_columns))#List of categorical variables
print('Categorial Data Columns:',categorical_columns)#print all categorical variables


#Describe Mean, Median for numarical values and Mode for categorical values.
print(data.describe())#Generate discriptive Staistics:Mean Standard_Deviation Range Count

#mean_median(dataframes)
data_mean= data.mean()#Describels the mean of all variables
Data_mean = pd.DataFrame(data_mean)#Create a dataframe 

data_median=data.median()#Describes median of all variables 
Data_median=pd.DataFrame(data_median)#Create a dataframe 

#print mean and median for numarical values
for i in numarical_columns:#For all numarical values
    m=Data_mean.loc[i].tolist()#Create list for 'i'th variable mean
    print("Mean for {0} is {1}.".format(i, m))#Print mean
    n=Data_median.loc[i].tolist()#Create list for 'i'th variable median
    print("Median for {0} is {1}.".format(i, n))#Print Median    
    
#DataFrame for modes    
data_Mode=data.mode()#Describels the mode of all variables 
data_Mode=data_Mode.T#Dataframe is into the vartical form so take transpose 
Data_Mode=pd.DataFrame(data_Mode)#Create a dataframe 
Data_Mode=Data_Mode.iloc[:,0:1]#Take first mode 
#print mode for all the dataset variables
for i in categorical_columns:
    z=Data_Mode.loc[i].tolist()#Take a value which corresponds to columns name
    print("Mode for {0} is {1}.".format(i, z))#Print Mode for categorical variables
    
#Visulization
#Numarical Values-(Hist,Box,Density,)
for i in numarical_columns:#
    print('Variable_name:',i)#Print variable name
    #--Histogram Plot
    data[i].hist()
    plt.show()#show the histogram
    #Box Plot
    data[i].plot(kind='box', subplots=True, layout=(1,2), sharex=False, sharey=False)
    plt.show()#show the Box
    #Density Plot:-Numarical Values
    data[i].plot.kde()
    plt.show()#show Density plot
    
#Scatter Matrix Plot 
scatter_matrix(data, alpha=0.2, figsize=(16, 16), diagonal='kde')
plt.show()#show the scatter plot

#Scatter Matrix Plot 
scatter_matrix(data, alpha=0.2, figsize=(16, 16), diagonal='kde')
plt.show()#show the scatter plot
#Bar_plot:-Categorical values
for i in categorical_columns:
    print('Variable_name:',i)#Print variable name
    data[i].value_counts().head(10).plot.bar()#Count and plot variables 
    plt.show()#show 
