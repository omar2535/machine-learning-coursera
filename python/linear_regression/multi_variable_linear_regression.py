import numpy as np
import csv
import matplotlib.pyplot as plt


def main():
    # load in the data
    data = np.loadtxt(open("ex1data2.csv", "rb"), delimiter=",", skiprows=1)

    X = data[:, 0]
    y = data[:, 1]
    m = y.size
    
    theta = gradient_descent(X, y, m, np.array([0,0]), 0.01, 1500)
    print("theta is", theta)


# computes the cost
def cost_function(X, y, theta, m):
    h = theta * X
    h_y = (h - y) ** 2
    cost = 1/(2*m) * sum(h_y)
    return cost


def gradient_descent(X, y, m, theta, alpha, iterations):
    for i in range(iterations):
        print("theta", theta)
        print("cost:", cost_function(X, y, theta, m))
        theta = theta - alpha * (1/m) * np.matmul(X.T, ((X * theta) - y))

        # for plotting
        # plt.plot(X, theta*X)
        # plt.scatter(X, y)
        # plt.xlabel('Population', fontsize=18)
        # plt.ylabel('Profits', fontsize=16)
        # plt.pause(0.05)
        # if i != iterations-1:
        #     plt.gcf().clear()
    #plt.show()
    return theta

def feature_normalization(X,y):
    for i in range(X[2].size):




main()
