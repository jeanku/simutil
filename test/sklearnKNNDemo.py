# import numpy as np
# import matplotlib.pyplot as plt
#
# X_train = np.array([
#     [158, 64],
#     [170, 86],
#     [183, 84],
#     [191, 80],
#     [155, 49],
#     [163, 59],
#     [180, 67],
#     [158, 54],
#     [170, 67],
# ])
#
# y_train = ['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']
# plt.figure()
# plt.title("Human heights and Weights by Sex")
# plt.xlabel('Height in cm')
# plt.ylabel('Weight in kg')
#
# for i, x in enumerate(X_train):
#     plt.scatter(x[0], x[1], c='k', marker='x' if y_train[i]== 'male' else 'D')
# plt.grid(True)
# plt.show()


import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.neighbors import KNeighborsClassifier

X_train = np.array([
    [158, 64],
    [170, 86],
    [183, 84],
    [191, 80],
    [155, 49],
    [163, 59],
    [180, 67],
    [158, 54],
    [170, 67],
])
y_train = ['male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']
lb = LabelBinarizer()
y_train_binarized = lb.fit_transform(y_train)

K = 3
clf = KNeighborsClassifier(n_neighbors=K)

clf.fit(X_train, y_train_binarized.reshape(-1))
predicted_binarized = clf.predict(np.array([155, 70]).reshape(1, -1))[0]
predicted_label = lb.inverse_transform(predicted_binarized)
print(predicted_label)
exit(0)
# model = LinearRegression()
# model.fit(X, y)
#
# test_pizza = np.array([[8]])
#
# for i in [8, 9, 11, 16, 18]:
#     test_pizza = np.array([[i]])
#     predicted_price = model.predict(test_pizza)
#     print(i, ':', predicted_price)
# exit(0)

#  # coding:utf8
# '''
# Created on 2016年4月24日
# @author: Gamer Think
# '''
# # Simple Regession
# import numpy as np
#
# # 周广告播放数量
# x = [6, 8, 10, 14, 18]
# # 周汽车销售数据
# y = [7, 9, 13, 17.5, 18]
#
#
# # 使用最小二乘法
# def fitSLR(x, y):
#     n = len(x)
#     denominator = 0
#     numerator = 0
#     for i in range(0, n):
#         numerator += ((x[i] - np.mean(x)) * (y[i] - np.mean(y)))
#         denominator += (x[i] - np.mean(x)) ** 2
#     print("denominator:", denominator / (n - 1))
#
#     print("numerator:", numerator / (n - 1))
#
#     b1 = numerator / float(denominator)
#     #     b0 = np.mean(y)/float(np.mean(x))
#     b0 = np.mean(y) - b1 * np.mean(x)
#
#     return b0, b1
#
#
# def predict(b0, b1, x):
#     return b0 + b1 * x
#
#
# b0, b1 = fitSLR(x, y)
#
#
# print(b0, b1)
#
# x_test = 16      # [17.5862069]
# print("y_test：", predict(b0, b1, x_test))
#
#
#
# exit(0)