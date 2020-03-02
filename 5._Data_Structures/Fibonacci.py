def fibonacci_generator(times):
    number_before_last = 0
    last_number = 0
    for number in range(times):
        number_before_last, last_number = last_number, last_number + number_before_last
        if number_before_last == 0:
            last_number = 1
        yield number_before_last


def fibonacci_recursive(number_of_elements):
    if number_of_elements < 0:
        print("Number too low")
    if number_of_elements == 1:
        return 0
    if number_of_elements == 2:
        return 1
    else:
        return fibonacci_recursive(number_of_elements-1) + fibonacci_recursive(number_of_elements-2)


if __name__ == "__main__":

    generated_list = list(fibonacci_generator(20))
    print("Generated List:")
    print(generated_list)
    print("Recursive list:")
    recursive_list = []
    for number in range(1, 21):
        recursive_list.append(fibonacci_recursive(number))
    print(recursive_list)
    print(fibonacci_recursive(1000))