import re
import sys


url = input("URL: ").strip()

# matches =
# using the walrus operator.

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_])$",url,re.IGNORECASE):
    print(f"Username: ",matches.group(1))