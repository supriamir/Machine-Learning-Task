from pandas import read_csv
path = r"D:\Sozo-lab-tasks\Machine Learning Task\datasets\iris.csv"
data = read_csv(path)
print(data.shape)
print(data[:3])
