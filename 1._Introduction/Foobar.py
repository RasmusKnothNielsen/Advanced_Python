# Program written on the first day of Advanced Python, Computer Science, KEA

# Given {0- 100}
# If divisible by 3 = print foo
# If divisible by 5 = print bar
# Otherwise print x

# Be wary of making the implementation fixed at compile time.
# It should be possible to change something at runtime.

def foo_bar(number, dictionary):
    """
    Takes a number and a dictionary, finds out if the key from the dictionary is divisible by the current number.
    If it is, the function will print out the corresponding value from dictionary.

    :param number: int
        The number of times we want to iterate. Inclusive.

    :param dictionary: dict
        Collection of numbers and corresponding words, that should be outputted each time the current
        number is divisible by the key in the dictionary.

    :return: void
        The function prints the output to the console.
    """
    for i in range(number + 1):
        message = ""
        for key, value in dictionary.items():
            if i % key == 0:
                message += value
        if not message:  # Since message is empty, it is falsy
            print(i)
        else:
            print(message)
        # Alternative method, that is not as logically solid
        # print(message or i)


dictionary = {
    3: "Foo",
    4: "Buz",
    5: "Bar",
    7: "Fiz"
}

foo_bar(25, dictionary)

help(foo_bar)
