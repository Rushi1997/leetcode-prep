# Trees

227 problems across 12 patterns.

## bfs_level_order

**What it is** — BFS level-order traversal processes a tree one level at a time using a queue. You push all nodes of the current level into the queue, then drain it completely before moving to the next level. Recognize this pattern when a problem asks about levels, depths, rows, or anything that requires comparing or aggregating nodes at the same depth.

**Common steps**
1. Initialize a queue with the root node (guard against null root).
2. While the queue is non-empty, record `level_size = len(queue)`.
3. Loop exactly `level_size` times: pop a node, process it, and enqueue its non-null children.
4. After the inner loop, one full level has been processed — store or update your result for that level.
5. Repeat until the queue is empty; return the accumulated result.

**Key variations**
- Collect all node values per level (standard level-order) vs. a single aggregate per level (sum, max, average).
- Zigzag / alternating direction: toggle a flag and reverse every other level's list.
- Right side view / left side view: only record the first or last node of each level.
- Next-right pointers: instead of a separate list, link siblings directly during traversal.
- BFS from a target node outward (treat tree as undirected graph) for distance problems.
- Track column indices (vertical order) by pairing each node with its column offset in the queue.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 637 | [Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) | Easy | 2/10 | 74.9% | [ ] |
| 1302 | [Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/) | Medium | 3/10 | 86.5% | [ ] |
| 3902 | [Zigzag Level Sum of Binary Tree](https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/) :lock: | Medium | 3/10 | 73.1% | [ ] |
| 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | 3/10 | 72.6% | [ ] |
| 429 | [N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | Medium | 3/10 | 71.5% | [ ] |
| 3157 | [Find the Level of Tree with Minimum Sum](https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/) :lock: | Medium | 3/10 | 69.4% | [ ] |
| 107 | [Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | Medium | 3/10 | 68.1% | [ ] |
| 515 | [Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/) | Medium | 3/10 | 66.3% | [ ] |
| 993 | [Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/) | Easy | 3/10 | 59.3% | [ ] |
| 111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Easy | 3/10 | 52.9% | [ ] |
| 3831 | [Median of a Binary Search Tree Level](https://leetcode.com/problems/median-of-a-binary-search-tree-level/) :lock: | Medium | 4/10 | 88.0% | [ ] |
| 2415 | [Reverse Odd Levels of Binary Tree](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/) | Medium | 4/10 | 86.7% | [ ] |
| 1602 | [Find Nearest Right Node in Binary Tree](https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/) :lock: | Medium | 4/10 | 75.1% | [ ] |
| 513 | [Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value/) | Medium | 4/10 | 72.3% | [ ] |
| 582 | [Kill Process](https://leetcode.com/problems/kill-process/) :lock: | Medium | 4/10 | 70.7% | [ ] |
| 199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | 4/10 | 70.1% | [ ] |
| 1161 | [Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/) | Medium | 4/10 | 70.0% | [ ] |
| 103 | [Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | Medium | 4/10 | 63.6% | [ ] |
| 2641 | [Cousins in Binary Tree II](https://leetcode.com/problems/cousins-in-binary-tree-ii/) | Medium | 5/10 | 75.8% | [ ] |
| 3372 | [Maximize the Number of Target Nodes After Connecting Trees I](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/) | Medium | 5/10 | 69.4% | [ ] |
| 3787 | [Find Diameter Endpoints of a Tree](https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/) :lock: | Medium | 5/10 | 68.1% | [ ] |
| 116 | [Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/) | Medium | 5/10 | 67.1% | [ ] |
| 1609 | [Even Odd Tree](https://leetcode.com/problems/even-odd-tree/) | Medium | 5/10 | 67.1% | [ ] |
| 2385 | [Amount of Time for Binary Tree to Be Infected](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/) | Medium | 5/10 | 65.3% | [ ] |
| 958 | [Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/) | Medium | 5/10 | 59.2% | [ ] |
| 2583 | [Kth Largest Sum in a Binary Tree](https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/) | Medium | 5/10 | 59.0% | [ ] |
| 3820 | [Pythagorean Distance Nodes in a Tree](https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/) | Medium | 5/10 | 57.9% | [ ] |
| 314 | [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) :lock: | Medium | 5/10 | 57.8% | [ ] |
| 742 | [Closest Leaf in a Binary Tree](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/) :lock: | Medium | 5/10 | 47.4% | [ ] |
| 2471 | [Minimum Number of Operations to Sort a Binary Tree by Level](https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/) | Medium | 6/10 | 74.2% | [ ] |
| 117 | [Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) | Medium | 6/10 | 57.5% | [ ] |
| 662 | [Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/) | Medium | 6/10 | 45.6% | [ ] |
| 3373 | [Maximize the Number of Target Nodes After Connecting Trees II](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/) | Hard | 7/10 | 73.1% | [ ] |
| 863 | [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | Medium | 7/10 | 67.6% | [ ] |

## dfs_traversal

**What it is** — DFS traversal visits every node in a tree by recursively (or iteratively with a stack) going as deep as possible before backtracking. The three orderings — preorder (root first), inorder (left, root, right), postorder (children first) — determine when you process a node relative to its subtrees. Recognize this pattern when you need to visit every node or propagate information up or down the tree.

**Common steps**
1. Define a recursive helper that takes the current node (and any state being carried, e.g., running sum, max so far).
2. Write the base case: if node is null, return a neutral value (0, True, infinity, etc.).
3. Recurse into left child, then right child (swap order for right-first variants).
4. Combine the results from left and right subtrees with the current node's value.
5. Return the combined result upward (postorder) or use the current node before recursing (preorder).
6. For iterative DFS, use an explicit stack; push right child before left so left is processed first.

**Key variations**
- Preorder for path-building and cloning (process node before children).
- Inorder for BST problems (yields sorted order).
- Postorder for bottom-up aggregation (height, diameter, subtree sums).
- Carry state downward (max from root, restricted nodes) vs. aggregate state upward.
- N-ary trees: loop over all children instead of just left/right.
- Iterative with an explicit stack to avoid recursion depth limits on large inputs.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | 1/10 | 78.1% | [x] |
| 1379 | [Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/) | Easy | 2/10 | 85.8% | [ ] |
| 1469 | [Find All The Lonely Nodes](https://leetcode.com/problems/find-all-the-lonely-nodes/) :lock: | Easy | 2/10 | 84.1% | [ ] |
| 2331 | [Evaluate Boolean Binary Tree](https://leetcode.com/problems/evaluate-boolean-binary-tree/) | Easy | 2/10 | 82.4% | [ ] |
| 590 | [N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) | Easy | 2/10 | 81.1% | [ ] |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy | 2/10 | 80.0% | [ ] |
| 589 | [N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/) | Easy | 2/10 | 76.8% | [ ] |
| 144 | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Easy | 2/10 | 75.7% | [ ] |
| 559 | [Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/) | Easy | 2/10 | 73.5% | [ ] |
| 2689 | [Extract Kth Character From The Rope Tree](https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/) :lock: | Easy | 2/10 | 73.4% | [ ] |
| 965 | [Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/) | Easy | 2/10 | 73.0% | [ ] |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Easy | 2/10 | 67.1% | [ ] |
| 404 | [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | Easy | 2/10 | 62.7% | [ ] |
| 1490 | [Clone N-ary Tree](https://leetcode.com/problems/clone-n-ary-tree/) :lock: | Medium | 3/10 | 83.0% | [ ] |
| 145 | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | Easy | 3/10 | 78.1% | [ ] |
| 872 | [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) | Easy | 3/10 | 70.2% | [ ] |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Easy | 3/10 | 61.1% | [ ] |
| 671 | [Second Minimum Node In a Binary Tree](https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/) | Easy | 3/10 | 46.1% | [ ] |
| 1315 | [Sum of Nodes with Even-Valued Grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/) | Medium | 4/10 | 85.9% | [ ] |
| 1485 | [Clone Binary Tree With Random Pointer](https://leetcode.com/problems/clone-binary-tree-with-random-pointer/) :lock: | Medium | 4/10 | 80.9% | [ ] |
| 2764 | [Is Array a Preorder of Some ‌Binary Tree](https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/) :lock: | Medium | 4/10 | 67.9% | [ ] |
| 2368 | [Reachable Nodes With Restrictions](https://leetcode.com/problems/reachable-nodes-with-restrictions/) | Medium | 4/10 | 60.3% | [ ] |
| 1430 | [Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree](https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/) :lock: | Medium | 4/10 | 47.5% | [ ] |
| 366 | [Find Leaves of Binary Tree](https://leetcode.com/problems/find-leaves-of-binary-tree/) :lock: | Medium | 5/10 | 81.3% | [ ] |
| 951 | [Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/) | Medium | 5/10 | 69.5% | [ ] |
| 655 | [Print Binary Tree](https://leetcode.com/problems/print-binary-tree/) | Medium | 5/10 | 66.6% | [ ] |
| 1443 | [Minimum Time to Collect All Apples in a Tree](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) | Medium | 5/10 | 63.6% | [ ] |
| 1376 | [Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | Medium | 5/10 | 60.5% | [ ] |
| 3558 | [Number of Ways to Assign Edge Weights I](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/) | Medium | 5/10 | 53.2% | [ ] |
| 3067 | [Count Pairs of Connectable Servers in a Weighted Tree Network](https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/) | Medium | 6/10 | 55.9% | [ ] |
| 3331 | [Find Subtree Sizes After Changes](https://leetcode.com/problems/find-subtree-sizes-after-changes/) | Medium | 6/10 | 53.8% | [ ] |
| 545 | [Boundary of Binary Tree](https://leetcode.com/problems/boundary-of-binary-tree/) :lock: | Medium | 6/10 | 48.1% | [ ] |
| 2872 | [Maximum Number of K-Divisible Components](https://leetcode.com/problems/maximum-number-of-k-divisible-components/) | Hard | 7/10 | 74.0% | [ ] |
| 987 | [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | Hard | 7/10 | 53.7% | [ ] |
| 2458 | [Height of Binary Tree After Subtree Removal Queries](https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/) | Hard | 8/10 | 54.9% | [ ] |
| 2003 | [Smallest Missing Genetic Value in Each Subtree](https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/) | Hard | 8/10 | 47.8% | [ ] |
| 1766 | [Tree of Coprimes](https://leetcode.com/problems/tree-of-coprimes/) | Hard | 8/10 | 44.0% | [ ] |
| 3715 | [Sum of Perfect Square Ancestors](https://leetcode.com/problems/sum-of-perfect-square-ancestors/) | Hard | 8/10 | 42.6% | [ ] |
| 3515 | [Shortest Path in a Weighted Tree](https://leetcode.com/problems/shortest-path-in-a-weighted-tree/) | Hard | 9/10 | 42.3% | [ ] |
| 2867 | [Count Valid Paths in a Tree](https://leetcode.com/problems/count-valid-paths-in-a-tree/) | Hard | 9/10 | 36.2% | [ ] |
| 3327 | [Check if DFS Strings Are Palindromes](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/) | Hard | 9/10 | 20.5% | [ ] |

## bst_operations

**What it is** — BST operations exploit the binary search tree invariant: every node in the left subtree is strictly less than the current node, and every node in the right subtree is strictly greater. This ordering lets you search, insert, delete, and validate in O(h) time by eliminating half the remaining tree at each step. Recognize this pattern when the problem involves a BST and you can use value comparisons to direct traversal instead of visiting every node.

**Common steps**
1. At each node, compare the target value (or range bounds) against `node.val`.
2. If the target equals `node.val`, you have found what you need — process it.
3. If the target is less than `node.val`, recurse or move to the left child.
4. If the target is greater than `node.val`, recurse or move to the right child.
5. For range queries (e.g., range sum), recurse into both subtrees only when the range overlaps that side; prune the other side.
6. For in-order traversal problems, use a running variable (previous node or accumulator) since inorder yields sorted order.

**Key variations**
- Search and closest-value: standard compare-and-move, track closest seen so far.
- Insert: recurse down until you hit null, create the new node there.
- Delete: three cases — leaf, one child, two children (replace with inorder successor/predecessor).
- Validate: pass allowed `[min, max]` bounds down recursively; a node is invalid if it violates its bounds.
- Convert to/from sorted order: inorder traversal + rebuild or running-sum accumulation (reverse inorder for greater sum tree).
- Two BSTs: merge by extracting inorder lists from both and merging like merge-sort.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 700 | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Easy | 1/10 | 82.7% | [ ] |
| 938 | [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/) | Easy | 2/10 | 87.6% | [ ] |
| 270 | [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/) :lock: | Easy | 2/10 | 49.2% | [ ] |
| 701 | [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | Medium | 3/10 | 73.5% | [ ] |
| 653 | [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) | Easy | 3/10 | 63.3% | [ ] |
| 783 | [Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) | Easy | 3/10 | 61.3% | [ ] |
| 530 | [Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/) | Easy | 3/10 | 59.4% | [ ] |
| 1038 | [Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/) | Medium | 4/10 | 88.4% | [ ] |
| 1305 | [All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/) | Medium | 4/10 | 80.3% | [ ] |
| 897 | [Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/) | Easy | 4/10 | 79.0% | [ ] |
| 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | 4/10 | 76.8% | [ ] |
| 538 | [Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/) | Medium | 4/10 | 71.6% | [ ] |
| 510 | [Inorder Successor in BST II](https://leetcode.com/problems/inorder-successor-in-bst-ii/) :lock: | Medium | 4/10 | 61.1% | [ ] |
| 501 | [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/) | Easy | 4/10 | 58.9% | [ ] |
| 285 | [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) :lock: | Medium | 4/10 | 51.2% | [ ] |
| 776 | [Split BST](https://leetcode.com/problems/split-bst/) :lock: | Medium | 5/10 | 82.2% | [ ] |
| 1214 | [Two Sum BSTs](https://leetcode.com/problems/two-sum-bsts/) :lock: | Medium | 5/10 | 68.2% | [ ] |
| 669 | [Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/) | Medium | 5/10 | 66.7% | [ ] |
| 426 | [Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) :lock: | Medium | 5/10 | 65.6% | [ ] |
| 2476 | [Closest Nodes Queries in a Binary Search Tree](https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/) | Medium | 5/10 | 44.4% | [ ] |
| 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | 5/10 | 35.7% | [ ] |
| 1586 | [Binary Search Tree Iterator II](https://leetcode.com/problems/binary-search-tree-iterator-ii/) :lock: | Medium | 6/10 | 63.4% | [ ] |
| 272 | [Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii/) :lock: | Hard | 6/10 | 61.2% | [ ] |
| 450 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium | 6/10 | 54.6% | [ ] |
| 333 | [Largest BST Subtree](https://leetcode.com/problems/largest-bst-subtree/) :lock: | Medium | 6/10 | 45.9% | [ ] |
| 99 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | Medium | 7/10 | 59.5% | [ ] |
| 1902 | [Depth of BST Given Insertion Order](https://leetcode.com/problems/depth-of-bst-given-insertion-order/) :lock: | Medium | 7/10 | 42.6% | [ ] |
| 1932 | [Merge BSTs to Create Single BST](https://leetcode.com/problems/merge-bsts-to-create-single-bst/) | Hard | 9/10 | 38.7% | [ ] |

## balanced_tree

**What it is** — A balanced binary tree has the property that for every node, the heights of its left and right subtrees differ by at most one (AVL-style balance). Problems in this pattern ask you to either check whether a tree satisfies this condition or to restructure an unbalanced tree into a balanced one. Recognize this pattern when the problem explicitly mentions balance, or when a BST is built from a sorted sequence and needs to be height-minimal.

**Common steps**
1. Write a postorder DFS helper that returns the height of each subtree.
2. At each node, compute `left_height` and `right_height` by recursing into both children.
3. Check if `abs(left_height - right_height) <= 1`; if not, mark the tree (or subtree) as unbalanced.
4. Return `1 + max(left_height, right_height)` upward, or -1 as a sentinel to signal imbalance.
5. To construct a balanced BST from a sorted list: pick the middle element as root, then recursively build left and right subtrees from the left and right halves.

**Key variations**
- Checking balance: return early (-1 sentinel) the moment any subtree is unbalanced to avoid unnecessary work.
- Constructing balance: extract BST inorder traversal into a sorted array, then recursively build from the sorted array using mid-point selection.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 110 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | 4/10 | 58.3% | [ ] |
| 1382 | [Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/) | Medium | 5/10 | 86.3% | [ ] |

## subtree_properties

**What it is** — Subtree property problems ask you to compute or verify a value that is defined over an entire subtree (e.g., sum, size, color, structure) and then use that result to answer a question about the whole tree. The key insight is that a subtree's property depends only on the properties of its children's subtrees, making postorder DFS the natural fit. Recognize this when a problem asks you to count, find, or compare subtrees based on some aggregate.

**Common steps**
1. Define what information each subtree needs to return (e.g., sum, size, min, max, is_valid flag).
2. Write a postorder DFS: recurse left, recurse right, then compute the current node's property from the returned values.
3. At each node, update a global result variable if the current subtree satisfies the target condition.
4. Return the subtree's property upward so the parent can use it.
5. For duplicate or equivalence checks, serialize the subtree into a hashable form (string or tuple) and use a hash map.

**Key variations**
- Aggregate sums/sizes: straightforward postorder accumulation.
- Structural checks (univalue, perfect, complete): return a flag alongside size/height.
- Subtree matching: serialize subtrees to strings and compare with a hash set.
- Diameter / longest path through a node: compute left and right depths, update global max with their sum, return the longer depth + 1.
- Equal partition: compute total sum first, then check if any subtree sum equals half the total.
- Label/color counting: carry a frequency map upward and merge children's maps.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2236 | [Root Equals Sum of Children](https://leetcode.com/problems/root-equals-sum-of-children/) | Easy | 1/10 | 84.9% | [ ] |
| 563 | [Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt/) | Easy | 3/10 | 65.8% | [ ] |
| 2265 | [Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/) | Medium | 4/10 | 86.8% | [ ] |
| 1973 | [Count Nodes Equal to Sum of Descendants](https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/) :lock: | Medium | 4/10 | 77.3% | [ ] |
| 2773 | [Height of Special Binary Tree](https://leetcode.com/problems/height-of-special-binary-tree/) :lock: | Medium | 4/10 | 74.5% | [ ] |
| 1612 | [Check If Two Expression Trees are Equivalent](https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/) :lock: | Medium | 4/10 | 71.7% | [ ] |
| 1120 | [Maximum Average Subtree](https://leetcode.com/problems/maximum-average-subtree/) :lock: | Medium | 4/10 | 66.9% | [ ] |
| 250 | [Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees/) :lock: | Medium | 4/10 | 57.5% | [ ] |
| 1522 | [Diameter of N-Ary Tree](https://leetcode.com/problems/diameter-of-n-ary-tree/) :lock: | Medium | 5/10 | 75.4% | [ ] |
| 222 | [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) | Easy | 5/10 | 72.5% | [ ] |
| 508 | [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/) | Medium | 5/10 | 69.2% | [ ] |
| 3319 | [K-th Largest Perfect Subtree Size in Binary Tree](https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/) | Medium | 5/10 | 62.2% | [ ] |
| 3004 | [Maximum Subtree of the Same Color](https://leetcode.com/problems/maximum-subtree-of-the-same-color/) :lock: | Medium | 5/10 | 58.7% | [ ] |
| 3249 | [Count the Number of Good Nodes](https://leetcode.com/problems/count-the-number-of-good-nodes/) | Medium | 5/10 | 55.4% | [ ] |
| 572 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy | 5/10 | 51.5% | [ ] |
| 663 | [Equal Tree Partition](https://leetcode.com/problems/equal-tree-partition/) :lock: | Medium | 5/10 | 42.3% | [ ] |
| 1530 | [Number of Good Leaf Nodes Pairs](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/) | Medium | 6/10 | 71.8% | [ ] |
| 652 | [Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/) | Medium | 6/10 | 60.7% | [ ] |
| 1519 | [Number of Nodes in the Sub-Tree With the Same Label](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/) | Medium | 6/10 | 55.4% | [ ] |
| 3203 | [Find Minimum Diameter After Merging Two Trees](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/) | Hard | 7/10 | 57.0% | [ ] |
| 3313 | [Find the Last Marked Nodes in Tree](https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/) :lock: | Hard | 8/10 | 56.4% | [ ] |

## tree_modification

**What it is** — Tree modification problems require you to structurally change a tree in-place or return a new tree with altered connections, node values, or shape. Unlike pure traversal, you must rewire child pointers or delete/insert nodes. Recognize this pattern when the problem asks you to prune, flatten, invert, merge, or otherwise reshape the tree rather than just read from it.

**Common steps**
1. Recurse postorder so children are already modified before you process the current node.
2. At each node, decide what to do based on the modified left and right subtrees (e.g., whether to keep or prune).
3. Rewire `node.left` and `node.right` to point to the new (possibly null) subtree roots.
4. Return the node that should take this position in the parent's tree — sometimes the node itself, sometimes a child, sometimes null.
5. For flattening or relinking (e.g., flatten to linked list), use a running "previous" pointer and reorder connections in postorder or reverse-preorder.

**Key variations**
- Prune based on a condition (leaf value, path sum): return null from base to remove a node; bubble up from postorder.
- Invert / mirror: swap left and right children at every node (preorder or postorder, both work).
- Merge two trees: simultaneously recurse both trees; sum values, recurse into paired children.
- Flatten to linked list: use reverse-preorder (right, left, root) with a `prev` pointer to build the list in-place.
- Add/delete a row at a specific depth: use BFS or DFS with a depth counter to reach the target level.
- Delete a set of nodes: postorder to handle children first, then decide whether the current node stays or becomes new roots.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | 2/10 | 80.0% | [ ] |
| 617 | [Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/) | Easy | 2/10 | 79.1% | [ ] |
| 1325 | [Delete Leaves With a Given Value](https://leetcode.com/problems/delete-leaves-with-a-given-value/) | Medium | 4/10 | 77.2% | [ ] |
| 1660 | [Correct a Binary Tree](https://leetcode.com/problems/correct-a-binary-tree/) :lock: | Medium | 5/10 | 74.3% | [ ] |
| 814 | [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/) | Medium | 5/10 | 72.5% | [ ] |
| 114 | [Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) | Medium | 5/10 | 70.7% | [ ] |
| 2445 | [Number of Nodes With Value One](https://leetcode.com/problems/number-of-nodes-with-value-one/) :lock: | Medium | 5/10 | 66.0% | [ ] |
| 156 | [Binary Tree Upside Down](https://leetcode.com/problems/binary-tree-upside-down/) :lock: | Medium | 5/10 | 65.5% | [ ] |
| 623 | [Add One Row to Tree](https://leetcode.com/problems/add-one-row-to-tree/) | Medium | 5/10 | 64.1% | [ ] |
| 1273 | [Delete Tree Nodes](https://leetcode.com/problems/delete-tree-nodes/) :lock: | Medium | 5/10 | 61.7% | [ ] |
| 1666 | [Change the Root of a Binary Tree](https://leetcode.com/problems/change-the-root-of-a-binary-tree/) :lock: | Medium | 6/10 | 75.1% | [ ] |
| 1110 | [Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/) | Medium | 6/10 | 72.5% | [ ] |
| 1080 | [Insufficient Nodes in Root to Leaf Paths](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/) | Medium | 6/10 | 55.1% | [ ] |
| 971 | [Flip Binary Tree To Match Preorder Traversal](https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/) | Medium | 6/10 | 51.9% | [ ] |
| 3812 | [Minimum Edge Toggles on a Tree](https://leetcode.com/problems/minimum-edge-toggles-on-a-tree/) | Hard | 8/10 | 68.8% | [ ] |
| 1516 | [Move Sub-Tree of N-Ary Tree](https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/) :lock: | Hard | 8/10 | 59.8% | [ ] |

## tree_design

**What it is** — Tree design problems ask you to implement a data structure or class that wraps a tree and supports efficient repeated queries or updates through a well-defined API. Rather than solving a single static problem, you design the internal state and methods so that each operation runs within a target time complexity. Recognize this pattern when the problem presents a class with multiple method signatures (e.g., `insert`, `find`, `next`, `getOrder`) that must be implemented together.

**Common steps**
1. Identify what data the class needs to store as instance variables (the tree itself, auxiliary structures like a deque or hash set, iterators).
2. In the constructor, build any precomputed structures (e.g., reconstruct a contaminated tree, lay out a complete binary tree as an array).
3. For each method, decide whether to traverse lazily on each call or maintain incremental state.
4. Use helper data structures alongside the tree — a queue for complete-tree insertion order, a stack for iterative inorder, a list for preorder traversal tracking.
5. Test edge cases: empty tree, single node, operations interleaved in unusual order.

**Key variations**
- Iterator pattern (BST Iterator): use a stack to simulate inorder traversal one step at a time; `next()` pops and pushes right subtree.
- Complete tree inserter: maintain a deque of nodes that still have room for children; pop when both children are filled.
- Contaminated tree recovery: DFS to assign correct values (root=0, left child=2*parent+1, right child=2*parent+2), store in a hash set for O(1) `find`.
- Hierarchy / inheritance modeling (Throne Inheritance): use an adjacency list and a dead set; DFS preorder for the order, skipping dead nodes.
- Tree encoding: map an N-ary tree onto a binary tree using left-child/right-sibling representation.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1261 | [Find Elements in a Contaminated Binary Tree](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/) | Medium | 4/10 | 84.1% | [ ] |
| 173 | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | Medium | 5/10 | 76.4% | [ ] |
| 1600 | [Throne Inheritance](https://leetcode.com/problems/throne-inheritance/) | Medium | 5/10 | 67.2% | [ ] |
| 919 | [Complete Binary Tree Inserter](https://leetcode.com/problems/complete-binary-tree-inserter/) | Medium | 5/10 | 65.0% | [ ] |
| 431 | [Encode N-ary Tree to Binary Tree](https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/) :lock: | Hard | 7/10 | 80.6% | [ ] |

## path_sum

**What it is** — Path sum problems ask you to find, count, or optimize over paths in a tree where each path's value is the sum (or some function) of the node values along it. A path can run root-to-leaf, root-to-any-node, or any-node-to-any-node (going up and over). Recognize this pattern when the problem involves accumulating values along a path and checking or optimizing that accumulated value.

**Common steps**
1. For root-to-leaf paths: carry a running sum downward through DFS; at each leaf check if it equals the target.
2. For root-to-any-node paths: track the current prefix sum; at each node check `current_sum == target`.
3. For any-node-to-any-node paths (path through a node): compute `left_gain` and `right_gain` from children (clamped to 0 if negative), update a global result with `node.val + left_gain + right_gain`, and return `node.val + max(left_gain, right_gain)` upward.
4. For counting paths with a given sum: use a prefix-sum hash map (similar to subarray sum equals k); store `{prefix_sum: count}` and look up `prefix_sum - target` at each node.
5. Backtrack the prefix-sum map when returning from a subtree (undo the current node's contribution).

**Key variations**
- Root-to-leaf only: must reach a leaf node, not just any node; add an explicit leaf check.
- Return all paths vs. just count: for all paths, carry a path list and append/pop (backtrack).
- Path as a number (binary number, digit string): multiply or concatenate instead of adding.
- Longest consecutive path: track direction (ascending/descending) and reset count when broken.
- Any-direction path with constraints (pseudo-palindrome, distinct values): carry a bitmask or set alongside the running value.
- Paths across two nodes using LCA: find the two paths from root to each node and combine at their meeting point.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1022 | [Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-root-to-leaf-binary-numbers/) | Easy | 2/10 | 76.6% | [ ] |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | Easy | 2/10 | 54.9% | [ ] |
| 257 | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | Easy | 3/10 | 68.6% | [ ] |
| 1448 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium | 4/10 | 73.8% | [ ] |
| 129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | Medium | 4/10 | 69.9% | [ ] |
| 113 | [Path Sum II](https://leetcode.com/problems/path-sum-ii/) | Medium | 4/10 | 62.2% | [ ] |
| 298 | [Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/) :lock: | Medium | 4/10 | 54.7% | [ ] |
| 1457 | [Pseudo-Palindromic Paths in a Binary Tree](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/) | Medium | 5/10 | 68.4% | [ ] |
| 666 | [Path Sum IV](https://leetcode.com/problems/path-sum-iv/) :lock: | Medium | 5/10 | 62.9% | [ ] |
| 988 | [Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/) | Medium | 5/10 | 61.2% | [ ] |
| 3879 | [Maximum Distinct Path Sum in a Binary Tree](https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/) :lock: | Medium | 5/10 | 57.2% | [ ] |
| 2467 | [Most Profitable Path in a Tree](https://leetcode.com/problems/most-profitable-path-in-a-tree/) | Medium | 6/10 | 67.3% | [ ] |
| 549 | [Binary Tree Longest Consecutive Sequence II](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/) :lock: | Medium | 6/10 | 50.1% | [ ] |
| 437 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Medium | 6/10 | 46.4% | [ ] |
| 3593 | [Minimum Increments to Equalize Leaf Paths](https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/) | Medium | 6/10 | 41.3% | [ ] |
| 2791 | [Count Paths That Can Form a Palindrome in a Tree](https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/) | Hard | 9/10 | 52.0% | [ ] |
| 2538 | [Difference Between Maximum and Minimum Price Sum](https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/) | Hard | 9/10 | 33.5% | [ ] |
| 3425 | [Longest Special Path](https://leetcode.com/problems/longest-special-path/) | Hard | 9/10 | 22.7% | [ ] |
| 3486 | [Longest Special Path II](https://leetcode.com/problems/longest-special-path-ii/) | Hard | 9/10 | 19.2% | [ ] |

## tree_construction

**What it is** — Tree construction problems ask you to build a tree from a non-tree representation such as a traversal sequence, a sorted array, a parent-child description list, or a string encoding. The core challenge is determining which element becomes the root and how to partition the remaining data into left and right subtrees. Recognize this pattern when you are given raw data (not an existing tree) and must reconstruct or generate a valid tree structure.

**Common steps**
1. Identify the root: in preorder sequences it is the first element; in sorted arrays it is the middle element; in inorder+postorder it is the last element of postorder.
2. Locate the root's position in any complementary traversal (e.g., find the root's index in the inorder array) to determine the split between left and right subtrees.
3. Recurse on the left portion of each sequence to build the left subtree.
4. Recurse on the right portion to build the right subtree.
5. Link root.left and root.right to the results and return root.
6. Use a hash map of value-to-index for the inorder array to make root-finding O(1) instead of O(n).

**Key variations**
- Preorder + inorder: root is preorder[0]; its inorder index splits left/right sizes.
- Inorder + postorder: root is postorder[-1]; same split logic.
- Sorted array to BST: always pick the mid index as root for minimum height.
- Sorted linked list to BST: use slow/fast pointer to find the mid node, or convert to array first.
- Single preorder sequence for BST: use a valid range [min, max] to greedily assign nodes without needing an inorder array.
- From parent-child description list: build a hash map of parent-to-children and a set of all children to identify the root (the node that appears as a parent but never as a child).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Easy | 3/10 | 75.5% | [ ] |
| 2196 | [Create Binary Tree From Descriptions](https://leetcode.com/problems/create-binary-tree-from-descriptions/) | Medium | 4/10 | 81.7% | [ ] |
| 1008 | [Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/) | Medium | 5/10 | 84.2% | [ ] |
| 536 | [Construct Binary Tree from String](https://leetcode.com/problems/construct-binary-tree-from-string/) :lock: | Medium | 5/10 | 58.7% | [ ] |
| 998 | [Maximum Binary Tree II](https://leetcode.com/problems/maximum-binary-tree-ii/) | Medium | 6/10 | 70.4% | [ ] |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | 6/10 | 68.8% | [ ] |
| 106 | [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | Medium | 6/10 | 68.6% | [ ] |
| 109 | [Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/) | Medium | 6/10 | 66.6% | [ ] |
| 95 | [Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) | Medium | 7/10 | 62.4% | [ ] |
| 1028 | [Recover a Tree From Preorder Traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/) | Hard | 8/10 | 83.2% | [ ] |

## lowest_common_ancestor

**What it is** — The Lowest Common Ancestor (LCA) of two nodes p and q is the deepest node in the tree that has both p and q as descendants (where a node is considered a descendant of itself). LCA is the foundation for computing distances between nodes, finding paths between nodes, and many tree query problems. Recognize this pattern when a problem involves two nodes and asks about their relationship, distance, or a shared structural point.

**Common steps**
1. Base case: if the current node is null, or equals p or q, return the current node.
2. Recurse into the left subtree and the right subtree.
3. If both recursive calls return non-null results, the current node is the LCA — return it.
4. If only one side returns non-null, bubble that result upward (both p and q are in the same subtree).
5. For BST-specific LCA: use the BST property — if both p and q are less than `node.val`, go left; if both are greater, go right; otherwise the current node is the LCA.
6. For node-distance problems: find LCA, compute depth of p and q from root, then `dist = depth(p) + depth(q) - 2 * depth(LCA)`.

**Key variations**
- Standard binary tree LCA: postorder DFS returning the found node or null.
- BST LCA: iterative comparison using BST ordering, no full traversal needed.
- LCA with parent pointers: walk both nodes up to root, collect ancestor sets, find the first common ancestor.
- LCA of deepest leaves: find the deepest level first, then find LCA of all nodes at that level.
- Multiple nodes LCA: treat the set of target nodes like p and q; return when a node is in the set.
- Path between two nodes: find LCA, extract path from each node to LCA and concatenate.
- Binary lifting for repeated LCA queries: precompute 2^k ancestors for each node; answer each query in O(log n).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1650 | [Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) :lock: | Medium | 4/10 | 83.0% | [ ] |
| 235 | [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | 4/10 | 70.5% | [ ] |
| 1257 | [Smallest Common Region](https://leetcode.com/problems/smallest-common-region/) :lock: | Medium | 4/10 | 68.3% | [ ] |
| 1676 | [Lowest Common Ancestor of a Binary Tree IV](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/) :lock: | Medium | 5/10 | 79.6% | [ ] |
| 1740 | [Find Distance in a Binary Tree](https://leetcode.com/problems/find-distance-in-a-binary-tree/) :lock: | Medium | 5/10 | 74.3% | [ ] |
| 1644 | [Lowest Common Ancestor of a Binary Tree II](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/) :lock: | Medium | 5/10 | 69.6% | [ ] |
| 2096 | [Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) | Medium | 5/10 | 56.4% | [ ] |
| 1123 | [Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/) | Medium | 6/10 | 79.5% | [ ] |
| 865 | [Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/) | Medium | 6/10 | 77.6% | [ ] |
| 236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | 6/10 | 69.2% | [ ] |
| 2509 | [Cycle Length Queries in a Tree](https://leetcode.com/problems/cycle-length-queries-in-a-tree/) | Hard | 7/10 | 60.3% | [ ] |
| 2277 | [Closest Node to Path in Tree](https://leetcode.com/problems/closest-node-to-path-in-tree/) :lock: | Hard | 8/10 | 62.3% | [ ] |
| 3559 | [Number of Ways to Assign Edge Weights II](https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/) | Hard | 8/10 | 59.5% | [ ] |
| 3553 | [Minimum Weighted Subgraph With the Required Paths II](https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/) | Hard | 9/10 | 50.0% | [ ] |
| 2846 | [Minimum Edge Weight Equilibrium Queries in a Tree](https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/) | Hard | 9/10 | 45.8% | [ ] |
| 3585 | [Find Weighted Median Node in Tree](https://leetcode.com/problems/find-weighted-median-node-in-tree/) | Hard | 9/10 | 26.6% | [ ] |

## serialization

**What it is** — Serialization converts a tree into a flat string or byte stream that can be stored or transmitted, and deserialization reconstructs the original tree from that encoding. The challenge is choosing an encoding that unambiguously captures the tree's structure, including null children, so the tree can be uniquely reconstructed. Recognize this pattern when asked to encode/decode a tree, or when you need to create a canonical string representation of a tree structure.

**Common steps**
1. Choose a traversal order for serialization — preorder is most common because the root comes first, making deserialization straightforward.
2. At each node, write the node's value followed by a delimiter (e.g., comma); write a null marker (e.g., `#`) when a child is absent.
3. For deserialization, split the string on the delimiter and use a pointer or iterator over the token list.
4. Reconstruct preorder: consume the next token — if it is the null marker, return null; otherwise create a node, recurse for its left child, then recurse for its right child.
5. For BST serialization, you can omit null markers and use the BST property during deserialization (valid-range approach), producing a more compact encoding.

**Key variations**
- Binary tree: requires explicit null markers to distinguish shape; preorder or level-order both work.
- BST: can skip null markers since node values constrain valid positions; reconstruct using valid range during preorder deserialization.
- N-ary tree: encode the number of children after each node's value, then recurse for each child.
- Canonical subtree hashing: serialize subtrees to strings and store in a hash map to identify duplicates (used in subtree problems, not just I/O).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 606 | [Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/) | Medium | 4/10 | 70.7% | [ ] |
| 449 | [Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/) | Medium | 6/10 | 59.6% | [ ] |
| 428 | [Serialize and Deserialize N-ary Tree](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/) :lock: | Hard | 7/10 | 68.8% | [ ] |
| 297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | 8/10 | 60.7% | [ ] |

## binary_tree_dp

**What it is** — Binary tree DP combines the structural recursion of DFS with dynamic programming: each node computes an optimal value based on the optimal values of its subtrees, and the choices made at a node can affect what choices are valid or beneficial in its subtrees. This is postorder DFS where the return value from each child encodes the DP state (e.g., "best result if I take this node" vs. "best result if I skip this node"). Recognize this pattern when a tree problem has an optimization objective and decisions at one node constrain or interact with decisions at its ancestors or descendants.

**Common steps**
1. Define the DP state returned by each recursive call — typically a tuple like `(take, skip)` or a single optimal value with constraints encoded implicitly.
2. Recurse into both children and receive their DP states.
3. At the current node, compute each possible choice by combining the appropriate child states (e.g., if you take this node, you must skip its children).
4. Return the DP state for this node upward to the parent.
5. After the full recursion, read the answer from the root's returned state.
6. For global-path problems (max path sum, diameter): maintain a global variable updated at each node, while the return value only carries the best single-arm contribution upward.

**Key variations**
- Include/exclude DP (e.g., tree cameras, house robber on tree): return `(with_node, without_node)` from each call.
- Diameter / longest path: the answer passes through a node using both arms; return only the best single arm upward.
- Coin/value redistribution (distribute coins): count excess at each subtree; moves = sum of absolute excesses.
- Rerooting technique: compute an answer for one root via postorder, then propagate corrections to all other roots in a second DFS — enables O(n) solutions for "answer at every root" problems.
- Tree knapsack: group related values by subtree and optimize a weighted selection; often requires Euler-tour flattening.
- Binary lifting / sparse table for ancestor queries: precompute 2^k-th ancestors in O(n log n) to answer kth-ancestor or path queries in O(log n).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 543 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | 4/10 | 65.5% | [ ] |
| 1026 | [Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/) | Medium | 5/10 | 78.2% | [ ] |
| 2477 | [Minimum Fuel Cost to Report to the Capital](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/) | Medium | 5/10 | 65.3% | [ ] |
| 2049 | [Count Nodes With the Highest Score](https://leetcode.com/problems/count-nodes-with-the-highest-score/) | Medium | 5/10 | 52.7% | [ ] |
| 979 | [Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/) | Medium | 6/10 | 77.3% | [ ] |
| 1372 | [Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/) | Medium | 6/10 | 67.1% | [ ] |
| 2673 | [Make Costs of Paths Equal in a Binary Tree](https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/) | Medium | 6/10 | 58.4% | [ ] |
| 2378 | [Choose Edges to Maximize Score in a Tree](https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/) :lock: | Medium | 6/10 | 56.7% | [ ] |
| 1339 | [Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/) | Medium | 6/10 | 55.7% | [ ] |
| 1145 | [Binary Tree Coloring Game](https://leetcode.com/problems/binary-tree-coloring-game/) | Medium | 6/10 | 52.9% | [ ] |
| 2925 | [Maximum Score After Applying Operations on a Tree](https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/) | Medium | 6/10 | 47.2% | [ ] |
| 687 | [Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/) | Medium | 6/10 | 43.9% | [ ] |
| 2246 | [Longest Path With Different Adjacent Characters](https://leetcode.com/problems/longest-path-with-different-adjacent-characters/) | Hard | 7/10 | 54.0% | [ ] |
| 3772 | [Maximum Subgraph Score in a Tree](https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/) | Hard | 8/10 | 70.6% | [ ] |
| 2313 | [Minimum Flips in Binary Tree to Get Result](https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/) :lock: | Hard | 8/10 | 56.8% | [ ] |
| 3786 | [Total Sum of Interaction Cost in Tree Groups](https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/) | Hard | 8/10 | 54.1% | [ ] |
| 2440 | [Create Components With Same Value](https://leetcode.com/problems/create-components-with-same-value/) | Hard | 8/10 | 53.7% | [ ] |
| 2973 | [Find Number of Coins to Place in Tree Nodes](https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/) | Hard | 8/10 | 37.4% | [ ] |
| 2322 | [Minimum Score After Removals on a Tree](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/) | Hard | 9/10 | 76.1% | [ ] |
| 834 | [Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/) | Hard | 9/10 | 65.6% | [ ] |
| 1916 | [Count Ways to Build Rooms in an Ant Colony](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/) | Hard | 9/10 | 51.3% | [ ] |
| 2646 | [Minimize the Total Price of the Trips](https://leetcode.com/problems/minimize-the-total-price-of-the-trips/) | Hard | 9/10 | 48.2% | [ ] |
| 2581 | [Count Number of Possible Root Nodes](https://leetcode.com/problems/count-number-of-possible-root-nodes/) | Hard | 9/10 | 48.1% | [ ] |
| 968 | [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) | Hard | 9/10 | 47.9% | [ ] |
| 1373 | [Maximum Sum BST in Binary Tree](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/) | Hard | 9/10 | 47.2% | [ ] |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | 9/10 | 42.3% | [ ] |
| 1483 | [Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node/) | Hard | 9/10 | 37.5% | [ ] |
| 2920 | [Maximum Points After Collecting Coins From All Nodes](https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/) | Hard | 9/10 | 36.5% | [ ] |
| 3367 | [Maximize Sum of Weights after Edge Removals](https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/) | Hard | 9/10 | 30.9% | [ ] |
| 3590 | [Kth Smallest Path XOR Sum](https://leetcode.com/problems/kth-smallest-path-xor-sum/) | Hard | 9/10 | 29.7% | [ ] |
| 3241 | [Time Taken to Mark All Nodes](https://leetcode.com/problems/time-taken-to-mark-all-nodes/) | Hard | 9/10 | 28.0% | [ ] |
