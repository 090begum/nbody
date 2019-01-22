# CS-UY 1114
# Final project
# Begum Ferdous
import turtle
import time
import math
import random
# gravitional constant (to be read from file)
G = 0
# current state of all bodies (to be read from file)
# each entry in the list is a tuple consisting of:
#   body name
#   body position (x,y)
#   body velocity (x,y)
#   body mass
# This value is updated at each step of the simulation
# by the update_positions and update_velocities functions.
bodies = [("Sun", 500.0, 500.0, 0.0, 0.0, 100000000.0), 
          ("Splat", 255.0, 255.0, 2.0, 0.0, 1.0)]

def readfile():
    """
    signature: () -> NoneType
    This function is called only once, when the
    program first starts. It  reads the file
    bodies.txt, which contains the correct value
    of the gravitional constant and the initial
    data about the planets, and store this data
    in the global variables. 
    """
    global G
    global bodies
    colors = ["purple","blue","red","violet","goldenrod","darkorange","midnightblue","darkviolet"] # list of colors for each body
    acc= []
    f = open("bodies.txt","r") # opens the file in the read mode
    for line in f:
        line = line.strip()  
        x = line.split()  #iterates through each line of the file in a list
        acc.append(x)       #appends each line of info to list
    f.close()          
    G = float(acc[0][0])  # changes the value of the global variable G
    bodies1 = acc[1:]     # slicing acc to change str -> float
    bodies=[] # empty new bodies list to check if there is an empty list in the file
    for line in bodies1:   
        for i in range(1,len(line)):
            line[i] = float(line[i])
        if line != []: # if there is not empty list,append to new bodies list
            bodies.append(line)
            line.append(random.choice(colors)) #appending a color for each body at random
    
def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables,all visual
    elements are drawn on the screen: the planets
    their labels and colors, and their current positions.
    This function is where the drawing happens.
    Other functions in this program merely update the state
    of global variables.
    This function also does not modify any
    global variables.
    """
    for i in range(len(bodies)): #for each body, turtle will be called to draw each body
        turtle.hideturtle()
        turtle.penup()
        turtle.goto((bodies[i][1]),(bodies[i][2])) # Each point 
        turtle.pendown()
        if (bodies[i][5])< 12000: # if the mass of a body is < 12000, the radius = 1, else radius = 10
            turtle.color("white")
            turtle.fillcolor(bodies[i][6]) #for each body there will be a color
            turtle.begin_fill()
            turtle.circle(1)
            turtle.end_fill()
        else:
            turtle.color("black")
            turtle.fillcolor(bodies[i][6]) #for each body there will be a color
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
        turtle.color("white")
        turtle.write(bodies[i][0]) # writing the name of each body
            
            
    
def update_velocities():
    """
    signature: () -> NoneType
    This function updates the global bodies variable
    with the updated velocities of the bodies, as
    described above.
    That is, given the current velocities and
    positions of each body, calculate their velocity
    at the next frame.
    """
    global bodies  
    for i in range (len(bodies)): #iterating through each body
        force_x = 0  # horizontal force is reset 
        force_y = 0  # vertical force is reset 
        for j in range(len(bodies)): # iterating through all the other bodies 
            horizontal_distance = (bodies[j][1]-bodies[i][1]) # horizontal distance of both bodies
            vertical_distance = (bodies[j][2]-bodies[i][2]) # vertical distance of both bodies
            distance = math.sqrt((horizontal_distance)**2 + (vertical_distance)**2) # distance between two bodies
            if distance != 0:  
                mass_1 = (bodies[i][5]) # mass of body 1
                mass_2 = (bodies[j][5]) # mass of body 2
                force_x += ((G * mass_1*mass_2*horizontal_distance)/(distance**3))# finding the horizontal net force for each body
                force_y += ((G * mass_1*mass_2*vertical_distance)/(distance**3)) #finding the vertical net force for each body
        acceleration_x = force_x / mass_1 # horizontal acceleration for each body
        acceleration_y = force_y /mass_1 # vertical accerleration for each body
        current_xvelocity = (bodies[i][3]) # current horizontal velocity for each body
        current_yvelocity = (bodies[i][4]) # current vertical velocity for each body
        bodies[i][3] = current_xvelocity + acceleration_x #updated horizontal velocity for each body
        bodies[i][4] = current_yvelocity + acceleration_y   #updated vertical velocity for each body
        


def update_positions():
    """
    signature: () -> NoneType
    This function updates the global bodies variable
    with the updated positions of the bodies, as
    described above.
    That is, given the current velocities and
    positions of each body, calculate their position
    at the next frame.
    """
    global bodies

    for i in range(len(bodies)):
        current_xposition = bodies[i][1] # current horizontal position for each body
        current_yposition = bodies[i][2] # current vertical position for each body
        bodies[i][1] = current_xposition + (bodies[i][3]) # updated horizontal position for each body
        bodies[i][2] = current_yposition + (bodies[i][4])  #updated vertical position for each body
               

def main():
    """
    signature: () -> NoneType
    Run the simulation. You shouldn't
    need to modify this function.
    """
    turtle.setworldcoordinates(100,100,800,800)# set the coordinates on turtle canvas
    turtle.Screen().bgcolor("black")# sets the background color for the canvas
    turtle.tracer(0,0)
    turtle.hideturtle()
    readfile()
    while True:
        update_velocities()
        update_positions()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)
main()

