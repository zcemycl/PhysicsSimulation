##################################################
#    PHAS1240 2015 final assignment
#    Frozen Angry Birds Star Wars
#    Template code
#    Student number: 15059955
##################################################

import numpy as np
from visual import sphere, vector, color, rate, mag, display

#!@!@### TEMPLATE HEADER STARTS ###@!@!#

scene = display(width = 640, height = 480, center = (5,0,0),autoscale=False, range = 6)

### Set up objects ### 

# Set implicit gravitational constant G = 1
G = 1
# All values are in Galactic Natural Units except where stated otherwise

## The Death Snowball ###
M = 2000 # mass of Death Snowball 
DSrad = 1.0 # radius of Death Snowball
DSpos = vector(7.0,0.0,0.0) # position vector of Death Snowball
DeathSnowball = sphere(pos=DSpos,radius=DSrad,color=color.white,make_trail=True)
vel_DS = vector(0.0,0.0,0.0) # initial velocity of Death Snowball


### The Death Star ###
M2 = 2000 # mass of Death Star
DS2rad = 0.5 # radius of Death Star
DS2pos = vector(10.0,-2.0,0.0) # position vector of Death Star
vel_DS2 = vector(0,15.0,0.0) # initial velocity of Death Star 
DeathStar = sphere(pos=DS2pos,radius=DS2rad,color=color.gray(0.5),make_trail=True)

## Olaf, the Sith Snowman ###
# You will need to complete this section yourself following the specification in the script
OlafAngle = np.radians(45) # angle of Olaf's position relative to DS centre
OlafRad = 0.1 # Olaf's radius
Olafx= 7 + DSrad * np.cos(OlafAngle)# Olaf's x-coordinate 
Olafy= DSrad * np.sin(OlafAngle)# Olaf's y-coordinate 
Olafpos = vector(Olafx, Olafy, 0 )# Olaf's position vector
Olaf = sphere(pos=(Olafx,Olafy,0),radius= OlafRad,color=color.white,opacity=0.5) 

### Angry Jedi bird ###
mbird = 1 # mass of angry bird, may be *much* bigger than 1 later
initpos = vector(0,0,0) # initial position vector of bird
Bird= sphere(pos=initpos,radius=0.1,color=color.red,make_trail=True)
Bird.trail_object.color=color.white # make the trail white

## Set initial parameters of bird ##
v0 = float(raw_input("Input the initial velocity in metres per second: "))# Input the initial velocity
theta = np.radians(float(raw_input("Input the initial angle in degrees: "))) # input the projection angle

## Set velocity, timestep etc ##
vel_bird = vector(v0*np.cos(theta), v0*np.sin(theta), 0) # initial velocity of Bird
dt = 0.0001 # timestep in seconds
step = 1 # loop counter
maxstep = 10000 # maximum number of calculation steps to include

#!@!@### TEMPLATE HEADER ENDS ###@!@!#
##In addition, I want to add one planet orbiting around the death star
## The planet orbiting the DeathStar##
massop0 = 3  # Mass of the planet
initposop0= vector(10.8,-2.0,0)  # initial position vector of the planet
OP0 = sphere(pos=initposop0 , radius=0.02*massop0,color=color.blue,make_trail=False)
veladd = vector(0,65,0)  # initial velocity vector of the planet
## Background setting for universe ##
sphere(pos=[5,0,0],n=5, radius=0.05,color=color.yellow) ##Distant bright stars with different colors in the universe##
sphere(pos=[1,1,1],radius=0.07,color=color.yellow)
sphere(pos=[0,-3,2],radius=0.05,color=color.yellow)
sphere(pos=[2,3,5],radius=0.02,color=color.yellow)
sphere(pos=[2,-2,4],radius=0.03,color=color.orange)
sphere(pos=[4,2.4],radius=0.04,color=color.magenta)
sphere(pos=[2,-1,0],radius=0.01,color=color.green)
sphere(pos=[3,3,3],radius=0.04,color=color.orange)
sphere(pos=[5,-4,4],radius=0.035,color=color.orange)
sphere(pos=[3,1,4],radius=0.03,color=color.magenta)
sphere(pos=[0,-3,2],radius=0.05,color=color.yellow)
sphere(pos=[4,3,5],radius=0.02,color=color.yellow)
sphere(pos=[4,-2,4],radius=0.03,color=color.orange)
sphere(pos=[4,2.4],radius=0.04,color=color.magenta)
sphere(pos=[3,-1,0],radius=0.01,color=color.green)
sphere(pos=[10,3,3],radius=0.04,color=color.orange)
sphere(pos=[0,-3,2],radius=0.05,color=color.yellow)
sphere(pos=[4,3,5],radius=0.02,color=color.yellow)
sphere(pos=[8,-2,4],radius=0.03,color=color.orange)
sphere(pos=[9,2.4],radius=0.04,color=color.magenta)
sphere(pos=[12,-1,0],radius=0.01,color=color.green)
sphere(pos=[9,9,3],radius=0.04,color=color.orange)
##Motion of the angry bird, olaf, death star, death snowball and the planet##
while maxstep >= step:   # Setting of condition for the while-loop
    relposDS1 = DSpos - initpos # Relative position vector of Death Snowball relative to the bird
    relposDS2 = DS2pos - initpos # Relative position vector of Death Star relative to the bird
    relposolaf = Olafpos - initpos # Relative position vector of Oalf relative to the bird
    relposDD = DSpos - DS2pos # Relative position vector of Death Snowball relative to the Death star
    vel_DS2 = vel_DS2 + G*mbird*(-relposDS2)*dt/ relposDS2.mag**3 # Influence of gravity from the bird to the death star
    DS2pos = DS2pos + vel_DS2 * dt # Motion of the Death Star (in Vertical Motion)
    vel_bird = vel_bird + G*M*relposDS1*dt/ relposDS1.mag**3 + G*M2*relposDS2*dt/ relposDS2.mag**3
    # Above shows the velocity of the bird will be affecting by the Gravity of Death Star and Death Snowball
    initpos = initpos + vel_bird*dt # Addition of initial position and the change of position to show the motion of the bird
    vel_DS = vel_DS + G*mbird*(-relposDS1)*dt/ relposDS1.mag**3 #Velocity of Death Star will be affected by the gravity of the bird
    DSpos = DSpos + vel_DS * dt # Addition of previous position and the change of position of the Death Snowball
    Olafpos = Olafpos + vel_DS * dt # Addition of previous position and the change of position of the olaf on the snowball
    
    step = step + 1 # Counting steps
    
    Bird.pos = initpos # Locating the current Bird position
    DeathStar.pos = DS2pos # Locating the current Death Star position
    DeathSnowball.pos = DSpos # Current Death Snowball position
    Olaf.pos = Olafpos  #Current Olaf position
    
    relpos0 = DS2pos - initposop0 # Relative position vector of the planet relative to the Death Star
    veladd = veladd + G*M2*relpos0*dt/ relpos0.mag**3 #Velocity of the planet is influenced by the gravity of the death star
    initposop0 = initposop0 + veladd*dt #Addition of previous position and the change of position for the planet
    OP0.pos = initposop0  #Current planet position
    
##Assuming that when the surface of the bird hits the surface of olaf or death star or death snowball,
##, it will not stop. Only if the centre of the bird hits any of the surface, it stops.
    if relposolaf.mag <= OlafRad: # If the bird hits the Olaf, 
        print "The speed of impact:" , vel_bird.mag , "m/s" # print out the collision velocity
        print "Angry bird collides with the Olaf" # And tell It hits the Olaf
        break        # Stop the animation
    if relposDS1.mag <= DSrad:  # If the bird hits the Death Snowball
        print "Angry bird collides with The Death Snowball" # Tell it hits the Snowball
        break       # Stop the animation
    if relposDS2.mag <= DS2rad: # If the bird hits the Death Star
        print "Angry bird collides with The Death Star"  # Tell it hits the Star
        break       # Stop the animation
    if relposDD.mag <= 1.5: # If the Death Snowball collides with the Death Star
        print "Death Star collides with Death Snowball"  # Show their collision
        break       # Stop the animation
    rate (1000)    # Rate of loop per second
    
if relposDS1.mag >= DSrad and relposDS2.mag >= DS2rad and relposolaf.mag >= OlafRad:  # If the bird misses everything
    print "Angry bird misses all the target"    # Show that it misses all the object 
print "end"   # print end if the loop is ended.

## Successful initial parameters resulting in collision between the bird and the olaf:
## Initial speed = 20 m/s and Initial angle = 26 in degrees in the case of M=1 angry bird
## Initial speed = 29 m/s and Initial angle = 20 in degrees in the case of M=1 angry bird


