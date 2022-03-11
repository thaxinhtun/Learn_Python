import sys
try:
    t = eval(sys.argv[1])
    v0 = eval(sys.argv[2])
except IndexError:
    print("You forget to enter parameters")
    t = eval(input("t?: "))
    v0 = eval(input("v0?: "))
    
g = 9.81
y = v0*t - 0.5*g*t**2
print("y=",y)