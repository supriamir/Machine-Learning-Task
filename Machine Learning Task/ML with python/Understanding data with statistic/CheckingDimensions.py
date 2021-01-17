from pandas import read_csv
path = r"D:\Machine Learning Task\datasets\pima-indians-diabetes.csv"
data = read_csv(path)
print(data.shape)