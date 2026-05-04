# https://github.com/TylerYep/stanfordkarel
from stanfordkarel import *

## Approach 1:
## - Mark every other (odd) field with a beeper.
## - Then go back and push all the beepers to the left most field.
## - Then turn back again and start pushing beepers to next fields while dropping one beeper in each position - Do this until you have only one beeper left.
def main():
    """
    The goal is produce a chess-style board.
    See https://csbridge.github.io/csbridge2019ctu/en/projects/checkerBoard.html
    """
    # NOTE: this doesn't work for 1-column worlds
    # because of the front_is_clear() condition below will terminate too early
    while front_is_clear():
        mark_odd()
        return_to_left()
        turn_right()
        if front_is_clear():
            move()
            turn_right()
            mark_even()
            return_to_left()
            turn_right()
            if front_is_clear():
                move()
                turn_right()

def return_to_left():
    while not_facing_west():
        turn_left()
    while front_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()



def mark_odd():
    """
    Puts a beeper on every odd field in the current row,
    until it reaches the end of the row.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def mark_even():
    """
    Puts a beeper on every even field in the current row,
    until it reaches the end of the row.
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()

if __name__ == "__main__":
    run_karel_program()
