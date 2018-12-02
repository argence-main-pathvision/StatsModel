#Shrikant Nande
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
for i in categiorical_columns:
    z=Data_Mode.loc[i].tolist()#Take a value which corresponds to columns name
    print("Mode for {0} is {1}.".format(i, z))#Print Mode for categorical variables



