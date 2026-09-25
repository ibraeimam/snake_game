# first , importing some modules <curses and random >
import random 
import curses 

# setting the score out 
score = 0

# returning the terminal as a screen we can handel it 
screen = curses.initscr() # initialize screen <terminal> .

# hide the curser from the screen .
curses.curs_set(0) 

# assign the max value of 