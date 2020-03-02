# -*- coding: utf-8 -*-

import time
import os
import sys


def init():
    """
    Function that returns the initial state for the Cellula Automata to evolve from.

    It takes into consideration how wide the current console is, when determining the initial state.
    Thus it works on different sizes consoles

    :return: String
        A representation of the initial state
    """
    pad = int((float(os.popen('stty size', 'r').read().split()[1]) / 2) - 1)  # 64
    return ('0' * pad) + '1' + ('0' * pad)


# prints to screen
def render(state):
    """
    Renders the state in the console in a more human pleasing way.

    :param state: String
        The current state of the Cellula Automata line

    >>> render("10010011001001")
    A  A  AA  A  A
    """
    print(state.replace('1', 'A').replace('0', ' '))  # \u2588 can be used to display white squares.


def evolve(state, rule):
    """
    Function used to calculate the new state of the Cellula Automata,
    depending on what the earlier state looked like, coupled with the rule.

    :param state: String
        The state upon we want to decide how the next state looks like.

    :param rule: Integer
        The chosen rule, must be a number between 0 and 255 inclusive.

    :return: String
        The new state is returned.
    """
    # Convert rule into binary,
    # remove the first two chars (0b)
    # and pad it with zeroes, until it is 8 numbers long
    ruleset = str(bin(rule))[2:].zfill(8)

    # make res population in witch all 1 are 0
    res = state.replace('1', '0')

    # run on every character in our population
    for y in range(0, len(state)):

        # run on every pattern
        for x in range(0, len(ruleset)):

            # get pattern
            pattern = str(bin(x))[2:].zfill(3).replace('0', '2').replace('1', '0').replace('2', '1')

            # update res to correct rules based on pattern
            if state[y - 1:y + 2] == pattern:
                res = list(res)
                res[y] = ruleset[x]
                res = "".join(res)

    return res


def user_input_is_valid(rule_number):
    """
    Function that decide if the user input is valid.

    :param rule_number: Integer
        The chosen rule.

    :return: bool
        Returns true if the input is between 0 and 255 inclusive, else it returns false.
    """
    return True if (-1 < rule_number < 256) else False


if __name__ == "__main__":

    # Import test module and execute it

    number_of_inputs = len(sys.argv)

    if number_of_inputs == 2:
        # Create the initial state
        state = init()
        rule = int(sys.argv[1])

    if number_of_inputs == 3:
        # Save and validate the chosen rule from the user
        rule, state = sys.argv[1:3]
        print(state)
        rule = int(rule)

    if number_of_inputs > 3:
        print(number_of_inputs)
        print("You must at least provide a rule and optionally an initial state.")
        exit("Not correct amount of arguments provided")

    # rule = int(sys.argv[1])
    if user_input_is_valid(rule):

        while True:
            render(state)
            state = evolve(state, rule)
            time.sleep(0.1)

    else:
        print('Please enter a rule number between 0 and 255.')
