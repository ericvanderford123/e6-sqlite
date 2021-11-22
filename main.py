import csv
with open('data folder/coffees.csv') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read())
    csvfile.seek(0)
    reader= csv.DictReader(csvfile, dialect=dialect)
    for line in reader:
        print(line)

