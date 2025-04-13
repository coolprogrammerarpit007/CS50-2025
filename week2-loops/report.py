def main():
    spacecraft = {
        "name":"Voyager 1",
        "distance":"163"
    }
    spacecraft1 = {
        "name":"Space-X",
    }
    spacecraft1.update({"distance":237,"orbit":"Mars"}) # update dictionary
    print(create_report(spacecraft))
    print(create_report(spacecraft1))

def create_report(spacecraft):
    return f"Name of Spacecraft: {spacecraft["name"]}, and distance it traveled is: {spacecraft.get("distance","Unknown")} AU"



if __name__ == "__main__":
    main()

    # dictionary.keys() will return all the keys in the dictnories