#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10710841
#    Student name: Sumin KIM
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked and will automatically be awarded a mark of 0.
#  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). [02021PT]
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  CITY SKYLINE
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  This template file must be used and you will submit
#  your final solution as a single file only.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *
from random import randint, choice

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]


#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid = True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font = grid_font)
     
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6]]
fixed_plan_2 = [[2, 'B', 7]]
fixed_plan_3 = [[3, 'C', 5]]
fixed_plan_4 = [[4, 'D', 4]]
fixed_plan_5 = [[1, 'A', 9]]
fixed_plan_6 = [[2, 'B', 2]]
fixed_plan_7 = [[3, 'C', 3]]
fixed_plan_8 = [[4, 'D', 6]]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10], [2, 'A', 5], [3, 'A', 1]]
fixed_plan_10 = [[1, 'B', 10], [2, 'B', 5], [3, 'B', 1]]
fixed_plan_11 = [[1, 'C', 10], [2, 'C', 5], [3, 'C', 1]]
fixed_plan_12 = [[1, 'D', 10], [2, 'D', 5], [3, 'D', 1]]
fixed_plan_13 = [[1, 'A', 10], [2, 'A', 5], [3, 'A', 1]]
fixed_plan_14 = [[1, 'B', 10], [2, 'B', 5], [3, 'B', 1]]
fixed_plan_15 = [[1, 'C', 10], [2, 'C', 5], [3, 'C', 1]]
fixed_plan_16 = [[1, 'D', 10], [2, 'D', 5], [3, 'D', 1]]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
         [[1, 'D', 2],
          [2, 'B', 7],
          [5, 'C', 6],
          [6, 'A', 4]]
fixed_plan_18 = \
         [[1, 'D', 6],
          [3, 'C', 5],
          [4, 'B', 3],
          [9, 'A', 9],
          [10, 'D', 2]]
fixed_plan_19 = \
         [[5, 'C', 6],
          [6, 'B', 9],
          [7, 'A', 5],
          [8, 'A', 7],
          [9, 'D', 4]]
fixed_plan_20 = \
         [[1, 'A', 4],
          [2, 'B', 4],
          [3, 'A', 5],
          [4, 'D', 7],
          [10, 'B', 10]]
fixed_plan_21 = \
         [[1, 'B', 6],
          [3, 'A', 4],
          [4, 'C', 4],
          [6, 'A', 8],
          [8, 'C', 7],
          [9, 'B', 5],
          [10, 'D', 3]]
fixed_plan_22 = \
         [[1, 'A', 10],
          [2, 'A', 9],
          [3, 'C', 10],
          [4, 'B', 5],
          [5, 'B', 7],
          [6, 'B', 9],
          [7, 'C', 2],
          [8, 'C', 4],
          [9, 'A', 6],
          [10, 'D', 7]]
fixed_plan_23 = \
         [[3, 'A', 8],
          [4, 'C', 8],
          [5, 'B', 4],
          [6, 'D', 5],
          [7, 'C', 5],
          [8, 'A', 3],
          [9, 'D', 2]]
fixed_plan_24 = \
         [[2, 'C', 3],
          [3, 'B', 1],
          [4, 'C', 3],
          [5, 'C', 1],
          [6, 'D', 2],
          [7, 'B', 1],
          [8, 'D', 2],
          [9, 'C', 7],
          [10, 'A', 1]]
fixed_plan_25 = \
         [[1, 'B', 7],
          [3, 'C', 1],
          [6, 'D', 3],
          [7, 'A', 7],
          [8, 'D', 3],
          [9, 'C', 7],
          [10, 'C', 9]]
fixed_plan_26 = \
         [[1, 'A', 6],
          [2, 'A', 2],
          [3, 'A', 9],
          [4, 'D', 1],
          [5, 'C', 7],
          [6, 'D', 6],
          [7, 'B', 5],
          [8, 'A', 1],
          [9, 'D', 10],
          [10, 'A', 6]]
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#

def random_plan(print_plan = True):
    building_probability = 70 # percent
    option_probability = 20 # percent
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1): # consider each building site
        if randint(1, 100) <= building_probability: # decide whether to build here
            style = choice(['A', 'B', 'C', 'D']) # choose building style
            num_floors = randint(1, 10) # choose number of floors
            city_plan.append([site, style, num_floors])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by completing the "build_city" function below.
#

##draw the office
def office(floor):#define office function.
    #draw the office's base
    setheading(0)
    color('black')
    pd()
    width(2)
    color('black','lightpink')
    begin_fill()
    forward(75)
    left(90)

    forward(60)
    left(90)
    forward(150)
    left(90)
    forward(60)
    left(90)
    forward(75)
    end_fill()


    pu()
    forward(30)
    left(90)
    pd()
    width(2)
    color('black','lightgoldenrod1')#draw the office's door
    begin_fill()
    circle(30,180)
    end_fill()
    
    right(90)
    pu()
    forward(45)
    right(90)
    forward(60)
    right(90)
    pd()
    #draw the office's floor
    def draw_floor():#define office's floor
            side=150
            height=30
            
            pd()
            color('black','lightpink')
            width(2)
            begin_fill()
            for step in range(2):
                forward(side)
                left(90)
                forward(height)
                left(90)
            end_fill()

            pu()
            forward(30)
            left(90)
            forward(10)
            pd()
            right(90)
            #draw the office's window
            for window in range(3):
                color('black','lightsteelblue3')
                begin_fill()
                for step in range(4):
                    forward(10)
                    left(90)
                end_fill()    
                pu()
                forward(40)
                pd()
            pu()
            left(90)
            forward(20)
            left(90)
            forward(150)
            right(180)
            pd()       




 #repitions of office's floors
    for step in range(floor-1):#It is necessary for -1 because it include the base.
        draw_floor()

#draw the office's roof
    pu()
    forward(50)
    pd()
    color('red','white')
    begin_fill()
    left(90)
    forward(20)
    left(90)
    forward(40)
    right(90)
    forward(30)
    right(90)
    forward(130)
    right(90)
    forward(30)
    right(90)
    forward(40)
    left(90)
    forward(20)
    right(90)
    forward(10)
    right(90)
    forward(20)
    left(90)
    forward(30)
    left(90)
    forward(20)
    right(90)
    forward(10)
    end_fill()
    pu()
    right(90)
    forward(20)
    left(90)
    forward(40)
    left(180)
    forward(70)
    #write down the word 'office'
    write('office',align='center',font=('Arial',27,'bold'))
    


##draw the apartment
def apartment(floor):
    #draw the apartment's base
        setheading(0)
        pd()
        width(2)
        color('black','brown')
        begin_fill()
        forward(30)
        left(90)
        forward(30)
        left(90)
        forward(60)
        left(90)
        forward(30)
        left(90)
        forward(30)
        end_fill()
        #draw the apartment's door.
        color('black','skyblue')
        begin_fill()
        forward(7.5)
        left(90)
        forward(15)
        left(90)
        forward(15)
        left(90)
        forward(15)
        left(90)
        forward(7.5)
        end_fill()
        pu()
        right(180)
        forward(7.5)
        right(90)
        forward(15)
        right(90)
        forward(10)
        #write down the name
        write('apartment',align='center',font=('Arial',10,'bold'))
        left(180)
        pu()
        forward(15)
        left(90)
        forward(15)
        right(90)
        forward(18)
        right(90)
        forward(30)
        right(90)
        pd()
        #draw the apartment's floor
        def draw_floor():#define apartment's floor
                width(2)
                color('black','brown')
                begin_fill()
                for step in range(2):
                    forward(60)
                    left(90)
                    forward(30)
                    
                    left(90)
                end_fill()
                #draw the apartment's window
                pu()
                forward(10)
                left(90)
                forward(7.5)
                pd()
                right(90)
                width(2)
                color('ivory','tan')
                begin_fill()
                for step in range(4):
                    forward(15)
                    left(90)
                end_fill()
                #draw the window's grid
                pu()
                left(90)
                forward(7.5)

                right(90)
                pd()
                width(2)
                color('ivory')
                forward(15)

                pu()
                left(90)
                forward(7.5)
                left(90)
                forward(7.5)
                left(90)
                pd()
                width(2)
                color('ivory')
                forward(15)

                pu()
                left(90)
                forward(17.5)
                pd()
                width(2)
                color('ivory','tan')
                begin_fill()
                for step in range(4):
                    forward(15)
                    left(90)
                end_fill()
                pu()
                left(90)
                forward(7.5)
                right(90)
                pd()
                width(2)
                color('ivory')
                forward(15)
                pu()
                left(90)
                forward(7.5)
                left(90)
                forward(7.5)
                left(90)
                pd()
                width(2)
                color('ivory')
                forward(15)
                pu()
                left(180)
                forward(22.5)
                left(90)
                forward(42.5)
                right(180)
                pd()
        


  #repitions of apartment's floors       
        for step in range(floor-1):
                draw_floor()
#draw the apartment's roof
        left(60)
        color('navy')
        begin_fill()
        for step in range(3):
                forward(60)
                right(120)
        end_fill()



##draw the palace
def palace(floor):#define the palace
    #draw the palace's base
    setheading(0)
    pd()
    width(2)
    color('brown','lemonchiffon3')
    begin_fill()

    forward(125)
    left(90)
    forward(30)
    left(90)
    forward(250)
    left(90)
    forward(30)
    left(90)
    forward(125)
    end_fill()
    
    #draw the palace's stairs
    color('brown','honeydew2')
    begin_fill()
    forward(50)
    left(90)
    forward(9)
    left(90)
    forward(100)
    left(90)
    forward(9)
    left(90)
    forward(50)
    end_fill()
    pu()
    left(90)
    forward(9)
    right(90)
    pd()
    color('brown','honeydew2')


    begin_fill()
    forward(40)
    left(90)
    forward(9)
    left(90)
    forward(80)
    left(90)
    
    forward(9)
    left(90)
    forward(40)
    end_fill()

    pu()
    left(90)
    forward(9)
    right(90)
    pd()
    color('brown','honeydew2')
  
    
    begin_fill()
    forward(30)
    left(90)
    forward(9)
    left(90)
    forward(60)
    left(90)
    forward(9)
    left(90)
    forward(30)
    end_fill()
    
    pu()
    left(90)
    forward(12)
    left(90)
    forward(115)
    right(180)
    pd()
  #draw the palace's floor
    def draw_floor():#define the palace
        width(1)
        color('brown','lemonchiffon3')
        begin_fill()
        for step in range(2):
            forward(230)
            left(90)
            forward(30)
            left(90)
        end_fill()
        pu()
        left(90)
        forward(30)
        right(90)
        pd()

 
    for step in range(floor-1):
        draw_floor()
   #draw the palace's columns
    pu()
    forward(10)
    pd()
    color('brown','lightyellow2')
    begin_fill()
    for step in range(2):
        forward(45)
        right(90)
        forward((floor-1)*30)
        right(90)
    end_fill()
    pu()
    forward(55)
    pd()
    color('brown','lightyellow2')
    begin_fill()
    for step in range(2):
        forward(45)
        right(90)
        forward((floor-1)*30)
        right(90)
    end_fill()
    pu()
    forward(55)
    pd()
    color('brown','lightyellow2')
    begin_fill()
    for step in range(2):
        forward(45)
        right(90)
        forward((floor-1)*30)
        right(90)
    end_fill()
    pu()
    forward(55)
    pd()
    color('brown','lightyellow2')
    begin_fill()
    for step in range(2):
        forward(45)
        right(90)
        forward((floor-1)*30)
        right(90)
    end_fill()
    left(180)
    #draw the palace's roof
    pu()
    forward(185)
    pd()
    left(180)
    width(2)
    color('brown','lemonchiffon3')
    begin_fill()
    for step in range(2):
        forward(250)
        left(90)
        forward(30)
        left(90)
    end_fill()
    pu()
    forward(125)
    left(90)
    forward(20)
    left(-72)
    pd()
    #draw the star(ref.https://blackboard.qut.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_151395_1&content_id=_8333347_1)
    def star(height, colour):#define the star

        left_angle = 72 
        right_angle = 144  
        line_size = height * 0.409 

        
        setheading(-left_angle) 
        color(colour) 
        pendown()
        begin_fill()
        segment_numbers = range(5)
        for seg_no in segment_numbers: 
          forward(line_size)
          left(left_angle)
          forward(line_size)
          right(right_angle)
        end_fill()
        penup()
    star(15,'yellow')



##draw the city_council
def city_council(floor):
    #draw the city_council's base.
    setheading(0)
    color('light grey')
    begin_fill()
    forward(125)
    left(90)
    forward(40)
    left(90)
    forward(250)
    left(90)
    forward(40)
    left(90)
    forward(125)
    end_fill()
    
    #draw the city_council's door.
    color('black')
    begin_fill()
    forward(25)
    left(90)
    forward(30)
    left(90)
    forward(50)
    left(90)
    forward(30)
    left(90)
    forward(25)
    end_fill()
    
    left(90)

    pd()
    color('white')
    forward(30)
    pu()
    forward(10)
    left(90)
    forward(125)
    left(180)
    #draw the city_council's floor
    def draw_floor():#define the city_council's floor
        color('steel blue')
        begin_fill()
        for step in range(2):
            forward(250)
            left(90)
            forward(40)
            left(90)
        end_fill()
        #draw the city_council's window
        pu()
        forward(25)
        left(90)
        forward(5)
        right(90)
        pd()
        color('cornsilk')
        begin_fill()
        for step in range(2):
            forward(40)
            left(90)
            forward(10)
            left(90)
        end_fill()
        pu()
        forward(40)
        left(90)
        forward(10)
        
        pd()
        begin_fill()
        circle(20,180)
        end_fill()
        pu()
        left(90)
        forward(80)
        right(90)
        forward(10)
        left(90)
        pd()
        begin_fill()
        for step in range(2):
            forward(40)
            left(90)
            forward(10)
            left(90)
        end_fill()
        pu()
        forward(40)
        left(90)
        forward(10)
        pd()
        begin_fill()
        circle(20,180)
        end_fill()
        pu()
        left(90)
        forward(80)
        right(90)
        forward(10)
        left(90)
        pd()
        begin_fill()
        for step in range(2):
            forward(40)
            left(90)
            forward(10)
            left(90)
        end_fill()
        pu()
        forward(40)
        left(90)
        forward(10)
        pd()
        begin_fill()
        circle(20,180)
        end_fill()
        pu()
        left(180)
        forward(25)
        left(90)
        forward(185)
        left(180)
        pd()
 #repititions city_council's floors
    for step in range(floor-1):
            draw_floor()



##drawing the roof of city_council
    color('black','slate grey')
    begin_fill()
    for step in range(2):
        forward(25)
        left(90)
        forward(100)
        left(90)
    end_fill()
    
    forward(225)
    left(90)
    color('black','slate grey')
    
    begin_fill()
    circle(100,180)
    end_fill()

    left(90)
    pu()
    forward(200)
    pd()
    color('black','slate grey')
    begin_fill()
    for step in range(2):
        forward(25)
        left(90)
        forward(100)
        left(90)
    end_fill()
 #draw the city_council's clock
    left(180)
    pu()
    forward(100)
    right(90)
    forward(25)
    right(90)
    pd()
    color('white')
    begin_fill()
    circle(25)
    end_fill()
    pu()
    left(90)
    forward(25)
    left(30)
    pd()
    color('black')
    width(2)
    forward(13)
    pu()
    left(180)
    forward(13)
    right(30)
    pd()
    color('black')
    width(2)
    forward(18)
    










# Erect buildings as per the provided city plan
def build_city(plan):
    for command in plan:
        pu()
        goto(sites[command[0]-1][1])#If we don't -1 in that case , sites[1] is built in site2,not sites1
        if command[1]=='A' :
            office(command[2])
        elif command[1]=='B':
            apartment(command[2])
        elif command[1]=='C':
            palace(command[2])
        else:### command[1]=='D':
              city_council(command[2])
             
             
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Sumin City")

### Call the student's function to build the city
### ***** While developing your program you can call the build_city
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_plan()" as the
### ***** argument to the build_city function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_plan function.
###build_city(fixed_plan_1) # <-- used for code development only, not marking
build_city(random_plan()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
