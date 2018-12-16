import random
import tkinter as tk
from ball import Ball
from score import Score


balls_array = []
checked_ball_pairs = []


def create_window():
    global window, canvas
    window = tk.Tk()
    window.geometry("{}x{}".format(window_width, window_height))
    canvas = tk.Canvas(window, width=window_width, height=window_height, bg='white')
    canvas.pack()
    canvas.create_rectangle(2, 2, window_width, window_height)
    return


def clear_checked_pairs():
    global checked_ball_pairs
    checked_ball_pairs = []


def ball_pair_checked(ball1, ball2):
    for ball_pair in checked_ball_pairs:
        if ball_pair[0] == ball1 and ball_pair[1] == ball2 or \
           ball_pair[0] == ball2 and ball_pair[1] == ball1:
            return True
        else:
            checked_ball_pairs.append((ball1, ball2))
            return False


def move_balls():
    global balls_array

    for ball in balls_array:
        ball.move()

        for wall in [(2, None), (window_width, None), (None, 2), (None, window_height)]:
            if ball.collide_with_wall(wall):
                ball.bounce_off_wall(wall)
                ball.check_glue_to_wall(wall)

        clear_checked_pairs()

        for ball2 in balls_array:
            if ball2 != ball and not ball_pair_checked(ball, ball2):
                if ball.collide_with_ball(ball2):
                    ball.bounce_off_ball(ball2)

    window.after(move_balls_speed, move_balls)
    return


def create_ball():
    return Ball(canvas,
                random.randint(50, window_width - 50),
                random.randint(50, window_height - 50),
                30,
                random.randint(-10, 10),
                random.randint(-10, 10),
                random.choice(ball_colors))


def mouse_click(event):
    global balls_array, move_balls_speed

    for ball in balls_array:
        if ball.check_hit(event.x, event.y):
            ball.destroy()
            score_indicator.inc_hits()
            balls_array.remove(ball)
            balls_array.append(create_ball())
            if move_balls_speed > 10:
                move_balls_speed -= 1
    return


#############################################################################

move_balls_speed = 50

window_width = 1200
window_height = 500

ball_colors = ['red', 'green', 'blue', 'yellow', 'black', 'violet', 'brown', 'orange']

window = None
canvas = None

create_window()
# create_score_indicator()

score_indicator = Score(canvas, 1000, 50)

balls_array.append(create_ball())

window.after(move_balls_speed, move_balls)
canvas.bind('<Button-1>', mouse_click)
window.mainloop()
