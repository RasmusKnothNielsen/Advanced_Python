import time
import os
import math
from colorama import Fore
from colorama import Style


class Node:

    def __init__(self, parent=None, position=None, weight=1):
        """
        Representation of a node on our 2d field.

        g = Distance between starting node and current node
        h = Distance between current node and ending node
        f = Sum of g and h ( f = g + h )

        :param parent:
            The node from which we came on our path to the end node

        :param position:
            Where on the 2d space this node is placed, provided as a tuple
        """
        self.parent = parent
        self.position = position
        self.weight = weight

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return str(self.position)

    def set_weight(self, val):
        self.weight = val

    def set_g(self, val):
        self.g = val

    def set_h(self, val):
        self.h = val

    def set_f(self, val):
        self.f = val


def astar(maze, start, end):
    """
    Function that defines the A* path finding algorithm

    :param maze:
        The field onto which the path has to be found

    :param start:
        Starting point given in a tuple

    :param end:
        Ending point given in a tuple

    """

    # Starting at -1, since the first step is just starting from the starting position
    number_of_steps = -1

    start_node = Node(None, start)
    end_node = Node(None, end)

    # Add end point to the maze
    maze[start[0]][start[1]] = 5

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)
        number_of_steps += 1
        os.system('clear')

        # If we are at the end node
        if current_node == end_node:
            path = []
            solution = maze

            print_maze(solution, start, end, number_of_steps)

            current = current_node
            while current is not None:
                solution[current.position[0]][current.position[1]] = 1

                print_maze(solution, start, end, number_of_steps, current.position)

                path.append(current.position)
                current = current.parent
            print("\nVery nice, great success!\n")
            return path[::-1]

        children = []

        # If we are not at the end node
        # Create a list of possible new positions
        possible_positions = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        for new_position in possible_positions:

            node_pos = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # If the node is "outside" our maze, continue without saving it as a viable path
            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze) - 1]) - 1) or \
                    node_pos[1] < 0:
                continue

            # If the node is not walkable, continue with another path
            if maze[node_pos[0]][node_pos[1]] != 0:
                continue

            # If inside maze and walkable, create node and add it to children
            # Add weight according to what direction we are going
            if new_position[0] == 0 or new_position[0] == 0:    # If we are going horizontal or vertical
                new_node = Node(current_node, node_pos)
            else:
                new_node = Node(current_node, node_pos, math.sqrt(2))
            children.append(new_node)

        # For every possible path in our collection
        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            maze[child.position[0]][child.position[1]] = 6
            print_maze(maze, end, start, number_of_steps, current_node)
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

            # The following node is on the way
            open_list.append(child)


def dijsktra(maze, start, end):
    pass


def breadth_first(maze, start, end):
    pass

def print_maze(maze, start, end, number_of_steps, current=None):
    """
    Helper method used to print the maze to the terminal in color.
    Chosen path = 1
    Walls = 2
    Tested path = 3
    Starting point = 5

    :param maze:
        The entire maze

    :param start:
        Starting point

    :param end:
        Ending point

    :param number_of_steps:
        The current number of steps that has been taken on the path towards the ending point

    :param current:
        The current node if applicable

    """
    os.system('clear')

    for line in maze:
        for char in line:
            print(possibilities.get(char), end="")
        print()
    print()
    print("Starting position:", end)
    print("Ending position:", start)
    print("Current position:", current)
    print("Number of steps:", number_of_steps)
    time.sleep(1/4)


# Dictionary of possibilities on the maze
possibilities = {
    0: f'O ',
    1: f'{Fore.GREEN}1{Style.RESET_ALL} ',
    2: f'{Fore.RED}X{Style.RESET_ALL} ',
    4: f'{Fore.YELLOW}1{Style.RESET_ALL} ',
    5: f'{Fore.GREEN}S{Style.RESET_ALL} ',
    6: f'{Fore.BLUE}1{Style.RESET_ALL} '
}



def predefined_main():
    """
    Alter the maze and start / end to the desired configuration.
    (2) in the maze means walls

    """
    maze = [[0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    #start = (2, 4)
    end = (7, 6)
    #end = (1, 8)

    astar(maze, start, end)


if __name__ == '__main__':
    predefined_main()
