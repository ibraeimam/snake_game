# first , importing some modules <curses and random >
import random 
import curses 

# setting the score out 
score = 0

# returning the terminal as a screen we can handel it 
screen = curses.initscr() # initialize screen <terminal> .

# hide the curser from the screen .
curses.curs_set(0) 

# assign the max value of height and width 
screen_height , screen_width = screen.getmaxyx() 

# setting the height and width to can handle with .
window = curses.getwin(screen_height , screen_width , 0 , 0)

# allowing window to recive inputs and from keybourd by jey [ pad ( ) ]
window.keypad(True)

# setting the delay for updating the screen .
window.timeout(100) # بالمللي ثانيه 

# set Y , X coordinates of the initial possion of snake's head .
snake_y = screen_height // 3
snake_x = screen_width // 3 

# define the snake's body (initial possition) 
snake = [
    [snake_y , snake_x] ,
    [snake_y , snake_x - 1] ,
    [snake_y , snake_x - 2]
]

# creat the food randomly .
food = [
    random.randint(2 , screen_height - 2), 
    random.randint(2 , screen_width - 2)
]   
window.addch(food[0] , food[1] , '')

# set the iniotial movement .
first_move = curses.KEY_RIGHT

# creating the loop that loops the game forever until the player quit or lose .
while (True) :
    
