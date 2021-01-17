from numpy import loadtxt
path = "D:\Sozo-lab-tasks\Machine Learning Task\datasets\pima-indians-diabetes.csv"
datapath = open(path, 'r')
data = loadtxt(datapath, delimiter=",")
print(data.shape)
print(data[:3])
