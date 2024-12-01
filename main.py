from turtle import Turtle,Screen
import pandas as pd
screen=Screen()
correct_guess=[]
t=Turtle()
t.color("red")
t.penup()
t.hideturtle()

screen.setup(850,850)
img="new_erangel.gif"
screen.bgpic(img)
def run():
    location=pd.read_csv("list_of_place.csv")
    current_loc=location.place
    all_places=current_loc.to_list()
    user_input=screen.textinput(title=f"{len(correct_guess)}/18 Guessed the locations",prompt="Enter the place").title()
    if not user_input:
        return user_input

    if user_input=="Exit":
        missed_location=[place for place in all_places if place not in correct_guess ]
        print(f"you missed{missed_location}")
        return "Exit"

    if user_input in all_places and user_input not in correct_guess:
        crt_loc=location[location.place==user_input]
        x=crt_loc.x.item()
        y=crt_loc.y.item()
        t.goto(x,y)
        t.write(f"{user_input}", align="center", font=("Arial", 20, "bold"))
        correct_guess.append(user_input)
    else:
        return user_input

while len(correct_guess)<18:
    return_val=run()
    if return_val=="Exit":
        turtle=Turtle()
        turtle.color("red")
        turtle.write(
            f"GAME OVER\n You found {len(correct_guess)}/18",align="center",font=("Arial",30,"bold")
                     )
        break

screen.mainloop()
