#Generate discriptive Staistics:Mean Standard_Deviation Range Count
print(data.describe())


#mean_median(dataframes)
data_mean= data.mean()
Data_mean = pd.DataFrame(data_mean)

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
#print mode for all the dataset variables
for i in cat_cols:
    z=Data_Mode.loc[i].tolist()
    print("Mode for {0} is {1}.".format(i, z))  



