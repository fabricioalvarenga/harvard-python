def main():
    input1: str = input("Enter a number: ")
    input2: str = input("Enter another number: ")

    try:
        number1: float = float(input1)
        number2: float = float(input2)
    except:
        print("Invalid input(s)!")
        exit(0)

    operation: str = input("Enter an operation: ")

    if not operation in ["+", "-", "*", "/", "**", "%", "//"]:
        print("Invalid operation!")
        exit(0)

    result: float = calculate(number1, number2, operation)

    print("The resutl of", number1, operation, number2, "is:", end = " ")
    print(f"{result:,}")

def calculate(number1: float, number2: float, operation: str) -> float:
    match operation:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2
        case "/":
            return number1 / number2
        case "**":
            return pow(number1, number2)
        case "%":
            return number1 % number2
        case "//":
            return number1 // number2
        case _:
            print("Invalid operation")
            exit(0)

main()
