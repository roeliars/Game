"""Snake, classic arcade game.
Exercises
1. How do you make the snake faster or slower?  
2. How can you make the snake go around the edges? 
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
import random
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#RMEV - 23/03/2022 - We add a list of colors and random choices
color=['black', 'blue', 'orange', 'purple']
c1=random.choice(color)
c2=random.choice(color)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #RMEV - 23/03/2022 - We define, that in each run, the color of the snake and the food change
    for body in snake:
        square(body.x, body.y, 9, c1)

    square(food.x, food.y, 9, c2)
    update()
    ontimer(move, 100)

#RAVR - 23/03/2022 - The food is moving one tile in a preselected time where it is created
def movefood():

    if inside(food):
        food.x += (randrange(-1, 2) * 10)
        food.y += (randrange(-1, 2) * 10)
        
    ontimer(movefood, 500)

    

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
movefood()
done()