# TODO

- Switch start and end, so that it matches all the way through
- Add a way to visualize tried paths as blue    (DONE)
- Add a count, to be able to display how many steps were used   (DONE)
- Add a weight of approx 1.4 to going slanted ways  (DONE)
- Add a way to create the possible paths programatically (line 106) (DONE)
- Implement algorithms
    - Dijkstra's        (DONE)
    - Breadth First     (DONE)
    - A*                (DONE)
- Show them next to each other with the same problem
- When printing, use a dictionary to get the proper prints, instead of a if/else if. (DONE)
- Add timing to the search, so it is more visible how fast it is going  (DONE)
- Research why the breadth first finds a way that is 7 instead of A*'s 10??
- Implement the algorithms as first class functions, thus being able to pass them to the pathfinding algorithm  (Sorta DONE)


- For Dijkstra's, implement a way to calculate distance from node to node.
    - Is it just the weight? (1 or sqrt(2)?)    (DONE)
    - Sum of previous path? (DONE)


Add docstrings
- Node  (DONE)
- Engine    (DONE)
- Algorithms
    - A*
    - Dijkstra's

Add unit tests to everything    (DONE)


Algoritmer:
- Breadth First Search  (DONE)
- Dijkstra’s Algoritme  (DONE)
- A*                    (DONE)


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