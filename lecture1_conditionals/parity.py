def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(value: int) -> bool:
    return value % 2 == 0

main()
