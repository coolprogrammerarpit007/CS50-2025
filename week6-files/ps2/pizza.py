import sys
from tabulate import tabulate
import csv

menus = []

if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit(1)

try:
    csv_file = sys.argv[1]
    with open(csv_file) as file:
        for line in file:
            row = line.rstrip().split(',')
            menus.append(row)

    print(tabulate(menus,headers="firstrow",tablefmt="grid"))


except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)