#ShrikantNande
#Visulization
#Numarical Values-(Hist,Box,Density,)
for i in numarical_columns:#
    print('Variable_name:',i)#Print variable name
    #--Histogram Plot
    data[i].hist()
    plt.show()#show the histogram
    #Box Plot
    data[i].plot(kind='box', subplots=True, layout=(1,2), sharex=False, sharey=False)
    plt.show()#show the Box
    #Density Plot:-Numarical Values
    data[i].plot.kde()
    plt.show()#show Density plot
    
#Scatter Matrix Plot 
scatter_matrix(data, alpha=0.2, figsize=(16, 16), diagonal='kde')
plt.show()#show the scatter plot
#Bar_plot:-Categorical values
for i in categorical_columns:
    print('Variable_name:',i)#Print variable name
    data[i].value_counts().head(10).plot.bar()#Count and plot variables 
    plt.show()#show 
