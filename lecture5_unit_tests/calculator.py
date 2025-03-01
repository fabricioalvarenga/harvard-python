def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n: float):
#    return n + n # The corret should be n * n
    return n * n

if __name__ == "__main__":
    main()

