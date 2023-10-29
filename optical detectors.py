import turtle
import time

wn = turtle.Screen()
wn.title("Prototype for ENGR 408")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# Red light
redLight = turtle.Turtle()
redLight.shape("circle")
redLight.color("grey")
redLight.penup()
redLight.goto(0, 40)

# Yellow light
yellowLight = turtle.Turtle()
yellowLight.shape("circle")
yellowLight.color("grey")
yellowLight.penup()
yellowLight.goto(0, 0)

# Green light
greenLight = turtle.Turtle()
greenLight.shape("circle")
greenLight.color("grey")
greenLight.penup()
greenLight.goto(0, -40)

def activateRed():
    redLight.color("red")
    yellowLight.color("grey")
    greenLight.color("grey")

def activateYellow():
    redLight.color("grey")
    yellowLight.color("yellow")
    greenLight.color("grey")

def activateGreen():
    redLight.color("grey")
    yellowLight.color("grey")
    greenLight.color("green")

class RunwayController:
    def __init__(self):
        self.runway_occupied = False

    def vehicle_enter_runway(self):
        if not self.runway_occupied:
            self.runway_occupied = True
            activateRed()  # Turn the lights red
            print("Runway_In_use token issued.")
        else:
            print("Runway is already in use. Wait for it to clear.")

    def vehicle_leave_runway(self):
        if self.runway_occupied:
            self.runway_occupied = False
            activateGreen()  # Turn the lights green
            print("Runway_clear token issued.")
        else:
            print("No vehicle on the runway. Cannot clear.")

# Create a RunwayController instance
controller = RunwayController()

while True:
    user_input = input("Enter 'enter' to signal a vehicle entering the runway, 'leave' to signal a vehicle leaving, or 'quit' to exit: ")

    if user_input == 'enter':
        controller.vehicle_enter_runway()
        activateRed()
    elif user_input == 'leave':
        controller.vehicle_leave_runway()
        activateGreen()
    elif user_input == 'quit':
        break
    else:
        print("Invalid input. Please enter 'enter', 'leave', or 'quit.")

    time.sleep(1)  # Delay for 1 second to see the light change

turtle.done()
