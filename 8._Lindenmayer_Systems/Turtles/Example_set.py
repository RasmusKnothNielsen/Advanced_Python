import turtle, tkinter

turtle.setup(1920, 1080, 0, 0)

canvas = turtle.Screen()
escher = turtle.Turtle()
escher.speed(5)

def apply_rules(letter):
    """Apply rules to an individual letter, and return the result."""
    # Rule 1
    if letter == 'A':
        new_string = 'B'

    # Rule 2
    elif letter == 'B':
        new_string = 'AB'

    # no rules apply so keep the character
    else:
        new_string = letter

    return new_string

def process_string(original_string):
    """Apply rules to a string, one letter at a time, and return the result."""
    tranformed_string = ""
    for letter in original_string:
        tranformed_string = tranformed_string + apply_rules(letter)

    return tranformed_string

def create_l_system(number_of_iterations, axiom):
    """Begin with an axiom, and apply rules to the original axiom string number_of_iterations times, then return the result."""
    start_string = axiom
    for counter in range(number_of_iterations):
        end_string = process_string(start_string)
        start_string = end_string

    return end_string


print(create_l_system(1, "A"))
print(create_l_system(2, "A"))
print(create_l_system(3, "A"))
print(create_l_system(4, "A"))
print(create_l_system(5, "A"))
print(create_l_system(10, "A"))

#tkinter.mainloop()