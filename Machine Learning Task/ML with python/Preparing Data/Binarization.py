from pandas import read_csv
from sklearn.preprocessing import Binarizer
path = r'D:\Sozo-lab-tasks\Machine Learning Task\datasets\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(path, names=names)
array = dataframe.values
binarizer = Binarizer(threshold=0.5).fit(array)
Data_binarized = binarizer.transform(array)
print ("\nBinary data:\n", Data_binarized [0:5])