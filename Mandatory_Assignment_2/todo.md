# TODO

- Switch start and end, so that it matches all the way through

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