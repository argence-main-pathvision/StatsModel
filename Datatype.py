#ShrikantNande
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
            if(threshold<=0.7):#If threshold showing lesser value than 0.7 as we elimniate noramilty condition above is consider to be categorical
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

