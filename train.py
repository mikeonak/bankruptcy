#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import pickle

from xgboost.training import train


col= []
for a in range(1,65):
    col.append('x'+str(a))
col.append('y')

df = pd.read_csv('3year.csv',header=None,names = col )

# data preparation

df.replace('?',np.NaN,inplace=True)
del df['x37']
df.x21.fillna(1,inplace=True)
df = df.astype('float')
df= df.apply(lambda x: x.fillna(x.mean()),axis=0)
ind = abs(df.corrwith(df.y)[abs(df.corrwith(df.y)) > 0.005]).sort_values(ascending=False).index
df_small = df[ind]
df_without_cor = df_small.drop(['x22','x10','x2','x38','x3','x51','x10','x6','x14','x11','x7','x26','x16','x62'],axis=1)
df_without_cor.drop('x29',axis=1,inplace=True)

#splitting the data

df_full_train, df_test = train_test_split(df_without_cor,test_size = 0.2, random_state=1, stratify=df_without_cor.y)
df_train, df_val = train_test_split(df_full_train, test_size = 0.25, random_state=1,stratify=df_full_train.y)
y_train = df_train.y.values
y_val = df_val.y.values
y_test = df_test.y.values
y_full_train = df_full_train.y.values
del df_train['y']
del df_val['y']
del df_test['y']
del df_full_train['y']

#scaling the features
sc_X = StandardScaler()
X_train = sc_X.fit_transform(np.array(df_train))
X_val = sc_X.transform(np.array(df_val))
X_test = sc_X.transform(np.array(df_test))
X_full_train = sc_X.transform(np.array(df_full_train))






# Training the final model
features = df_train.columns
dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=features)


xgb_params = {
    'eta': 0.1, 
    'max_depth': 7,
    'min_child_weight': 10,
    'colsample_bytree':1,
    'subsample': 1,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'nthread': 4,

    'seed': 1,
    'verbosity': 1,
}


model = xgb.train(xgb_params, dtrain,  verbose_eval=5, num_boost_round=220)
y_pred = model.predict(dtrain)

with open('bankruptcy.bin', 'wb') as f_out:
    pickle.dump((sc_X,model), f_out)