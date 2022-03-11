import sys
try:
    F = eval(sys.argv[1])
except IndexError:
    raise IndexError("You forgot to enter value from command")
    sys.exit(1)
C = 5/9*(F-32)
print("clesius is %.2f"%C)