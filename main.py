import turtle
import time
from snake import Snake
import food
import scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Kemal's Snake Project")
screen.tracer(0)

snake = Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Соприкосновение змейки и "еды"
    if snake.segments[0].distance(food) < 15:
        food.change_position()
        snake.speed_up()
        snake.add_part()
        scoreboard.score_up()
    # Соприкосновение змейки и стенки
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        scoreboard.reset_score()
        snake.reset()
    # Соприкосновение змейки и хвоста
    if snake.segments[0].distance(snake.segments[-1]) < len(snake.segments):
        scoreboard.reset_score()
        snake.reset()

screen.exitonclick()
