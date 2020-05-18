# TODO

- Switch start and end, so that it matches all the way through
- Add a way to visualize tried paths as yellow
- Add a count, to be able to display how many steps were used
- Add a weight of approx 1.4 to going slanted ways
- Add a way to create the possible paths programatically (line 106)
- Implement both Dijkstra's and Breadth First
- Show them next to each other with the same problem
- When printing, use a dictionary to get the propper prints, instead of a if/else if.

 Add Two
- Separate node class and implement it in matrix
- Fill the squares with color instead of just sides
- Implement buttondown paint walls, instead of clicking
- Implement algorithm start on space

Add docstrings
- Node
- Engine
- Algorithms
    - A*
    - Dijkstra's

Add unit tests to everything


Algoritmer:
- Breadth First Search
- Dijkstra’s Algoritme
- A*


### A* Pseudocode
```
open_list  
closed_list  
add the start node to open_list  

loop  
    current = node in open_list with the lowest f_cost
    remove curent from open_list
    add current to closed_list

    if current is end node  // End node found
        return
    
    foreach neighbour of the current node
        if neighbour is not traversable OR neighbour is in closed_list
            skip to next neighbour

        if new path to neighbour is shorter OR neighbour is not in open_list
            set f_cost of neighbour
            set parent of neighbour to current
            if neighbour is not in open_list
                add neighbour to open_list

```