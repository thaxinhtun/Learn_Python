import sys
t = eval(sys.argv[1])
v0 = eval(sys.argv[2])
g = 9.81
y = v0*t - 0.5*g*t**2
print("y=",y)