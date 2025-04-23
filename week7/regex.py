import re
import sys

name = input("What's your name? ").strip()
# last = ''
# first = ''
# if "," in name:
#     last,first = name.split(", ")
# print(f"Hello {first} {last}")

pattern = r'^([a-zA-Z]+),\s?([a-zA-Z]+)$'
match = re.search(pattern,name)
# print(match)

if match:
    last,first = match.groups()
    name = f"{first} {last}"
    print(f"Hello {name}")