from pandas import read_csv
path = r"D:\Machine Learning Task\datasets\iris.csv"
data = read_csv(path)
print(data.shape)
print(data[:3])