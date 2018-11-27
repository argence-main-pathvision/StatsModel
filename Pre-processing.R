rm(list=ls())
# load libraries
library(caret)
library(lattice)
library(ggplot2)
library(VIM)
# load the dataset
data<-read.csv(file.choose(),stringsAsFactors = F, na.strings = c("","NA"))
# attach the data
attach(data)
# dimension of the data
dim(data)
str(data)
# coloumn names
col_name<-colnames(data)
# remove the variable with more than 50% missing or "NA" values
data <- data[ lapply( data, function(x) sum(is.na(x)) / length(x) ) < 0.5 ]

# Classify categorical variable 
col_name<-colnames(data)
cat_var<-c(0);not_cat_var<-c(0);k=1;j=1
n<-length(col_name)
for(i in 1:n){
  if(length(unique(data[,col_name[i]]))<40){
    cat_var[j]<-col_name[i]
    j=j+1
  }else{
    not_cat_var[k]<-col_name[i]
    k=k+1
  }
}
# Converting categorical variable into factor 
data[cat_var] <- lapply(data[cat_var] , factor)
str(data)

# classify b/w character variable and numeric variable
col_name<-colnames(data)
char_var<-c(0);no_char_var<-c(0);r=1;s=1
n<-length(col_name)
for(i in 1:n){
  if(class(data[,col_name[i]])=="character"){
    char_var[r]<-col_name[i]
    r=r+1
  }else{
    no_char_var[s]<-col_name[i]
    s=s+1
  }
}
# identifying the charecter variable which has less than 5% unique value
in_var<-c(0);out_var<-c(0);k=1;j=1
n<-length(char_var)
for(i in 1:n){
  if(length(unique(data[,char_var[i]]))<ceiling((5*nrow(data))/100)){
    in_var[j]<-char_var[i]
    j=j+1
  }else{
    out_var[k]<-char_var[i]
    k=k+1
  }
}

# remove those character variable which has more than 5% unique values
data[out_var]<-data[out_var][,-grep ("character", sapply (data[out_var], class))]
str(data)

#Missing Value imputation Using kNN for categorical variable
n_col<-ncol(data)
data<-kNN(data,variable = cat_var,k=6)
data<-data[,1:n_col]


# find the mode for character variable
df<-data[in_var]
Mode <- function(df){
  columns <- colnames(df)
  mode.v <- c(0)
  for(i in 1:ncol(df)){
    mode.v[i] <- names(which(table(df[,i])==max(table(df[,i]))))[1]
  }
  return(mode.v)
}

# missing value imputation for character variable and numeric variable

for (i in 1:ncol(data)) {
  if (class(data[,i])=="numeric" | class(data[,i])=="integer") {
    data[is.na(data[,i]),i] <- ceiling(mean(data[,i], na.rm = TRUE))
  } else if (class(data[,i]) %in% c("character")) {
    data[is.na(data[,i]),i] <- Mode(df)[1]
  }
}

# which variable has missing value
n_miss_value<-sapply(data, function(data) sum(is.na(data)))

if(any(is.na(data))=="FALSE"){
  print("Congratulations! Everythings looks good and well organised and it seems Your data Pre-Processing is done.Now you can do whatever what you want to do")
  print("But I recommend you to do feature engineering")
}

