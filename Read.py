#ShrikantNande
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
