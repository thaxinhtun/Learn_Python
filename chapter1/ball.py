v0 = 5 
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print("The height of the ball is: ",y)
#print("After 0.6 s, the ball with initial velocity of 5 m/s is at height of 1.2342 m")
print("After %.1f s, the ball with initial velocity of %d m/s is at height of %.4f m" %(t,v0,y))
print("""
      After %.1f s, the ball with 
      initial velocity of %d m/s 
      is at height of %.4f m
      """ %(t,v0,y)
      )
