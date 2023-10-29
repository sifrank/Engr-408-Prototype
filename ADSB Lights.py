import turtle

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
redLight.color("red")
redLight.penup()
redLight.goto(0, 40)

# Yellow light
yellowLight = turtle.Turtle()
yellowLight.shape("circle")
yellowLight.color("yellow")
yellowLight.penup()
yellowLight.goto(0, 0)

# Green light
greenLight = turtle.Turtle()
greenLight.shape("circle")
greenLight.color("green")
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

def generate_alert(altitude, distance):
    if altitude < 2000 and distance <= 4:
        return "Track_Aircraft"
    return "No_Alert"

def main():
    try:
        num_aircraft = int(input("Enter the number of aircraft: "))
        most_severe_alert = "No_Alert"  # Initialize to the least severe

        for _ in range(num_aircraft):
            altitude = int(input("Enter aircraft altitude (feet AGL): "))
            distance = float(input("Enter aircraft distance from the airport (miles): "))

            alert = generate_alert(altitude, distance)

            if alert == "Track_Aircraft":
                print(f"Generate {alert} token for the lighting control hardware.")
                if altitude < 500 and distance <= 1:
                    most_severe_alert = "Runway_In_Use"
                elif altitude < 1000 and distance <= 2:
                    most_severe_alert = "Runway_Use_Imminent"

        if most_severe_alert == "Runway_In_Use":
            print("Red Light - Runway in use")
            activateRed()
        elif most_severe_alert == "Runway_Use_Imminent":
            print("Yellow Light - Runway use imminent")
            activateYellow()
        else:
            print("Green Light - The runway is clear")
            activateGreen()

        wn.update()  # Update the screen to reflect light changes
    except ValueError:
        print("Invalid input. Please enter valid numbers for altitude and distance.")

if __name__ == "__main__":
    main()

turtle.done()
