from turtle import *
import random
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color = ["black", "yellow", "blue", "green", "orange"]
random.shuffle(color)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
        
    else:
        snake.pop(0)
    
    clear()
    
    for body in snake:
        square(body.x, body.y, 9, color[0])

    square(food.x, food.y, 9, color[1])
    update()
    ontimer(move, 100)
    
def comi():
    if food.x < 189 and food.x > -199:
            food.x += random.randrange(-1,1) * 10
    if food.y < 189 and food.y > -199:
            food.y += random.randrange(-1,1) * 10
    square(food.x, food.y, 9, color[1])
    update()
    ontimer(comi, 10000)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
comi()
done()