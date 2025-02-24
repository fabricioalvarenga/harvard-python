def main():
    list_of_students: list[str] = ["Hermione", "Harry", "Ron"]

    for student in list_of_students:
        print(student)
    print("")

    for i  in range(len(list_of_students)):
        print(i + 1, list_of_students[i])
    print("")

    dict_of_students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin"
    }

    for student in dict_of_students:
        print(student, dict_of_students[student], sep = ", ")
    print("")

    students = [
            {"student_name": "Hermione", "student_house": "Gryffindor", "patronus_name": "Otter"},
            {"student_name": "Harry", "student_house": "Gryffindor", "patronus_name": "Stag"},
            {"student_name": "Ron", "student_house": "Gryffindor", "patronus_name": "Jack Russell Terrier"},
            {"student_name": "Draco", "student_house": "Slytherin", "patronus_name": None}
    ]

    for student in students:
        print(student["student_name"], student["student_house"], student["patronus_name"], sep = ", ")
    print("")

    houses: list[str | None] = []
    for student in students:
        if student["student_house"] == "Gryffindor":
            houses.append(student["student_name"])
    print(houses)
    print("")

#    houses = [student["student_name"] for student in houses if student["student_house"] == "Gryffindor"]

main()
