

## BFS - Breadth First Search 


![[Pasted image 20251113210515.png]]

BFS rules (quick recap)

- Use a FIFO queue.
- Start by enqueueing the root (A).
- Repeatedly: dequeue the front node, expand it (visit its children left→right), enqueue each child that hasn’t been seen yet, and record each node’s parent so you can reconstruct the path when you find the goal.
- Stop when you dequeue the goal (or when the queue is empty).

Apply BFS to the pictured tree (children ordered left→right) Children: A → [B, C, D, E]  
B → [F, G]  
G → [K, L]  
L → [O]  
C → [H]  
D → [I, J]  
I → [M]  
J → [N]  
All others have no children.

We’ll show: (1) queue before each dequeue, (2) node we dequeue (expand), (3) children we enqueue, and (4) when we find O we reconstruct the path.

1. Start

- Queue: [A]

2. Dequeue A (expand)

- Dequeued: A
- Enqueue children B, C, D, E
- Queue now: [B, C, D, E]
- Parent(B)=A, Parent(C)=A, Parent(D)=A, Parent(E)=A

3. Dequeue B (expand)

- Dequeued: B
- Enqueue children F, G
- Queue now: [C, D, E, F, G]
- Parent(F)=B, Parent(G)=B

4. Dequeue C (expand)

- Dequeued: C
- Enqueue child H
- Queue now: [D, E, F, G, H]
- Parent(H)=C

5. Dequeue D (expand)

- Dequeued: D
- Enqueue children I, J
- Queue now: [E, F, G, H, I, J]
- Parent(I)=D, Parent(J)=D

6. Dequeue E (expand)

- Dequeued: E
- E has no children
- Queue now: [F, G, H, I, J]

7. Dequeue F (expand)

- Dequeued: F
- F has no children
- Queue now: [G, H, I, J]

8. Dequeue G (expand)

- Dequeued: G
- Enqueue children K, L
- Queue now: [H, I, J, K, L]
- Parent(K)=G, Parent(L)=G

9. Dequeue H (expand)

- Dequeued: H
- H has no children
- Queue now: [I, J, K, L]

10. Dequeue I (expand)

- Dequeued: I
- Enqueue child M
- Queue now: [J, K, L, M]
- Parent(M)=I

11. Dequeue J (expand)

- Dequeued: J
- Enqueue child N
- Queue now: [K, L, M, N]
- Parent(N)=J

12. Dequeue K (expand)

- Dequeued: K
- K has no children
- Queue now: [L, M, N]

13. Dequeue L (expand)

- Dequeued: L
- Enqueue child O
- Queue now: [M, N, O]
- Parent(O)=L

14. Dequeue M (expand)

- Dequeued: M
- M has no children
- Queue now: [N, O]

15. Dequeue N (expand)

- Dequeued: N
- N has no children
- Queue now: [O]

16. Dequeue O → goal found

- Dequeued: O (goal)
- Stop the search.

Reconstruct the path from O using stored parents:

- O → parent L → parent G → parent B → parent A
- Path (root → goal): A → B → G → L → O

Why BFS returned that path

- BFS explores level by level. Although other nodes at the same deeper level get discovered later, BFS found O only after expanding L (which was reached via G and B), and reconstructing parents yields A,B,G,L,O.
- BFS guarantees this is a shortest path in terms of edges (minimum number of edges from A to O).

Notes / tips

- If you were not searching for a specific goal and wanted the full traversal order, BFS full order (level order) would be: A, B, C, D, E, F, G, H, I, J, K, L, M, N, O
- Keep track of visited nodes (or parent pointers) to avoid re-enqueueing nodes in graphs (not needed in a tree).
- BFS uses more memory than DFS in wide trees, because the queue can hold many nodes at a level.


APPLICATIONS OF BFS 
	• Social Networking Websites: In social networks, we can find people within a given distance ‘k’ from a person using Breadth First Search till ‘k’ levels.
	• GPS Navigation systems: Breadth First Search is used to find all neighboring locations. 
	• Broadcasting in Network: In networks, a broadcasted packet follows Breadth First Search to reach all nodes


## DFS - Depth First Search 

Depth first search (DFS) algorithm starts with the initial node of the graph G, and then goes to deeper and deeper until the goal node or the node which has no children. 

• The algorithm, then backtracks from the dead end towards the most recent node that is yet to be completely unexplored. 
• The data structure which is being used in DFS is stack. In DFS, the edges that leads to an unvisited node are called discovery edges while the edges that leads to an already visited node are called block edges. 
• Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures. 
• The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

![[Pasted image 20251113211127.png]]

![[Pasted image 20251113211733.png]]



![[Pasted image 20251113215947.png]]


- b: branching factor (average number of successors per state).
- d: depth of the shallowest (first) solution (number of actions from start to a goal).
- m: maximum depth of the search tree (could be infinite).
- l: depth limit (used by depth-limited search).
- C*: cost of optimal solution (total path cost).
- ε: a positive lower bound on every step cost (i.e., every action costs at least ε > 0).



A* Algorithm - https://www.youtube.com/watch?v=lusRf5v-TI0 
AO* Algorithm - https://www.youtube.com/watch?v=NiY32wS2UVw
Hill Claiming - https://www.youtube.com/watch?v=3OO3vWTpFqY&t=9s
Simulated annealing -  https://www.geeksforgeeks.org/artificial-intelligence/what-is-simulated-annealing/

Alpha beta tuing - https://www.youtube.com/watch?v=DCNP5L9_t4E