## Dijkstra's Algorithm

Dijkstra’s algorithm is also known as the single-source shortest path algorithm. It is used for finding the shortest path between the nodes of a graph where the cost of each path is not the same.

In real-world applications, Dijkstra’s algorithm is used to automatically find directions between physical locations, as the directions you get on Google Maps is an example of Dijkstra’s algorithm.

We can also use the [Breadth-First Search algorithm](https://thecleverprogrammer.com/2021/02/17/breadth-first-search-using-python/) to find the shortest path, but the problem is, it assumes the cost of traversing each path is the same. While Dijkstra’s algorithm helps us find the shortest path where the cost of each path is not the same.

In the Breadth-First Search algorithm, we move from one node to all the other nodes, which means we follow the first-come, first-served method. But in Dijkstra’s algorithm, instead of following the first-come, first-served method, we deal with the closest nodes first so that it takes a very small number of steps to find the shortest path.

### Dijkstra’s Algorithm using Python

 To implement it we have to choose the first node that is closest to the source to find the shortest path.

 ### Output

 ```
=== Dijkstra ===
A >> G:
[(5, 'D', ('A', ())), (7, 'B', ('A', ()))]
[(7, 'B', ('A', ())), (12, 'E', ('D', ('A', ()))), (11, 'F', ('D', ('A', ())))]
[(11, 'F', ('D', ('A', ()))), (12, 'E', ('D', ('A', ()))), (15, 'C', ('B', ('A', ()))), (14, 'E', ('B', ('A', ())))]
[(12, 'E', ('D', ('A', ()))), (14, 'E', ('B', ('A', ()))), (15, 'C', ('B', ('A', ()))), (22, 'G', ('F', ('D', ('A', ()))))]       
[(14, 'E', ('B', ('A', ()))), (21, 'G', ('E', ('D', ('A', ())))), (15, 'C', ('B', ('A', ()))), (22, 'G', ('F', ('D', ('A', ()))))]
[(15, 'C', ('B', ('A', ()))), (21, 'G', ('E', ('D', ('A', ())))), (22, 'G', ('F', ('D', ('A', ()))))]
[(21, 'G', ('E', ('D', ('A', ())))), (22, 'G', ('F', ('D', ('A', ()))))]
(21, ('G', ('E', ('D', ('A', ())))))
 ```

 ### Summary

 In this project, I introduced you to Dijkstra’s algorithm and its implementation using Python. It is a better approach to find the shortest path when the cost of each path is not the same. The directions that you get in Google Maps is one of the examples where Dijkstra’s algorithm is used.