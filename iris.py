# Patrick Meehan 2018-03-01
# Using Fisher's iris data to learn formatting (https://en.wikipedia.org/wiki/Iris_flower_data_set)

# use the import function to import the iris data set.

import csv 

# use open function to open the file with the data.

x = open("data/iris.csv")  

# The reader object allows iteration, much like a regular file object does. This let’s us iterate over each row 
# in the reader object and print out the line of data, minus the commas. This works because each row is a list
# and we can join each element in the list together, forming one long string.
# https://dzone.com/articles/python-101-reading-and-writing

csv_x = csv.reader(x)

# use a for statement to run through each row.

for row in csv_x:

# use print statement along with format to format the data in each row with certain amount of spaces. 
  
  print('{:<5} {:<5} {:<5} {:<5}'.format(*row))
    