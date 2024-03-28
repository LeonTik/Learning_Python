#畫龜
import another_module 
print(another_module.another_variable)

#_____________________________________________________________________________________________________________________________________________________________________________________________________________________
import turtle 
timmy = turtle.Turtle() 
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________

from turtle import Turtle, Screen #Screen係turtle模組的classes

# object = Blueprint(class) 
timmy = Turtle()        # timmy 是一個object  龜係一個class 裡面有其attribute & function 
print(timmy) 
#而家我地可以用 龜class 裡的attribute & function 
timmy.shape("turtle") # attribute 視覺上變左隻龜
timmy.color("green") #attribute 視覺 上色  #https://docs.python.org/3/library/turtle.html?highlight=turtle#turtle.color
timmy.forward(100) #function 上佢做到d咩
      #forward method is the function , but shape and color are the attribute 
      

def a_set_movement():
    timmy.forward(100)
    timmy.right(100)
    timmy.forward(100)
    timmy.right(100)
    timmy.forward(100)

a_set_movement()

timmy.forward(1000)


my_screen = Screen() #開一個視窗 
print(my_screen.canvheight) 
    #    object .attribute    

my_screen.exitonclick() #exit on click 
#        .hold著個window 

#_______________________________________________________________________________________________________________________________

#py pi == Python package index
from prettytable import PrettyTable

# create a new table object
table = PrettyTable()

# add columns to the table
table.field_names = ["Name", "Age", "City"]

# add rows to the table
table.add_row(["Alice", 25, "New York"])
table.add_row(["Bob", 30, "San Francisco"])
table.add_row(["Charlie", 35, "London"])

# display the table
print(table)

#_______________________________________________________________________________________________________________________________
from prettytable import PrettyTable

         #package/ class
table = PrettyTable()  #table 是一個object  PrettyTable係一個class 裡面有其attribute & function 
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])         #標題 + 打直一列list
table.add_column("Type", ["Electric", "Water", "Fire"])                         #標題 + 打直一列list

table.align = "l" #將裡面d字偏向左 
#object.attribute = 左
 
print(table)
 