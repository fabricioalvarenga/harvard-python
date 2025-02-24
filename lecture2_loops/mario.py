def main():
    print_column(3)
    print_row(4)
    print_square(3)

def print_column(height: int):
    print("#\n" * height, end = "")

def print_row(width: int):
    print("[]" * width)

def print_square(size: int):
    for _ in range(size):
        print_row(size)

main()
