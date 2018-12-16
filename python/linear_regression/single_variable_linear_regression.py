import numpy as np
import csv

def main():
    # load in the data
    data = np.loadtxt(open("ex1data1.csv", "rb"), delimiter=",", skiprows=1)

    X = data[:,0]
    y = data[:,1]
    m = y.size
    theta = gradient_descent(X,y,0,0.01,1500)
        


# computes the cost
def cost_function(X, theta, m):
    h = theta * X
    h_y = (h - y) ** 2
    cost = 1/(2*m) * sum(h_y)
    return cost

def gradient_descent(X, y, theta, alpha, iterations):
    m = y.size
    for _ in range(iterations):
        theta = theta - alpha * (1/m) * (X.T * ((X * theta) - y))
    return theta

main()
