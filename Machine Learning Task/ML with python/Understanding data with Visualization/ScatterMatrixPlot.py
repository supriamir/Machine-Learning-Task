from matplotlib import pyplot
from pandas import read_csv
from pandas.plotting import scatter_matrix
path = r"D:\Machine Learning Task\datasets\pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=names)
scatter_matrix(data)
pyplot.show()