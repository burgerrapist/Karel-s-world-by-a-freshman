"""
File: Steeplechase.py
Name: Chiang Po
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    up()
    cross()
    down()

def up():
    """pre-condition:karel facing east with wall in front of him
    post-condition:karel facing east and have no wall in front of him"""
    while not front_is_clear():
        turn_left()
        move()
        turn_right()

def cross():
    """pre-condition:karel facing east and have no wall in front of him
    post-condition:karel facing south and have no wall next to him"""
    if front_is_clear():
        move()
        turn_right()

def down():
    """pre-condition:karel facing south and have no wall next to him
        post-condition:karel facing east and the wall is on right and front side"""
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
