# you are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
# Given a random height and width of wall
#number of cans = (wall height x wall width) / coverage per can
#eg. Height=2, width = 4, coverage = 5 
#number of can = (2 x 4)/ 5
#              =6  用round up 

#我既方法
height = float(input("please input height: "))
width = float(input("please input width: "))
coverage = float(input("Please input coverage: "))

Answer = (height * width)/coverage 

def sth(H, W, C):
    print(f"The height of wall is {H}")
    print(f"The width of wall is {W}")
    print(f"The coverage is {C}")
sth(height, width, coverage)

print(Answer)
print(f"The answer is {round(Answer)}")

#------------------------------------------------------------------------------------------------------------
#solution
import math 

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover) #math.ceil() 好似round() 但要import math先用到 同埋不是四捨五入 係大躍進
    return num_of_cans

height = float(input("please input height: "))
width = float(input("please input width: "))
cover= float(input("Please input coverage: "))

num_of_cans = paint_calc(height, width, cover)
print(f"You'll need {num_of_cans} cans of paint")
