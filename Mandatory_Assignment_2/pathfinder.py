import time
import os
import math
import heapq    # Used for Dijkstra's algorithm
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

    def __lt__(self, other):            # Used for Dijkstra's Priority Queue
        return self.distance < other.distance

    def __str__(self):
        return str(self.position)

    def set_weight(self, val):
        self.weight = val

    def set_distance(self, val):
        self.distance = val

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

    find_path(maze, start, end, astar)

def dijkstra(maze, start, end):

    find_path(maze, start, end, dijkstra)


def breadth_first(maze, start, end):

    find_path(maze, start, end, breadth_first)

def print_maze(maze, start, end, algo, searched_nodes=0, current=None):
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

    :param searched_nodes:
        Number of nodes that has already been searched for possible paths

    :param current:
        The current node if applicable

    """
    os.system('clear')

    print(algo.__name__ + "\n")
    for line in maze:
        for char in line:
            print(possibilities.get(char), end="")
        print()
    print()
    print("Starting position:", end)
    print("Ending position:", start)
    print("Current position:", current)
    print("Number of searched Nodes:", searched_nodes)
    """
    if number_of_steps > 0:
        print("Number of steps:", number_of_steps)
    """
    time.sleep(1/16)


# Dictionary of possibilities on the maze
possibilities = {
    0: f'O ',
    1: f'{Fore.GREEN}1{Style.RESET_ALL} ',
    2: f'{Fore.RED}X{Style.RESET_ALL} ',
    4: f'{Fore.YELLOW}1{Style.RESET_ALL} ',
    5: f'{Fore.GREEN}S{Style.RESET_ALL} ',
    6: f'{Fore.BLUE}1{Style.RESET_ALL} '
}


def find_path(maze, start, end, algorithm):

    # Starting at -1, since the first step is just starting from the starting position
    number_of_steps = -1

    # Counting the number of searched nodes
    searched_nodes = 0

    if algorithm == dijkstra:
        start_node = Node(None, start, 1, 0)
    else:
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
            if algorithm == dijkstra:
                if item.distance < current_node.distance:
                    current_node = item
                    current_index = index
            elif algorithm == astar:
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
            else:
                continue

        open_list.pop(current_index)
        closed_list.append(current_node)
        number_of_steps += 1
        os.system('clear')

        # If we are at the end node
        if current_node == end_node:
            path = []
            solution = maze

            print_maze(solution, start, end, algorithm, searched_nodes)

            current = current_node
            while current is not None:
                solution[current.position[0]][current.position[1]] = 1

                print_maze(solution, start, end, algorithm, searched_nodes, current.position)

                path.append(current.position)
                current = current.parent
            print("Number of steps:", len(path) - 1)
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
            if new_position[0] == 0 or new_position[1] == 0:  # If we are going horizontal or vertical
                if algorithm == dijkstra:
                    new_node = Node(current_node, node_pos, 1, current_node.distance + 1)
                else:
                    new_node = Node(current_node, node_pos, 1)
            else:
                if algorithm == dijkstra:
                    new_node = Node(current_node, node_pos, math.sqrt(2), current_node.distance + math.sqrt(2))
                else:
                    new_node = Node(current_node, node_pos, math.sqrt(2))
            children.append(new_node)

        # For every possible path in our collection
        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            maze[child.position[0]][child.position[1]] = 6
            searched_nodes += 1
            print_maze(maze, end, start, algorithm, searched_nodes, current_node)

            if algorithm == astar:
                star(current_node, child, end_node, open_list)

            # The following node is on the way
            open_list.append(child)


def star(current_node, child, end_node, open_list ):

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


def main(algorithm):
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
    """
    maze = [[0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0]]
            """

    start = (0, 0)
    #start = (7,1)
    #start = (4, 4)
    end = (7, 6)
    #end = (1, 8)
    #end = (7, 7)

    starting_time = time.time()

    algorithm(maze, start, end)

    ending_time = time.time()
    result = ending_time - starting_time
    print(str(algorithm.__name__) + " took: " + str(round(result, 3)) + " seconds")


if __name__ == '__main__':
    main(astar)
    main(dijkstra)
    main(breadth_first)
