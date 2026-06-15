# Stack

100 problems across 15 patterns.

## stack_design

**What it is** — Stack design problems ask you to build a data structure that augments a standard stack with additional constant-time operations (such as retrieving the current minimum or maximum). The core idea is to maintain a secondary stack that tracks auxiliary information in sync with the main stack so every push/pop keeps the extra state up to date.

**Common steps**
1. Identify the extra operation that must be O(1) (e.g., `getMin`, `getMax`, `getMedian`).
2. Maintain a parallel "auxiliary" stack alongside the main stack.
3. On `push`: compute the new auxiliary value (e.g., `min(val, aux_stack.top())`) and push it onto both stacks.
4. On `pop`: pop from both the main stack and the auxiliary stack simultaneously.
5. For the extra operation, simply return the top of the auxiliary stack.

**Key variations**
- Minimum vs. maximum tracking (auxiliary stack stores running min or max).
- Space-optimized variants that only push to the auxiliary stack when the value changes.
- Supporting both min and max simultaneously requires two auxiliary stacks.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | 3/10 | 58.1% | [x] |

## stack_simulation

**What it is** — Stack simulation problems model a real-world process (a game, a file system, a log of events) where the most recent state must be undone or referenced before moving forward. The stack naturally represents the "current context" — you push when entering a new state and pop when exiting or undoing. Recognize this pattern when operations are nested or when you need to cancel the most recent action.

**Common steps**
1. Parse the input sequence of operations one at a time.
2. Maintain a stack representing the current "active" state or history.
3. For each operation: push new state, pop to undo/exit, or read the top to inspect the current context.
4. Handle edge cases where the stack is empty before a pop (e.g., already at root directory).
5. After processing all operations, derive the answer from the stack's final contents or a running tally.

**Key variations**
- Undo operations (pop the last entry): Baseball Game, Crawler Log Folder.
- Tracking nested contexts with timestamps: Exclusive Time of Functions.
- Collision/cancellation logic between stack elements: Asteroid Collision.
- Path normalization where `..` means "go up one level": Simplify Path.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 682 | [Baseball Game](https://leetcode.com/problems/baseball-game/) | Easy | 2/10 | 80.4% | [ ] |
| 1598 | [Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/) | Easy | 2/10 | 71.7% | [ ] |
| 1441 | [Build an Array With Stack Operations](https://leetcode.com/problems/build-an-array-with-stack-operations/) | Medium | 3/10 | 80.9% | [ ] |
| 946 | [Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/) | Medium | 4/10 | 70.4% | [ ] |
| 71 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Medium | 4/10 | 50.5% | [ ] |
| 388 | [Longest Absolute File Path](https://leetcode.com/problems/longest-absolute-file-path/) | Medium | 4/10 | 49.4% | [ ] |
| 636 | [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions/) | Medium | 5/10 | 66.2% | [ ] |
| 735 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Medium | 5/10 | 47.8% | [ ] |

## stack_string_manipulation

**What it is** — Stack string manipulation uses a stack as a "result buffer" that you build character by character, allowing you to look back at — and remove — the most recently added character when a cancellation condition is met. This avoids rebuilding the string from scratch and handles cascading deletions elegantly. Recognize this pattern when a character can invalidate the character immediately before it.

**Common steps**
1. Initialize an empty stack (or list used as a stack) to hold the output characters.
2. Iterate through the input string character by character.
3. At each character, check whether it cancels the top of the stack (e.g., same char, opposite case, matches a target substring's last char).
4. If cancellation: pop from the stack (and possibly continue popping for multi-char patterns).
5. If no cancellation: push the current character onto the stack.
6. Join the stack into the final result string.

**Key variations**
- Single-character removal: Remove All Adjacent Duplicates In String.
- Case-based cancellation (upper vs. lower): Make The String Great.
- Fixed-length substring removal: Remove All Adjacent Duplicates in String II (track counts alongside chars).
- Encoded/compressed strings that require recursion-like unwinding: Decode String (push count and partial string).
- Greedy score maximization by choosing which pair to remove first: Maximum Score From Removing Substrings.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1047 | [Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | Easy | 2/10 | 73.2% | [ ] |
| 1544 | [Make The String Great](https://leetcode.com/problems/make-the-string-great/) | Easy | 3/10 | 68.5% | [ ] |
| 1910 | [Remove All Occurrences of a Substring](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/) | Medium | 4/10 | 78.5% | [ ] |
| 1003 | [Check If Word Is Valid After Substitutions](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/) | Medium | 4/10 | 61.2% | [ ] |
| 1717 | [Maximum Score From Removing Substrings](https://leetcode.com/problems/maximum-score-from-removing-substrings/) | Medium | 5/10 | 66.5% | [ ] |
| 394 | [Decode String](https://leetcode.com/problems/decode-string/) | Medium | 5/10 | 62.6% | [ ] |
| 1209 | [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | Medium | 5/10 | 61.2% | [ ] |

## bracket_matching

**What it is** — Bracket matching validates or transforms strings containing opening and closing delimiters by using a stack to track unmatched openers. When a closer is encountered, you check whether the stack top is its corresponding opener and pop if so; otherwise the string is invalid. Recognize this pattern whenever nesting depth or balanced pairs are at the heart of the problem.

**Common steps**
1. Initialize an empty stack.
2. Iterate through each character in the string.
3. If it is an opening bracket/tag, push it onto the stack.
4. If it is a closing bracket/tag, check whether the stack is non-empty and the top matches; if yes, pop; if no, record a mismatch.
5. After full traversal, the stack should be empty for a fully valid string; remaining entries represent unmatched openers.
6. For removal problems, reconstruct the string by excluding the indices of unmatched brackets.

**Key variations**
- Pure validation (return true/false): Valid Parentheses.
- Nesting depth tracking (count open brackets, track max): Maximum Nesting Depth.
- Minimum removals to make valid: Minimum Remove to Make Valid Parentheses (store indices, then delete).
- Scoring based on structure: Score of Parentheses (accumulate value based on depth).
- Longest valid substring: Longest Valid Parentheses (use index-based stack or DP).
- HTML/XML tag matching with additional string logic: Tag Validator.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1021 | [Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/) | Easy | 2/10 | 87.0% | [ ] |
| 1614 | [Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/) | Easy | 2/10 | 84.9% | [ ] |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | 2/10 | 44.1% | [ ] |
| 1249 | [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) | Medium | 5/10 | 71.4% | [ ] |
| 856 | [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/) | Medium | 5/10 | 63.6% | [ ] |
| 591 | [Tag Validator](https://leetcode.com/problems/tag-validator/) | Hard | 8/10 | 40.5% | [ ] |
| 32 | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | Hard | 8/10 | 38.7% | [ ] |

## monotonic_stack_next_greater_smaller

**What it is** — A monotonic stack maintains elements in strictly increasing or decreasing order; when a new element breaks that order, it "resolves" all stack elements it dominates, giving you the next greater (or smaller) element for each in O(n) total. Recognize this pattern when you need, for every element, the first element to its left or right that is larger or smaller than it.

**Common steps**
1. Initialize an empty stack (stores indices, not values, for flexibility).
2. Decide the invariant: decreasing stack for "next greater," increasing stack for "next smaller."
3. Iterate through the array left to right (or right to left, depending on direction needed).
4. While the stack is non-empty and the current element breaks the invariant, pop the top index — the current element is its "next greater/smaller." Record the answer for that popped index.
5. Push the current index onto the stack.
6. After iteration, any indices still in the stack have no next greater/smaller element; fill with the default (e.g., -1 or 0).

**Key variations**
- Next greater to the right vs. next greater to the left (reverse the iteration direction).
- Circular arrays: iterate twice (indices mod n) to wrap around: Next Greater Element II.
- Applied to linked lists instead of arrays: Next Greater Node In Linked List.
- Two-pointer variant where you need the second next greater: Next Greater Element IV.
- Problems framed as discarding nodes that are dominated: Remove Nodes From Linked List.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 496 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Easy | 2/10 | 76.1% | [x] |
| 1475 | [Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) | Easy | 3/10 | 84.1% | [ ] |
| 1762 | [Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/) :lock: | Medium | 4/10 | 80.9% | [ ] |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | 4/10 | 68.6% | [x] |
| 503 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | Medium | 4/10 | 68.3% | [ ] |
| 1019 | [Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/) | Medium | 5/10 | 64.3% | [ ] |
| 2487 | [Remove Nodes From Linked List](https://leetcode.com/problems/remove-nodes-from-linked-list/) | Medium | 6/10 | 74.9% | [ ] |
| 1776 | [Car Fleet II](https://leetcode.com/problems/car-fleet-ii/) | Hard | 8/10 | 57.9% | [ ] |
| 2940 | [Find Building Where Alice and Bob Can Meet](https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/) | Hard | 9/10 | 52.2% | [ ] |
| 2454 | [Next Greater Element IV](https://leetcode.com/problems/next-greater-element-iv/) | Hard | 9/10 | 41.9% | [ ] |

## tree_sequence_validation

**What it is** — Tree sequence validation problems use a stack to simulate traversing a binary tree in a given order (preorder, inorder, postorder) and verify that a flat sequence corresponds to a valid tree structure. The stack tracks the "current path" from root to the node being visited, and popping corresponds to backtracking up the tree. Recognize this pattern when you must confirm that a serialized sequence could be produced by a valid BST or binary tree traversal.

**Common steps**
1. Initialize an empty stack and a lower-bound variable (for BST problems) or a slot-counter (for general binary trees).
2. Iterate through the sequence element by element.
3. For BST preorder: pop elements from the stack that are less than the current value (we are moving to a right subtree); update the lower bound to the last popped value. If the current value is less than the lower bound, the sequence is invalid.
4. For serialization validation: treat each node as consuming one slot; null markers fill slots without adding new ones. Track available slots and verify they never go negative.
5. At the end, confirm the stack or slot count reflects a fully consumed, valid tree.

**Key variations**
- BST preorder validation (uses lower-bound tracking): Verify Preorder Sequence in BST.
- Generic binary tree serialization validation (uses slot/degree counting): Verify Preorder Serialization of a Binary Tree.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 331 | [Verify Preorder Serialization of a Binary Tree](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/) | Medium | 5/10 | 47.3% | [ ] |
| 255 | [Verify Preorder Sequence in Binary Search Tree](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/) :lock: | Medium | 6/10 | 51.8% | [ ] |

## monotonic_stack_span_range

**What it is** — Span and range problems use a monotonic stack to efficiently determine, for each element, how far left or right it "dominates" (i.e., remains the maximum or minimum over a contiguous range). Rather than computing next-greater to get a single neighbor, you use both the previous-greater and next-greater boundaries to define the full span of influence for each element. Recognize this pattern when a problem asks for the range or subarray for which an element is the extremum.

**Common steps**
1. Use two passes (or a single pass with careful bookkeeping) to find, for each index, the nearest greater element to its left (`left_bound`) and to its right (`right_bound`).
2. The "span" or "range" of element `i` as the maximum is `[left_bound[i]+1, right_bound[i]-1]`.
3. For online/streaming problems (e.g., Stock Span), maintain a decreasing stack of (value, span) pairs and merge spans when the stack is popped.
4. Combine span lengths with element values to compute the required aggregate (count, score, length, etc.).
5. Handle ties carefully — typically one boundary is strict (`<`) and the other is non-strict (`<=`) to avoid double-counting.

**Key variations**
- Online streaming (Stock Span): process one element at a time, merging spans on the fly.
- Finding the maximum width ramp or semi-decreasing subarray: Maximum Width Ramp, Maximum Length of Semi-Decreasing Subarrays.
- Vehicle/group merging based on speed and position: Car Fleet.
- Three-value pattern detection across indices: 132 Pattern.
- Counting subarrays where boundary elements are maximum: requires combining left/right span counts.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3205 | [Maximum Array Hopping Score I](https://leetcode.com/problems/maximum-array-hopping-score-i/) :lock: | Medium | 5/10 | 76.9% | [ ] |
| 2832 | [Maximal Range That Each Element Is Maximum in It](https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/) :lock: | Medium | 5/10 | 75.4% | [ ] |
| 901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | Medium | 5/10 | 69.0% | [ ] |
| 2863 | [Maximum Length of Semi-Decreasing Subarrays](https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/) :lock: | Medium | 6/10 | 70.0% | [ ] |
| 1966 | [Binary Searchable Numbers in an Unsorted Array](https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/) :lock: | Medium | 6/10 | 63.6% | [ ] |
| 962 | [Maximum Width Ramp](https://leetcode.com/problems/maximum-width-ramp/) | Medium | 6/10 | 55.9% | [ ] |
| 853 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | Medium | 6/10 | 55.1% | [ ] |
| 1950 | [Maximum of Minimum Values in All Subarrays](https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/) :lock: | Medium | 6/10 | 48.0% | [ ] |
| 2345 | [Finding the Number of Visible Mountains](https://leetcode.com/problems/finding-the-number-of-visible-mountains/) :lock: | Medium | 6/10 | 37.2% | [ ] |
| 1944 | [Number of Visible People in a Queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) | Hard | 7/10 | 73.0% | [ ] |
| 3221 | [Maximum Array Hopping Score II](https://leetcode.com/problems/maximum-array-hopping-score-ii/) :lock: | Medium | 7/10 | 59.7% | [ ] |
| 456 | [132 Pattern](https://leetcode.com/problems/132-pattern/) | Medium | 7/10 | 34.7% | [ ] |
| 3113 | [Find the Number of Subarrays Where Boundary Elements Are Maximum](https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/) | Hard | 8/10 | 33.2% | [ ] |

## monotonic_stack_greedy_sequence

**What it is** — Greedy sequence problems use a monotonic stack to build the lexicographically smallest (or largest) subsequence or permutation by greedily deciding, at each step, whether to discard a previously chosen element in favor of the current one. The key insight is that it is always locally optimal to pop a larger element from the stack when a smaller one arrives — as long as future supply allows it. Recognize this pattern when the goal is to construct an optimal sequence under a budget of removals or a fixed output length.

**Common steps**
1. Precompute any needed frequency or suffix information (e.g., remaining count of each character, suffix minimum).
2. Iterate through the input left to right, maintaining a stack representing the current best candidate sequence.
3. Before pushing the current element, pop from the stack while: (a) the top is greater than (or not better than) the current element, (b) you still have a removal budget remaining, and (c) the popped element will still appear later in the input (or budget allows permanent removal).
4. Push the current element if it belongs in the output (respecting length constraints and mandatory character requirements).
5. After the loop, if the budget is not exhausted, trim from the end of the stack.
6. Return the stack as the result sequence.

**Key variations**
- Fixed removal budget (Remove K Digits, Find the Most Competitive Subsequence): pop greedily until budget is zero.
- Duplicate removal with mandatory uniqueness (Remove Duplicate Letters, Smallest Subsequence of Distinct Characters): track last-occurrence indices; only pop if the character appears again later.
- DI-string construction (Construct Smallest Number From DI String): push runs and reverse them on 'I'.
- Mandatory character inclusion with length constraint: Smallest K-Length Subsequence With Occurrences of a Letter.
- Optimization objective is a non-lexicographic score: Minimum Cost Tree From Leaf Values, The Number of Weak Characters.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2375 | [Construct Smallest Number From DI String](https://leetcode.com/problems/construct-smallest-number-from-di-string/) | Medium | 5/10 | 85.6% | [ ] |
| 3523 | [Make Array Non-decreasing](https://leetcode.com/problems/make-array-non-decreasing/) | Medium | 5/10 | 57.1% | [ ] |
| 1081 | [Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/) | Medium | 6/10 | 63.4% | [ ] |
| 2434 | [Using a Robot to Print the Lexicographically Smallest String](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/) | Medium | 6/10 | 62.4% | [ ] |
| 3638 | [Maximum Balanced Shipments](https://leetcode.com/problems/maximum-balanced-shipments/) | Medium | 6/10 | 61.4% | [ ] |
| 316 | [Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/) | Medium | 6/10 | 53.2% | [ ] |
| 1673 | [Find the Most Competitive Subsequence](https://leetcode.com/problems/find-the-most-competitive-subsequence/) | Medium | 6/10 | 53.0% | [ ] |
| 1996 | [The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/) | Medium | 6/10 | 44.6% | [ ] |
| 402 | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | Medium | 6/10 | 36.8% | [ ] |
| 1130 | [Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/) | Medium | 7/10 | 67.9% | [ ] |
| 2030 | [Smallest K-Length Subsequence With Occurrences of a Letter](https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/) | Hard | 9/10 | 39.7% | [ ] |
| 3816 | [Lexicographically Smallest String After Deleting Duplicate Characters](https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/) | Hard | 9/10 | 19.9% | [ ] |

## expression_tree_parsing

**What it is** — Expression tree parsing problems convert a flat infix (or prefix/postfix) expression into a binary tree where leaves are operands and internal nodes are operators. A stack manages the tree nodes built so far, and operator precedence determines when to reduce (pop and combine) vs. shift (push). Recognize this pattern when you must construct a structured representation of a mathematical expression that can then be evaluated or inspected.

**Common steps**
1. Define a node structure with value, left child, and right child.
2. Use a stack for operand/subtree nodes and a separate stack (or precedence check) for operators.
3. Scan tokens left to right; push operand nodes immediately.
4. When an operator is encountered, pop all pending operators of greater or equal precedence from the operator stack, combine their top two operand nodes into a subtree, and push the subtree back.
5. Handle parentheses by pushing `(` as a sentinel and flushing to it when `)` is seen.
6. After scanning all tokens, drain the operator stack, combining nodes until one root remains.

**Key variations**
- Design-only (implement evaluate on a pre-built tree): Design an Expression Tree With Evaluate Function.
- Full construction from infix with precedence and parentheses: Build Binary Expression Tree From Infix Expression.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1628 | [Design an Expression Tree With Evaluate Function](https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/) :lock: | Medium | 5/10 | 82.5% | [ ] |
| 1597 | [Build Binary Expression Tree From Infix Expression](https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/) :lock: | Hard | 8/10 | 62.8% | [ ] |

## nested_structure_parsing

**What it is** — Nested structure parsing problems decode or transform strings that use delimiters (parentheses, brackets, braces) to define recursive nesting levels. A stack saves the "outer context" each time you descend into a deeper level, and you restore that context when the closing delimiter is found. Recognize this pattern when the meaning of a character or token depends on the current nesting depth.

**Common steps**
1. Initialize a stack to hold partial results from outer scopes.
2. Scan the string character by character (or token by token).
3. On an opening delimiter: push the current accumulated result (and any relevant metadata like a repeat count) onto the stack, then reset for the new inner scope.
4. On a closing delimiter: pop the outer context from the stack and combine it with the completed inner result (e.g., repeat, reverse, expand, or merge).
5. For regular characters: append to the current scope's accumulator.
6. Return the final accumulator as the answer.

**Key variations**
- Reversal on close: Reverse Substrings Between Each Pair of Parentheses.
- Repetition on close (with a count prefix): Decode String — same template, push `(count, partial_str)`.
- Chemical formula with element counts and groups: Number of Atoms (use dicts/maps at each level, scale on close).
- Brace expansion generating sets of strings: Brace Expansion II (stack holds sets, merge on close).
- General JSON/list parsing with mixed types: Mini Parser.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1190 | [Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/) | Medium | 5/10 | 72.0% | [ ] |
| 385 | [Mini Parser](https://leetcode.com/problems/mini-parser/) | Medium | 6/10 | 42.5% | [ ] |
| 726 | [Number of Atoms](https://leetcode.com/problems/number-of-atoms/) | Hard | 8/10 | 65.1% | [ ] |
| 1096 | [Brace Expansion II](https://leetcode.com/problems/brace-expansion-ii/) | Hard | 9/10 | 63.8% | [ ] |

## expression_evaluation

**What it is** — Expression evaluation problems parse a mathematical or logical expression given as a string and compute its numeric (or boolean) result directly, without building an explicit tree. A value stack holds intermediate results, and an operator stack (or recursive parsing) enforces precedence and associativity. Recognize this pattern when you must evaluate arithmetic, boolean, or custom operators with potential parentheses and multi-character tokens.

**Common steps**
1. Tokenize or scan the expression character by character, handling multi-digit numbers and whitespace.
2. Maintain a number stack (for operands and partial results) and optionally an operator stack.
3. On a number: push it to the number stack.
4. On an operator: before pushing it, pop and evaluate all pending operators of higher or equal precedence from the operator stack (respecting left-associativity).
5. On `(`: push a sentinel to the operator stack; on `)`: evaluate until the matching sentinel is popped.
6. After scanning, drain the operator stack and return the single remaining value in the number stack.

**Key variations**
- Postfix (RPN) — no precedence needed, evaluate on every operator token: Evaluate Reverse Polish Notation.
- Infix with `+`, `-`, `*`, `/` only (no parentheses): Basic Calculator II (use a "pending sign" trick with one stack).
- Infix with parentheses and `+`, `-` only: Basic Calculator (track sign, push/pop on parentheses).
- Infix with all four operators plus parentheses: Basic Calculator III (full two-stack or recursive descent).
- Ternary expressions: Ternary Expression Parser (right-to-left scan collapses `?:` pairs).
- Boolean expressions with `&`, `|`, `!`: Parsing A Boolean Expression.
- Lisp-style with variables and `let`/`add`/`mult`: Parse Lisp Expression (use environment stack for scoping).
- Symbolic polynomial expressions: Basic Calculator IV.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | 4/10 | 57.7% | [ ] |
| 439 | [Ternary Expression Parser](https://leetcode.com/problems/ternary-expression-parser/) :lock: | Medium | 5/10 | 62.6% | [ ] |
| 227 | [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) | Medium | 5/10 | 46.9% | [ ] |
| 1106 | [Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/) | Hard | 7/10 | 69.8% | [ ] |
| 3749 | [Evaluate Valid Expressions](https://leetcode.com/problems/evaluate-valid-expressions/) :lock: | Hard | 8/10 | 70.8% | [ ] |
| 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Hard | 8/10 | 46.9% | [ ] |
| 772 | [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) :lock: | Hard | 9/10 | 53.3% | [ ] |
| 1896 | [Minimum Cost to Change the Final Value of Expression](https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/) | Hard | 9/10 | 49.6% | [ ] |
| 736 | [Parse Lisp Expression](https://leetcode.com/problems/parse-lisp-expression/) | Hard | 10/10 | 53.4% | [ ] |
| 770 | [Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/) | Hard | 10/10 | 49.8% | [ ] |

## monotonic_stack_dp

**What it is** — Monotonic stack DP problems combine a monotonic stack with dynamic programming: the stack efficiently finds the optimal "previous dominating element" for each index in O(1) amortized time, replacing an O(n) inner loop in the naive DP recurrence. Recognize this pattern when a DP transition of the form `dp[i] = f(dp[j], arr[j..i])` always involves the nearest element satisfying a monotonic condition.

**Common steps**
1. Write the naive O(n²) DP recurrence first to understand what "previous relevant element" means for each index.
2. Observe that the optimal `j` for each `i` is always the most recent index where `arr[j]` is greater than (or less than) `arr[i]` — a monotonic relationship.
3. Maintain a monotonic stack of indices alongside the DP array.
4. For each index `i`, pop the stack while the top violates the monotonic property; use the top (before/after popping) as the transition index `j`.
5. Compute `dp[i]` using the transition, then push `i` onto the stack.
6. The final answer is typically `dp[n-1]` or the maximum/minimum over all `dp` values.

**Key variations**
- Jump game where you must jump to a greater element: Jump Game VIII (monotonic stack finds valid jump targets in O(n)).
- Counting steps to make an array non-decreasing: Steps to Make Array Non-decreasing (stack layers encode merge chains).
- Sliding-window minimum subarray to sort: Smallest Subarray to Sort in Every Sliding Window.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2297 | [Jump Game VIII](https://leetcode.com/problems/jump-game-viii/) :lock: | Medium | 7/10 | 45.7% | [ ] |
| 3555 | [Smallest Subarray to Sort in Every Sliding Window](https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/) :lock: | Medium | 8/10 | 58.2% | [ ] |
| 2289 | [Steps to Make Array Non-decreasing](https://leetcode.com/problems/steps-to-make-array-non-decreasing/) | Medium | 8/10 | 24.8% | [ ] |

## monotonic_stack_area_contribution

**What it is** — Area contribution problems calculate aggregate values (sums, areas, counts) over all subarrays by computing, for each element, how many subarrays it is the minimum (or maximum) of, then multiplying by its value. A monotonic stack finds the left and right boundaries of each element's "dominance range" in O(n), collapsing an O(n²) or O(n³) brute-force into a linear solution. Recognize this pattern when the problem involves the sum or max/min over all subarrays and a single element governs each subarray's contribution.

**Common steps**
1. For each index `i`, find `left[i]` = the nearest index to the left where `arr[left[i]] < arr[i]` (strict), and `right[i]` = the nearest index to the right where `arr[right[i]] <= arr[i]` (non-strict, to avoid double-counting).
2. Use a single left-to-right pass with a monotonic increasing stack to compute both `left` and `right` arrays (pop on violation to set `right`, use stack top to set `left`).
3. The number of subarrays where element `i` is the minimum is `(i - left[i]) * (right[i] - i)`.
4. Multiply by `arr[i]` (or another function of the element) to get its total contribution, then sum across all elements.
5. Apply modular arithmetic if required.
6. For 2D problems (Maximal Rectangle), reduce each row to a histogram and apply the 1D technique.

**Key variations**
- Sum of subarray minimums / maximums: sum all contributions.
- Largest rectangle in histogram: for each bar, find the maximal width it can extend as the shortest bar.
- Maximal rectangle in a binary matrix: reduce each row to a histogram, then apply histogram technique.
- Mountain-shaped arrays (Beautiful Towers): use two passes (left and right) combining prefix sums.
- Contribution involves a product with index distance (Min-Product): precompute prefix sums.
- Complex scoring with prime scores and ranking: Apply Operations to Maximize Score.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2104 | [Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/) | Medium | 6/10 | 61.1% | [ ] |
| 3542 | [Minimum Operations to Convert All Elements to Zero](https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/) | Medium | 6/10 | 53.0% | [ ] |
| 1063 | [Number of Valid Subarrays](https://leetcode.com/problems/number-of-valid-subarrays/) :lock: | Hard | 7/10 | 79.9% | [ ] |
| 1526 | [Minimum Number of Increments on Subarrays to Form a Target Array](https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/) | Hard | 7/10 | 78.2% | [ ] |
| 3676 | [Count Bowl Subarrays](https://leetcode.com/problems/count-bowl-subarrays/) | Medium | 7/10 | 48.3% | [ ] |
| 2865 | [Beautiful Towers I](https://leetcode.com/problems/beautiful-towers-i/) | Medium | 7/10 | 44.5% | [ ] |
| 1856 | [Maximum Subarray Min-Product](https://leetcode.com/problems/maximum-subarray-min-product/) | Medium | 7/10 | 40.3% | [ ] |
| 907 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | Medium | 7/10 | 38.5% | [ ] |
| 768 | [Max Chunks To Make Sorted II](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/) | Hard | 8/10 | 54.8% | [ ] |
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | 8/10 | 49.8% | [ ] |
| 2334 | [Subarray With Elements Greater Than Varying Threshold](https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/) | Hard | 8/10 | 45.4% | [ ] |
| 3229 | [Minimum Operations to Make Array Equal to Target](https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/) | Hard | 8/10 | 41.5% | [ ] |
| 2866 | [Beautiful Towers II](https://leetcode.com/problems/beautiful-towers-ii/) | Medium | 8/10 | 36.4% | [ ] |
| 85 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | Hard | 9/10 | 58.7% | [ ] |
| 2281 | [Sum of Total Strength of Wizards](https://leetcode.com/problems/sum-of-total-strength-of-wizards/) | Hard | 9/10 | 29.3% | [ ] |
| 3430 | [Maximum and Minimum Sums of at Most Size K Subarrays](https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/) | Hard | 9/10 | 25.6% | [ ] |
| 2818 | [Apply Operations to Maximize Score](https://leetcode.com/problems/apply-operations-to-maximize-score/) | Hard | 10/10 | 53.6% | [ ] |
| 3878 | [Count Good Subarrays](https://leetcode.com/problems/count-good-subarrays/) | Hard | 10/10 | 24.6% | [ ] |

## monotonic_stack_2d

**What it is** — 2D monotonic stack problems extend the standard 1D histogram technique to a matrix by processing the grid row by row and maintaining a height array that accumulates upward runs of valid cells. Each row of the matrix is converted into a 1D "histogram" problem, which is then solved with a monotonic stack. Recognize this pattern when a 2D problem reduces naturally to finding the largest rectangle, the number of dominant elements, or visibility in a grid.

**Common steps**
1. Build a `heights` array of length `n_cols`, initialized to zero.
2. For each row of the matrix, update `heights[j]` — increment if the cell is valid (e.g., `1`), reset to `0` if not.
3. Apply a 1D monotonic stack algorithm to the current `heights` array to compute the row's contribution to the answer.
4. Accumulate results across all rows.
5. For visibility or "can-see" problems, apply the stack column by column instead of row by row.

**Key variations**
- Largest filled rectangle in a binary matrix: Maximal Rectangle (classic histogram approach per row).
- Visibility counting in a grid (who can see whom): Number of People That Can Be Seen in a Grid (per-column decreasing stack).
- Finding sorted submatrices with bounded maximum: Find Sorted Submatrices With Maximum Element at Most K.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2282 | [Number of People That Can Be Seen in a Grid](https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/) :lock: | Medium | 7/10 | 47.5% | [ ] |
| 3359 | [Find Sorted Submatrices With Maximum Element at Most K](https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/) :lock: | Hard | 9/10 | 51.1% | [ ] |

## greedy_reverse_simulation

**What it is** — Greedy reverse simulation problems work backwards from the desired target state, repeatedly identifying and undoing the last valid operation that could have produced it. By reversing the problem — asking "what was stamped/applied last?" instead of "what to stamp/apply next?" — a greedy choice at each step becomes obvious and provably correct. Recognize this pattern when forward simulation is ambiguous but working backwards yields a clear unique or greedy choice.

**Common steps**
1. Start with the target state and simulate in reverse.
2. At each step, greedily find the most recent "valid" operation that could have been applied (e.g., a stamp position that matches the current pattern modulo wildcards).
3. Apply the reverse of that operation (mark those positions as wildcards/"don't care").
4. Record the operation in a list.
5. Repeat until all positions are wildcards (success) or no valid operation exists (failure).
6. Reverse the recorded list to produce the forward sequence of operations.

**Key variations**
- Currently, Stamping The Sequence is the primary representative of this pattern; variations would differ in what constitutes a "valid" reverse operation and how wildcards propagate.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 936 | [Stamping The Sequence](https://leetcode.com/problems/stamping-the-sequence/) | Hard | 9/10 | 62.3% | [ ] |
