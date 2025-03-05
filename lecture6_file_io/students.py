import os
import csv

####################################################################################################################
with open("students.csv") as file:
    students: list[dict[str, str]] = []

    for line in file:
        name, city, state = line.rstrip().split(",")

#        student = {}
#        student["name"] = name
#        student["city"] = city
#        student["state"] = state
        student = {"name": name, "city": city, "state": state}
        students.append(student)

def get_name(student: dict[str, str]) -> str:
    return student["name"]

def get_city(student: dict[str, str]) -> str:
    return student["city"]

for student in sorted(students, key = get_city):
    print(f"{student['name']} is from {student['city']}/{student['state']}")

print()

for student in sorted(students, key = get_name, reverse = True):
    print(f"{student['name']} is from {student['city']}/{student['state']}")

print()

# The code 'lambda: student: student["name"]' is equivalent to the funtion:
# get_name(student: dict[str, str]) -> str:
#   return student["name"]
for student in sorted(students, key = lambda student: student["name"]): # lambda defines a function that has no name
    print(f"{student['name']} is from {student['city']}/{student['state']}")

print()

####################################################################################################################
with open("students.csv") as file:
    for line in sorted(file):
        name, city, state = line.rstrip().split(",")
        print(f"{name} is in {city}/{state}")

print()

####################################################################################################################
with open("students.csv") as file:
    students = []

    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "city": row[1], "state": row[2]})

for student in sorted(students, key = lambda student: student["name"]): 
    print(f"{student['name']} is from {student['city']}/{student['state']}")

print()

####################################################################################################################
with open("students.csv") as file:
    students = []

    reader = csv.reader(file)
    for name, city, state in reader:
        students.append({"name": name, "city": city, "state": state})

for student in sorted(students, key = lambda student: student["name"]): 
    print(f"{student['name']} is from {student['city']}/{student['state']}")

print()

####################################################################################################################
with open("students2.csv") as file: # Opening 'students2.csv'
    students = []

    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "city": row["city"], "state": row["state"]})

for student in sorted(students, key = lambda student: student["name"]): 
    print(f"{student['name']} is from {student['city']}/{student['state']}")

print()

####################################################################################################################
name: str = input("What's your name? ")
home: str = input("Where's your home? ")

file_name: str = "students3.csv"
file_size: int

try:
    file_size = os.path.getsize(file_name)
except FileNotFoundError :
    file_size = 0

with open(file_name, "a") as file:
    writer = csv.writer(file)
    if file_size == 0: writer.writerow(["name", "home"])
    writer.writerow([name, home])

    dict_writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    dict_writer.writerow({"home": "_" + home, "name": "_" + name})

