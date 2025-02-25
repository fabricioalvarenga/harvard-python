def main():
    x: int = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt: str) -> int:
    while True:
        try:
            x: int = int(input(prompt))
        except ValueError:
            print("x is not an integer")
#            pass
        else:
            return x

main()
