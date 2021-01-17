from numpy import loadtxt
path = "D:\Machine Learning Task\datasets\pima-indians-diabetes.csv"
datapath=open(path,'r')
data = loadtxt(datapath,delimiter=",")
print(data.shape)
print(data[:3])

