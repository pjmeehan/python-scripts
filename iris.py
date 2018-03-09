# Patrick Meehan 2018-03-01
# Using Fisher's iris data to learn formatting (https://en.wikipedia.org/wiki/Iris_flower_data_set)

import csv 

x = open("data/iris.csv") # opens the file with the data 

csv_x = csv.reader(x)

for row in csv_x:
  print('{:<5} {:<5} {:<5} {:<5}'.format(*row))
    