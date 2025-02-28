def main():
    hello("world")
    goodbye("world")

def hello(name: str):
    print(f"hello, {name}")

def goodbye(name: str):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()
