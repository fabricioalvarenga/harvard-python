import sys

#try:
#    print("Hello, my name is", sys.argv[1])
#except IndexError:
#    print("Too few arguments")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

print("My name is", end = " ")
for arg in sys.argv[1:]:
    print(arg, end = " ")
print()
