from pandas import read_csv
path = r"D:\Machine Learning Task\datasets\pima-indians-diabetes.csv"
headernames =['preg','plas','pres','skin','test','mas','pedi','age','class']
data = read_csv(path,names=headernames)
print(data.shape)
print(data[:3])
