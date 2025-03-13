import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

class LinearRegression:
    def __init__(self, method, times=1000, learn_rate=0.01):
        self.times = times
        self.learn_times = learn_rate
        self.method = method
        self.means = None
        self.std = None
        self.theta = None

    def standardization(self, X):
        if self.means is None or self.std is None:
            self.means = np.mean(X, axis=0)
            self.std = np.std(X, axis=0)
            return (X - self.means) / self.std
        else:
            return (X - self.means) / self.std

    def normal_function(self, X, y):
        return np.linalg.inv(X.T @ X) @ X.T @ y

    def gradient_descent(self, X, y):
        m = len(y)
        n = X.shape[1]
        theta = np.zeros((n, 1))
        for i in range(self.times):
            theta = theta - self.learn_times * (1 / m) * X.T @ (X @ theta - y)
        return theta

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        X_std = self.standardization(X)
        X_with_bias = np.c_[np.ones(X_std.shape[0]), X_std]
        if self.method == "normal":
            self.theta = self.normal_function(X_with_bias, y)
        elif self.method == "gradient_descent":
            self.theta = self.gradient_descent(X_with_bias, y)
        return self.theta

    def predict(self, X):
        X = np.array(X)
        X_std = self.standardization(X)
        X_with_bias = np.c_[np.ones(X_std.shape[0]), X_std]
        return X_with_bias @ self.theta

    def score(self, X, y):
        y_pred = self.predict(X)
        y = np.array(y)
        return r2_score(y, y_pred)


data = pd.read_csv('BostonHousing.csv')
cols = data.shape[1]
X = data.iloc[:,:-1]
y = data.iloc[:,cols-1:cols]
normal = LinearRegression(method="normal", times=200000, learn_rate=0.02)
normal.fit(X, y)
print(f"正规方程R2={normal.score(X, y)}")
gd = LinearRegression(method="gradient_descent", times=200000, learn_rate=0.02)
gd.fit(X, y)
print(f"梯度下降R2={gd.score(X, y)}")







