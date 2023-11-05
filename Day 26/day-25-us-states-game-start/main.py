import turtle
import pandas

screen = turtle.Screen()
screen.title("Name the States")
image = "Day 25/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct = []
raw_states = pandas.read_csv("Day 25/day-25-us-states-game-start/50_states.csv")
while len(correct) < 50:
    answer_state = screen.textinput(title=f'{len(correct)}/50 States Correct', prompt='Whats another states name?').title()

    if answer_state == "Exit":
        #change this to execute list comprehension
        # missed_states=[]
        # for state in raw_states.state.to_list():
        #     if state not in correct:
        #         missed_states.append(state)
        missed_states = [state for state in raw_states.state.to_list() if state not in correct]
        missed_df = pandas.DataFrame(missed_states)
        missed_df.to_csv("Day 26/Missed_States.csv")
        break

    if answer_state in raw_states.state.to_list() and answer_state not in correct:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        curr_state = raw_states[raw_states.state == answer_state]
        t.goto(int(curr_state.x), int(curr_state.y))
        t.write(answer_state)
        correct.append(answer_state)

