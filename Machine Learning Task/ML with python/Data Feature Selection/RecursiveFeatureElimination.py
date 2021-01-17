from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
path = r'D:\Machine Learning Task\datasets\pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin',
         'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(path, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]
model = LogisticRegression(solver='lbfgs', max_iter=150)
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)


print("Number of Features: ",rfe.n_features_)
print("Selected Features: ",rfe.support_)
print("Feature Ranking: ",rfe.ranking_)
