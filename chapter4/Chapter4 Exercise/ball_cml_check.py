import sys
g = 9.81
try:
    t = eval(sys.argv[1])
    v0 = eval(sys.argv[2])
except IndexError:
    print("You forget to enter parameters")
    t = eval(input("t?: "))
    v0 = eval(input("v0?: "))
    
if not t>=0 and t<= 2*v0/g:
    raise ValueError("You entered not real value for t")
    sys.exit(1)
else:
    y = v0*t - 0.5*g*t**2
    print("y=",y)
  