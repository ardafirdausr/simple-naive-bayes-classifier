
CATEGORY = ('miskin', 'sedang', 'kaya')
dataset = [1]
def readFile():
        # open file with read operation
        file = open('data.csv', 'r')

        # get title from csv
        title = file.readline()
        # get data table from csv
        table = file.readlines()
        for row in table:
            row = [column.strip() for column in row.split(';')]
            dataset.append(row)
        print(dataset)


        # close file
        file.close()

readFile()
print(dataset)