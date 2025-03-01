def main(): 
    name: str = input("What's your name? ")
    print(hello(name))


def hello(to: str = "world") -> str:
    return f"hello, {to}"


if __name__ == "__main__":
    main()
