import sqlite3
import csv
connection_handle = sqlite3.connect('data/cafe.sqlite3')


with open('data folder/coffees.csv') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read())
    csvfile.seek(0)
    reader= csv.DictReader(csvfile, dialect=dialect)
    done=False
    while not done:
        try:
            line=next(reader)
            print(line)
        except:
            done=True
