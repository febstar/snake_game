from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))


    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=('Spooky', 20, 'normal'))

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))
