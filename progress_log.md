# Progress Log

Daily journal of problems solved, learnings, and next steps.

---

## 2026-05-06 — Day 1

**Problems solved: 3**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| 1 | Two Sum (#1) | Hashing | two_sum_pair | 2/10 |
| 2 | Contains Duplicate (#217) | Hashing | set_lookup | 1/10 |
| 3 | Fair Candy Swap (#888) | Hashing | two_sum_pair | 3/10 |

**Python learned:**
- `for i in range(len(nums))` vs `for i, num in enumerate(nums)` vs `for num in nums`
- Dict: `d[key] = value` is assignment, `d[key, value]` is a tuple lookup — NOT the same
- `if key in d` for O(1) existence check, `d.get(key)` vs `d[key]`
- `set.add(item)` not `set(item)`; `tuple(sorted([a, b]))` for hashable sorted pairs
- `sum()` not `Sum()`, `sorted([...])` not `sorted[...]` — built-ins are lowercase, use parens
- `//` for integer division, `/` gives floats
- Don't shadow built-in names like `map`

**Patterns learned:**
- Complement lookup: instead of O(n^2) nested loops, store seen values in a map and check if complement exists — O(n)
- The complement formula changes per problem (sum vs difference vs derived equation) — always derive from math first
- Set lookup: simplest hash pattern, just "have I seen this before?"
- Always store current element every iteration, not conditionally in an else branch

**Common bugs made:**
- Returning True/False backwards (Contains Duplicate)
- Wrong variable name (`map` vs `myMap`)
- Wrong complement formula (addition vs subtraction)
- `sorted[...]` instead of `sorted([...])`

---

## 2026-05-07 — Day 2

**Problems solved: 8**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| 4 | K-diff Pairs (#532) | Hashing | two_sum_pair | 4/10 |
| 5 | Valid Anagram (#242) | Hashing | frequency_counting | 2/10 |
| 6 | Ransom Note (#383) | Hashing | frequency_counting | 1/10 |
| 7 | Group Anagrams (#49) | Hashing | grouping_by_key | 4/10 |
| 8 | Valid Palindrome (#125) | TwoPointers | palindrome_check | 2/10 |
| 9 | Reverse String (#344) | TwoPointers | in_place_array_modification | 1/10 |
| 10 | Valid Parentheses (#20) | Stack | bracket_matching | 2/10 |
| 11 | Two Sum II (#167) | TwoPointers | opposite_ends_pair_sum | 3/10 |

**Python learned:**
- Strings are iterable just like arrays — `for char in s` works
- `c.isalnum()`, `c.lower()`, `c.isalpha()`, `c.isdigit()` — character methods, called on the char, no arguments
- `"".join(sorted(string))` — sort a string (sorted gives list, join makes it a string again)
- `s[l], s[r] = s[r], s[l]` — Python swap without temp variable
- `d.get(key, default)` — e.g., `d.get(c, 0) + 1` for counting
- `list(d.values())` — dict views aren't lists, wrap with `list()` when returning
- Stack in Python: `list` with `append()` (push), `pop()`, `[-1]` (peek)

**Patterns learned:**
- Difference complement needs BOTH directions (`num - k` AND `num + k`), unlike sum which only needs one — use two `if` statements, not `elif`
- Frequency counting: build map with `d[c] = d.get(c, 0) + 1`, decrement to validate
- Anagram = exact match (check map empty), Ransom Note = subset (don't check map empty)
- Grouping by key: sort string → use as dict key → collect values with `list(d.values())`
- Same problem, different constraints → different technique: Two Sum unsorted = hashmap, sorted = two pointers
- When input is sorted, two pointers often replaces a hashmap (O(1) space vs O(n))
- Stack bracket matching: map closing → opening, push opens, check top on close, verify empty at end
- Check `len(stack) > 0` before accessing `stack[-1]`

**Common bugs made:**
- `elif` vs two `if` statements — `elif` skips second check even when both could be true
- Typo in map values (`}` → `}` instead of `}` → `{`)
- Comparing wrong things (`i == st[-1]` vs `myMap[i] == st[-1]`)

---

## 2026-05-08 — Day 3

**Problems solved: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 12 | Move Zeroes (#283) | TwoPointers | partition | 2/10 | YES — redo later |

**Patterns learned:**
- Partition pattern: slow pointer (`r`) = write position, fast pointer (`l`) = scanner
- When fast finds a qualifying element, swap with slow position, advance slow
- The invariant: everything before `r` is processed, `r` is always on the next write spot — no need to search for it
- Don't add unnecessary conditions (`l != r`) — swapping same position is harmless, and skipping it breaks the logic
- Trust the invariant instead of trying to verify it with extra checks

**Mistakes to remember:**
- `nums[l] != 0` checks the VALUE, `l != 0` checks the INDEX — got these confused
- Kept adding unnecessary guards (`l != r`, inner search loops, helper functions) instead of keeping it simple
- Overcomplicating = sign of not trusting the invariant

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 13 | Sort Colors (#75) | TwoPointers | partition | 4/10 | |

**Patterns learned:**
- Dutch National Flag algorithm (Sort Colors #75): 3-way partition with three pointers — low, mid, high
- Swap with left → safe to advance scanner (value came from processed side)
- Swap with right → DON'T advance scanner (value is unprocessed)
- `<=` not `<` in the while condition — need to process the element where pointers meet

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 14 | Remove Duplicates from Sorted Array (#26) | TwoPointers | in_place_array_modification | 2/10 | |
| 15 | Binary Search (#704) | BinarySearch | classic_binary_search | 1/10 | |

**Patterns learned:**
- Remove duplicates: slow pointer = write position for next unique, fast scans — same partition template
- Binary search template: `while l <= r`, `m = (l + r) // 2`, move `l` or `r` based on comparison
- `//` not `/` for mid calculation — need integer index

---

## 2026-05-09 — Day 4

**Problems solved: 6**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 16 | Reverse Linked List (#206) | LinkedList | reversal | 1/10 | |
| 17 | Middle of the Linked List (#876) | LinkedList | fast_slow_pointers | 1/10 | |
| 18 | Linked List Cycle (#141) | LinkedList | fast_slow_pointers | 2/10 | |

**Python learned:**
- `None` not `null` in Python
- ListNode has `.val` and `.next`
- Save `.next` before overwriting it or you lose the rest of the list

**Patterns learned:**
- Linked list reversal template: `pr=None, cu=head`, each iteration: save next → reverse link → move forward → return `pr`
- Fast/slow pointers: `while fast and fast.next` — handles both odd and even length
- Middle of list: slow lands on the middle when fast reaches the end
- Cycle detection: same setup, but check if slow meets fast. Move FIRST, then compare — they start at the same place
- Minimum work per iteration: don't try to handle two nodes in one loop, trust the next iteration

**Common bugs made:**
- `==` vs `!=` in while condition — loop never executed
- Checking slow == fast before moving — always true on first iteration since both start at head

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 19 | Merge Two Sorted Lists (#21) | LinkedList | merge_lists | 2/10 | YES — redo later |
| 20 | Search Insert Position (#35) | BinarySearch | classic_binary_search | 1/10 | |
| 21 | Best Time to Buy and Sell Stock (#121) | Greedy | stock_trading | 2/10 | |

**Python learned:**
- `float('inf')` and `float('-inf')` for infinity — no integer infinity in Python
- `min(a, b)` and `max(a, b)` built-in functions

**Patterns learned:**
- Greedy stock trading: track min price so far, check if selling today beats best profit — one pass O(n)
- Initialize running min/max with first element or `float('inf')`/`float('-inf')`

---

## 2026-05-10 — Day 5

**Problems solved: 3**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 22 | Maximum Average Subarray I (#643) | SlidingWindow | fixed_window | 1/10 | |
| 23 | Minimum Size Subarray Sum (#209) | SlidingWindow | variable_window | 3/10 | |
| 24 | Longest Substring Without Repeating Characters (#3) | SlidingWindow | variable_window_unique_elements | 4/10 | |

**Python learned:**
- `for i in range(k, len(nums))` — start a for loop from an offset
- Prefer integer math inside loops, transform (e.g. divide) once at the end
- Python ternary: `value_if_true if condition else value_if_false` — no `? :` syntax

**Patterns learned:**
- Fixed-size sliding window: compute first window sum, then slide by adding right and subtracting left
- `currentVal = currentVal + nums[i] - nums[i-k]` — the slide step
- Do minimum work per iteration — avoid dividing every step when you can divide once at the end
- Variable-size sliding window: expand right, shrink left while condition holds
- Use `l <= r` not `l < r` when a single-element window can be valid
- Initialize min tracking with `float('inf')`, return 0 if unchanged
- Variable window + set: use a set to track what's in the current window, shrink until duplicate is removed
- `not in` works for sets just like dicts
- Structure loops so add/advance/update happen once per iteration, put shrinking in a separate `if` block

---

## 2026-05-11 — Day 6

**Problems solved: 3**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Move Zeroes (#283) | TwoPointers | partition | — | review done |
| 25 | Permutation in String (#567) | SlidingWindow | variable_window_unique_elements | 3/10 | |
| 26 | Implement Queue using Stacks (#232) | Design | stack_as_queue | 2/10 | |
| 27 | Maximum Depth of Binary Tree (#104) | Trees | dfs_traversal | 1/10 | |

**Python learned:**
- `.get(key, 0)` not `.getOrDefault(key, 0)` — that's Java
- `for key, value in d.items()` — iterate dict with keys and values
- `del d[key]` — remove key from dict (needed when count reaches 0 for dict equality)
- `Counter(s)` from `collections` — builds frequency map in one line
- Dict equality `d1 == d2` checks all keys and values match
- `self.varName` in `__init__` for instance variables — without `self.` they're local and disappear
- `len(x) > 0` not `len(x > 0)` — parentheses matter
- `not stack` or `len(stack) == 0` to check empty — no built-in `empty()`

**Patterns learned:**
- Fixed window + frequency map: slide window of size `len(s1)`, compare frequency maps at each position
- Add new char, remove leftmost char, delete key if count hits 0 (so `==` comparison works)
- Always check `len(s1) > len(s2)` early — window can't be bigger than the string
- Queue from two stacks: push to st1, pop/peek from st2 — only transfer when st2 is empty
- Popping from one stack into another reverses the order (LIFO → FIFO)
- DFS recursive tree traversal: base case `node == None → return 0`, recurse on left and right
- `maxDepth = 1 + max(left, right)` — the recursive formula for tree depth
- Three ways to write recursive helpers: reuse the method itself, inner function (no `self`), or parallel method (`self` needed)
- BFS uses `collections.deque` — `popleft()` is O(1) vs `list.pop(0)` is O(n)

---

## 2026-05-12 — Day 7

**Problems solved: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Merge Two Sorted Lists (#21) | LinkedList | merge_lists | — | review done |
| 28 | Same Tree (#100) | Trees | dfs_traversal | 2/10 | YES — redo later |

**Patterns learned:**
- Same Tree: check both None → True, one None → False, vals not equal → False, then recurse both children
- `p.val == q.val` not `p.val and q.val` — the latter checks truthiness (0 would fail)
- Merge sorted lists optimization: attach leftover tail directly (`current.next = list1 or list2`)

---

## 2026-05-13 — Day 8

**Problems solved: 4**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| — | Maximum Depth of Binary Tree (#104) | Trees | dfs_traversal | — | BFS version done |
| 29 | Invert Binary Tree (#226) | Trees | tree_modification | 2/10 | |
| 30 | Path Sum (#112) | Trees | path_sum | 2/10 | YES — redo cleaner |
| 31 | Search in a Binary Search Tree (#700) | Trees | bst_operations | 1/10 | |
| 32 | Average of Levels in Binary Tree (#637) | Trees | bfs_level_order | 2/10 | |

**Patterns learned:**
- BFS level-order template: `while q` → `for _ in range(len(q))` → `popleft()` → add children
- `len(q)` captured at start of for loop — new children wait for next level
- `popleft()` for FIFO (queue), `pop()` for LIFO (stack)
- Invert tree: swap children then recurse — same base case pattern as other tree problems
- Path sum: subtract current val from target going down, check `val == remaining` at leaf — cleaner than tracking a running total
- Leaf node = `node.left is None and node.right is None`
- BST property: left < root < right — only search one side, like binary search on a sorted array
- BFS level-order to compute per-level stats: save `count = len(q)` before the inner loop, use it for average
- Don't shadow built-in names like `sum` — use `level_sum` or `total`

---

## 2026-05-14 — Day 9

**Problems solved: 3**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 33 | Symmetric Tree (#101) | Trees | dfs_traversal | 2/10 | YES — redo later |
| 34 | Subtree of Another Tree (#572) | Trees | dfs_traversal | 5/10 | |
| 35 | Lowest Common Ancestor of a BST (#235) | Trees | lowest_common_ancestor | 4/10 | |

**Patterns learned:**
- Symmetric tree = Same Tree but mirrored: compare `left.left` with `right.right` and `left.right` with `right.left`
- Helper function takes two nodes — same base cases as Same Tree
- Don't forget the value check along with structure checks
- Subtree check = DFS through main tree + isSameTree at each matching node
- Reuse helper functions (isSameTree) across problems — composing simple functions beats writing complex ones
- LCA in BST: both smaller → go left, both larger → go right, otherwise you're at the split point → return root
- The split point catches all cases: one left one right, or one equals root
- Python chained comparisons: `a <= b <= c` works

---

## 2026-05-15 — Day 10

**Problems solved: 3**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Same Tree (#100) | Trees | dfs_traversal | — | review done, retry 05-19 |
| 36 | Binary Tree Level Order Traversal (#102) | Trees | bfs_level_order | 3/10 | |
| 37 | Next Greater Element I (#496) | Stack | monotonic_stack | 2/10 | |
| 38 | Daily Temperatures (#739) | Stack | monotonic_stack | 4/10 | YES — redo later |

**Patterns learned:**
- Level order traversal: same BFS template, collect each level into a sublist
- `p is None or q is None` not `and` — a node can't be both None and not None
- Monotonic stack: stack holds elements waiting for their next greater element
- When a bigger number arrives, pop and resolve everything smaller on the stack
- Store results in a dict, look up at the end — missing keys default to -1
- Daily Temperatures variant: push `(value, index)` tuples, answer is `current_index - popped_index`
- Put the pop condition in the `while` or use `else: break` — don't pop unconditionally

---

## 2026-05-16 — Day 11

**Problems solved: 0**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Path Sum (#112) | Trees | path_sum | — | review done, retry 05-21 |

**Patterns learned:**
- Path Sum review: remember to check leaf node (`left == None and right == None`) not just value match

---

## 2026-05-17 — Day 12

**Problems solved: 2**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Symmetric Tree (#101) | Trees | dfs_traversal | — | review done |
| 39 | Flood Fill (#733) | Graphs | grid_traversal | 1/10 | |
| 40 | Number of Islands (#200) | Graphs | grid_traversal | 3/10 | |

**Patterns learned:**
- Grid DFS: check bounds (`< 0` and `> len - 1`) before processing, recurse in 4 directions
- Color change acts as "visited" — no separate set needed when modifying the grid
- Handle `originalColor == newColor` early to avoid infinite recursion
- Four directions: `(row±1, col)` and `(row, col±1)` — direct calls or use a directions list
- Number of Islands: iterate grid, DFS to sink each island, count DFS triggers
- Grid values can be strings (`"1"`) not ints (`1`) — check the problem

---

## 2026-05-18 — Day 13

**Problems solved: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Daily Temperatures (#739) | Stack | monotonic_stack | — | review done, retry 05-24 |
| 41 | Find if Path Exists in Graph (#1971) | Graphs | dfs_connected_components | 2/10 | |

**Python learned:**
- `defaultdict(list)` from `collections` — auto-creates empty list for new keys
- Tuple unpacking in for loop: `for u, v in edges`

**Patterns learned:**
- Adjacency list: dict mapping each node to list of neighbors, add both directions for undirected graphs
- Graph DFS: same as tree DFS but need a visited set to avoid cycles
- Short-circuit: `if self.dfs(...): return True` instead of `found = found or self.dfs(...)` — stops early

---

## 2026-05-21 — Day 14

**Problems solved: 3**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 42 | Clone Graph (#133) | Graphs | graph_traversal | 5/10 | |
| R | Same Tree (#100) | Trees | dfs_traversal | — | review done |
| R | Path Sum (#112) | Trees | path_sum | — | review done, retry 05-28 |
| 43 | Max Area of Island (#695) | Graphs | grid_traversal | 3/10 | |
| 44 | Keys and Rooms (#841) | Graphs | dfs_connected_components | 3/10 | |

**Patterns learned:**
- Clone graph: DFS with a map of `original → clone`, return cloned node
- Store clone in map BEFORE recursing into neighbors — prevents infinite loop on cycles
- Inner functions (closures) can access variables from the outer function without `self`
- Max Area of Island: same as Number of Islands but DFS tracks area via visited set or return count
- Two approaches: visited set with `len(visited)`, or sink cells and return count — both work
- Reachability check: DFS from start, compare `len(visited) == len(total)` at the end
- Avoid class-level variables — shared across test cases on LeetCode, pass state as parameters instead

---

## 2026-05-22 — Day 15

**Problems solved: 5**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 45 | Course Schedule (#207) | Graphs | topological_sort | 5/10 | YES — redo later |
| 46 | Course Schedule II (#210) | Graphs | topological_sort | 5/10 | YES — redo later |
| 47 | Subsets (#78) | Backtracking | subset_enumeration | 4/10 | YES — redo later |
| 48 | Permutations (#46) | Backtracking | permutation_generation | 4/10 | YES — redo later |
| 49 | Combinations (#77) | Backtracking | combination_generation | 4/10 | YES — redo later |

**Patterns learned:**
- Cycle detection in directed graph: DFS with two sets — `visiting` (current path) and `visited` (fully processed)
- `visiting` = backtracking set: add before recursing, remove after — tracks current DFS path
- `visited` = permanent set: once proven safe, never re-check
- If node in `visiting` → cycle. If node in `visited` → skip. Otherwise explore.
- Short-circuit in loops: `if not self.dfs(...): return False` — stop as soon as cycle is found
- `.append()` returns `None` — don't chain it with assignment
- Topological sort via DFS: append course to result at backtrack point (after all prereqs processed)
- Deepest nodes (no dependencies) get added first — order builds naturally
- Pass result list as parameter — lists are by reference, no need to return it
- `.append([x])` appends a list, `.append(x)` appends the value — watch the brackets
- Propagate cycle detection consistently: if recursive call finds cycle, return True (not False)
- Backtracking template: pass `current` and `result` as params, choose → recurse → unchoose
- Base case: `index == len(nums)` → append `current.copy()` to result
- `.copy()` is critical — without it all entries in result point to the same mutating list
- `list.pop()` to unchoose (remove last element)
- Permutations: no index, loop all elements, use a `used` set, one DFS call inside for loop
- Subsets = order doesn't matter → index moves forward, include/skip
- Permutations = order matters → full array, loop + used set
- Key question: "does [1,2] differ from [2,1]?" → yes = permutation, no = subset

---

## 2026-05-23 — Day 16

**Problems solved: 4**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 50 | Letter Combinations of a Phone Number (#17) | Backtracking | combination_generation | 4/10 | |
| 51 | Validate Binary Search Tree (#98) | Trees | bst_operations | 4/10 | YES — redo later |
| 52 | Climbing Stairs (#70) | DynamicProgramming | linear_dp | 1/10 | YES — redo later |
| 53 | Min Cost Climbing Stairs (#746) | DynamicProgramming | linear_dp | 1/10 | YES — redo later |

**Patterns learned:**
- Combinations: forward loop from `start` to `n`, recurse with `i + 1`, base case `len(current) == k`
- Forward loop template handles both subsets and combinations — difference is the base case
- Two backtracking templates: forward loop (subsets/combinations) vs full loop + used set (permutations)
- `"".join(list)` to convert list of chars to string
- `.append(x)` not `.append[x]` — parentheses not brackets
- Check empty input early to avoid appending empty results
- Validate BST: pass (min, max) bounds down the recursion — each node must be within its allowed range
- Go left → update max to current val. Go right → update min to current val
- Checking only immediate children is NOT enough — must validate against the entire ancestor chain
- Use strict inequality (`<=`, `>=`) — BST doesn't allow duplicates
- DP framework: define subproblem (`dp[i]` = what?), base cases, recurrence relation
- Bottom-up DP: set base cases first, then loop fills the rest
- Climbing Stairs: `dp[i] = dp[i-1] + dp[i-2]` — Fibonacci pattern
- Base cases cover everything the recurrence can't compute
- Can use dict or list for DP table — list when keys are sequential integers
- Min cost DP: `dp[i] = cost[i] + min(dp[i-1], dp[i-2])` — add current cost to cheapest way to get here
- When you can reach the top from multiple steps, return `min()` of those options

---

## 2026-05-24 — Day 17

**Problems solved: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Subsets (#78) | Backtracking | subset_enumeration | — | review done, retry 05-28 |
| R | Permutations (#46) | Backtracking | permutation_generation | — | review done, retry 05-28 |
| R | Daily Temperatures (#739) | Stack | monotonic_stack | — | review done |
| 54 | House Robber (#198) | DynamicProgramming | linear_dp | 3/10 | YES — redo later |

**Patterns learned:**
- House Robber: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])` — skip or rob at each step
- When dp[i] already considers dp[i-1], the final answer is just dp[n-1] (no need for max of last two)
- Subsets forward loop: append `current.copy()` at every level, not just base case
- Use `i` from the loop, not `index` from the parameter — common backtracking bug

## 2026-05-25 — Day 18

**Problems solved: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Combinations (#77) | Backtracking | combination_generation | — | review done, retry 05-30 |
| 55 | Coin Change (#322) | DynamicProgramming | knapsack | 4/10 | YES — redo soon |

**Python learned:**
- `float('inf')` as default for minimization DP — any valid answer beats it, and `inf + 1` is still `inf`
- Can use dict or list for DP table — list is simpler when indices are 0..n

**Patterns learned:**
- Coin Change DP: `dp[i] = min(dp[i], dp[i - coin] + 1)` — for each amount, try every coin
- The `+ 1` counts the coin you're using right now; `dp[i - coin]` is the best for the remainder
- Initialize to `float('inf')` = "impossible"; if still inf at end, return -1
- Build table bottom-up from `dp[0] = 0` so smaller subproblems are solved first
- Unbounded knapsack: same coin can be reused (unlike 0/1 knapsack)

---

## 2026-05-26 — Day 19

**Problems solved: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Course Schedule (#207) | Graphs | topological_sort | — | review done, retry 05-30 |
| R | Course Schedule II (#210) | Graphs | topological_sort | — | review done, retry 05-30 |
| R | Validate BST (#98) | Trees | bst_operations | — | review done |
| R | Climbing Stairs (#70) | DynamicProgramming | linear_dp | — | review done, retry 05-30 |
| R | Min Cost Climbing Stairs (#746) | DynamicProgramming | linear_dp | — | review done, retry 05-30 |
| 56 | Maximum Subarray (#53) | DynamicProgramming | linear_dp | 3/10 | YES — redo later |

**Patterns learned:**
- Kadane's algorithm: `dp[i] = max(nums[i], dp[i-1] + nums[i])` — extend or start fresh
- A negative running sum always hurts — start fresh when dp[i-1] < 0
- Answer is `max(dp)`, not `dp[-1]` — best subarray can end anywhere

---

## 2026-05-27 — Day 20

**Problems solved: 4**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 57 | House Robber II (#213) | DynamicProgramming | linear_dp | 4/10 | YES — redo later |
| 58 | Delete and Earn (#740) | DynamicProgramming | linear_dp | 4/10 | YES — redo later |
| 59 | Kth Largest Element in an Array (#215) | Heap | top_k_elements | 4/10 | no |
| 60 | Top K Frequent Elements (#347) | Heap | top_k_frequent | 4/10 | no |

**Python learned:**
- `heapq` module operates on a regular list — `heapq.heappush(heap, val)`, `heapq.heappop(heap)`
- Python heap is min heap by default — smallest at `heap[0]`
- Push tuples `(priority, value)` — heap sorts by first element
- Negate values for max heap behavior: push `-val`, negate result back
- `freqMap.items()` for key-value pairs, not `.values()`
- Don't reuse parameter names (`k`) as loop variables — overwrites the parameter

**Patterns learned:**
- House Robber II (circular): run House Robber twice — `nums[0:n-1]` and `nums[1:n]`, take max
- Delete and Earn: build `earn[i] = i * count[i]`, then House Robber on that array
- Top-K with min heap: keep heap size k, pop smallest when too big — `heap[0]` is the answer
- Frequency + heap combo: `Counter` for freq map, push `(freq, val)` tuples

---

## 2026-05-28 — Day 21

**Problems solved: 2**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Path Sum (#112) | Trees | path_sum | — | review done, retired |
| R | Subsets (#78) | Backtracking | subset_enumeration | — | review done, retry 06-07 |
| R | Permutations (#46) | Backtracking | permutation_generation | — | review done, retry 06-07 |
| R | House Robber (#198) | DynamicProgramming | linear_dp | — | review done, retry 06-07 |
| R | Coin Change (#322) | DynamicProgramming | knapsack | — | review done, retry 06-07 |
| 61 | K Closest Points to Origin (#973) | Heap | top_k_elements | 4/10 | no |
| 62 | Last Stone Weight (#1046) | Heap | simulation_heap | 1/10 | no |

**Python learned:**
- `heapq.heapify(list)` — converts a list to a heap in-place, faster than pushing one by one
- List comprehension `[-s for s in stones]` — transform all elements in one line
- `abs(x)` — built-in absolute value, no import needed
- `%` — modulo operator

**Patterns learned:**
- K closest = max heap of size k (negate distances) — pop farthest, keep closest
- No need for sqrt when comparing distances — squared distances preserve ordering
- Min heap + negate = max heap: pop removes largest actual value
- Simulation heap: repeatedly pop two largest, push difference back if unequal

---

## 2026-05-29 — Day 22

**Problems solved: 4**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Maximum Subarray (#53) | DynamicProgramming | linear_dp | — | review done, retry 06-05 |
| 63 | Sort an Array (#912) | DivideAndConquer | merge_sort | 4/10 | YES — redo 06-01 |
| 64 | Kth Largest Element in a Stream (#703) | Heap | design_priority_queue | 2/10 | no |
| 65 | Merge Intervals (#56) | Greedy | interval_merge | 4/10 | YES — redo 06-05 |

**Python learned:**
- `.sort()` on list of lists sorts by first element automatically
- Tuple unpacking in for loops: `for start, end in intervals`

**Patterns learned:**
- Merge sort: split in half recursively, merge two sorted halves with two pointers
- Both functions return a new sorted list; base case is `len <= 1`
- Merge intervals: sort first, then check if current start <= previous end → extend
- Seed result with first interval to avoid empty checks

---

## 2026-05-30 — Day 23

**Reviews: 7**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Combinations (#77) | Backtracking | combination_generation | — | review done, retry 06-04 |
| R | Course Schedule (#207) | Graphs | topological_sort | — | review done, retry 06-05 |
| R | Course Schedule II (#210) | Graphs | topological_sort | — | review done, retry 06-05 |
| R | Climbing Stairs (#70) | DynamicProgramming | linear_dp | — | review done, retry 06-08 |
| R | Min Cost Climbing Stairs (#746) | DynamicProgramming | linear_dp | — | review done, retry 06-08 |
| R | House Robber II (#213) | DynamicProgramming | linear_dp | — | review done, retry 06-09 |
| R | Delete and Earn (#740) | DynamicProgramming | linear_dp | — | review done, retry 06-06 |

**Bugs during reviews:**
- Combinations: still using `index` instead of `i` in loop body
- Course Schedule: confused visited (safe) vs visiting (in progress), forgot to propagate DFS result
- Course Schedule II: iterated over range instead of prereq map in DFS
- Climbing Stairs: used `max` instead of addition — it's counting ways, not optimizing
- Min Cost Climbing Stairs: added arbitrary +2/+1 instead of just `min(dp[i-1], dp[i-2]) + cost[i]`
- House Robber II: `dp[1] = nums[1]` instead of `max(nums[0], nums[1])`

---

## 2026-05-31 — Day 24

**Problems solved: 2**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 66 | Insert Interval (#57) | Greedy | interval_merge | 5/10 | YES — redo 06-04 |
| 67 | Non-overlapping Intervals (#435) | Greedy | interval_scheduling | 4/10 | YES — redo 06-05 |

**Python learned:**
- `intervals.sort(key=lambda x: x[1])` — sort by second element
- Lambda is standard Python way; can also use a named function with `key=`

**Patterns learned:**
- Insert interval: three cases per interval — before (add as-is), after (swap trick), overlap (expand with min/max)
- The swap trick (`result.append(newInterval); newInterval = i`) avoids needing a flag or break
- Final `result.append(newInterval)` always needed — catches merged or last swapped interval
- Non-overlapping intervals: sort by end time (greedy — finish earliest), track lastEnd, count overlaps
- Check current start vs lastEnd, not current end

---

## 2026-06-01 — Day 25

**Problems solved: 2**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Sort an Array (#912) | DivideAndConquer | merge_sort | — | review done, retry 06-16 |
| 68 | Task Scheduler (#621) | Greedy | cooldown_scheduling | 5/10 | YES — redo 06-04 |

**Patterns learned:**
- Task Scheduler: max heap for most frequent task + queue with cooldown timer
- After popping from heap, add to queue with `(count, task, time + n + 1)` as available time
- When available time matches current time, push back to heap
- Keep looping while either heap or queue has items

**Bugs:**
- Merge sort: forgot `// 2` in `mid = len(nums)` — infinite recursion

---

## 2026-06-02 — Day 26

**Problems solved: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 69 | Find Median from Data Stream (#295) | Heap | two_heaps_median | 8/10 | YES — redo 06-06 |

**Python learned:**
- `heapq.heappush(heap, val)` — heap is first arg, value is second (got this backwards multiple times)
- Operator precedence: `(a + b) % 2` needs parentheses, otherwise only `b % 2` is computed

**Patterns learned:**
- Two heaps for streaming median: max heap (smaller half), min heap (larger half)
- Max heap gives largest of small numbers, min heap gives smallest of large numbers — tops are the middle
- Compare new num against `-maxHeap[0]` to decide which half it belongs to
- Rebalance: max heap can be at most 1 bigger than min heap
- When moving between heaps, always negate the value (max heap stores negated)

---

## 2026-06-02 — Day 27

**Problems solved: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 70 | Implement Trie (#208) | Trie | prefix_tree | 3/10 | no |

**Patterns learned:**
- Trie: tree where each node has `children` dict (char → TrieNode) and `is_end` boolean
- Insert: walk letters, create nodes if missing, mark last as `is_end = True`
- Search: walk letters, return False if char missing, check `is_end` at the end
- startsWith: same as search but just return True after walking (don't check `is_end`)
- Root node is an empty TrieNode — all words start from root's children

---

## 2026-06-03 — Day 28

**Problems solved: 4**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 71 | Word Search (#79) | Backtracking | grid_backtracking | 6/10 | YES — redo 06-07 |
| 72 | Search in Rotated Sorted Array (#33) | BinarySearch | rotated_sorted_search | 5/10 | no |
| 73 | Find Min in Rotated Sorted Array (#153) | BinarySearch | rotated_sorted_search | 4/10 | YES — redo 06-07 |
| 74 | Koko Eating Bananas (#875) | BinarySearch | binary_search_on_answer | 4/10 | YES — redo 06-06 |

**Patterns learned:**
- Word Search: DFS + backtracking on grid — visit, try 4 directions, unvisit. Check `index == len(word)` before bounds check
- Rotated sorted array: at each mid, one half is always sorted. Check if target is in sorted half, else go other side
- Find min in rotated: binary search with `result` variable. If window is sorted, min is `nums[left]` — save and break
- Binary search on answer: "find min/max value satisfying condition" → define range, write checker, binary search
- Koko: range is 1 to max(piles), checker sums `ceil(pile/speed)`, compare with `h`
- When loop ends, `left` is the minimum valid answer — no need to track separately

**Python learned:**
- `math.ceil(x)` — rounds up, needs `import math`

---

## 2026-06-04 — Day 29

**Problems solved: 2, Reviews: 3**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Combinations (#77) | Backtracking | combination_generation | — | review done, retry 06-08 |
| R | Insert Interval (#57) | Greedy | interval_merge | — | review done, retry 06-11 |
| R | Task Scheduler (#621) | Greedy | cooldown_scheduling | — | review done, retry 06-08 |
| 75 | 3Sum (#15) | TwoPointers | three_sum | 6/10 | YES — redo 06-08 |
| 76 | Container With Most Water (#11) | TwoPointers | container | 5/10 | YES — redo 06-09 |

**Bugs during reviews:**
- Combinations: still off-by-one with starting index — `range(index, n+1)` not `range(index+1, n+1)` when starting from 1
- Task Scheduler: `and` instead of `or` in while loop, forgot heap arg in heappop

**Patterns learned:**
- 3Sum: sort, fix one element, two pointers for remaining pair. Skip duplicates with `if i > 0 and nums[i] == nums[i-1]: continue`
- Use set of tuples for dedup: `results.add((a, b, c))`
- Container With Most Water: two pointers from ends, move the shorter side inward
- Area = `min(height[left], height[right]) * (right - left)` — gap between walls, not inclusive

---

## 2026-06-06 — Day 30

**Reviews: 5**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Course Schedule (#207) | Graphs | topological_sort | — | review done, retry 06-20 |
| R | Course Schedule II (#210) | Graphs | topological_sort | — | review done, retry 06-22 |
| R | Maximum Subarray (#53) | DynamicProgramming | linear_dp | — | review done, retry 06-20 |
| R | Non-overlapping Intervals (#435) | Greedy | interval_scheduling | — | review done, retry 06-16 |
| R | Merge Intervals (#56) | Greedy | interval_merge | — | review done, retry 06-20 |

**Bugs during reviews:**
- Course Schedule: forgot `visited.add(course)` after processing — caused TLE from re-processing safe nodes
- Non-overlapping Intervals: `float(-inf)` missing quotes, `>` instead of `>=` for non-overlap check

---

## 2026-06-07 — Day 31

**Reviews: 6**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Delete and Earn (#740) | DynamicProgramming | linear_dp | — | review done, retry 06-25 |
| R | Find Median from Data Stream (#295) | Heap | two_heaps_median | — | review done, retry 06-14 |
| R | Koko Eating Bananas (#875) | BinarySearch | binary_search_on_answer | — | review done, retry 06-21 |
| R | Subsets (#78) | Backtracking | subset_enumeration | — | review done, retry 06-25 |
| R | Permutations (#46) | Backtracking | permutation_generation | — | review done, retry 06-25 |
| R | House Robber (#198) | DynamicProgramming | linear_dp | — | review done, retry 06-25 |

**Bugs during reviews:**
- Find Median: forgot ordering check (max heap top must be ≤ min heap top), forgot rebalance when min > max
- Koko: swapped the left/right pointer moves — "works" should move right, "too slow" should move left

---

## 2026-06-08 — Day 32

**Reviews: 6**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Coin Change (#322) | DynamicProgramming | knapsack | — | review done, retry 06-25 |
| R | Word Search (#79) | Backtracking | grid_backtracking | — | review done, retry 06-18 |
| R | Find Min in Rotated Array (#153) | BinarySearch | rotated_sorted_search | — | review done, retry 06-12 |
| R | Combinations (#77) | Backtracking | combination_generation | — | review done, retry 06-22 |
| R | Climbing Stairs (#70) | DynamicProgramming | linear_dp | — | review done, retired |

**Bugs during reviews:**
- Word Search: forgot to backtrack (remove from visited), forgot to put index check before bounds check
- Climbing Stairs: used `min` instead of `+` — counting ways, not optimizing cost

---

## 2026-06-09 — Day 33

**Reviews: 4**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Min Cost Climbing Stairs (#746) | DynamicProgramming | linear_dp | — | review done, retry 06-23 |
| R | Task Scheduler (#621) | Greedy | cooldown_scheduling | — | review done, retry 06-23 |
| R | House Robber II (#213) | DynamicProgramming | linear_dp | — | review done, retry 06-24 |
| R | Container With Most Water (#11) | TwoPointers | container | — | review done, retry 06-24 |

**Bugs during reviews:**
- Min Cost Climbing Stairs: `dp[1] = min(cost[0], cost[1])` should be `cost[1]`; forgot `min` of last two at return
- Task Scheduler: used `heap[-1]` (peek last) instead of `heapq.heappop(heap)`; missing empty-queue guard

---

## 2026-06-10 — Day 34

**Problems solved: 4, Reviews: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | 3Sum (#15) | TwoPointers | three_sum | — | review done, retry 06-26 |
| 77 | Product of Array Except Self (#238) | Arrays | prefix_suffix_products | 5/10 | YES — redo 06-15 |
| 78 | Longest Consecutive Sequence (#128) | Hashing | consecutive_sequence | 5/10 | YES — redo 06-15 |
| 79 | Valid Anagram (#242) | Hashing | frequency_counting | 2/10 | no |
| 80 | Group Anagrams (#49) | Hashing | grouping_by_key | 4/10 | YES — redo 06-28 |

**Patterns learned:**
- Product except self: prefix pass fills `result[i]` with left product, suffix pass multiplies in right product
- `result[i]` should NOT include `nums[i]` — assign the running product BEFORE multiplying in `nums[i]`
- Reuse output array as left-product storage → O(1) extra space
- Right-to-left loop: `range(len(nums) - 1, -1, -1)`
- Longest consecutive: put all in set, only start counting from sequence-starts (`num - 1` not in set) → O(n)
- Iterate over the SET, not the list — duplicates in the list re-run the full scan and cause TLE
- You can iterate a set directly: `for x in mySet` (no guaranteed order)
- Valid Anagram: compare two `Counter`s directly with `==`
- Group Anagrams: key = `"".join(sorted(word))` — anagrams share the same sorted key
- `.sort()` is a list method; strings are immutable — use `sorted(word)` which returns a new list
- `defaultdict(list)` auto-creates an empty list per key → `myMap[key].append(x)` with no get/assign dance

---

## 2026-06-11 — Day 35

**Problems solved: 2, Reviews: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Insert Interval (#57) | Greedy | interval_merge | — | review done, retry 06-25 |
| 81 | Longest Palindromic Substring (#5) | String | expand_around_center | 6/10 | YES — redo 06-16 |
| 82 | Palindromic Substrings (#647) | DynamicProgramming | expand_around_center | 4/10 | YES — redo 06-17 |

**Patterns learned:**
- Longest palindrome: expand around center — O(n²), the expected answer (not O(n))
- Every palindrome has a center; check both odd (i, i) and even (i, i+1) centers
- Brute force is O(n³); expand-around-center IS the optimization
- `max(a, b, c, key=len)` — compare by length instead of value; works on min/sorted too
- Each expansion step's substring is guaranteed a palindrome (inner already matched)
- Palindromic Substrings: same expand-around-center, but COUNT each match instead of tracking longest
- Count by position, not content — `"aaa"` has 6 palindromes, not 3 (no set/dedup)
- Reused the exact same helper structure — just `count += 1` instead of `max(..., key=len)`

**Bug during review:**
- Insert Interval: second condition backwards (`newInterval[1] > interval[0]` should be `<`); overlap-case used both starts for max instead of ends

---

## 2026-06-12 — Day 36

**Problems solved: 3, Reviews: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Find Min in Rotated Array (#153) | BinarySearch | rotated_sorted_search | — | review done, retry 06-26 |
| 83 | Two Sum II (#167) | TwoPointers | opposite_ends_pair_sum | 3/10 | no |
| 84 | Single Number (#136) | BitManipulation | xor_cancellation | 1/10 | YES — redo 06-19 |
| 85 | Number of 1 Bits (#191) | BitManipulation | bit_counting | 1/10 | YES — redo 06-19 |

**Python / bit learned:**
- XOR is `^`, AND is `&`, right-shift is `>>`
- XOR properties: `a ^ a = 0`, `a ^ 0 = a`, order doesn't matter
- XOR works on any integers — operates bit-by-bit on the binary form
- `n & 1` isolates the last bit (since `1` is `000...001`)
- `n >> 1` drops the last bit; loop `while n > 0` to walk all bits

**Patterns learned:**
- Single Number: XOR all elements — pairs cancel to 0, lone number remains
- Number of 1 Bits: check `n & 1`, add to count, `n >>= 1`, repeat until 0
- Two Sum II (sorted): two pointers from ends — sum too big move right, too small move left

---

## 2026-06-13 — Day 37

**Problems solved: 1, Reviews: 1**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| R | Find Median from Data Stream (#295) | Heap | two_heaps_median | — | review done (cleaner this time), retry 06-28 |
| 86 | Valid Palindrome (#125) | TwoPointers | palindrome_check | 2/10 | no |

**Python learned:**
- `.isalnum()` — True for letters and digits; `.isalpha()` letters only; `.isdigit()` digits only
- `.lower()` — lowercase for case-insensitive comparison

**Patterns learned:**
- Valid Palindrome: filter to alphanumeric + lowercase, then two pointers from both ends
- Find Median (cleaner): push to max, always move max-top to min (keeps order), then rebalance sizes

---

## 2026-06-14 — Day 38

**Problems solved: 3**

| # | Problem | Category | Pattern | Score | Review? |
|---|---------|----------|---------|-------|---------|
| 87 | Find the Duplicate Number (#287) | TwoPointers | floyd_cycle | 6/10 | YES — redo 06-19 |
| 88 | Maximum Product Subarray (#152) | DynamicProgramming | multi_state_dp | 5/10 | YES — redo 06-18 |
| 89 | Min Stack (#155) | Stack | min_stack | 3/10 | YES — redo 06-20 |

**Patterns learned:**
- Find the Duplicate: treat values as pointers (index → nums[index]), the duplicate is the cycle entrance
- Floyd's cycle detection: phase 1 slow+1/fast+2 until they meet; phase 2 reset one to start, both +1, meet at entrance
- Max Product Subarray: track BOTH max and min product ending here — negatives flip min↔max
- `maxDp[i] = max(nums[i], nums[i]*maxDp[i-1], nums[i]*minDp[i-1])`, minDp mirrors with min
- Min Stack: second stack stores running min; push `min(val, minStack[-1])`, pop both in sync → O(1) getMin

---

## Problems to redo
- Move Zeroes (#283) — review done 2026-05-11
