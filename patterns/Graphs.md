# Graphs

187 problems across 11 patterns.

## grid_traversal

**What it is** — Grid traversal treats a 2D matrix as an implicit graph where each cell is a node and its neighbors (up/down/left/right, sometimes diagonals) are edges. You recognize this pattern when a problem asks you to explore connected regions, measure areas, or propagate values across a grid. The key insight is that you never need to build an explicit adjacency list — you navigate by shifting row/column indices.

**Common steps**
1. Define your neighbor directions (typically `[(0,1),(0,-1),(1,0),(-1,0)]`).
2. Identify starting cells (a single given cell, all border cells, all cells matching a condition, etc.).
3. Mark a cell as visited the moment you first touch it — either by flipping its value in-place or using a separate `visited` set — to avoid revisiting.
4. Use DFS (recursive or iterative stack) or BFS (queue) to explore all reachable neighbors that pass your validity check (in-bounds, correct value, not visited).
5. Accumulate whatever the problem asks for (area count, cell list, transformed values) during traversal.
6. After processing all starting cells, return the result (or perform a second pass if a two-phase approach is needed, e.g., Surrounded Regions).

**Key variations**
- Single source vs. multi-source flood fill (seed from one cell vs. every cell of a given type simultaneously).
- In-place mutation vs. separate visited tracking (mutation is O(1) space but destructive).
- Border-first traversal: start from the edges to identify cells that should NOT be captured/flipped.
- Counting components vs. finding max/min area vs. reconstructing a path.
- Diagonal or directional movement constraints (e.g., The Maze, Check Valid Path with pipe tiles).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 733 | [Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | 1/10 | 68.2% | [x] |
| 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | 3/10 | 74.0% | [ ] |
| 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | 3/10 | 64.3% | [x] |
| 1992 | [Find All Groups of Farmland](https://leetcode.com/problems/find-all-groups-of-farmland/) | Medium | 4/10 | 75.5% | [ ] |
| 1020 | [Number of Enclaves](https://leetcode.com/problems/number-of-enclaves/) | Medium | 4/10 | 71.7% | [ ] |
| 529 | [Minesweeper](https://leetcode.com/problems/minesweeper/) | Medium | 4/10 | 68.7% | [ ] |
| 1254 | [Number of Closed Islands](https://leetcode.com/problems/number-of-closed-islands/) | Medium | 4/10 | 67.1% | [ ] |
| 490 | [The Maze](https://leetcode.com/problems/the-maze/) :lock: | Medium | 4/10 | 60.4% | [ ] |
| 3905 | [Multi Source Flood Fill](https://leetcode.com/problems/multi-source-flood-fill/) | Medium | 4/10 | 55.9% | [ ] |
| 1905 | [Count Sub Islands](https://leetcode.com/problems/count-sub-islands/) | Medium | 5/10 | 73.0% | [ ] |
| 1391 | [Check if There is a Valid Path in a Grid](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) | Medium | 5/10 | 64.5% | [ ] |
| 1034 | [Coloring A Border](https://leetcode.com/problems/coloring-a-border/) | Medium | 5/10 | 51.2% | [ ] |
| 130 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | 5/10 | 45.2% | [ ] |
| 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | 6/10 | 60.9% | [ ] |
| 2556 | [Disconnect Path in a Binary Matrix by at Most One Flip](https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/) | Medium | 6/10 | 27.9% | [ ] |
| 827 | [Making A Large Island](https://leetcode.com/problems/making-a-large-island/) | Hard | 8/10 | 56.5% | [ ] |
| 749 | [Contain Virus](https://leetcode.com/problems/contain-virus/) | Hard | 9/10 | 54.8% | [ ] |

## dfs_connected_components

**What it is** — This pattern finds and processes groups of nodes that are all reachable from one another in an undirected (or sometimes directed) graph. You recognize it when a problem asks how many clusters exist, whether two nodes are connected, or wants you to compute something for each isolated subgraph. Unlike grid traversal, the graph is typically given explicitly as an edge list or adjacency list.

**Common steps**
1. Build an adjacency list from the given edges (or use the input structure directly if it already is one).
2. Initialize a `visited` set or boolean array.
3. Iterate over every node; for each unvisited node, launch a DFS (or BFS) to explore the entire component it belongs to.
4. Inside the DFS, mark each node visited immediately upon entry, then recurse into all unvisited neighbors.
5. Collect or aggregate whatever the problem needs during or after each component's traversal (count of components, component size, path enumeration, etc.).
6. Return the aggregated result after all nodes have been processed.

**Key variations**
- Undirected components (symmetric edges) vs. directed reachability (only follow edge direction).
- Enumerating all paths vs. just checking connectivity.
- Attaching metadata to each component (e.g., sum, size, distinct shape signature for island uniqueness).
- Graph cloning — must map old nodes to new nodes during DFS to avoid infinite loops.
- Functional/tree graphs where each node has exactly one outgoing edge (rho-shaped traversal).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1791 | [Find Center of Star Graph](https://leetcode.com/problems/find-center-of-star-graph/) | Easy | 1/10 | 86.6% | [ ] |
| 339 | [Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/) :lock: | Medium | 2/10 | 86.0% | [ ] |
| 1971 | [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | Easy | 2/10 | 55.1% | [x] |
| 997 | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | Easy | 2/10 | 50.7% | [ ] |
| 841 | [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) | Medium | 3/10 | 75.7% | [x] |
| 2658 | [Maximum Number of Fish in a Grid](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/) | Medium | 3/10 | 70.6% | [ ] |
| 690 | [Employee Importance](https://leetcode.com/problems/employee-importance/) | Medium | 3/10 | 69.4% | [ ] |
| 1236 | [Web Crawler](https://leetcode.com/problems/web-crawler/) :lock: | Medium | 3/10 | 68.8% | [ ] |
| 364 | [Nested List Weight Sum II](https://leetcode.com/problems/nested-list-weight-sum-ii/) :lock: | Medium | 3/10 | 66.9% | [ ] |
| 3528 | [Unit Conversion I](https://leetcode.com/problems/unit-conversion-i/) | Medium | 3/10 | 54.1% | [ ] |
| 2374 | [Node With Highest Edge Score](https://leetcode.com/problems/node-with-highest-edge-score/) | Medium | 3/10 | 49.3% | [ ] |
| 797 | [All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/) | Medium | 4/10 | 83.6% | [ ] |
| 2685 | [Count the Number of Complete Components](https://leetcode.com/problems/count-the-number-of-complete-components/) | Medium | 4/10 | 77.8% | [ ] |
| 2852 | [Sum of Remoteness of All Cells](https://leetcode.com/problems/sum-of-remoteness-of-all-cells/) :lock: | Medium | 4/10 | 70.7% | [ ] |
| 1306 | [Jump Game III](https://leetcode.com/problems/jump-game-iii/) | Medium | 4/10 | 66.8% | [ ] |
| 1615 | [Maximal Network Rank](https://leetcode.com/problems/maximal-network-rank/) | Medium | 4/10 | 66.0% | [ ] |
| 1245 | [Tree Diameter](https://leetcode.com/problems/tree-diameter/) :lock: | Medium | 4/10 | 61.3% | [ ] |
| 3619 | [Count Islands With Total Value Divisible by K](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/) | Medium | 4/10 | 56.3% | [ ] |
| 1743 | [Restore the Array From Adjacent Pairs](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/) | Medium | 5/10 | 75.0% | [ ] |
| 3535 | [Unit Conversion II](https://leetcode.com/problems/unit-conversion-ii/) :lock: | Medium | 5/10 | 66.5% | [ ] |
| 1466 | [Reorder Routes to Make All Paths Lead to the City Zero](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/) | Medium | 5/10 | 65.8% | [ ] |
| 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | 5/10 | 65.2% | [x] |
| 694 | [Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/) :lock: | Medium | 5/10 | 62.8% | [ ] |
| 3387 | [Maximize Amount After Two Days of Conversions](https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/) | Medium | 5/10 | 61.3% | [ ] |
| 2077 | [Paths in Maze That Lead to Same Room](https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/) :lock: | Medium | 5/10 | 56.7% | [ ] |
| 2359 | [Find Closest Node to Given Two Nodes](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/) | Medium | 5/10 | 53.0% | [ ] |
| 1242 | [Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/) :lock: | Medium | 5/10 | 51.2% | [ ] |
| 3310 | [Remove Methods From Project](https://leetcode.com/problems/remove-methods-from-project/) | Medium | 5/10 | 50.5% | [ ] |
| 2101 | [Detonate the Maximum Bombs](https://leetcode.com/problems/detonate-the-maximum-bombs/) | Medium | 5/10 | 50.1% | [ ] |
| 1361 | [Validate Binary Tree Nodes](https://leetcode.com/problems/validate-binary-tree-nodes/) | Medium | 5/10 | 44.1% | [ ] |
| 711 | [Number of Distinct Islands II](https://leetcode.com/problems/number-of-distinct-islands-ii/) :lock: | Hard | 7/10 | 55.4% | [ ] |
| 1377 | [Frog Position After T Seconds](https://leetcode.com/problems/frog-position-after-t-seconds/) | Hard | 7/10 | 38.4% | [ ] |
| 1761 | [Minimum Degree of a Connected Trio in a Graph](https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/) | Hard | 8/10 | 44.4% | [ ] |
| 1782 | [Count Pairs Of Nodes](https://leetcode.com/problems/count-pairs-of-nodes/) | Hard | 8/10 | 42.3% | [ ] |
| 2242 | [Maximum Score of a Node Sequence](https://leetcode.com/problems/maximum-score-of-a-node-sequence/) | Hard | 8/10 | 40.1% | [ ] |
| 1568 | [Minimum Number of Days to Disconnect Island](https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/) | Hard | 9/10 | 58.7% | [ ] |
| 1719 | [Number Of Ways To Reconstruct A Tree](https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/) | Hard | 9/10 | 45.7% | [ ] |
| 3311 | [Construct 2D Grid Matching Graph Layout](https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/) | Hard | 9/10 | 29.7% | [ ] |
| 3615 | [Longest Palindromic Path in Graph](https://leetcode.com/problems/longest-palindromic-path-in-graph/) | Hard | 9/10 | 22.2% | [ ] |

## graph_coloring

**What it is** — Graph coloring assigns labels ("colors") to nodes so that no two adjacent nodes share the same color, using as few colors as possible (or verifying that a specific number suffices). You recognize this pattern when a problem asks whether a conflict-free assignment exists or asks you to construct one, especially when constraints are expressed as "A and B cannot be the same." For most interview problems only 2 or 3 colors are needed.

**Common steps**
1. Build an adjacency list from the edge list or constraint pairs.
2. Choose a color representation (e.g., an integer array initialized to -1/uncolored, or a dictionary).
3. Iterate over all nodes; for each uncolored node, start a BFS/DFS and assign it color 0.
4. For every neighbor of the current node, assign the opposite color (or the next available color); if the neighbor is already colored and matches the current node's color, a conflict exists — return false or handle accordingly.
5. If all nodes are colored without conflict, construct and return the coloring assignment.
6. For harder variants (3+ colors), use backtracking or verify degree-sequence feasibility (Erdos-Gallai theorem).

**Key variations**
- 2-coloring (bipartite check) vs. k-coloring with k > 2.
- Constructing a valid coloring vs. only checking feasibility.
- Degree-sequence / Erdos-Gallai feasibility checks (no explicit graph given).
- Greedy coloring with a fixed number of colors when conflicts must be minimized.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1042 | [Flower Planting With No Adjacent](https://leetcode.com/problems/flower-planting-with-no-adjacent/) | Medium | 4/10 | 53.6% | [ ] |
| 3656 | [Determine if a Simple Graph Exists](https://leetcode.com/problems/determine-if-a-simple-graph-exists/) :lock: | Medium | 6/10 | 47.9% | [ ] |

## floyd_warshall

**What it is** — Floyd-Warshall computes the shortest path between every pair of nodes in a weighted graph in O(V^3) time by iteratively relaxing paths through each intermediate node k. Recognize this pattern when the graph is small (V <= ~400), you need all-pairs shortest paths, or you need to propagate transitive reachability/relationships across all node pairs.

**Common steps**
1. Build a V x V distance matrix `dist` where `dist[i][j]` is the direct edge weight, 0 on the diagonal, and infinity where no direct edge exists.
2. Run the triple nested loop: for each intermediate node `k`, for each source `i`, for each destination `j`, update `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`.
3. After the loop, `dist[i][j]` holds the true shortest path length between every pair.
4. Use the completed matrix to answer the problem's specific query (e.g., find the city with the fewest reachable neighbors within a threshold).
5. For reachability instead of distance, use a boolean matrix and `OR` instead of `min`/`+`.

**Key variations**
- Shortest distance vs. transitive reachability (boolean matrix).
- Detecting negative cycles (if `dist[i][i] < 0` after the algorithm, a negative cycle exists).
- Enumerating subsets of nodes to close (combine with bitmask enumeration for small V).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1334 | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | 5/10 | 72.7% | [ ] |
| 1462 | [Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/) | Medium | 5/10 | 59.8% | [ ] |
| 2959 | [Number of Possible Sets of Closing Branches](https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/) | Hard | 8/10 | 50.8% | [ ] |

## topological_sort

**What it is** — Topological sort produces a linear ordering of nodes in a Directed Acyclic Graph (DAG) such that every directed edge u -> v appears with u before v in the ordering. You recognize it whenever a problem involves dependency ordering, task scheduling, or asks whether a set of constraints is satisfiable (cycle = impossible). It is also the foundation for computing longest/shortest paths in DAGs.

**Common steps**
1. Build a directed adjacency list and an in-degree array for every node.
2. Seed a queue (BFS / Kahn's algorithm) with all nodes whose in-degree is 0 (no prerequisites).
3. Repeatedly dequeue a node, add it to the result order, and decrement the in-degree of each of its neighbors; enqueue any neighbor whose in-degree drops to 0.
4. If the result order contains all nodes, the graph is a valid DAG; otherwise a cycle exists — return the appropriate answer.
5. For DFS-based topo sort: do a post-order DFS, push each node to a stack after all its descendants are processed, then reverse the stack.
6. For DP-on-DAG problems (e.g., longest path, propagate color values), process nodes in topological order and update state.

**Key variations**
- Cycle detection as the primary goal vs. ordering as the primary goal.
- Multi-level / grouped topological sort (Parallel Courses — level = BFS depth = minimum time).
- Reverse topo sort: find nodes with no outgoing edges first (e.g., find vertices reachable from all others).
- Nested topo sort: sort groups, then sort items within groups respecting inter-group dependencies.
- Propagating per-node state (color, value) forward along topological order.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1557 | [Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) | Medium | 4/10 | 81.6% | [ ] |
| 3481 | [Apply Substitutions](https://leetcode.com/problems/apply-substitutions/) :lock: | Medium | 4/10 | 77.4% | [ ] |
| 1136 | [Parallel Courses](https://leetcode.com/problems/parallel-courses/) :lock: | Medium | 5/10 | 62.2% | [ ] |
| 2192 | [All Ancestors of a Node in a Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/) | Medium | 5/10 | 62.1% | [ ] |
| 2115 | [Find All Possible Recipes from Given Supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/) | Medium | 5/10 | 56.9% | [ ] |
| 210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | 5/10 | 55.4% | [x] |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | 5/10 | 51.3% | [x] |
| 444 | [Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction/) :lock: | Medium | 5/10 | 30.8% | [ ] |
| 851 | [Loud and Rich](https://leetcode.com/problems/loud-and-rich/) | Medium | 6/10 | 63.4% | [ ] |
| 310 | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | Medium | 6/10 | 42.5% | [ ] |
| 2392 | [Build a Matrix With Conditions](https://leetcode.com/problems/build-a-matrix-with-conditions/) | Hard | 7/10 | 79.3% | [ ] |
| 2050 | [Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/) | Hard | 7/10 | 66.8% | [ ] |
| 1591 | [Strange Printer II](https://leetcode.com/problems/strange-printer-ii/) | Hard | 8/10 | 60.8% | [ ] |
| 1857 | [Largest Color Value in a Directed Graph](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/) | Hard | 8/10 | 57.3% | [ ] |
| 2603 | [Collect Coins in a Tree](https://leetcode.com/problems/collect-coins-in-a-tree/) | Hard | 8/10 | 40.1% | [ ] |
| 269 | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) :lock: | Hard | 8/10 | 37.2% | [ ] |
| 1203 | [Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) | Hard | 9/10 | 65.9% | [ ] |
| 3383 | [Minimum Runes to Add to Cast Spell](https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/) :lock: | Hard | 9/10 | 44.8% | [ ] |

## bfs_shortest_path

**What it is** — BFS finds the shortest path in terms of number of edges (or uniform-cost steps) because it explores nodes level by level, guaranteeing the first time a node is reached it is via the shortest route. You recognize this pattern whenever you need minimum steps/moves/transformations in an unweighted or unit-weight graph — including abstract state-space graphs where "nodes" are configurations and "edges" are valid transitions.

**Common steps**
1. Model the problem as a graph: define what a "state" (node) is and what a valid "move" (edge) looks like.
2. Initialize a queue with the starting state(s) and a `visited` set containing them.
3. Process the queue level by level (or track distance per node); for each current state, generate all valid next states.
4. If a next state is the target, return the current distance + 1 immediately.
5. Otherwise, if unseen, add it to `visited` and enqueue it.
6. If the queue empties without finding the target, return -1 (unreachable).

**Key variations**
- Single-source vs. multi-source BFS (seed queue with multiple starting nodes simultaneously — e.g., Rotting Oranges, 01 Matrix).
- State augmentation: encode extra dimensions in the state (keys collected, obstacles remaining, direction of travel) to allow revisiting the same position with different state.
- Bidirectional BFS: expand from both source and target to reduce search space (useful for Word Ladder, large state spaces).
- 0-1 BFS / deque BFS: when edges have cost 0 or 1, use a deque — push cost-0 moves to the front, cost-1 moves to the back.
- Abstract state-space BFS: the "grid" is a string, permutation, or other structure (Sliding Puzzle, Word Ladder, Open the Lock).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1765 | [Map of Highest Peak](https://leetcode.com/problems/map-of-highest-peak/) | Medium | 4/10 | 75.8% | [ ] |
| 286 | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) :lock: | Medium | 4/10 | 64.0% | [ ] |
| 3243 | [Shortest Distance After Road Addition Queries I](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/) | Medium | 4/10 | 61.9% | [ ] |
| 994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | 4/10 | 58.6% | [ ] |
| 3015 | [Count the Number of Houses at a Certain Distance I](https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/) | Medium | 4/10 | 57.6% | [ ] |
| 1730 | [Shortest Path to Get Food](https://leetcode.com/problems/shortest-path-to-get-food/) :lock: | Medium | 4/10 | 57.2% | [ ] |
| 433 | [Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/) | Medium | 4/10 | 56.6% | [ ] |
| 1311 | [Get Watched Videos by Your Friends](https://leetcode.com/problems/get-watched-videos-by-your-friends/) | Medium | 4/10 | 52.9% | [ ] |
| 1091 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | 4/10 | 51.4% | [ ] |
| 1926 | [Nearest Exit from Entrance in Maze](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/) | Medium | 4/10 | 48.5% | [ ] |
| 1215 | [Stepping Numbers](https://leetcode.com/problems/stepping-numbers/) :lock: | Medium | 4/10 | 48.4% | [ ] |
| 1197 | [Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/) :lock: | Medium | 4/10 | 41.9% | [ ] |
| 1625 | [Lexicographically Smallest String After Applying Operations](https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/) | Medium | 5/10 | 79.3% | [ ] |
| 752 | [Open the Lock](https://leetcode.com/problems/open-the-lock/) | Medium | 5/10 | 61.3% | [ ] |
| 542 | [01 Matrix](https://leetcode.com/problems/01-matrix/) | Medium | 5/10 | 53.8% | [ ] |
| 1162 | [As Far from Land as Possible](https://leetcode.com/problems/as-far-from-land-as-possible/) | Medium | 5/10 | 52.3% | [ ] |
| 2059 | [Minimum Operations to Convert Number](https://leetcode.com/problems/minimum-operations-to-convert-number/) | Medium | 5/10 | 51.8% | [ ] |
| 2998 | [Minimum Number of Operations to Make X and Y Equal](https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/) | Medium | 5/10 | 48.7% | [ ] |
| 909 | [Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/) | Medium | 5/10 | 48.1% | [ ] |
| 2146 | [K Highest Ranked Items Within a Price Range](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/) | Medium | 5/10 | 46.6% | [ ] |
| 2174 | [Remove All Ones With Row and Column Flips II](https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/) :lock: | Medium | 6/10 | 67.4% | [ ] |
| 399 | [Evaluate Division](https://leetcode.com/problems/evaluate-division/) | Medium | 6/10 | 64.2% | [ ] |
| 934 | [Shortest Bridge](https://leetcode.com/problems/shortest-bridge/) | Medium | 6/10 | 59.4% | [ ] |
| 2039 | [The Time When the Network Becomes Idle](https://leetcode.com/problems/the-time-when-the-network-becomes-idle/) | Medium | 6/10 | 55.5% | [ ] |
| 2812 | [Find the Safest Path in a Grid](https://leetcode.com/problems/find-the-safest-path-in-a-grid/) | Medium | 6/10 | 48.7% | [ ] |
| 1129 | [Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/) | Medium | 6/10 | 48.0% | [ ] |
| 1778 | [Shortest Path in a Hidden Grid](https://leetcode.com/problems/shortest-path-in-a-hidden-grid/) :lock: | Medium | 6/10 | 44.6% | [ ] |
| 3629 | [Minimum Jumps to Reach End via Prime Teleportation](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/) | Medium | 6/10 | 31.9% | [ ] |
| 1654 | [Minimum Jumps to Reach Home](https://leetcode.com/problems/minimum-jumps-to-reach-home/) | Medium | 6/10 | 30.7% | [ ] |
| 3552 | [Grid Teleportation Traversal](https://leetcode.com/problems/grid-teleportation-traversal/) | Medium | 6/10 | 23.6% | [ ] |
| 773 | [Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/) | Hard | 7/10 | 74.4% | [ ] |
| 2290 | [Minimum Obstacle Removal to Reach Corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/) | Hard | 7/10 | 70.6% | [ ] |
| 2045 | [Second Minimum Time to Reach Destination](https://leetcode.com/problems/second-minimum-time-to-reach-destination/) | Hard | 7/10 | 62.3% | [ ] |
| 3690 | [Split and Merge Array Transformation](https://leetcode.com/problems/split-and-merge-array-transformation/) | Medium | 7/10 | 58.7% | [ ] |
| 1345 | [Jump Game IV](https://leetcode.com/problems/jump-game-iv/) | Hard | 7/10 | 46.3% | [ ] |
| 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | 7/10 | 45.5% | [ ] |
| 317 | [Shortest Distance from All Buildings](https://leetcode.com/problems/shortest-distance-from-all-buildings/) :lock: | Hard | 7/10 | 44.9% | [ ] |
| 3568 | [Minimum Moves to Clean the Classroom](https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/) | Medium | 7/10 | 26.7% | [ ] |
| 1298 | [Maximum Candies You Can Get from Boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/) | Hard | 8/10 | 67.5% | [ ] |
| 2503 | [Maximum Number of Points From Grid Queries](https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/) | Hard | 8/10 | 59.3% | [ ] |
| 2858 | [Minimum Edge Reversals So Every Node Is Reachable](https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/) | Hard | 8/10 | 59.3% | [ ] |
| 2814 | [Minimum Time Takes to Reach Destination Without Drowning](https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/) :lock: | Hard | 8/10 | 54.6% | [ ] |
| 815 | [Bus Routes](https://leetcode.com/problems/bus-routes/) | Hard | 8/10 | 47.3% | [ ] |
| 1293 | [Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | Hard | 8/10 | 46.3% | [ ] |
| 2608 | [Shortest Cycle in a Graph](https://leetcode.com/problems/shortest-cycle-in-a-graph/) | Hard | 8/10 | 39.6% | [ ] |
| 847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | Hard | 9/10 | 66.0% | [ ] |
| 864 | [Shortest Path to Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/) | Hard | 9/10 | 54.6% | [ ] |
| 1210 | [Minimum Moves to Reach Target with Rotations](https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/) | Hard | 9/10 | 52.1% | [ ] |
| 1263 | [Minimum Moves to Move a Box to Their Target Location](https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/) | Hard | 9/10 | 49.7% | [ ] |
| 854 | [K-Similar Strings](https://leetcode.com/problems/k-similar-strings/) | Hard | 9/10 | 40.9% | [ ] |
| 1036 | [Escape a Large Maze](https://leetcode.com/problems/escape-a-large-maze/) | Hard | 9/10 | 36.6% | [ ] |
| 675 | [Cut Off Trees for Golf Event](https://leetcode.com/problems/cut-off-trees-for-golf-event/) | Hard | 9/10 | 36.4% | [ ] |
| 3534 | [Path Existence Queries in a Graph II](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/) | Hard | 9/10 | 26.6% | [ ] |
| 2617 | [Minimum Number of Visited Cells in a Grid](https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/) | Hard | 9/10 | 23.9% | [ ] |
| 2612 | [Minimum Reverse Operations](https://leetcode.com/problems/minimum-reverse-operations/) | Hard | 9/10 | 17.0% | [ ] |
| 126 | [Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) | Hard | 10/10 | 27.7% | [ ] |

## dijkstra

**What it is** — Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights, using a min-heap (priority queue) to always expand the cheapest unvisited node first. Recognize this pattern when edge weights vary (ruling out plain BFS) and all weights are non-negative — the moment you need minimum cost, minimum effort, or maximum probability paths in a weighted graph.

**Common steps**
1. Build a weighted adjacency list from the given edges.
2. Initialize a `dist` array to infinity for all nodes except the source (dist[src] = 0).
3. Push `(0, src)` onto a min-heap.
4. Pop the node with the smallest tentative distance; if it equals the already-recorded best distance, process it — otherwise skip (stale entry).
5. For each neighbor, compute `new_dist = dist[current] + edge_weight`; if `new_dist < dist[neighbor]`, update `dist[neighbor]` and push `(new_dist, neighbor)` onto the heap.
6. Return `dist[target]` (or the full `dist` array for all-pairs from source) once the heap is empty.

**Key variations**
- Standard shortest path vs. maximizing the minimum value along a path (use a max-heap with negated costs).
- Maximizing probability: replace addition with multiplication, use max-heap.
- State augmentation: include extra state in the heap tuple (e.g., remaining discount uses, current direction) to allow revisiting a node in a different state.
- Counting shortest paths: maintain a `count` array alongside `dist`, incrementing/resetting when a new shortest path is found.
- Modified edge weights: edges that appear only in one direction or have conditional costs (time-dependent, alternating colors).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2737 | [Find the Closest Marked Node](https://leetcode.com/problems/find-the-closest-marked-node/) :lock: | Medium | 4/10 | 65.4% | [ ] |
| 2473 | [Minimum Cost to Buy Apples](https://leetcode.com/problems/minimum-cost-to-buy-apples/) :lock: | Medium | 5/10 | 67.2% | [ ] |
| 1514 | [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium | 5/10 | 65.5% | [ ] |
| 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | 5/10 | 60.3% | [ ] |
| 3341 | [Find Minimum Time to Reach Last Room I](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/) | Medium | 5/10 | 55.4% | [ ] |
| 3112 | [Minimum Time to Visit Disappearing Nodes](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/) | Medium | 5/10 | 37.8% | [ ] |
| 3286 | [Find a Safe Walk Through a Grid](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/) | Medium | 5/10 | 33.2% | [ ] |
| 3342 | [Find Minimum Time to Reach Last Room II](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/) | Medium | 6/10 | 67.7% | [ ] |
| 1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Medium | 6/10 | 63.1% | [ ] |
| 3650 | [Minimum Cost Path with Edge Reversals](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/) | Medium | 6/10 | 61.8% | [ ] |
| 2093 | [Minimum Cost to Reach City With Discounts](https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/) :lock: | Medium | 6/10 | 60.9% | [ ] |
| 1810 | [Minimum Path Cost in a Hidden Grid](https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/) :lock: | Medium | 6/10 | 58.8% | [ ] |
| 505 | [The Maze II](https://leetcode.com/problems/the-maze-ii/) :lock: | Medium | 6/10 | 55.1% | [ ] |
| 1102 | [Path With Maximum Minimum Value](https://leetcode.com/problems/path-with-maximum-minimum-value/) :lock: | Medium | 6/10 | 54.7% | [ ] |
| 3604 | [Minimum Time to Reach Destination in Directed Graph](https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/) | Medium | 6/10 | 45.6% | [ ] |
| 2662 | [Minimum Cost of a Path With Special Roads](https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/) | Medium | 6/10 | 43.0% | [ ] |
| 1976 | [Number of Ways to Arrive at Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) | Medium | 6/10 | 37.5% | [ ] |
| 3377 | [Digit Operations to Make Two Integers Equal](https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/) | Medium | 6/10 | 30.4% | [ ] |
| 1786 | [Number of Restricted Paths From First to Last Node](https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/) | Medium | 7/10 | 41.1% | [ ] |
| 1368 | [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) | Hard | 8/10 | 71.0% | [ ] |
| 2714 | [Find Shortest Path with K Hops](https://leetcode.com/problems/find-shortest-path-with-k-hops/) :lock: | Hard | 8/10 | 68.8% | [ ] |
| 778 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | 8/10 | 67.8% | [ ] |
| 2577 | [Minimum Time to Visit a Cell In a Grid](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/) | Hard | 8/10 | 56.3% | [ ] |
| 499 | [The Maze III](https://leetcode.com/problems/the-maze-iii/) :lock: | Hard | 8/10 | 52.3% | [ ] |
| 882 | [Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/) | Hard | 8/10 | 52.1% | [ ] |
| 3123 | [Find Edges in Shortest Paths](https://leetcode.com/problems/find-edges-in-shortest-paths/) | Hard | 8/10 | 46.6% | [ ] |
| 2699 | [Modify Graph Edge Weights](https://leetcode.com/problems/modify-graph-edge-weights/) | Hard | 9/10 | 55.6% | [ ] |
| 2203 | [Minimum Weighted Subgraph With the Required Paths](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/) | Hard | 9/10 | 42.0% | [ ] |
| 3620 | [Network Recovery Pathways](https://leetcode.com/problems/network-recovery-pathways/) | Hard | 9/10 | 29.9% | [ ] |

## cycle_detection

**What it is** — Cycle detection determines whether a graph contains a cycle and, in harder problems, characterizes the cycle (length, nodes involved, distance to it). In directed graphs the standard approach uses DFS with a three-color (white/gray/black) scheme or tracks the recursion stack; in undirected graphs you check whether a visited neighbor is not the parent. Recognize this pattern when a problem asks about "loops," "eventual safe nodes," "bridges," or whether a structure is truly a tree/DAG.

**Common steps**
1. Build an adjacency list. For directed graphs, also prepare an in-degree array if using Kahn's approach.
2. Initialize a `state` array: 0 = unvisited, 1 = in current DFS path (gray), 2 = fully processed (black).
3. For each unvisited node, launch a DFS. If you reach a gray neighbor, a cycle exists — return/record accordingly.
4. Mark a node gray on entry and black on exit (after all neighbors are processed).
5. For undirected cycle detection, track the parent node and flag any visited neighbor that is not the parent as a cycle.
6. For bridge/articulation-point detection (Tarjan's), additionally track discovery times and low values to find edges whose removal disconnects the graph.

**Key variations**
- Simple yes/no cycle detection vs. finding the cycle length or all nodes in the cycle.
- Directed graph (recursion stack coloring) vs. undirected graph (parent tracking).
- Finding "eventual safe" nodes — nodes from which all paths lead to a terminal, not a cycle.
- Bridge and articulation-point detection (Tarjan's algorithm) — edges/nodes whose removal increases connectivity components.
- Functional graphs (each node has exactly one outgoing edge) — use fast/slow pointer or coloring to find cycles efficiently.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1559 | [Detect Cycles in 2D Grid](https://leetcode.com/problems/detect-cycles-in-2d-grid/) | Medium | 5/10 | 63.2% | [ ] |
| 1059 | [All Paths from Source Lead to Destination](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/) :lock: | Medium | 5/10 | 37.3% | [ ] |
| 802 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Medium | 6/10 | 70.7% | [ ] |
| 2204 | [Distance to a Cycle in Undirected Graph](https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/) :lock: | Hard | 7/10 | 73.8% | [ ] |
| 1153 | [String Transforms Into Another String](https://leetcode.com/problems/string-transforms-into-another-string/) :lock: | Hard | 7/10 | 34.6% | [ ] |
| 1192 | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | 8/10 | 59.6% | [ ] |
| 2360 | [Longest Cycle in a Graph](https://leetcode.com/problems/longest-cycle-in-a-graph/) | Hard | 8/10 | 50.6% | [ ] |
| 2876 | [Count Visited Nodes in a Directed Graph](https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/) | Hard | 8/10 | 30.7% | [ ] |
| 2127 | [Maximum Employees to Be Invited to a Meeting](https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/) | Hard | 9/10 | 61.8% | [ ] |

## minimum_spanning_tree

**What it is** — A Minimum Spanning Tree (MST) connects all nodes of a weighted undirected graph with exactly V-1 edges such that the total edge weight is minimized. Recognize this pattern when a problem asks for the minimum cost to connect all nodes, or involves choosing a subset of edges to form a connected structure with minimum total weight. The two canonical algorithms are Kruskal's (sort edges, use Union-Find) and Prim's (greedy expansion with a priority queue).

**Common steps**
1. Collect all edges with their weights; for implicit graphs (e.g., points in a plane), generate all possible edges first.
2. **Kruskal's**: Sort edges by weight ascending. Use a Union-Find structure. Iterate through edges — for each edge (u, v, w), if u and v are in different components, union them and add w to the MST cost. Stop when V-1 edges are added.
3. **Prim's**: Start from any node. Use a min-heap seeded with all edges from the start node. Greedily pick the cheapest edge that connects an unvisited node; add it to the MST and push its neighbors onto the heap.
4. Track the total cost accumulated and the number of edges (or nodes) added to verify full connectivity.
5. Return the total MST weight, or -1 if the graph is disconnected.

**Key variations**
- Standard MST cost vs. identifying which specific edges are in the MST (critical vs. pseudo-critical edges).
- Virtual node trick: model a "free" operation (e.g., drilling a well) as a virtual node with edges to all real nodes, then run MST on the augmented graph.
- Maximum spanning tree: negate weights or sort in descending order.
- Determining which edges are critical (removing them increases MST cost) vs. pseudo-critical (they can appear in some but not all MSTs).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | 5/10 | 70.8% | [ ] |
| 1135 | [Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) :lock: | Medium | 5/10 | 63.5% | [ ] |
| 1168 | [Optimize Water Distribution in a Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) :lock: | Hard | 7/10 | 65.6% | [ ] |
| 1489 | [Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) | Hard | 9/10 | 66.5% | [ ] |
| 3710 | [Maximum Partition Factor](https://leetcode.com/problems/maximum-partition-factor/) | Hard | 9/10 | 31.6% | [ ] |

## bipartite

**What it is** — A bipartite graph is one whose nodes can be split into two groups such that every edge connects a node from one group to a node in the other — equivalently, the graph has no odd-length cycles. You recognize this pattern when a problem involves matching (assigning items from one set to items from another), checking 2-colorability, or maximizing a pairing subject to constraints. BFS/DFS 2-coloring is used to verify bipartiteness; harder problems apply maximum bipartite matching algorithms (e.g., Hungarian algorithm, Hopcroft-Karp).

**Common steps**
1. Build an adjacency list from the given edges or constraints.
2. Initialize a `color` array (e.g., -1 = uncolored, 0 = group A, 1 = group B).
3. For each uncolored node, assign it color 0 and launch a BFS/DFS.
4. For each neighbor, if uncolored assign the opposite color and enqueue/recurse; if already colored and matches the current node's color, the graph is NOT bipartite — return false.
5. If 2-coloring succeeds for all components, the graph is bipartite.
6. For matching problems, apply maximum bipartite matching on top of the validated bipartite structure (augmenting paths via DFS, or use a standard matching library).

**Key variations**
- Pure bipartite check (is it 2-colorable?) vs. maximum matching (how many pairs can be matched?).
- Minimum vertex cover / maximum independent set (related via König's theorem).
- Assigning tasks to workers with minimum cost — can use Hungarian algorithm or min-cost max-flow.
- Problems where bipartiteness is not given but must be inferred from the constraint structure.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 785 | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | Medium | 5/10 | 59.2% | [ ] |
| 886 | [Possible Bipartition](https://leetcode.com/problems/possible-bipartition/) | Medium | 5/10 | 52.6% | [ ] |
| 1820 | [Maximum Number of Accepted Invitations](https://leetcode.com/problems/maximum-number-of-accepted-invitations/) :lock: | Medium | 6/10 | 52.6% | [ ] |
| 2493 | [Divide Nodes Into the Maximum Number of Groups](https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/) | Hard | 9/10 | 66.9% | [ ] |
| 3385 | [Minimum Time to Break Locks II](https://leetcode.com/problems/minimum-time-to-break-locks-ii/) :lock: | Hard | 9/10 | 45.1% | [ ] |
| 2123 | [Minimum Operations to Remove Adjacent Ones in Matrix](https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/) :lock: | Hard | 9/10 | 43.1% | [ ] |

## euler_path

**What it is** — An Eulerian path visits every edge in a graph exactly once; an Eulerian circuit does the same and returns to the starting node. You recognize this pattern when a problem requires using every connection/relationship exactly once, or when it involves constructing a sequence where consecutive elements share a property (like a de Bruijn sequence). Hierholzer's algorithm finds an Eulerian circuit/path in O(E) time.

**Common steps**
1. Model the problem as a directed or undirected graph where edges represent the items that must each be used exactly once.
2. Check Eulerian path/circuit conditions: for directed graphs, an Eulerian circuit requires every node to have equal in-degree and out-degree; an Eulerian path requires exactly one node with out-degree - in-degree = 1 (start) and one with in-degree - out-degree = 1 (end), with all others balanced.
3. Choose the starting node: for a circuit, any node with edges; for a path, the node with the surplus out-degree.
4. Run Hierholzer's algorithm: use a stack, follow edges greedily (removing used edges), and push a node to the result only when it has no remaining edges.
5. Reverse the result (since nodes are added in post-order) to get the final path/circuit.
6. Verify the result length equals E + 1 (number of edges + 1); if shorter, the graph was not connected or conditions were not met.

**Key variations**
- Directed Eulerian path/circuit vs. undirected (degree conditions differ).
- Lexicographically smallest path — use a sorted adjacency list (min-heap or sorted list) so you always pick the smallest next node.
- De Bruijn sequence construction — model k-length substrings as edges between (k-1)-length nodes, then find an Eulerian circuit.
- Existence check only vs. constructing the actual path.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2097 | [Valid Arrangement of Pairs](https://leetcode.com/problems/valid-arrangement-of-pairs/) | Hard | 8/10 | 66.6% | [ ] |
| 332 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard | 8/10 | 44.5% | [ ] |
| 753 | [Cracking the Safe](https://leetcode.com/problems/cracking-the-safe/) | Hard | 9/10 | 58.4% | [ ] |
