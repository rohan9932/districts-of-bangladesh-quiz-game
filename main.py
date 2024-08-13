from turtle import Turtle, Screen
import pandas as pd

# Screen Setup
screen = Screen()
screen.title("Districts of Bangladesh")
image = "64Districts.gif"
screen.bgpic(image)
screen.setup(605,832)

# Data Processing
districts_data = pd.read_csv("64Divisions.csv")
all_districts = districts_data.district.tolist()
guessed_districts = []

while len(guessed_districts) < 64:
    # take the input
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/64 Districts Correct",
                                       prompt="What's another district's name?").title()

    # Exit functionality
    if answer_district == "Exit":
        missing_districts = [district for district in all_districts if district not in guessed_districts]
        data = pd.DataFrame(missing_districts)
        data.to_csv("districts_to_learn.csv")
        break

    # move the district name to the location on the map    
    if answer_district in all_districts:
        guessed_districts.append(answer_district)
        # move the name of the state to the location
        t = Turtle()
        t.hideturtle()
        t.penup()
        district_data = districts_data[districts_data.district == answer_district]
        t.goto(district_data.x.item(), district_data.y.item())
        t.write(answer_district)

