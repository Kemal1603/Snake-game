import turtle


class Scoreboard(turtle.Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		# Так тоже оказывается можно делать:)
		with open('high_score.txt') as file:
			self.high_score = int(file.read())
		self.color('white')
		self.penup()
		self.goto(0, 270)
		self.write(f"Я съел: ", move=False, align="center", font=("Arial", 20, "bold"))
		self.hideturtle()

	def score_up(self):
		self.score += 1
		self.clear()
		self.write(f"Я съел: {self.score} Максимальный результат: {self.high_score}", move=False, align="center",
		           font=("Arial", 20, "bold"))

	def reset_score(self):
		if self.score > self.high_score:
			self.high_score = self.score
		self.score = 0
		self.score_up()
		with open('high_score.txt', 'w') as file:
			file.write(str(self.high_score))

# def game_over(self):
# 	self.clear()
# 	self.goto(0, 0)
# 	if self.score == 1:
# 		self.write(f"Игра окончена вы набрали: {self.score} балл", move=False, align="center", font=("Arial", 20, "bold"))
# 	elif 1 < self.score < 5:
# 		self.write(f"Игра окончена вы набрали: {self.score} балла", move=False, align="center", font=("Arial", 20, "bold"))
# 	else:
# 		self.write(f"Игра окончена вы набрали: {self.score} баллов", move=False, align="center", font=("Arial", 20, "bold"))
