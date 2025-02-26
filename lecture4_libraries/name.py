import sys

try:
    print("Hello, my name is", sys.argv[0])
except IndexError:
    print("Too few arguments")
