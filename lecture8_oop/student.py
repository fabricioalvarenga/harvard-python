class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}, patronus {self.charm()}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def patronus(self):
        return self._patronus

    @patronus.setter
    def patronus(self, patronus):
        self._patronus = patronus

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "😎"
            case "Jack":
                return "🐶"
            case _:
                return "🪄"

    @classmethod
    def get(cls):
        name = input("Name:  ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return cls(name, house, patronus)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
