import turtle
import random

sc = turtle.Screen()
sc.setup(height=400, width=800)
sc.bgcolor("Black")
p = turtle.Turtle()
p.color("White")
p.hideturtle()
pn = turtle.Turtle()
pn.color("White")
pn.hideturtle()
pn.penup()
pn.goto(80, 100)
pn.write("Tonoy", align= "Right", font=("JetBrains Mono", 16, "bold"))


for i in range(2):
    p.forward(90)
    p.left(90)
    p.forward(30)
    p.left(90)
    
p.penup()
p.goto(7, 6)
p.write("Start Game", font=("JetBrains Mono", 10, 'normal'))

def button(x, y):
    if x > 0 and x < 91 and y > 0 and y < 30:
        p.clear()
        pn.clear()
        s = turtle.Screen()
        s.setup(height=400, width=800)
        s.bgcolor("black")
        s.tracer(0)
        s.title("Mario Remake")

        # Movement
        dx = 0.2
        dy = -0.2
        gravity = -0.1

        # Score
        score = 0
        high_score = 0

        # Score turtle
        pen = turtle.Turtle()
        pen.speed(0)
        pen.penup()
        pen.color("White")
        pen.hideturtle()
        pen.goto(0, 150)
        pen.write(f"Score: {score}", align="Center", font=("JetBrains Mono", 18, "normal"))


        # Build the base
        base = turtle.Turtle()
        base.shape("square")
        base.goto(0, -120)
        base.color("white")
        base.shapesize(stretch_len=50, stretch_wid=1)

        # Build the catcher
        catcher = turtle.Turtle()
        catcher.penup()
        catcher.shape("square")
        catcher.color("Red") 
        catcher.goto(0, -99)
        catcher.speed(0)
        catcher.h = 20
        catcher.w = 20

        # Meteor from sky
        ball = turtle.Turtle()
        ball.shape("circle")
        ball.color("yellow")
        ball.speed(0)
        ball.penup()
        ball.goto((random.randint(-10,10)*20), 70)

        # Movement function
        def left():
            x = catcher.xcor()
            catcher.setx(x - 10)
            # print(catcher.xcor())
            if catcher.xcor() < -390:
                catcher.setx(-390)
        def right():
            x = catcher.xcor()
            catcher.setx(x + 10)
            # print(catcher.xcor())
            if catcher.xcor() > 390:
                catcher.setx(390)
            

        # Moving the catcher
        s.listen()
        s.onkeypress(left, "a")
        s.onkeypress(right, "d")

        # Main game loop
        while True:

            s.update()

            y = ball.ycor()
            y += gravity
            ball.sety(y)
            if y < -99:
                # break
                ball.sety(99)
                
            bpx = ball.xcor()
            bpy = ball.ycor()
            mx = catcher.xcor()
            my = catcher.ycor()
            
            # print(bpx, bpy, mx , my)
            # print (bpx, mx)
            if bpy == -my and bpx == mx:
                score += 1
                ball.goto((random.randint(-10,10)*20), 70)
                if score > high_score:
                    high_score = score
            elif bpy == -my and bpx != mx:
                score = 0
                ball.goto((random.randint(-10,10)*20), 70)
                if score > high_score:
                    high_score = score
            

            pen.clear()
            pen.write(f"Score: {score}         ", align="right", font=("JetBrains Mono", 18, "normal"))
            pen.write(f"High Score: {high_score}", align="left", font=("JetBrains Mono", 18, "normal"))
            
turtle.onscreenclick(button, 1)
turtle.listen()

turtle.done()
