# Getting and knowing your data

import os

import pandas as pd

import numpy as np

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
c = chipotle['quantity'].sum()
print('Total ordered quantity = {:,}'.format(c))

# what is the total value of the orders placed?
total_value = 0.0
for index, row in chipotle.iterrows():
    total_value = total_value + float(row[1]) * float(row[4].strip('$'))

print('Total value of order placed = ${:,.2f}'.format(total_value))

# check the item_price type
print('item_price data type is = ' + str(chipotle.item_price.dtype))

# convert the item_price type to float
dollarizer = lambda x: float(x[1:-1])
chipotle.item_price = chipotle.item_price.apply(dollarizer)
print('item_price data type is = ' + str(chipotle.item_price.dtype))
print(chipotle.head(3))

# find the total revenue
total_revenue = (chipotle['quantity'] * chipotle['item_price']).sum()
print('Total sales revenue is = ${:,.2f}'.format(total_revenue))

# how many orders were placed in that period?
# total_orders_placed = chipotle.shape[0]  # row count = [0] and column count = [1]
total_orders_placed = chipotle['order_id'].nunique()  # number of unique/distinct values in a column
print('Total orders placed = {}'.format(total_orders_placed))

# how many orders were made in the total period
total_orders_quantity = chipotle['quantity'].sum()
print('Total order quantity = {}'.format(total_orders_quantity))

# what is the average revenue per order?
ave_revenue = total_revenue/total_orders_placed
print('Average revenue per order is ${:,.2f}'.format(ave_revenue))

# how many different items are sold?
distinct_items_sold = chipotle['item_name'].nunique()
print('Total distinct items sold = {}'.format(distinct_items_sold))