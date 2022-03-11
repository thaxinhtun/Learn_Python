import sys
try:
    C = float(sys.argv[1])
except IndexError:
    print("No command arguments for C!")
    sys.exit(1)
except ValueError:
    print("C must be pure number , not%s!"%sys.argv[1])
    sys.exit(1)
F = 9/5*C + 32
print("%gC is %.1f F"%(C,F))