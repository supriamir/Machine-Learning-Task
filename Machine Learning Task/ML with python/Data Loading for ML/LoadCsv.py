import csv
import numpy as np
path = r"D:\Machine Learning Task\datasets\iris.csv"

with open(path,'r') as f:
    reader =csv.reader(f,delimiter=',')
    header = next(reader)
    data = list(reader)
    data = np.array(data)

print(header)
print(data.shape)
print(data[:3])
