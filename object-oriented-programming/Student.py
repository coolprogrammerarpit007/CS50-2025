
class Student:
    def __init__(self,name,house):
        # self gives the acess to the current object.
        if not name:
            raise ValueError("Missing Name")

        if house not in ["Gryffindorr","Hupplepuff","Slythrin","Revenclaw"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"Student {student.name} is from the house of {student.house}")


def get_student():
    name = input("Enter Name: ")
    house = input("Enter House: ")
    try:
        student = Student(name,house)
        return student

    except ValueError:
        print("Fail")






if __name__ == "__main__":
    main()