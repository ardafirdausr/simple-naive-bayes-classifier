# open file with read operation
file = open('data.csv', 'r')

# get title from csv
title = file.readline()
# get data table from csv
table = file.readlines()
data = []
for row in table:
    row = [column.strip() for column in row.split(';')]
    data.append(row)
print(data)


# close file
file.close()