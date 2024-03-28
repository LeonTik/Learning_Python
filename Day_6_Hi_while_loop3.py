# maze 困難
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def back():
    turn_left()
    turn_left()

#front_is_clear() or wall_in_front() or at_goal()
#wall_on_right() or right_is_clear

while not at_goal():
    if right_is_clear(): #sense到右邊係空 就轉右 再直行
        turn_right()
        move()
    elif front_is_clear(): #sense到前方是空 就直行
        move()
    else: #如果右邊不是空 前方不是空 就轉左
        turn_left()

#有一個超大既bug 由於 if right_is_clear(): 會令到個戇鳩機械人不停向右 造成不停轉圈之現象發生 