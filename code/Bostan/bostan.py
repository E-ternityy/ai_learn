import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.linear_model import SGDRegressor


def standardization(x):
    means = np.mean(x, axis=0)
    std = np.std(x, axis=0)
    x = (x - means) / std
    return x

def normal_function(x, y):
    theta = np.linalg.inv(x.T@x)@x.T@y
    return theta

def gradient_descent(x, y, a, times):
    m = len(y)
    n = x.shape[1]
    theta = np.zeros((n, 1))
    for i in range(times):
        theta = theta - a * (1 / m) * x.T @ (x @ theta - y)
    return theta
data = pd.read_csv('BostonHousing.csv')
cols = data.shape[1]
x = data.iloc[:,:-1]
y = data.iloc[:,cols-1:cols]
x = standardization(x)
x2 = x.copy()
x.insert(0, 'Ones', 1)
x = np.matrix(x.values)
y = np.matrix(y.values)
theta1 = gradient_descent(x, y, 0.02, 3000)
theta2 = normal_function(x, y)
sgd_reg = SGDRegressor(
    loss='squared_error',
    learning_rate='constant',
    eta0=0.01,
    max_iter=1000,
    tol=1e-3,
    random_state=42
)
y2 = np.ravel(y)
sgd_reg.fit(x2, y2)
p1 = x @ theta1
p2 = x @ theta2
p3 = sgd_reg.predict(x2)
print(r2_score(p1.A, y.A))
print(r2_score(p2.A, y.A))
print(r2_score(p3, y.A))






