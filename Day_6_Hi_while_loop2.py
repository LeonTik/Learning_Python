# Hurdle4 D hurdle 會隨便升高升低  

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()        
    while wall_on_right(): #當右手邊是牆就繼續前行
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
#front_is_clear() or wall_in_front() or at_goal()
while not at_goal():
    if wall_in_front(): #見到牆就跳
        jump()
    else:
        move()          