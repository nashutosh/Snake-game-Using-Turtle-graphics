import turtle as ttl  
import time  
import random as rdm  
import pyttsx3  
engine = pyttsx3.init()

delay = 0.1  
score = 0  
high_score = 0  
w_n = ttl.Screen()  
w_n.title("Snake Game by Ashutosh Singh")  
w_n.bgcolor("black")  
w_n.setup(width=650, height=650)  
w_n.tracer(0)  
head1 = ttl.Turtle()  
head1.shape("circle")  
head1.color("white")  
head1.penup()  
head1.goto(0, 0)  
head1.direction = "Stop"  
food1 = ttl.Turtle()  
colors = rdm.choice(['pink', 'yellow', 'blue'])  
shapes = rdm.choice(['triangle', 'square', 'circle'])  
food1.speed(0)  
food1.shape(shapes)  
food1.color(colors)  
food1.penup()  
food1.goto(0, 100)  

pen1 = ttl.Turtle()  
pen1.speed(0)  
pen1.shape("square")  
pen1.color("white")  
pen1.penup()  
pen1.hideturtle()  
pen1.goto(0, 250)  
pen1.write("Score: 0, High Score: 0", align="center",  
          font=("Consoles", 22, "bold"))  

# Assign the key directions  
def group1():  
    if head1.direction != "down":  
        head1.direction = "up"  

def go_down():  
    if head1.direction != "up":  
        head1.direction = "down"  

def go_left():  
    if head1.direction != "right":  
        head1.direction = "left"  

def go_right():  
    if head1.direction != "left":  
        head1.direction = "right"  

def move():  
    if head1.direction == "up":  
        head1.sety(head1.ycor() + 20)  
    if head1.direction == "down":  
        head1.sety(head1.ycor() - 20)  
    if head1.direction == "left":  
        head1.setx(head1.xcor() - 20)  
    if head1.direction == "right":  
        head1.setx(head1.xcor() + 20)  

w_n.listen()  
w_n.onkeypress(group1, "w")  
w_n.onkeypress(go_down, "s")  
w_n.onkeypress(go_left, "a")  
w_n.onkeypress(go_right, "d")  

segments1 = []  
def explain_rules_of_game():
    engine.say("Hello sir, before playing the game, let's understand the rules of the game. "
               "Rule 1: To move forward, press 'W'. To move backward, press 'S'. "
               "To move left, press 'A', and to move right, press 'D'. "
               "If you hit the canvas, you will be out. Let's start! Thanks.")
    engine.runAndWait()
def announce_scores():
    engine.say(f"Game Over! Your score is {score}. Your high score is {high_score}.")
    engine.runAndWait()
explain_rules_of_game()
while True:  
    ttl.update()
    if head1.xcor() > 290 or head1.xcor() < -290 or head1.ycor() > 290 or head1.ycor() < -290:  
        time.sleep(1)  
        head1.goto(0, 0)  
        head1.direction = "Stop"  
        colors = rdm.choice(['pink', 'blue', 'yellow'])  
        shapes = rdm.choice(['square', 'triangle'])  
        for segment1 in segments1:  
            segment1.goto(1050, 1050)  
        segments1.clear()  
        score = 0  
        delay = 0.1  
        pen1.clear()  
        pen1.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("candara", 24, "bold"))
    
        announce_scores()  
        
    if head1.distance(food1) < 20:  
        x1 = rdm.randint(-275, 275)  
        y1 = rdm.randint(-275, 275)  
        food1.goto(x1, y1)  
        new_segment1 = ttl.Turtle()  
        new_segment1.speed(0)  
        new_segment1.shape("square")  
        new_segment1.color("orange")  
        new_segment1.penup()  
        segments1.append(new_segment1)  
        delay -= 0.001  
        score += 10  
        if score > high_score:  
            high_score = score  
        pen1.clear()  
        pen1.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Consoles", 22, "bold"))   
    for index in range(len(segments1)-1, 0, -1):  
        x1 = segments1[index - 1].xcor()  
        y1 = segments1[index - 1].ycor()  
        segments1[index].goto(x1, y1)  
    if len(segments1) > 0:  
        x1 = head1.xcor()  
        y1 = head1.ycor()  
        segments1[0].goto(x1, y1)  
    move()  
    for segment1 in segments1:  
        if segment1.distance(head1) < 20:  
            time.sleep(1)  
            head1.goto(0, 0)  
            head1.direction = "Stop"  
            colors = rdm.choice(['pink', 'blue', 'yellow'])  
            shapes = rdm.choice(['square', 'triangle'])  
            for segment1 in segments1:  
                segment1.goto(1050, 1050)  
            segment1.clear()  
   
            score = 0  
            delay = 0.1  
            pen1.clear()  
            pen1.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Consoles", 22, "bold"))

            announce_scores()  
            
    time.sleep(delay)  

w_n.mainloop()  
