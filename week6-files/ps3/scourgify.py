import sys
import os.path
import csv

if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)


path = f'./{sys.argv[1]}'
if not os.path.isfile(path):
    print(f"Could not read {sys.argv[1]}")
    sys.exit(1)

if len(sys.argv) == 3 and (not sys.argv[1].endswith(".csv")):
    print("Not CSV File")
    sys.exit(1)

try:
    students = []
    file_name = sys.argv[1]
    with open(file_name) as file:
        line_count = 0
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            last,first = row['name'].strip().split(", ")
            students.append([first,last,row['house']])
            # print(f"Student {row['name']} in the {row['house']}")


    with open(sys.argv[2],"w",newline='') as student_file:
        line_count = 0
        for student in students:
            student_writer = csv.writer(student_file,delimiter=',')
            if line_count == 0:
                student_writer.writerow(["first","last","house"])
                line_count += 1
            student_writer.writerow(student)

    # with open(sys.argv[2],"w") as file:
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)
