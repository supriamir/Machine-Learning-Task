from pandas import read_csv
path = r"D:\Sozo-lab-tasks\Machine Learning Task\datasets\pima-indians-diabetes.csv"
headernames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=headernames)
print(data.head(50))