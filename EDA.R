
# Classify categorical variable 
col_name<-colnames(data1)
cat_var1<-c(0);j=1
n<-length(col_name)
for(i in 1:n){
  if(length(unique(data1[,col_name[i]]))<40){
    cat_var1[j]<-col_name[i]
    j=j+1
  }
}
# Converting categorical variable into factor 
data1[cat_var1] <- lapply(data1[cat_var1] , factor)
str(data1)

# classify b/w character variable
col_name<-colnames(data1)
char_var1<-c(0);r=1
n<-length(col_name)
for(i in 1:n){
  if(class(data1[,col_name[i]])=="character"){
    char_var1[r]<-col_name[i]
    r=r+1
  }
}
# identify numeric variable/continuous variabe
drops <- c(cat_var1,char_var1)
numeric_var<-colnames(data1[ , !(names(data1) %in% drops)])




r1<-nrow(data1);c1<-ncol(data1)
r2<-nrow(data);c2<-ncol(data)
miss_var1<-if(any(is.na(data1))=="TRUE"){
  print("Yes")
}else{
  print("No")
}

miss_var2<-if(any(is.na(data))=="TRUE"){
  print("Yes")
}else{
  print("No")
}


Parameters=c("Rows","Columns","Numeric","Charecter","Categorical","Missing")
Descriptive_Measures<-c(r1,c1,length(numeric_var),length(char_var1),length(cat_var1),miss_var1)
df<-data.frame(Parameters,Descriptive_Measures)


