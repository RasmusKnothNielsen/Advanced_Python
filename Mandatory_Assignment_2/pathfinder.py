import time
import os
from colorama import Fore
from colorama import Style


class Node:

    def __init__(self, parent=None, position=None):
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

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return str(self.position)

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
        os.system('clear')

        # If we are at the end node
        if current_node == end_node:
            path = []
            solution = maze

            print_maze(solution, start, end)

            current = current_node
            while current is not None:
                solution[current.position[0]][current.position[1]] = 1

                print_maze(solution, start, end, current.position)

                path.append(current.position)
                current = current.parent
            print("Very nice, great success!")
            return path[::-1]

        children = []

        # If we are not at the end node
        # Create a list of possible new positions
        # TODO create the new places programatically
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            node_pos = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # If the node is "outside" our maze, continue without saving it as a viable path
            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze) - 1]) - 1) or \
                    node_pos[1] < 0:
                continue

            # If the node is not walkable, continue with another path
            if maze[node_pos[0]][node_pos[1]] != 0:
                continue

            # If inside maze and walkable, create node and add it to children
            new_node = Node(current_node, node_pos)
            children.append(new_node)

        # For every possible path in our collection
        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Set the g, h and f of the current node
            child.set_g(current_node.g + 1)
            child.set_h(
                (child.position[0] - end_node.position[0]) ** 2 + ((child.position[1] - end_node.position[1]) ** 2))
            child.set_f(child.g + child.h)

            for open_node in open_list:
                # If we are further away from the ending point, continue with another available path
                if child == open_node and child.g > open_node.g:
                    continue

            # The following node is on the way
            open_list.append(child)


def print_maze(maze, start, end, current=None):
    """
    Helper method used to print the maze to the terminal in color.
    Chosen path = 1
    Walls = 2
    Tested path = 3
    Ending point = 5

    :param maze:
        The entire maze

    :param start:
        Starting point

    :param end:
        Ending point

    :param current:
        The current node if applicable

    """
    os.system('clear')
    for line in maze:
        for char in line:
            # dictionary
            if char == 1:
                print(f'{Fore.GREEN}1{Style.RESET_ALL} ', end="")

            elif char == 2:
                print(f'{Fore.RED}X{Style.RESET_ALL} ', end="")

            elif char == 4:
                print(f'{Fore.YELLOW}1{Style.RESET_ALL} ', end="")

            elif char == 5:
                print(f'{Fore.GREEN}E{Style.RESET_ALL} ', end="")

            else:
                print(f'O ', end="")
        print()
    print()
    print("Starting position:", end)
    print("Ending position:", start)
    print("Current position:", current)
    time.sleep(1)


def predefined_main():
    """
    Alter the maze and start / end to the desired configuration.
    (2) in the maze means walls

    """
    maze = [[0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    #start = (2, 4)
    end = (7, 6)
    #end = (1, 8)

    astar(maze, end, start)


if __name__ == '__main__':
    predefined_main()
