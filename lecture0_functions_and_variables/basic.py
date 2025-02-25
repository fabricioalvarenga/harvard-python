#
def main():
    print(hello())

    a: int = 15
    print(a)

    b = None
    print("The type of b is: ", type(b))

    c: bool = True
    print(c)

    e: float = 7.5678
    print(e)
    print(round(e, 2))

    name: str = "fabricio de oliveira alvarenga   "
    print(f"My name is: {name}")
    print("My name is:", name)
    print(hello(name))

    # Remove whitespace from trailing and leading of string
    print("Strip:", name.strip())

    # Remove whitespace from trailing of string
    print("Right strip:", name.rstrip())

    # Remove whitespace from leading of string
    print("Left strip:", name.lstrip())

    # Capitalize the string
    print("Capitalize:", name.capitalize())
    print("Title:", name.title())

    # Split the string
    u: list[str] = name.split()
    print("Split:", u)

    g: complex = complex(8, 2)
    print(g)

    l: list[int | list[str]] = [0, 2, 3, ["fabricio", "giseuda"]]
    print(l)

    t: tuple[tuple[str, str], tuple[str, str], tuple[int, int]] = (("fabricio", "giseuda"), ("fabiano", "priscila"), (1, 2))
    print(t)

    d: dict[str, int] = {"age": 47, "year": 2024}
    print(d)

    print(a + e)
    print(a - e)
    print(a * e)
    print(a / e)
    print(a // e)
    print(a % e)
    print(e ** 2)

    # Implict type casting
    i = 1.9
    j = 8
    print(i + j) # Converts j to float

# Function hello
def hello(to: str = "world"):
    print("Hello,", to)

# Call main
main()
