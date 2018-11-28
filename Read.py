#Read Dataset

#split Filename
file = "housing.csv"
filetype = file.split(".")[1]
print('File Type:',filetype)


#File Path 
import os
import os.path
os.chdir( "/home/shri/Desktop/ZEUS")#Path for the file directory


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
