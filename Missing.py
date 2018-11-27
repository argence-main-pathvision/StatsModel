#Missing Values
missing_value=data.isnull().sum()
print(missing_value)

#Drop The Missing Value Rows
data=data.dropna()

