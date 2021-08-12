#GOAL
""" Write a code that efficently executes the ability to graph 
the accumulation of data following a series of rolling a die """
#imports
from pandas.plotting import scatter_matrix
from pandas import read_csv
from matplotlib import pyplot
import matplotlib
import random
import csv  
import os

# Load dataset
file = r'C:\Users\ajax0\OneDrive\Documents\Dice Roll Data spreadsheet from CSV deposit.csv'
names = ['x', 'y']
dataset = read_csv(file, names=names)

#Passing path
path = r'C:\Users\ajax0\OneDrive\Documents\Dice Roll Data spreadsheet from CSV deposit.csv'
assert os.path.isfile(path)
with open(path, 'w', encoding='UTF8') as f:
    pass

#Declaring variables


#Assign data's random values

data1 = [1, 1]
data2 = [1, 2]
data3 = [2, 3]
data4 = [2, 1]
data5 = [3, 2]
data6 = [3, 3]
data7 = [4, 1]
data8 = [4, 2]
data9 = [5, 3]
data10 = [5, 1]


# write the data
f = open(r'C:\Users\ajax0\OneDrive\Documents\Dice Roll Data spreadsheet from CSV deposit.csv', 'w', newline='')
writer = csv.writer(f)

writer.writerow(data1)
writer.writerow(data2)
writer.writerow(data3)
writer.writerow(data4)
writer.writerow(data5)
writer.writerow(data6)
writer.writerow(data7)
writer.writerow(data8)
writer.writerow(data9)
writer.writerow(data10)


# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()
