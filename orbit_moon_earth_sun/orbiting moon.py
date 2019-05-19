#Initial Settings
from visual import sphere, vector, color, rate, mag #input the useful function
dt = 0.00001 #Set the difference of time small to make the distance travelled by time small
step = 1  #Initial number of steps
maxstep = 2000000000  #Maximum numbder of steps

M =18  #Mass of Sun
mass0 = 0.5  #Mass of Earth
massop0 = 0.15   #Mass of moon
initpos0 = vector(0,1,0)   #Using position vector to locate the initial position of earth
initposop0= vector(0,1.03685,0)  #Initial position of moon
Planet0 = sphere(pos=initpos0,radius=0.04*mass0,color=color.blue,make_trail=True)  #Appearance settings of moon and earth
OP0 = sphere(pos=initposop0 , radius=0.01*mass0,color=color.white,make_trail=True)  #If you want to see the trail of moon, 
Planet0.trail_object.color=color.white                                               #Please type in True instead of False
OP0.trail_object.color=color.white
Star = sphere(pos=(0,0,0),radius=0.18,color=color.yellow)  #Appearance setting of sun and its position which is constant in the task
vel0 = vector(-2.95,0,0)               #initial velocity of the earth
veladd = vector(-4.3125,0,0)           #initial velocity of the moon, which I believe it is the summ of vel0 and the relative velocity 
                                       #of the moon relative to the earth 
while step <= maxstep:  #Make the easier condition to let the programme continue to run
    relpos0 = initpos0 - initposop0   #relative position of the moon relative to the earth, so that the vector is always pointing to the centre of the earth
    vel0 = vel0 - M*mass0*initpos0*dt/ initpos0.mag**3   #The velocity of the earth is changing under the gravity of sun
    veladd = veladd + massop0*mass0*relpos0*dt/ relpos0.mag**3 -M*mass0*initpos0*dt/ initpos0.mag**3  # ****it reveals that 
#the calculation of the double addition of fictitious forces to the non-inertial frame of the moon, one is the gravity of earth 
#one is the gravity of sun towards the earth
    initposop0 = initposop0 + veladd*dt  #the initial position of the moon keeps on changing with its new velocity
    initpos0 = initpos0 + vel0*dt #the initial position of the earth keeps on changing with its new velocity
    Planet0.pos = initpos0 #Shows the relationship of the name of code and its object
    OP0.pos = initposop0
    step = step +1 #adding up the step to fulfill the condition
    rate (50000) #Number of calculation per second
    
###If you wish to trace the orbiting radius of the moon around the earth,
###please uncomment (Alt+ 1) codes from line 35-39
#    if relpos0.mag == 0.03685:
#        print "It is under constant orbit"
#    else:
#        print "It reveals the reality of not orbiting a constant orbit"
#        print relpos0.mag 
print("end of program")