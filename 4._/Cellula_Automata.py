"""
# Cellula Automata

The following script can be run in two different ways:
- Inside an IDE
- In a terminal

If you want to start it from a terminal, use the following command

> python Cellula_automata.py [rule] [initial state]

Initial state is optional.

Remember to change the two variables rule and state on line 124-125
"""

import time
import os
import sys


def draw(state):
    """
    Draws the state in the console in a more human pleasing way.

    :param state: String
        The current state of the Cellula Automata line

    >>> draw("10010011001001")
    A  A  AA  A  A

    >>> draw("0101101010001101001010111")
     A AA A A   AA A  A A AAA

    >>> draw("101010101")
    A A A A A

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

    >>> evolve("00000100000", 126)
    '00001110000'

    >>> evolve("00010001000", 37)
    '01010101010'

    >>> evolve("10010001011", 20)
    '01011001000'
    """
    # Convert rule into binary,
    # remove the first two chars (0b)
    # and pad it with zeroes, until it is 8 numbers long
    ruleset = str(bin(rule))[2:].zfill(8)

    # make res population in which all 1 are 0
    res = state.replace('1', '0')

    # run on every character in the state
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

    >>> user_input_is_valid(23)
    True
    >>> user_input_is_valid(270)
    False
    >>> user_input_is_valid(-31)
    False
    >>> user_input_is_valid(42)
    True
    """
    return -1 < rule_number < 256


if __name__ == "__main__":

    # Import test module and execute it
    import doctest

    doctest.testmod()

    number_of_inputs = len(sys.argv)

    if number_of_inputs < 2:
        # Change these two values, if you want to run the program from inside the IDE
        rule = 126
        state = "0" * 64 + "1" + "0" * 64

    elif number_of_inputs == 2:
        # Create the initial state
        state = "0" * 64 + "1" + "0" * 64
        rule = int(sys.argv[1])

    elif number_of_inputs == 3:
        # Save and validate the chosen rule from the user
        rule, state = sys.argv[1:3]
        rule = int(rule)

    elif number_of_inputs > 3:
        print(number_of_inputs)
        print("You must at least provide a rule and optionally an initial state.")
        exit("Not correct amount of arguments provided")

    if user_input_is_valid(rule):

        while True:
            draw(state)
            state = evolve(state, rule)
            time.sleep(0.1)

    else:
        print('Please enter a rule number between 0 and 255.')
