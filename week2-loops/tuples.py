# tuples in python

def main():
    coordinates = (42.376,-71.115)
    latitude,longitude = coordinates
    print(f"Latitude: {coordinates[0]} and Longitude is: {coordinates[1]}")
    print(f"Latitude: {latitude} and Longitude is: {longitude}")


    # Tuples are immutable and are much faster than lists. so if you are sure your collection is not going to change than use tuples.
if __name__ == '__main__':
    main()