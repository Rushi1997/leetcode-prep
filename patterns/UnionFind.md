# UnionFind

51 problems across 11 patterns.

## connected_components_basic

**What it is** — Union-Find (Disjoint Set Union) groups nodes into components by repeatedly merging sets that share an edge, and answers "are these two nodes connected?" in nearly O(1) with path compression and union by rank. Recognize it when a problem involves undirected graph connectivity, grouping, or counting distinct components.

**Common steps**
1. Initialize a `parent` array where `parent[i] = i` and a `rank` (or `size`) array of all ones.
2. Implement `find(x)` with path compression: if `parent[x] != x`, set `parent[x] = find(parent[x])` and return it.
3. Implement `union(x, y)`: find roots of both; if different, attach the smaller-rank tree under the larger-rank root and decrement the component count.
4. Process all edges by calling `union` on each pair.
5. Answer connectivity queries with `find(x) == find(y)`, and read the component count from your counter.

**Key variations**
- Count components (initialize counter = n, decrement on each successful union)
- Find the earliest time all nodes are connected (process edges sorted by time)
- Detect whether a graph is a valid tree (n-1 edges, no cycle: a union fails if nodes already share a root)

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 323 | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) :lock: | Medium | 2/10 | 64.9% | [ ] |
| 2782 | [Number of Unique Categories](https://leetcode.com/problems/number-of-unique-categories/) :lock: | Medium | 3/10 | 83.7% | [ ] |
| 547 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | 3/10 | 70.3% | [x] |
| 1101 | [The Earliest Moment When Everyone Become Friends](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/) :lock: | Medium | 3/10 | 66.0% | [ ] |
| 261 | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) :lock: | Medium | 3/10 | 50.0% | [ ] |
| 1319 | [Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | Medium | 4/10 | 66.5% | [ ] |
| 947 | [Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Medium | 4/10 | 62.9% | [ ] |
| 2492 | [Minimum Score of a Path Between Two Cities](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/) | Medium | 4/10 | 58.8% | [ ] |
| 3532 | [Path Existence Queries in a Graph I](https://leetcode.com/problems/path-existence-queries-in-a-graph-i/) | Medium | 4/10 | 55.4% | [ ] |
| 3493 | [Properties Graph](https://leetcode.com/problems/properties-graph/) | Medium | 4/10 | 48.8% | [ ] |
| 839 | [Similar String Groups](https://leetcode.com/problems/similar-string-groups/) | Hard | 6/10 | 56.3% | [ ] |
| 765 | [Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/) | Hard | 7/10 | 59.3% | [ ] |

## component_merging_with_auxiliary_map

**What it is** — When nodes are identified by non-integer keys (characters, strings, account emails), you use a hash map to assign each unique key an integer ID on first encounter, then apply standard Union-Find on those IDs. Recognize it when entities to merge are named (not already indexed 0..n-1) or when merging must respect an ordering within each component (e.g., lexicographic minimum).

**Common steps**
1. Build a map from each unique key (character, email, string) to a unique integer ID.
2. Initialize Union-Find on the integer IDs.
3. For each merging rule, look up both keys in the map and union their IDs.
4. Group all keys by their root ID using a second pass.
5. For each group, apply the required within-component operation (sort, pick minimum, generate combinations).

**Key variations**
- Lexicographically smallest equivalent (always union to the smaller character's root)
- Accounts merge (group emails by root, sort within each group, prepend account name)
- Smallest string by swaps (sort characters within each component and reassign by sorted order)
- Bit-mask merging for string groups (union by single-bit differences in character sets)

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1061 | [Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/) | Medium | 4/10 | 81.2% | [ ] |
| 737 | [Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/) :lock: | Medium | 4/10 | 51.3% | [ ] |
| 1722 | [Minimize Hamming Distance After Swap Operations](https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/) | Medium | 5/10 | 69.6% | [ ] |
| 721 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | 5/10 | 61.3% | [ ] |
| 1202 | [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/) | Medium | 5/10 | 60.6% | [ ] |
| 2948 | [Make Lexicographically Smallest Array by Swapping Elements](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/) | Medium | 5/10 | 60.3% | [ ] |
| 1258 | [Synonymous Sentences](https://leetcode.com/problems/synonymous-sentences/) :lock: | Medium | 5/10 | 57.3% | [ ] |
| 2157 | [Groups of Strings](https://leetcode.com/problems/groups-of-strings/) | Hard | 9/10 | 27.7% | [ ] |

## connected_components_with_analysis

**What it is** — Beyond simply counting components, this pattern requires reasoning about the sizes of components or the impact of removing/adding specific nodes. Recognize it when a problem asks which node to remove to minimize spread, maximize a score, or compute the number of unreachable pairs between components.

**Common steps**
1. Build components using standard Union-Find, storing component sizes.
2. Identify nodes with special roles (e.g., initially infected nodes, special nodes).
3. For each candidate operation (removing a node, making an addition), simulate the effect on component structure.
4. Compute the target metric using component sizes (e.g., unreachable pairs = sum over components of size_i * remaining_total, or spread = size of component containing the removed node).
5. Select the optimal candidate based on the metric.

**Key variations**
- Count unreachable pairs: for each component of size s, add s * (total_remaining - s) / 2
- Minimize malware spread: find the infected node whose component contains only that one infected node and is largest
- Maximize alternating sum: exploit component structure to greedily assign values

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2316 | [Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) | Medium | 4/10 | 49.9% | [ ] |
| 924 | [Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/) | Hard | 6/10 | 43.2% | [ ] |
| 3695 | [Maximize Alternating Sum Using Swaps](https://leetcode.com/problems/maximize-alternating-sum-using-swaps/) | Hard | 7/10 | 64.5% | [ ] |
| 928 | [Minimize Malware Spread II](https://leetcode.com/problems/minimize-malware-spread-ii/) | Hard | 7/10 | 45.6% | [ ] |

## cycle_detection_and_redundant_edge

**What it is** — Union-Find detects cycles in an undirected graph by checking, before each union, whether the two endpoints are already in the same component — if they are, the edge is redundant and creates a cycle. Recognize this pattern when asked to find the edge that causes a cycle or to remove edges to maintain full connectivity.

**Common steps**
1. Initialize Union-Find for all nodes.
2. Process edges one by one (in input order, or sorted by some criterion).
3. For each edge (u, v): call `find(u)` and `find(v)`.
4. If they share the same root, this edge is the redundant/cycle-forming edge — record it.
5. Otherwise, union them and continue.
6. For directed graphs (Redundant Connection II), first check for in-degree violations, then apply Union-Find to the remaining candidate edges.

**Key variations**
- Undirected graph: last edge that causes a cycle is the answer
- Directed graph: handle nodes with in-degree 2 separately, then detect cycle in the remaining graph
- Edge removal to keep both of two spanning trees (process edges by type, track two separate DSUs)

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | 4/10 | 67.6% | [ ] |
| 1579 | [Remove Max Number of Edges to Keep Graph Fully Traversable](https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/) | Hard | 7/10 | 70.2% | [ ] |
| 685 | [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) | Hard | 8/10 | 36.1% | [ ] |

## union_find_with_size_tracking

**What it is** — This variant augments each Union-Find component with a size counter, enabling O(1) lookup of how many nodes are in any component after path compression. Recognize it when the problem's answer depends on the size of the component a node belongs to, especially after dynamic merging.

**Common steps**
1. Initialize `size[i] = 1` for all nodes alongside the standard `parent` array.
2. In `union(x, y)`: after finding roots, if they differ, merge the smaller-size root under the larger, and add the smaller's size to the larger root's size counter.
3. After all merges, answer queries by looking up `size[find(node)]`.
4. For problems requiring a specific size at a specific time, track the size history or process events in the right order.

**Key variations**
- Find the latest step at which a component of exactly size m exists (track sizes over time)
- Count good paths: merge nodes sorted by value, counting pairs within the same component that share the maximum value

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1562 | [Find Latest Group of Size M](https://leetcode.com/problems/find-latest-group-of-size-m/) | Medium | 6/10 | 43.8% | [ ] |
| 2421 | [Number of Good Paths](https://leetcode.com/problems/number-of-good-paths/) | Hard | 7/10 | 56.3% | [ ] |

## number_theory_union_find

**What it is** — Number theory Union-Find builds a graph where nodes share an edge if they have a common factor (GCD > 1, share a prime factor, or share a divisor above a threshold), then uses Union-Find to determine connectivity or component properties. Recognize it when a problem connects numbers by divisibility or GCD relationships and asks about reachability or grouping.

**Common steps**
1. For each number, factorize it (trial division up to sqrt, or sieve up to max value).
2. Create a virtual node for each prime factor; union each number's node with its prime factor nodes.
3. Two numbers are connected if and only if they share at least one prime factor (same component after unioning through shared primes).
4. Answer connectivity queries with `find(u) == find(v)`.
5. For threshold-based problems, use a sieve to enumerate multiples of each value above the threshold and union them.

**Key variations**
- GCD sort: union numbers that share a GCD > 1, then check if target sorted order is achievable within components
- Graph connectivity with threshold: for each value v > threshold, union all multiples of v
- Largest component by common factor: find the component with the most original (non-prime) nodes

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1998 | [GCD Sort of an Array](https://leetcode.com/problems/gcd-sort-of-an-array/) | Hard | 7/10 | 49.9% | [ ] |
| 1627 | [Graph Connectivity With Threshold](https://leetcode.com/problems/graph-connectivity-with-threshold/) | Hard | 7/10 | 49.4% | [ ] |
| 952 | [Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/) | Hard | 7/10 | 42.9% | [ ] |
| 2709 | [Greatest Common Divisor Traversal](https://leetcode.com/problems/greatest-common-divisor-traversal/) | Hard | 7/10 | 41.8% | [ ] |
| 3378 | [Count Connected Components in LCM Graph](https://leetcode.com/problems/count-connected-components-in-lcm-graph/) | Hard | 8/10 | 31.0% | [ ] |

## constraint_satisfaction_union_find

**What it is** — Constraint satisfaction Union-Find encodes equality constraints as union operations and inequality constraints as checks, then verifies whether all constraints can be simultaneously satisfied. Recognize it when a problem gives you a list of `==` and `!=` (or similar) relationships between variables and asks if they are consistent.

**Common steps**
1. Process all equality constraints first: for each `a == b`, union their nodes.
2. Process all inequality constraints second: for each `a != b`, check if `find(a) == find(b)`.
3. If any inequality constraint finds both sides in the same component, the constraints are unsatisfiable — return false/invalid.
4. For construction problems, build the structure while checking that constraints are not violated.

**Key variations**
- Equation satisfiability: union `==` pairs, then check `!=` pairs
- Restricted friend requests: maintain a separate "enemy" tracking alongside the DSU
- Matrix rank assignment: use DSU to group cells that must share a rank, then assign ranks by component
- LCP string construction: union positions that must be equal, then verify consistency

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 990 | [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | Medium | 4/10 | 51.8% | [ ] |
| 2076 | [Process Restricted Friend Requests](https://leetcode.com/problems/process-restricted-friend-requests/) | Hard | 7/10 | 60.3% | [ ] |
| 2573 | [Find the String with LCP](https://leetcode.com/problems/find-the-string-with-lcp/) | Hard | 9/10 | 63.2% | [ ] |
| 1632 | [Rank Transform of a Matrix](https://leetcode.com/problems/rank-transform-of-a-matrix/) | Hard | 9/10 | 42.2% | [ ] |

## grid_region_union_find

**What it is** — Grid region Union-Find maps 2D grid cells (or subdivisions of cells) to 1D indices and applies Union-Find to group adjacent cells into connected regions. Recognize it when a 2D grid has connectivity defined by adjacency rules that are non-standard (e.g., diagonal slashes, circular adjacency) or when you need to count distinct enclosed regions.

**Common steps**
1. Map each cell (r, c) to a 1D index: `r * cols + c` (or `r * cols * k + c * k + subdivision` for split cells).
2. Initialize Union-Find over all 1D indices, plus a virtual "outside" node if needed.
3. For each cell, apply the connectivity rule to determine which neighboring indices to union.
4. After processing all cells, count distinct components (excluding the virtual outside node if used).
5. Answer queries by checking `find(cell_a) == find(cell_b)`.

**Key variations**
- Slash/backslash grid: split each cell into 4 triangles, union triangles within a cell and across cell boundaries based on the slash direction
- Rectangle corner reachability: union circles that touch or overlap, then check if any circle connects the top-left boundary to the bottom-right boundary
- Grid with activation: union newly activated cells with their active neighbors and track max component size

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 959 | [Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/) | Medium | 5/10 | 77.5% | [ ] |
| 3873 | [Maximum Points Activated with One Addition](https://leetcode.com/problems/maximum-points-activated-with-one-addition/) | Hard | 8/10 | 43.8% | [ ] |
| 3235 | [Check if the Rectangle Corner Is Reachable](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/) | Hard | 9/10 | 25.2% | [ ] |

## weighted_union_find

**What it is** — Weighted Union-Find stores a value (weight, ratio, XOR distance) on each edge from a node to its parent, so that `find` not only returns the root but also computes the cumulative weight along the path. Recognize it when a problem has ratio or difference constraints between elements that can be composed transitively (e.g., if a/b = 2 and b/c = 3, then a/c = 6).

**Common steps**
1. Add a `weight` array alongside `parent`; initialize `weight[i] = identity_value` (0 for XOR/additive, 1 for multiplicative).
2. In `find(x)` with path compression: compute the cumulative weight to the root by composing weights along the path, and update `weight[x]` to be the direct weight to the root.
3. In `union(x, y, w)` (meaning the relationship between x and y has weight w): find both roots and their weights, then set the parent and compute the correct weight for the new root edge using the constraint equation.
4. To query the relationship between two nodes: if they share a root, compute `weight[x] OP weight[y]^{-1}` (or the equivalent).

**Key variations**
- XOR-weighted DSU: weight[x] = XOR distance from x to its root; union by XOR composition
- Ratio/division weighted DSU: weight[x] = ratio of x's value to root's value
- Minimum cost walk: union components and track the AND of all edge weights in the component

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3108 | [Minimum Cost Walk in Weighted Graph](https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/) | Hard | 6/10 | 68.2% | [ ] |
| 3887 | [Incremental Even-Weighted Cycle Queries](https://leetcode.com/problems/incremental-even-weighted-cycle-queries/) | Hard | 8/10 | 51.4% | [ ] |
| 2307 | [Check for Contradictions in Equations](https://leetcode.com/problems/check-for-contradictions-in-equations/) :lock: | Hard | 8/10 | 43.9% | [ ] |

## dynamic_connectivity_online

**What it is** — Dynamic connectivity handles graphs where edges or nodes are added one at a time (online), and after each addition you must answer a connectivity query or update a running answer. Recognize it when nodes "activate" incrementally and you need a running count of components or connected pairs after each activation.

**Common steps**
1. Initialize Union-Find with all nodes inactive; maintain a count of active components.
2. When activating a node or adding an edge: first add the node/edge to the DSU.
3. Check all neighbors: for each already-active neighbor, attempt to union; each successful union decrements the active component count.
4. Record or output the component count after each operation.
5. For "secret sharing" variants: after each time step, reset temporary merges (rollback DSU) or process in rounds.

**Key variations**
- Number of islands II: activate grid cells one by one, union with active neighbors, track component count
- Secret propagation in rounds: within each meeting round, temporarily merge attendees; at round end, rollback non-secret-holder merges

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 305 | [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) :lock: | Hard | 7/10 | 40.6% | [ ] |
| 2092 | [Find All People With Secret](https://leetcode.com/problems/find-all-people-with-secret/) | Hard | 8/10 | 48.4% | [ ] |

## offline_reverse_union_find

**What it is** — Offline reverse Union-Find processes deletion queries by reversing them: since DSU supports union but not split, you process queries in reverse order (treating deletions as additions), build up the DSU, and then answer queries in reverse. Recognize it when a problem asks for connectivity or component properties after a sequence of removals, and all queries are known in advance.

**Common steps**
1. Read all queries offline; identify the final state after all deletions.
2. Initialize Union-Find with only the nodes/edges present after all deletions.
3. Process deletion queries in reverse order (i.e., add back the deleted element).
4. After each "un-deletion," union the restored element with its neighbors and record the current state (component count, max segment sum, etc.).
5. Reverse your recorded answers to match the original query order.

**Key variations**
- Path existence with edge length limit: sort queries and edges by limit, sweep with offline DSU
- Maximum segment sum after removals: reverse to additions, track component sums with DSU size tracking
- Bricks falling: process brick removals in reverse as additions, track which bricks become connected to the top row

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3607 | [Power Grid Maintenance](https://leetcode.com/problems/power-grid-maintenance/) | Medium | 6/10 | 56.2% | [ ] |
| 1697 | [Checking Existence of Edge Length Limited Paths](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/) | Hard | 7/10 | 63.3% | [ ] |
| 2382 | [Maximum Segment Sum After Removals](https://leetcode.com/problems/maximum-segment-sum-after-removals/) | Hard | 7/10 | 49.6% | [ ] |
| 1724 | [Checking Existence of Edge Length Limited Paths II](https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/) :lock: | Hard | 9/10 | 51.5% | [ ] |
| 803 | [Bricks Falling When Hit](https://leetcode.com/problems/bricks-falling-when-hit/) | Hard | 9/10 | 37.2% | [ ] |
