# https://github.com/TylerYep/stanfordkarel
from stanfordkarel import *

## Approach 1:
## - Mark every other (odd) field with a beeper.
## - Then go back and push all the beepers to the left most field.
## - Then turn back again and start pushing beepers to next fields while dropping one beeper in each position - Do this until you have only one beeper left.
def main():
    """
    The goal is to find the midpoint of a row.
    See https://csbridge.github.io/turkey-21-website/en/projects/midpointKarel.html
    Remember that you may only use Karel syntax and cannot use Python variables.
    This problem is difficult because Karel cannot count.
    """
    if front_is_blocked():
        # handle the case of a single-column row
        put_beeper()
    else:
        mark_odd()
        turn_back()
        push_left()
        turn_back()
        push_right_decrementing()
        # restore the final beeper
        turn_back()
        move()
        put_beeper()

def mark_odd():
    """
    Puts a beeper on every other (odd) field in the current row,
    until it reaches the end of the row.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()

def push_left():
    """
    Assumes Karel is facing west (to the left) already.
    """
    while front_is_clear():
        # move all the beepers at the current field to the next one
        while beepers_present():
            move_one_beeper_ahead()
        # advance to the next field
        move()

def push_right_decrementing():
    """
    Assumes Karel is on the left-most field, facing east (to the right) already.
    Also assumes that the number of beepers is strictly smaller than the number of fields
    (actually it should correspond to roughly half of the field count, as determined by the mark_odd procedure).

    Moves all the beepers except the last one at the current position to the next field,
    removing the final beeper altogether.
    When this function completes, no beepers are left on the board
    and Karel is supposed to be one column to the right of the "midpoint".
    """
    while (front_is_clear() and beepers_present()):
        # move all the beepers except the last one at the current field to the next one
        while beepers_present():
            pick_beeper()
            if (beepers_present()):
                put_beeper()
                move_one_beeper_ahead()
        # advance to the next field
        move()

def move_one_beeper_ahead():
    """
    Assumes there's at least one beeper at the current position.
    Picks a beeper and moves it to the next field.
    Then goes back to restores Karel's original position.
    """
    pick_beeper()
    move()
    put_beeper()
    turn_back()
    move()
    turn_back()



## Approach 2 [UNFINISHED]:
## Put beeper on every field,
## then try to collect right most and left most ones,
## until there's only one beeper left
def mark():
   while no_beepers_present():
        put_beeper()
        if front_is_clear():
            move()

def collect():
    while (beepers_present or front_is_clear()):
        pick_beeper()
    turn_back()

def last_beeper():
    if front_is_clear():
        move()

def turn_back():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()
