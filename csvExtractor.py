import sys, csv

# Arg1 is Path to Data file
# Arg2 is Column to Display

values = []
with open(sys.argv[1], newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        values.append(row[sys.argv[2]])

values = set(values)
for item in values:
    print(item)
