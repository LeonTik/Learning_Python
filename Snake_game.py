from turtle import Screen 
from snake import Snake 
from food import Food 
from scoreboard import Scoreboard 
import time 

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


