import json

import requests
from requests import RequestException


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist}
        )
        response.raise_for_status()

    except RequestException:
        print("Some Error occured....")
        return

    data = response.json()
    # print(json.dumps(data,indent=2))
    for artwork in data["data"]:
        print(f"* {artwork["title"]}")


if __name__ == "__main__":
    main()
