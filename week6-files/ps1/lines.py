import sys


if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

if len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
    print("Not a Python file")
    sys.exit(1)

try:
    count_lines = 0
    file_name = sys.argv[1]
    with open(file_name) as f_hand:
        for line in f_hand:
            if not line.lstrip().startswith("#") and not line.isspace():
                count_lines += 1
            else:
                continue

    print(f"{count_lines}")

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
