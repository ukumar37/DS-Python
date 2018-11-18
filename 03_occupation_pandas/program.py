# Getting and knowing your data - Part 2

import os

import pandas as pd  # its convention to refer to 'pandas' as pd

import numpy as np  # its conventional to refer to "numpy" as np

# Define the read folder
read_folder = os.path.abspath("")
file_name = 'user.txt'

# create data file object
data_file = open(read_folder + '/' + file_name, 'rb')

# print('data file name = {}'.format(data_file))

# read the user file
users = pd.read_table(data_file, sep='|')

# print the user file (first and last 5 entries)
print(users.head(5))
print(users.tail(5))

# number of observations in the df
total_rows = users.shape[0]
total_columns = users.shape[1]
print("Total observations = {} rows and {} columns".format(total_rows, total_columns))

# print column names
print('columns names are = {}'.format(users.columns))

# how is the data indexed? (aka "the labels")
print(users.index)

# what is the type of data in each column
print('data types are as follows: \n {}'.format(users.dtypes))

# print only the occupation column
print(users['occupation'])

# what is the most frequent occupation
print(users.groupby(['occupation']).count().sort_values(by=['user_id'], ascending=False))

# summarize the dataframe (note: by default, only the numeric columns are returned)
print(users.describe())

# summarize ALL the dataframe
print(users.describe(include="all"))

# summarize the 'occupation' column only
print(users['occupation'].describe())

# what is the mean age of users?
print('mean age of users is = {:,.2f} years'.format(users['age'].mean()))

# what is the age with the least occurrence?
print('age with the least occurrence is {} years'.format(users['age'].value_counts().tail()))
