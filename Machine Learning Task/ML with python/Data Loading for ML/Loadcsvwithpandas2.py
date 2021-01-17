from pandas import read_csv
path = r"D:\Sozo-lab-tasks\Machine Learning Task\datasets\iris.csv"
headernames =['preg','plas','pres','skin','test','mas','pedi','age','class']
data = read_csv(path,names=headernames)
print(data.shape)
print(data[:3])
