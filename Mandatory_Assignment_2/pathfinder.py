import time
import os
import math
from colorama import Fore
from colorama import Style


class Node:

    def __init__(self, parent=None, position=None, weight=1, distance=math.inf):
        """
        Representation of a node on our 2d field.

        g = Distance between starting node and current node
        h = Distance between current node and ending node
        f = Sum of g and h ( f = g + h )

        :param parent:
            The node from which we came on our path to the end node

        :param position:
            Where on the 2d space this node is placed, provided as a tuple

        :param weight:
            Used to determine what the weight is from one node back to this one.
            Should be 1 if we are going horizontally or vertical, otherwise it should be the square root of 2

        :param distance:
            Used for Dijkstra's to keep track of the total distance from the current node, back to the starting node.


        Breadth First requires neither weight or distance
        >>> parent = Node(None, (1,2))
        >>> child = Node(parent, (2,2))
        >>> child.parent.position
        (1, 2)


        A* requires weigth and two types of distance, one from starting node and one from ending node
        >>> start_node = Node(None, (1,2))
        >>> start_node.set_g(0)

        >>> end_node = Node(None, (4,4))

        >>> a_node = Node(start_node, (2,2), 1)
        >>> a_node.set_g(start_node.g + 1)
        >>> a_node.set_h(((a_node.position[0] - end_node.position[0]) ** 2 + ((a_node.position[1] - end_node.position[1])
        ... ** 2)) * child.weight)
        >>> a_node.set_f(a_node.g + a_node.h)

        >>> b_node = Node(a_node, (3,3), math.sqrt(2))
        >>> b_node.set_g(a_node.g + 1)
        >>> b_node.set_h(((b_node.position[0] - end_node.position[0]) ** 2 + ((b_node.position[1] - end_node.position[1])
        ... ** 2)) * child.weight)
        >>> b_node.set_f(b_node.g + b_node.h)

        >>> c_node = Node(b_node, (4,4), math.sqrt(2))
        >>> c_node.set_g(b_node.g + 1)
        >>> c_node.set_h(((c_node.position[0] - end_node.position[0]) ** 2 + ((c_node.position[1] - end_node.position[1])
        ... ** 2)) * child.weight)
        >>> c_node.set_f(c_node.g + c_node.h)


        Dijkstra's require weight and distance from starting node
        >>> a_node = Node(None, (1,2), 1, 0)
        >>> b_node = Node(a_node, (2,2), 1, a_node.distance + 1)
        >>> c_node = Node(b_node, (3,3), math.sqrt(2), b_node.distance + math.sqrt(2))
        >>> c_node.distance
        2.414213562373095

        """
        self.parent = parent
        self.position = position
        self.weight = weight
        self.distance = distance    # Used for Dijkstra's

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):            # Used for Dijkstra's
        return self.distance < other.distance

    def __str__(self):
        return str(self.position)

    def set_weight(self, val):          # Used for Dijkstra's and A*
        self.weight = val

    def set_distance(self, val):        # Used for Dijkstra's
        self.distance = val

    def set_g(self, val):               # Used for A*
        self.g = val

    def set_h(self, val):               # Used for A*
        self.h = val

    def set_f(self, val):               # Used for A*
        self.f = val


def find_path(maze, start, end, algorithm):
    """
    Base function for finding the shortest path, depending on what algorithm that is chosen.

    :param maze:
        The grid upon the pathfinding is going to happen

    :param start:
        Starting point provided as a tuple that represents a point on the maze

    :param end:
        Ending point provided as a tuple that represents a point on the maze

    :param algorithm:
        String name of chosen algorithm.
        'astar', 'dijkstra' or 'breadth_first'
    """

    # Starting at -1, since the first step is just starting from the starting position
    number_of_steps = -1

    # Counting the number of searched nodes
    searched_nodes = 0

    if algorithm == 'dijkstra':
        start_node = Node(None, start, 1, 0)
    else:
        start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        """ Special cases depending on what algorithm is chosen """
        if algorithm == 'dijkstra':
            # Find the shortest distance from start to this node
            for index, item in enumerate(open_list):
                if item.distance < current_node.distance:
                    current_node = item
                    current_index = index
        elif algorithm == 'astar':
            # Find the shortest sum of distance from start to this node and from this node to end
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)
        number_of_steps += 1
        os.system('clear')

        """ If we are at the end node """
        if current_node == end_node:
            path = []
            solution = maze

            print_maze(solution, start, end, algorithm, searched_nodes)

            current = current_node
            while current is not None:
                # Set the node to a 1, for printing purposes
                solution[current.position[0]][current.position[1]] = 1

                print_maze(solution, start, end, algorithm, searched_nodes, current.position)

                path.append(current.position)
                current = current.parent
            print("Number of steps:", len(path) - 1)
            print("\nVery nice, great success!\n")
            time.sleep(2)

            return path[::-1]

        children = []

        """ If we are not at the end node """
        # Create a list of possible new positions
        possible_positions = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        for new_position in possible_positions:

            node_pos = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            """ If the node is "outside" our maze, continue without saving it as a viable path """
            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze) - 1]) - 1) or \
                    node_pos[1] < 0:
                continue

            """ If the node is not walkable, continue with another path """
            if maze[node_pos[0]][node_pos[1]] not in [0, 4]:
                continue

            """ If inside maze and walkable, create node and add it to children """
            # Add weight according to what direction we are going
            if new_position[0] == 0 or new_position[1] == 0:  # If we are going horizontal or vertical
                if algorithm == 'dijkstra':
                    new_node = Node(current_node, node_pos, 1, current_node.distance + 1)
                else:
                    new_node = Node(current_node, node_pos, 1)
            else:
                if algorithm == 'dijkstra':
                    new_node = Node(current_node, node_pos, math.sqrt(2), current_node.distance + math.sqrt(2))
                else:
                    new_node = Node(current_node, node_pos, math.sqrt(2))
            children.append(new_node)

        """ For every possible path in our collection """
        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            maze[child.position[0]][child.position[1]] = 3
            searched_nodes += 1
            print_maze(maze, end, start, algorithm, searched_nodes, current_node)

            """ Set g, h and f for A* """
            if algorithm == 'astar':
                star(current_node, child, end_node, open_list)

            # The following node is on the way
            open_list.append(child)


def star(current_node, child, end_node, open_list):
    """
    Helper function that sets g, h and f for A* algorithm

    :param current_node:
        The node from which we came, on the current path.

    :param child:
        The next possible step on a given path.

    :param end_node:
        The position of the end node. Is used to determine how far from the ending point we are.

    :param open_list:
        List of nodes that are still contenders for the shortest path.
    """

    # Set the g, h and f of the current node
    child.set_g(current_node.g + 1)
    # Calculate the difference a^2 + b^2 * weight
    child.set_h(
        ((child.position[0] - end_node.position[0]) ** 2 + ((child.position[1] - end_node.position[1]) ** 2))
        * child.weight)
    child.set_f(child.g + child.h)

    for open_node in open_list:
        # If we are further away from the ending point, continue with another available path
        if child == open_node and child.g > open_node.g:
            continue


def print_maze(maze, start, end, algo, searched_nodes=0, current=None):
    """
    Helper method used to print the maze to the terminal in color.
    Chosen path = 1
    Walls = 2
    Tested path = 3
    Starting point = 4

    :param maze:
        The entire maze

    :param start:
        Starting point

    :param end:
        Ending point

    :param algo:
        Used for printing which algorithm is currently used

    :param searched_nodes:
        Number of nodes that has already been searched for possible paths

    :param current:
        The current node if applicable

    """
    os.system('clear')

    # Add start and end point to the maze
    maze[start[0]][start[1]] = 4
    maze[end[0]][end[1]] = 4

    print(algo + "\n")
    for line in maze:
        for char in line:
            print(possibilities.get(char), end="")
        print()
    print()

    print("Starting position:", end)
    print("Ending position:", start)
    print("Current position:", current)
    print("Number of searched Nodes:", searched_nodes)
    time.sleep(1/16)


# Dictionary of how to format and which text to print in the maze
possibilities = {
    0: f'O ',
    1: f'{Fore.GREEN}1{Style.RESET_ALL} ',
    2: f'{Fore.RED}X{Style.RESET_ALL} ',
    3: f'{Fore.BLUE}1{Style.RESET_ALL} ',
    4: f'{Fore.GREEN}X{Style.RESET_ALL} '
}


def main(algorithm):
    """
    Alter the maze and start / end to the desired configuration.
    (2) in the maze means walls
    """

    maze1 = [[0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0]]

    maze2 = [[0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0]]


    """ Set Start and End points here """
    start = (0, 0)
    #start = (7,1)
    #start = (4, 4)
    end = (7, 6)
    #end = (1, 8)
    #end = (7, 7)

    starting_time = time.time()

    find_path(maze1, start, end, algorithm)

    ending_time = time.time()
    result = ending_time - starting_time
    print(str(algorithm) + " took: " + str(round(result, 3)) + " seconds")


if __name__ == '__main__':

    import doctest
    doctest.testmod()

    main('breadth_first')
    path = main('dijkstra')
    main('astar')

