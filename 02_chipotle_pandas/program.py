# Getting and knowing your data
import os

import pandas as pd

import numpy as np

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

# Define the read folder
read_folder = os.path.abspath("")
file_name = 'chipotle.tsv'

# create data file object
data_file = open(read_folder + '/' + file_name, 'rb')

# print('data file name = {}'.format(data_file))

# read the data file
chipotle = pd.read_csv(data_file, sep='\t')

# print the first 10 entries
print(chipotle.head(10))

# what are the number of observations in the dataset?
print(chipotle.info())

# what are the number of columns in the dataset?
print(chipotle.columns)

# how is the dataset indexed?
print(chipotle.index)

# which is the most ordered item?
c = chipotle.groupby('item_name').sum()
# c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
print(c.head(10))  # print the top 10 most ordered items

# which is the most ordered item in the choice description column?
c = chipotle.groupby('choice_description').sum()
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

# how many items were ordered in total?
c = chipotle.quantity.sum()
print('Total ordered quantity = {}'.format(c))

# what is the total value of the orders placed?
total_value = 0.0
for index, row in chipotle.iterrows():
    total_value = total_value + float(row[1]) * float(row[4].strip('$'))

print('Total value of order placed = ${}'.format(total_value))
