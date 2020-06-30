# import numpy as np
# import matplotlib.pyplot as plt
#
# from sklearn.linear_model import LinearRegression
#
# X = np.array([[6], [8], [10], [14], [18]]).reshape(-1, 1)
# y = [7, 9, 13, 17.5, 18]
# # plt.figure()
# # plt.title("Pizza pricce plotted against diameter")
# # plt.xlabel('Diameter in dollars')
# # plt.ylabel('Price in dollars')
# # plt.plot(X, y, 'k.')
# # plt.axis([0, 25, 0, 25])
# # plt.grid(True)
# # plt.show()
#
#
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

 # coding:utf8
'''
Created on 2016年4月24日
@author: Gamer Think
'''
# Simple Regession
import numpy as np

# 周广告播放数量
x = [6, 8, 10, 14, 18]
# 周汽车销售数据
y = [7, 9, 13, 17.5, 18]


# 使用最小二乘法
def fitSLR(x, y):
    n = len(x)
    denominator = 0
    numerator = 0
    for i in range(0, n):
        numerator += ((x[i] - np.mean(x)) * (y[i] - np.mean(y)))
        denominator += (x[i] - np.mean(x)) ** 2
    print("denominator:", denominator / (n - 1))

    print("numerator:", numerator / (n - 1))

    b1 = numerator / float(denominator)
    #     b0 = np.mean(y)/float(np.mean(x))
    b0 = np.mean(y) - b1 * np.mean(x)

    return b0, b1


def predict(b0, b1, x):
    return b0 + b1 * x


b0, b1 = fitSLR(x, y)


print(b0, b1)

x_test = 16      # [17.5862069]
print("y_test：", predict(b0, b1, x_test))



exit(0)