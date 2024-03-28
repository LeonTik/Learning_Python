#len() 你打既string有幾多個字母 包括空格
x_man = len("fuck you")
print(x_man)

#https://reeborg.ca/index_en.html 呢到可以學到function and loop 實質操作
def this_function():
  print("hello")
  print("bye")

this_function()

------------------------------------------------------------------------------------------------------
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(): #用function完成一組動作 到用個陣召喚呢個function 
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

jump()
jump()
jump()
jump()
jump()
jump()

#==========================================
#如果用 jump() 6次 有點笨柒 所以我地可以用 for loop 
for step in range (6): # 等於  range(0,6)
   jump()

