def gen_fib(num_elements):
    """
        A Generator that returns a stream of numbers that comply to the fibonacci sequence

        :param num_elements: Int
            How many elements is going to be computed
        :return: Int
            The computed number
        """
    list = []
    p, pp = 0, 1
    for number in range(num_elements):
        list.append(p)
        pp, p = p, p + pp
    return list


def recursive_fib(num_elements):
    """
    A Recursive function that returns the computed number.

    :param num_elements: Int
        The index of the number that we want to calculate

    :return: Int
        The computed value at the decided index.
    """
    if num_elements == 1:
        return 0
    if num_elements == 2:
        return 1
    else:
        return recursive_fib(num_elements - 2) + recursive_fib(num_elements - 1)


if __name__ == "__main__":

    print(gen_fib(20))

    recursive_list = []
    for number in range(1, 21):
        recursive_list.append(recursive_fib(number))
    print(recursive_list)

    # generated_list = list(fibonacci_generator(20))
    # print("Generated List:")
    # print(generated_list)
    # print("Recursive list:")
    # recursive_list = []
    # for number in range(1, 21):
    #    recursive_list.append(fibonacci_recursive(number))
    # print(recursive_list)
    # print(fibonacci_recursive(10))
