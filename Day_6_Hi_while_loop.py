#while loop --  while sth is true                      #For loop 
#Do sth repeatedly                                     #for item in list_items:
                                                       #    Do sth to each item 
                                                       #for number in range (a, b):
                                                       #    print(number)

#https://reeborg.ca/index_en.html 呢到可以學到function and loop 實質操作

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
  
for step in range(5):
    jump()
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
number_of_hurdles = 5 #有5個欄架 
while number_of_hurdles > 0: #除非跨剩0個欄架(直至到個statement 變成false)，才能停 (目標)
    jump() #執行呢個fuction裡既指令跳過一個 (執行)
    number_of_hurdles -=1 #每跳過一個就減一個 (每一次執行完指令就會點)  number_of_hurdles = number_of_hurdles + 1
    #the result will be brought back to the "While", see whether it could satisfy the condition or not(T/F)
    print(number_of_hurdles) 


while at_goal() != True: #當係呢個"達到終點既事實"不是真，就行下面個command
    jump()  
#or 上下一鳩樣
while not at_goal():
    jump()

#---------------------------------------------------------------------------------------------------------------------------
#呢次係hurdle3 D hurdle 會隨機 所以要寫特定既condition 令到隻機械人遇上不同情況可以隨機應變

# front_is_clear() or wall_in_front() or at_goal()  前面條路係清 or 前面有牆 or 到終點個陣
while not at_goal(): #當未到終點個陣 
    if wall_in_front(): #當見到牆個陣
        jump()
    elif front_is_clear:#當見前面條路係清個陣 等於 else:
        move()                            #       move()

#---------------------------------------------------------------------------------------------------------------------------
