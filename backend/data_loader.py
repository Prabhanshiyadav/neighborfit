import csv

def load_data():
    with open("data/neighborhoods.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
