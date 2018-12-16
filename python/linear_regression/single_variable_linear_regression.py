import numpy as np
import csv

# load in the data
data = np.loadtxt(open("ex1data1.csv", "rb"), delimiter=",", skiprows=1)

X = data[:,0]
y = data[:,1]
