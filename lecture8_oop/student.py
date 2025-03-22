class Student:
    name: str
    house: str

    def __init__(self, name:str , house: str):
        self.name = name
        self.house = house

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_house(self) -> str:
        return self.house

    def set_house(self, house: str):
        self.house = house


def main():
    student: Student = get_student()
    print(f"{student.name} from {student.house}")


def get_student() -> Student:
    name: str = input("Name:  ")
    house: str = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
