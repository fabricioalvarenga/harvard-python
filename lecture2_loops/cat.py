#
def main():

    print("meow\n" * 3, end = "")
    print("")

    i: int = 0
    while i < 3:
        print("meow")
        i += 1
    print("")

    for _ in range(3):
        print("meow")
    print("")

    for _ in [0, 1, 2]:
        print("meow")
    print("")

    number = get_number()
    meow(number)
    print("")

def get_number() -> int:
    while True:
        n = int(input("What's  n? "))
        if n > 0:
            return n

def meow(n: int):
    for _ in range(n):
        print("meow")

main()
