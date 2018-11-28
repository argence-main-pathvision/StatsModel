#Find Catagorical Values
cols = data.columns
num_cols = data._get_numeric_data().columns#list of numarical variables
#print('Numaric Data columns:',num_cols)
cat_cols=list(set(cols) - set(num_cols))#List of categorical variables
#print('Categorial Data Columns:',cat_cols)

for i in cat_cols:
     data[i] = pd.Categorical(data[i])#Convert Object Type to Categorical.

print(data.info())





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
              #How to check a variable is continuous or discrete?
#Values are integers: +.7
#Values are floats: +.8
#Values are normally distributed: +.3
#Values not contain a relatively small number of unique values: +.3
#Values aren't all the same number of characters: +.1
#Values don't contain leading zeros: +.1

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
print(Numaric_to_Categorical)
#Convert Datatype name to categorical
for i in Numaric_to_Categorical:
    data[i] = pd.Categorical(data[i])

#Find Final Number of Catagorical Values
num_cols = data._get_numeric_data().columns#list of numarical variables
print('Numaric Data columns:',num_cols)
cat_cols=list(set(cols) - set(num_cols))#List of categorical variables
print('Categorial Data Columns:',cat_cols)

