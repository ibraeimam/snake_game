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
# window = curses.newwin(screen_height, screen_width , 0 , 0)   
        # or 
window = screen #  <= this 

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


# for snake's color
curses.start_color()
curses.init_pair(1 , curses.COLOR_BLUE , curses.COLOR_BLACK)
curses.init_pair(2 , curses.COLOR_RED , curses.COLOR_BLACK)


# creating the loop that loops the game forever until the player quit or lose .
while (True) :
    # what is the next move after starting .
    next_move = window.getch()

    # if the user didn't pass any key the initial movement still exist .
    first_move = next_move if next_move != -1 else first_move

    # setting the next move by the input .
    HEAD = [snake[0][0] , snake[0][1]] # inisialize the head if snake
    if first_move == curses.KEY_RIGHT :
        HEAD[1] += 1
    elif first_move == curses.KEY_LEFT :
        HEAD[1] -= 1
    elif first_move == curses.KEY_UP :
        HEAD[0] -= 1
    elif first_move == curses.KEY_DOWN :
        HEAD[0] += 1

    # check if the Snake collided with wall or itself .
    if HEAD in snake[ 1 : ] or HEAD[1] <= 0 or HEAD[1] >= screen_width or HEAD[0] <= 0 or HEAD[0] >= screen_height :
        curses.endwin()
        quit()

# add a new head for the snake . 
    snake.insert(0 , HEAD)

    # check if the snake ate the food or not . 
    if HEAD == food:
        score += 10  

        # creating food forever randomly .   
        while True :
            new_food = [
                random.randint(2 , screen_height - 2), 
                random.randint(2 , screen_width - 2)
            ]

            # if the food appares on snake's body remove it and generate a new one .
            if new_food not in snake :  
               food = new_food       
               break 

    # if the snake didn't eat the food remove the tail .
    else : 
        snake.pop()

# refreshing content [ for drowing the new frame ]
    window.clear()
    window.addstr( 1 , 2 , f"score: {score}" )

    window.addch(food[0] , food[1] , '' ,curses.color_pair(2))
    

    for Y , X in snake :
        window.addch( Y , X , '●' , curses.color_pair(1) )

    window.refresh()