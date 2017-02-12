import csv

with open('graph1.csv') as graphFile:
    readCSV = csv.reader(graphFile, delimiter=',')

    for xrow in readCSV:
        for i in range(len(xrow)):
            print(xrow[i], end = ":")

    for row in readCSV:
        print(row)
