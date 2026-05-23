# Backtracking

69 problems across 11 patterns.

## combination_generation

**What it is:** Combination generation is the process of selecting a fixed-size (or variable-size) subset of elements from a pool where order does not matter. Recognize this pattern when a problem asks you to enumerate all ways to pick k items from n, or to build valid sequences character-by-character from a constrained alphabet (e.g., phone digits, parentheses).

**Common steps:**
1. Define a recursive helper that takes the current index (or start position) and the current partial result.
2. At each call, decide whether to include the next candidate element and recurse forward.
3. Use a `start` pointer to avoid re-picking earlier elements, enforcing the "no repeat, forward-only" invariant that makes it a combination rather than a permutation.
4. Add the current partial result to the answer list when it reaches the target size or satisfies the completion condition.
5. Backtrack by removing the last added element before trying the next candidate.

**Key variations:**
- Fixed k vs. all lengths (Combinations vs. Subsets problems overlap here).
- Alphabet-mapped input: phone digits map to letter sets; brace groups map to character sets — iterate each mapped character instead of raw indices.
- Validity constraints that prune early (e.g., Generate Parentheses tracks open/close counts and prunes invalid states immediately).
- Iterator-style problems (1286) require storing state between `next()` calls rather than collecting all results at once.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 77 | [Combinations](https://leetcode.com/problems/combinations/) | Medium | 4/10 | 74.5% | [ ] |
| 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | 4/10 | 66.0% | [x] |
| 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | 5/10 | 78.6% | [ ] |
| 1286 | [Iterator for Combination](https://leetcode.com/problems/iterator-for-combination/) | Medium | 5/10 | 72.6% | [ ] |
| 1087 | [Brace Expansion](https://leetcode.com/problems/brace-expansion/) :lock: | Medium | 5/10 | 66.9% | [ ] |
| 254 | [Factor Combinations](https://leetcode.com/problems/factor-combinations/) :lock: | Medium | 6/10 | 50.5% | [ ] |
| 1467 | [Probability of a Two Boxes Having The Same Number of Distinct Balls](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/) | Hard | 8/10 | 61.1% | [ ] |

## subset_enumeration

**What it is:** Subset enumeration explores the full power set of a collection — every possible sub-selection including the empty set and the full set. Recognize this pattern when a problem asks "how many / which subsets satisfy property X" and the input size is small enough (typically n <= 20) for exponential-time search.

**Common steps:**
1. Start a recursive helper at index 0 with an empty current subset.
2. At each index, make two choices: skip the current element, or include it and recurse to the next index.
3. Record the current subset (or update a running aggregate) at every node of the recursion tree, not just leaf nodes.
4. If duplicates exist in the input, sort first and skip duplicate elements at the same recursion depth to avoid counting the same subset twice.
5. Backtrack by removing the last added element after the "include" branch returns.

**Key variations:**
- Collect all subsets vs. count subsets satisfying a condition (e.g., 2044 counts subsets with maximum bitwise OR).
- Duplicate elements require a sort-and-skip deduplication step (Subsets II vs. Subsets).
- Subsequence ordering constraints (Non-decreasing Subsequences) require checking the last element rather than sorting and skipping.
- Aggregate optimization (Closest Dessert Cost, Beautiful Subsets) tracks a running value and prunes branches that can't improve the best answer.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2044 | [Count Number of Maximum Bitwise-OR Subsets](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/) | Medium | 4/10 | 89.5% | [ ] |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | Medium | 4/10 | 82.3% | [x] |
| 491 | [Non-decreasing Subsequences](https://leetcode.com/problems/non-decreasing-subsequences/) | Medium | 5/10 | 62.7% | [ ] |
| 90 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium | 5/10 | 61.2% | [ ] |
| 1774 | [Closest Dessert Cost](https://leetcode.com/problems/closest-dessert-cost/) | Medium | 5/10 | 48.7% | [ ] |
| 2597 | [The Number of Beautiful Subsets](https://leetcode.com/problems/the-number-of-beautiful-subsets/) | Medium | 6/10 | 51.0% | [ ] |
| 2014 | [Longest Subsequence Repeated k Times](https://leetcode.com/problems/longest-subsequence-repeated-k-times/) | Hard | 8/10 | 71.2% | [ ] |

## combination_sum

**What it is:** Combination sum is a variant of combination generation where elements are chosen to reach a specific numerical target, and elements may be reused (or not). Recognize this pattern when a problem asks for all combinations of numbers that sum to a target value with constraints on reuse and uniqueness.

**Common steps:**
1. Sort the candidates array — this enables early termination when a candidate already exceeds the remaining target.
2. Define a recursive helper with parameters: current start index, remaining target, and current path.
3. Iterate candidates from the start index; for each candidate, if it exceeds the remaining target, break immediately (pruning).
4. Include the candidate, subtract it from the remaining target, and recurse — allowing the same index again if reuse is permitted, or advancing the index if not.
5. When remaining target reaches exactly 0, add the current path to results.
6. Backtrack by removing the last candidate and continuing the loop.

**Key variations:**
- Reuse allowed (Combination Sum): recurse with the same index.
- No reuse, no duplicates (Combination Sum III): recurse with index + 1, pick exactly k numbers.
- No reuse, input has duplicates (Combination Sum II): sort, recurse with index + 1, and skip `candidates[i] == candidates[i-1]` at the same depth to deduplicate.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | 5/10 | 76.5% | [ ] |
| 216 | [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/) | Medium | 5/10 | 73.2% | [ ] |
| 40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Medium | 6/10 | 59.4% | [ ] |

## permutation_generation

**What it is:** Permutation generation constructs all ordered arrangements of a set of elements. Recognize this pattern when a problem asks for every possible ordering, or when the position of each element in the result matters (unlike combinations, where order is irrelevant).

**Common steps:**
1. Maintain a boolean `used[]` array (or swap elements in-place) to track which elements are already in the current permutation.
2. At each recursive call, iterate over all elements; skip those already used.
3. Add the chosen element to the current path and mark it used, then recurse to fill the next position.
4. When the path length equals the number of elements, record the complete permutation.
5. Backtrack by removing the last element and marking it unused before the next loop iteration.
6. For duplicates (Permutations II): sort the array first, and skip `nums[i] == nums[i-1]` when `used[i-1]` is false (same-depth duplicate pruning).

**Key variations:**
- All elements used exactly once (standard Permutations) vs. counting valid arrangements without collecting them (Letter Tile Possibilities).
- Duplicate elements require sort-and-skip deduplication (Permutations II, Palindrome Permutation II).
- Problem-specific validity filters applied at each position (Number of Squareful Arrays checks that adjacent pairs are perfect squares).
- Optimization problems that generate permutations to find the maximum (Largest Time for Given Digits).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 46 | [Permutations](https://leetcode.com/problems/permutations/) | Medium | 4/10 | 81.9% | [x] |
| 949 | [Largest Time for Given Digits](https://leetcode.com/problems/largest-time-for-given-digits/) | Medium | 4/10 | 35.9% | [ ] |
| 1079 | [Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities/) | Medium | 5/10 | 83.5% | [ ] |
| 47 | [Permutations II](https://leetcode.com/problems/permutations-ii/) | Medium | 6/10 | 63.4% | [ ] |
| 267 | [Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/) :lock: | Medium | 6/10 | 42.3% | [ ] |
| 996 | [Number of Squareful Arrays](https://leetcode.com/problems/number-of-squareful-arrays/) | Hard | 8/10 | 51.4% | [ ] |

## string_generation

**What it is:** String generation builds valid strings character-by-character where each position has a constrained set of choices. Recognize this pattern when a problem asks to enumerate or count strings of a given length satisfying local character-level rules (no adjacent duplicates, digit constraints, symmetry requirements, etc.).

**Common steps:**
1. Define a recursive helper that tracks the current position in the string and the characters chosen so far.
2. At each position, iterate over the valid character choices (which may depend on the previous character or other state).
3. Apply local validity checks before recursing — prune the branch immediately if the choice violates the constraint.
4. When the string reaches the target length (or satisfies the completion condition), record or count it.
5. Backtrack by removing the last character (or popping from a list) before trying the next choice.

**Key variations:**
- Avoiding adjacent duplicates (Generate Binary Strings, Happy Strings): filter choices based on the last character appended.
- Symmetric construction (Strobogrammatic Numbers): build from both ends inward simultaneously, choosing valid pairs.
- Count vs. collect: some problems only need the k-th result or a count, allowing early termination once the target is reached.
- Removal-based generation (Remove Invalid Parentheses): instead of building from scratch, generate all strings reachable by deleting characters, then filter by validity.
- Digit-sequence problems (Numbers With Same Consecutive Differences): treat digits as the alphabet and enforce an absolute-difference constraint between consecutive digits.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3211 | [Generate Binary Strings Without Adjacent Zeros](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/) | Medium | 3/10 | 88.3% | [ ] |
| 784 | [Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/) | Medium | 4/10 | 75.8% | [ ] |
| 1415 | [The k-th Lexicographical String of All Happy Strings of Length n](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/) | Medium | 5/10 | 87.1% | [ ] |
| 320 | [Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/) :lock: | Medium | 5/10 | 60.4% | [ ] |
| 967 | [Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/) | Medium | 5/10 | 59.2% | [ ] |
| 247 | [Strobogrammatic Number II](https://leetcode.com/problems/strobogrammatic-number-ii/) :lock: | Medium | 6/10 | 53.5% | [ ] |
| 301 | [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/) | Hard | 8/10 | 49.9% | [ ] |
| 1088 | [Confusing Number II](https://leetcode.com/problems/confusing-number-ii/) :lock: | Hard | 8/10 | 47.1% | [ ] |
| 248 | [Strobogrammatic Number III](https://leetcode.com/problems/strobogrammatic-number-iii/) :lock: | Hard | 8/10 | 42.7% | [ ] |
| 3646 | [Next Special Palindrome Number](https://leetcode.com/problems/next-special-palindrome-number/) | Hard | 9/10 | 28.1% | [ ] |

## string_partitioning

**What it is:** String partitioning splits a string into a sequence of substrings where each part must satisfy some condition (e.g., is a palindrome, is a valid IP segment, forms a Fibonacci sequence). Recognize this pattern when a problem asks you to enumerate or validate all ways to "cut" a string at different positions.

**Common steps:**
1. Define a recursive helper with the current start index into the string.
2. Iterate all possible end indices from start to the end of the string, forming the next substring `s[start:end+1]`.
3. Check whether the current substring satisfies the required property; if not, skip (prune) it.
4. If valid, add the substring to the current partition and recurse from `end + 1`.
5. When the start index reaches the end of the string, the current partition is complete — record it.
6. Backtrack by removing the last added substring before trying the next end index.

**Key variations:**
- Palindrome check per segment (Palindrome Partitioning): precompute a 2D palindrome table to make validity O(1).
- Fixed format with hard upper bounds (Restore IP Addresses): each segment has a maximum length and value, enabling aggressive pruning.
- Numeric sequence constraints (Split Array into Fibonacci, Additive Number): the first two chosen numbers fully determine all subsequent ones, so only the first split point needs backtracking.
- Uniqueness constraint (Split into Max Unique Substrings): track a set of already-used substrings and prune duplicate choices.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium | 5/10 | 74.0% | [ ] |
| 1593 | [Split a String Into the Max Number of Unique Substrings](https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/) | Medium | 6/10 | 68.7% | [ ] |
| 93 | [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) | Medium | 6/10 | 55.9% | [ ] |
| 842 | [Split Array into Fibonacci Sequence](https://leetcode.com/problems/split-array-into-fibonacci-sequence/) | Medium | 7/10 | 40.3% | [ ] |
| 1849 | [Splitting a String Into Descending Consecutive Values](https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/) | Medium | 7/10 | 37.6% | [ ] |
| 306 | [Additive Number](https://leetcode.com/problems/additive-number/) | Medium | 7/10 | 33.8% | [ ] |

## partition_into_k_subsets

**What it is:** Partition into k subsets assigns every element of an array into exactly k groups such that each group satisfies a target condition (usually equal sum or minimum maximum). Recognize this pattern when a problem requires exhaustive assignment of all elements into a fixed number of buckets with a goal on the bucket values.

**Common steps:**
1. Sort the elements in descending order — placing large elements first prunes infeasible branches quickly.
2. Maintain an array of k running bucket sums (or counts).
3. Define a recursive helper that assigns the current element to one of the k buckets.
4. For each bucket, check feasibility before placing (e.g., bucket sum + element <= target); skip if not feasible.
5. Skip duplicate bucket values at the same recursion depth to avoid redundant symmetric assignments.
6. When all elements are assigned, check if the condition is satisfied; backtrack otherwise.

**Key variations:**
- Minimize the maximum bucket value (Fair Distribution of Cookies) vs. verify all buckets hit an exact target (Partition to K Equal Sum Subsets, Matchsticks to Square).
- Pruning strength: equal-target problems can terminate a branch the moment any bucket exceeds target; min-max problems prune when the current maximum is already worse than the best found.
- k=4 is a special case (Matchsticks to Square) — the target is total/4 and any element exceeding target can be pruned before starting.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2305 | [Fair Distribution of Cookies](https://leetcode.com/problems/fair-distribution-of-cookies/) | Medium | 6/10 | 69.9% | [ ] |
| 473 | [Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) | Medium | 7/10 | 41.8% | [ ] |
| 698 | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | Medium | 7/10 | 38.6% | [ ] |

## grid_path_search

**What it is:** Grid path search explores paths through a 2D (or graph) space, marking cells visited as part of the current path and unmarking them on backtrack. Recognize this pattern when a problem asks for all paths, the best path, or whether a path exists in a grid where the same cell cannot be revisited within a single path.

**Common steps:**
1. Choose a starting cell (or iterate all cells if any can be a start).
2. Mark the current cell as visited (modify the grid in place or use a visited set).
3. Recursively explore all valid neighbors (up/down/left/right, or problem-specific moves like a knight's L-shape).
4. At each neighbor, check boundary conditions, the visited flag, and any problem-specific validity rule before recursing.
5. Update any running aggregate (gold collected, path length, word matched) and record the result at a terminal condition.
6. Backtrack by unmarking the current cell and undoing the aggregate update before returning.

**Key variations:**
- Word matching (Word Search): compare the current cell to a target character at the corresponding word index and prune mismatches immediately.
- Full-coverage requirement (Unique Paths III): count all non-obstacle cells first; only record a path when all cells are visited.
- Graph instead of grid (Maximum Path Quality): use an adjacency list and allow revisiting nodes, but not revisiting edges in the same traversal.
- Robot with relative movement (Robot Room Cleaner): no direct coordinate access; use direction vectors and a relative-coordinate visited set.
- Optimization (Path with Maximum Gold): try all valid starting cells and track the maximum gold accumulated.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1219 | [Path with Maximum Gold](https://leetcode.com/problems/path-with-maximum-gold/) | Medium | 5/10 | 68.4% | [ ] |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) | Medium | 6/10 | 47.3% | [ ] |
| 2664 | [The Knight's Tour](https://leetcode.com/problems/the-knights-tour/) :lock: | Medium | 7/10 | 72.7% | [ ] |
| 3565 | [Sequential Grid Path Cover](https://leetcode.com/problems/sequential-grid-path-cover/) :lock: | Medium | 7/10 | 60.5% | [ ] |
| 980 | [Unique Paths III](https://leetcode.com/problems/unique-paths-iii/) | Hard | 8/10 | 82.8% | [ ] |
| 489 | [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/) :lock: | Hard | 8/10 | 78.0% | [ ] |
| 2065 | [Maximum Path Quality of a Graph](https://leetcode.com/problems/maximum-path-quality-of-a-graph/) | Hard | 8/10 | 62.1% | [ ] |

## bitmask_backtracking

**What it is:** Bitmask backtracking uses an integer bitmask to compactly represent which elements have been used or which constraints have been met, replacing a boolean `used[]` array with bitwise operations. Recognize this pattern when n is small (typically <= 20), you need to track element usage or character coverage, and bit operations can speed up state transitions and pruning.

**Common steps:**
1. Represent the set of used/available elements as a bitmask (one bit per element).
2. In the recursive helper, iterate over all bits that are still unset (available elements).
3. Set the bit for the chosen element (`mask | (1 << i)`) and recurse.
4. Apply any validity or pruning check using bitwise AND/OR before recursing (e.g., check character overlap with `mask & char_mask == 0`).
5. Update any running value (score, length, count) and record the best result at a terminal condition.
6. Backtrack implicitly — since the bitmask is passed by value (or restored), no explicit undo is needed in many implementations.

**Key variations:**
- Existence check (Beautiful Arrangement): verify `i % pos == 0 || pos % i == 0` at each position before placing.
- Character set intersection (Maximum Length of Concatenated String): use a bitmask per string to check for overlapping characters in O(1).
- Scoring (Maximum Score Words): track letter frequency counts alongside the bitmask and accumulate word scores.
- Full enumeration of subsets (Maximum Number of Achievable Transfer Requests): iterate all 2^n request subsets and check net flow balance.
- Debt settlement (Optimal Account Balancing): enumerate assignments of debtors to creditors using a bitmask of remaining unpaid parties.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 526 | [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) | Medium | 6/10 | 64.8% | [ ] |
| 1239 | [Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) | Medium | 6/10 | 54.7% | [ ] |
| 1255 | [Maximum Score Words Formed by Letters](https://leetcode.com/problems/maximum-score-words-formed-by-letters/) | Hard | 7/10 | 81.5% | [ ] |
| 351 | [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/) :lock: | Medium | 7/10 | 53.8% | [ ] |
| 2850 | [Minimum Moves to Spread Stones Over Grid](https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/) | Medium | 7/10 | 45.6% | [ ] |
| 1601 | [Maximum Number of Achievable Transfer Requests](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/) | Hard | 8/10 | 64.7% | [ ] |
| 465 | [Optimal Account Balancing](https://leetcode.com/problems/optimal-account-balancing/) :lock: | Hard | 9/10 | 50.4% | [ ] |
| 411 | [Minimum Unique Word Abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation/) :lock: | Hard | 9/10 | 40.5% | [ ] |

## constraint_satisfaction

**What it is:** Constraint satisfaction places elements into a structured layout (grid, sequence, board) one at a time, enforcing hard rules that must hold globally across the entire configuration. Recognize this pattern when a problem resembles a puzzle — N-Queens, Sudoku, word squares — where each placement restricts what can be placed at all future positions.

**Common steps:**
1. Identify the "next empty slot" to fill (the next row, the next empty cell, the next position in the sequence).
2. Iterate all candidate values for that slot.
3. Check whether the candidate is valid given everything placed so far — use efficient data structures (row/col/box sets for Sudoku, column/diagonal sets for N-Queens) for O(1) conflict detection.
4. Place the candidate and update the constraint tracking structures.
5. Recurse to fill the next slot; if recursion succeeds, return immediately (for existence problems) or continue (for enumeration problems).
6. Backtrack by removing the candidate and restoring the constraint structures.

**Key variations:**
- Existence vs. enumeration: Sudoku Solver returns as soon as one solution is found; N-Queens counts or collects all solutions.
- Row-by-row placement (N-Queens): one queen per row guarantees no row conflicts; only track column and two diagonal sets.
- Cell-by-cell placement (Sudoku): scan cells left-to-right, top-to-bottom; skip pre-filled cells.
- Word-based constraints (Word Squares, Word Pattern II): use a trie or prefix map to prune invalid placements before completing a word.
- Sequence construction with distance constraints (1718 Largest Valid Sequence): placing element k at position i forces element k to also be placed at i + k, so check both positions together.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1718 | [Construct the Lexicographically Largest Valid Sequence](https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/) | Medium | 6/10 | 72.7% | [ ] |
| 756 | [Pyramid Transition Matrix](https://leetcode.com/problems/pyramid-transition-matrix/) | Medium | 7/10 | 60.6% | [ ] |
| 291 | [Word Pattern II](https://leetcode.com/problems/word-pattern-ii/) :lock: | Medium | 7/10 | 48.8% | [ ] |
| 52 | [N-Queens II](https://leetcode.com/problems/n-queens-ii/) | Hard | 8/10 | 78.6% | [ ] |
| 51 | [N-Queens](https://leetcode.com/problems/n-queens/) | Hard | 8/10 | 75.5% | [ ] |
| 37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | Hard | 8/10 | 65.5% | [ ] |
| 425 | [Word Squares](https://leetcode.com/problems/word-squares/) :lock: | Hard | 8/10 | 54.7% | [ ] |
| 1240 | [Tiling a Rectangle with the Fewest Squares](https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/) | Hard | 9/10 | 54.9% | [ ] |
| 2056 | [Number of Valid Move Combinations On Chessboard](https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/) | Hard | 9/10 | 48.7% | [ ] |
| 1307 | [Verbal Arithmetic Puzzle](https://leetcode.com/problems/verbal-arithmetic-puzzle/) | Hard | 9/10 | 34.8% | [ ] |

## expression_building

**What it is:** Expression building inserts operators (or applies operations) between numbers or values to reach a target result, exploring all possible operator placements and operand groupings. Recognize this pattern when a problem asks you to combine a fixed set of numbers with arithmetic operators to evaluate to a specific value, or to enumerate all arithmetically distinct expressions.

**Common steps:**
1. Define a recursive helper that processes the input left-to-right, carrying the expression built so far and a running evaluated value.
2. At each position, try inserting each valid operator ('+', '-', '*', or none for multi-digit number concatenation) between the current position and the next.
3. For multiplication, track the last operand separately so you can undo its contribution and re-apply with the new factor (since multiplication breaks left-to-right accumulation).
4. Recurse with the updated expression string, running total, and last-operand value.
5. When the entire input is consumed, check if the running total matches the target and record the expression if so.
6. For problems like the 24 Game, apply operators to all permutations of operands and all recursive sub-groupings rather than a fixed left-to-right order.

**Key variations:**
- Fixed target (Expression Add Operators): carry `current_value` and `last_operand`; multiplication requires `current + (last * next) - last`.
- No fixed target, check reachability (24 Game): try all permutations of 4 numbers and all pairwise operator applications recursively until one number remains; compare to 24 with floating-point epsilon.
- Multi-digit numbers: when concatenating digits, track whether leading zeros form an invalid multi-digit number and prune those branches.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 679 | [24 Game](https://leetcode.com/problems/24-game/) | Hard | 8/10 | 59.5% | [ ] |
| 282 | [Expression Add Operators](https://leetcode.com/problems/expression-add-operators/) | Hard | 8/10 | 43.1% | [ ] |
