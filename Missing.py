#ShrikantNande
#Missing Values
missing_value=data.isnull().sum()#calculate total missing values in columns
print(missing_value)#print missing with there column names

#Visualization 
import seaborn as sns #visualization of missing values
sns.heatmap(data.isnull(), yticklabels=False, cmap='viridis') #plot coloured heatmap for missing values
data=data.dropna() #Drop The Missing Value Rows
