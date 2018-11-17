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