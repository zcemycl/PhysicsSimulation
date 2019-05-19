## Name: Leung Yui Chun,Leo
## Topic: Animation of the projectile and rebouncing motion of the ball
from visual import sphere, curve, color, display, rate
import numpy as np
# set up the scene
scene = display(x = 50, y = 50, width = 640, height = 480, center = (20,0,0))
ground = curve(pos=[(-5,0,0),(50,0,0)],color = color.green)

# initial ball coordinates (metres)
x0 = 0.0
y0 = 0.0
y = y0
g = 9.8 # gravitational acceleration, m/s2
dt = 0.01 # time interval for loop, in seconds

# input initial angle and velocity and the coefficient of restitution
dtheta = float(raw_input("Input the initial angle in degrees: "))
theta = np.radians(dtheta)  #changing the angle from degree into radian
v0 = float(raw_input("Input the initial velocity in metres/second: "))
e= float(raw_input("Input the coefficient of restitution: "))
# start the animation
ball = sphere(pos = (x0,y0,0),radius = 1,make_trail=True)
t = 0 # initial time
# print the calculation time and range for the first projection
tc = 2*v0*np.sin(theta) / g
print "Time travelled:(by calculation)" , tc, "(s)"
r = (v0**2)*np.sin(2*theta) /g
print "Travelling range:(calculated by range equation)" , r, "(m)"

#then let's set up a while-loop with condition.
while v0 > 0.1:     
    while y >= y0:
        x = x0 + v0*np.cos(theta)*t
        y = y0 + v0*np.sin(theta)*t - 0.5*g*(t**2)
        t = t+dt
        ball.pos = (x,y,0)
        rate(50)
    print "Time travelled:(counted by the while-loop)" , t, "(s)"
    print "Travelling range:(counted by the while-loop)" , x, "(m)"

    t=0
    alptha = np.pi*0.5 - theta
    beta = np.arctan(np.tan(alptha)/e)
    v0 = v0*e*(np.cos(alptha)/np.cos(beta))
    theta = np.pi*0.5 - beta
    ball.pos = (x,y,0)
    x0 = x     #the ball bounces in the previous position.
    y = y0
    if (v0*np.sin(theta) == 0) :  #Every time when the system runs the code again, 
        break     #it sees whether the vertical velocity = 0, if it is, the while-loop finally stops. 

#1. Finally, we can see that when comparing the first calculation and counting in the beginning of the console, we can see
#there is a difference between the answers. It is because we assume dt= 0.01s, time is so large comparing with the 
#reality, therefore, in the reality the ball moves in the curve, but ball moves in a curve with infinite small straight line, 
#then the range will then be different. 


#2. The calculation will be more accurate to the answer calculated by the range equation, when the dt goes so small, which is fit in
#the reality. 

#Challenge:
#1. I actually use the break to stop the loop with some conditions.
#2. The code doesn't reveal the realistic result. As we do not have included other factors, like air resistance, friction acting 
#on the ball causing the deceleration of the xcomponent of velocity. Even more, the ball will stop bouncing and start to rotate and travel 
#for a distance before it stops.



    