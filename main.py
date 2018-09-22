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

#Hitung mean
def mean(numbers):
	return sum(numbers)/float(len(numbers))

#hitung Standar Deviasi
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
	return math.sqrt(variance)


# close file
file.close()
