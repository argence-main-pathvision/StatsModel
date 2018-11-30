#ShrikantNande
#Read Different types of File
def Read_file():#Read the Files 
    #split Filename
    file = "housing.csv" #File name
    filetype = file.split(".")[1] #Split filename and take extension
    print('File Type:',filetype) #Print filename
    #File Path 
    import os #Import library to acccess os
    import os.path #Import library to access path
    os.chdir( "/home/Desktop/ZEUS") #Path for the file directory
    #Read File
    def file_data_read(filetype):#Read the file with corresponding with extension
        if filetype=='csv': 
            data=pd.read_csv(file)#Read CSV file.
        elif filetype=='xls':
            data=pd.read_excel(file)#Read excel file.
        elif filetype=='xlsx':
            data=pd.read_excel(file)#Read excel file.
        elif filetype=='json':
            data=pd.read_json(file)#Read json file.
        else:
            print('file not found') #Print the file type is not found
        return data #Write data into structured format  
    data=file_data_read(filetype)#Read the function file type read
    print(data.head(5))
Read_file()#Call the function
