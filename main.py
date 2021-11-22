
import csv

with open('data folder/coffees.csv') as f:
    csv_reader = csv.reader(f)


    next(csv_reader)

    # show the data
    for line in csv_reader:
        print(line)