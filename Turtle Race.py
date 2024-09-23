import turtle
import time
import random

WIDTH = 500
HEIGHT = 500

COLOURS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

def getNumberOfTurtles():
    racers = 0

    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit() and 2 <= int(racers) <= 10:
            return int(racers)
        print("Invalid input!")   

def initTurtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")

def race(colours):
    turtles = createTurtles(colours)

    while True:
        for racer in turtles:
            racer.forward(random.randrange(1, 20))

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colours[turtles.index(racer)]

def createTurtles(colours):
    turtles = []
    spacing = WIDTH // (len(colours) + 1)
    for i, colour in enumerate(colours):
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacing, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

numRacers = getNumberOfTurtles()
initTurtle()

random.shuffle(COLOURS)
colours = COLOURS[:numRacers]

print("The colours of the turtles:", colours)
choice = input("Enter the colour of the turtle you think will win: ")

winner = race(colours)

if choice == winner:
    print("Your turtle of colour", winner, "won!")
else:
    print("The winer is the turtle with colour:", winner)

time.sleep(5)