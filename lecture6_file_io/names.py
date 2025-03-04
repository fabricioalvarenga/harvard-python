#file = open("names.txt", "a")

with open("names.txt", "w") as file:
    for _ in range(3):
        name = input("What's your name? ")
        file.write(f"{name}\n")

#file.close()

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())

print()

with open("names.txt", "r") as file:
    for line in file:
        print(line.rstrip())

print()

with open("names.txt", "r") as file:
    names = file.readlines()

for name in sorted(names):
    print(name.rstrip())

print()

with open("names.txt", "r") as file:
    for line in sorted(file):
        print(line.rstrip())
