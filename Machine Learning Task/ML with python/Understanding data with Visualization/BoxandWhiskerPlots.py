from matplotlib import pyplot
from pandas import read_csv
path = r"D:\Sozo-lab-tasks\Machine Learning Task\datasets\pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=names)
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False,sharey=False)
pyplot.show()