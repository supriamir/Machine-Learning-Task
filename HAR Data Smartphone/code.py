from time import time
from lightgbm import LGBMClassifier
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from scipy.optimize import curve_fit
from scipy.stats import norm, skew, probplot
from cycler import cycler
from collections import Counter
import pandas as pd

# To do linear algebra
import numpy as np
from numpy import pi

# To create plots
from matplotlib.colors import rgb2hex
from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt

# To create nicer plots
import seaborn as sns

# To create interactive plots
#from plotly.offline import init_notebook_mode, plot
#import plotly.graph_objs as go
# init_notebook_mode(connected=True)

# To get new datatypes and functions

# To investigate distributions

# To build models

# To gbm light

# To measure time

train = r"D:\Sozo-lab-task\HAR Data Smartphone\dataset\train.csv"
test = r"D:\Sozo-lab-task\HAR Data Smartphone\dataset\test.csv"

train_df = pd.read_csv(train)
test_df = pd.read_csv(test)


# Combine boths dataframes
train_df['Data'] = 'Train'
test_df['Data'] = 'Test'
both_df = pd.concat([train_df, test_df], axis=0).reset_index(drop=True)
both_df['subject'] = '#' + both_df['subject'].astype(str)

# Create label
label = both_df.pop('Activity')

print('Shape Train:\t{}'.format(train_df.shape))
print('Shape Test:\t{}\n'.format(test_df.shape))

# print(train_df.head())
datafeature = pd.DataFrame.from_dict(Counter([col.split('-')[0].split('(')[0] for col in both_df.columns]),
                                     orient='index').rename(columns={0: 'count'}).sort_values('count', ascending=False)

print(datafeature)


print('Null Values In DataFrame: {}\n'.format(both_df.isna().sum().sum()))
both_df.info()


enc = LabelEncoder()
label_encoded = enc.fit_transform(label)
X_train, X_test, y_train, y_test = train_test_split(
    tsne_data, label_encoded, random_state=3)

# Create the model
lgbm = LGBMClassifier(n_estimators=500, random_state=3)
lgbm = lgbm.fit(X_train, y_train)

# Test the model
score = accuracy_score(y_true=y_test, y_pred=lgbm.predict(X_test))
print('Accuracy on testset:\t{:.4f}\n'.format(score))

