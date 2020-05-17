"""
URL: https://towardsdatascience.com/logistic-regression-explained-and-implemented-in-python-880955306060
"""

import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from math import exp
plt.rcParams["figure.figsize"] = (10, 6)

data = pd.read_csv("C:\\Users\\USER\\Downloads\\Social_Network_Ads.csv")

# # Visualization of dataset
# plt.scatter(data['Age'], data['Purchased'])
# plt.show()

# Divide the data into training set and testing set
X_train, X_test, y_train, y_test = train_test_split(data['Age'], data['Purchased'], test_size=0.20)

# # Creating the logistic regression model
#
# # Helper function to normalize data
# def normalize(X):
#     return X - X.mean()
#
# # Method to make predictions
# def predict(X, b0, b1):
#     return np.array([1/(1+exp(-1*b0 + -1*b1*x)) for x in X])
#
# # Method to train the model
# def logistic_regression(X, Y):
#
#     X = normalize(X)
#
#     # Initializing variables
#     b0 = 0
#     b1 = 0
#     L = 0.001
#     epochs = 10000
#
#     for epoch in range(epochs):
#         y_pred = predict(X, b0, b1)
#         D_b0 = -2 * sum((Y - y_pred) * y_pred * (1 - y_pred)) # Derivative of loss wrt b0
#         D_b1 = -2 * sum(X * (Y - y_pred) * y_pred * (1 - y_pred)) # Derivative of loss wrt b1
#         # Update b0 and b1
#         b0 = b0 - L * D_b0
#         b1 = b1 - L * D_b1
#
#     return b0, b1
#
# # Training the model
# b0, b1 = logistic_regression(X_train, y_train)
#
# # Making predictions
# X_test_norm = normalize(X_test)
# y_pred = predict(X_test_norm, b0, b1)
# y_pred = [1 if p >= 0.5 else 0 for p in y_pred]
#
# plt.clf()
# plt.scatter(X_test, y_test)
# plt.scatter(X_test, y_pred, c='red')
# plt.show()
#
# # The accuracy
# accuracy = 0
# for i in range(len(y_pred)):
#     if y_pred[i] == y_test.iloc[i]:
#         accuracy += 1
# print(f"Accuracy = {accuracy/len(y_pred)}")

# Making predictions using scikit learn
from sklearn.linear_model import LogisticRegression

# Create an instance and fit the model
lr_model = LogisticRegression()
lr_model.fit(X_train.values.reshape(-1, 1), y_train.values.reshape(-1,1))

# Making predictions
y_pred_sk = lr_model.predict(X_test.values.reshape(-1, 1))

plt.clf()
plt.scatter(X_test, y_test)
plt.scatter(X_test, y_pred_sk, c="red")
plt.show()

# Accuracy
print(f"Accuracy = {lr_model.score(X_test.values.reshape(-1, 1), y_test.values.reshape(-1, 1))}")
