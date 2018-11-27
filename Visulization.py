#Visulization
#Box_plot:- Numarical Values
for i in num_cols:
    print('Variable_name:',i)
    #Histogram Plot
    data[i].hist()
    plt.show()
    #Box Plot
    data[i].plot(kind='box', subplots=True, layout=(1,2), sharex=False, sharey=False)
    plt.show()
    #Density Plot:-Numarical Values
    data[i].plot.kde()
    plt.show()
#Scatter Matrix Plot 
scatter_matrix(data, alpha=0.2, figsize=(16, 16), diagonal='kde')
plt.show()
#Bar_plot:-Categorical values
for i in cat_cols:
    print('Variable_name:',i)
    data[i].value_counts().head(10).plot.bar()
    plt.show()


