import time
import os

from colorama import Fore
from colorama import Style


class Node:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0  # dist between current node and start node
        self.h = 0  # estimated dist between current node and end node
        self.f = 0  # dist from start plus estimated dist from end (g + h)

    def __eq__(self, other):
        return self.position is other.position

    def __str__(self):
        return str(self.position)

    def set_g(self, val):
        self.g = val

    def set_h(self, val):
        self.h = val

    def set_f(self, val):
        self.f = val


def astar(maze, start, end):
    start_node = Node(None, start)
    start_node.set_g(0)
    start_node.set_h(0)
    start_node.set_f(0)

    end_node = Node(None, end)
    end_node.set_g(0)
    end_node.set_h(0)
    end_node.set_f(0)

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
        if current_node == end_node:
            path = []
            # solution = [[0 for x in range(len(maze[numrows]))] for numrows in range(len(maze))]
            solution = maze

            print_maze(solution)
            time.sleep(2)
            os.system('clear')
            current = current_node
            while current is not None:
                os.system('clear')
                solution[current.position[0]][current.position[
                    1]] = 1  # Should find a better way of representing so that the dead nodes dont have the same appearance
                print_maze(solution)
                print("Starting position:", end)
                print("Ending position:", start)
                print("Current position:", current.position)
                print("Number of steps:", count_number_of_steps(maze))
                time.sleep(2)
                path.append(current.position)
                current = current.parent

            return path[::-1]

        children = []

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            node_pos = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze) - 1]) - 1) or \
                    node_pos[1] < 0:
                continue

            if maze[node_pos[0]][node_pos[1]] != 0:
                continue

            new_node = Node(current_node, node_pos)

            children.append(new_node)

        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.set_g(current_node.g + 1)
            child.set_h(
                (child.position[0] - end_node.position[0]) ** 2 + ((child.position[1] - end_node.position[1]) ** 2))
            child.set_f(child.g + child.h)

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


def print_maze(maze):
    for line in maze:
        for char in line:
            if char == 1:
                print(f'{Fore.GREEN}1{Style.RESET_ALL} ', end="")

            elif char == 2:
                print(f'{Fore.RED}2{Style.RESET_ALL} ', end="")

            elif char == 4:
                print(f'{Fore.YELLOW}3{Style.RESET_ALL} ', end="")

            else:
                print(f'{char} ', end="")
        print()
    print()


def set_starting_point(maze, start):
    maze[start[0]][start[1]] = 3


def set_ending_point(maze, end):
    maze[end[0]][end[1]] = 4


def count_number_of_steps(maze):
    """ Counts how many steps we have taken so far.
    Starts at minus one because the first step is not a real step, but just placing the 'cursor' on the starting node"""
    i = -1
    for line in maze:
        for char in line:
            if char == 1:
                i += 1
    return i


def main():
    maze = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (2, 0)
    end = (8, 7)

    # set_starting_point(maze, start)
    set_ending_point(maze, end)

    path = astar(maze, end, start)


if __name__ == '__main__':
    main()
