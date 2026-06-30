# Arrays

224 problems across 12 patterns.

## hash_map_frequency

**What it is** — This pattern uses a hash map (dictionary) to count how many times each element appears, then answers questions about those counts. Recognize it when a problem asks about duplicates, element frequency, matching between two arrays, or any question where "how often does X appear" is the key insight.

**Common steps**
1. Iterate through the array(s) and populate a `freq` map: `freq[x] += 1`.
2. Iterate through the map (or a second array) and apply the problem's condition to the counts.
3. If comparing two arrays, build a freq map for each, then compare maps or look up one map while iterating the other.
4. Return the collected results (a count, a list, a boolean, etc.).

**Key variations**
- Single array frequency check (all equal, lucky number, degree of array).
- Two-array intersection / difference (check membership, find common elements).
- Frequency-of-frequency (e.g., "how many elements appear exactly once").
- Counting pairs that satisfy a relationship (a + k = b, a + b = target, etc.).
- Multi-key hash maps where the key is a tuple or frozenset (grid illumination, image overlap).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2006 | [Count Number of Pairs With Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/) | Easy | 1/10 | 85.4% | [ ] |
| 2215 | [Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) | Easy | 1/10 | 81.4% | [ ] |
| 961 | [N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) | Easy | 1/10 | 79.9% | [ ] |
| 1436 | [Destination City](https://leetcode.com/problems/destination-city/) | Easy | 1/10 | 79.5% | [ ] |
| 1941 | [Check if All Characters Have Equal Number of Occurrences](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/) | Easy | 1/10 | 79.5% | [ ] |
| 2206 | [Divide Array Into Equal Pairs](https://leetcode.com/problems/divide-array-into-equal-pairs/) | Easy | 1/10 | 79.2% | [ ] |
| 1460 | [Make Two Arrays Equal by Reversing Subarrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/) | Easy | 1/10 | 75.8% | [ ] |
| 1394 | [Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-integer-in-an-array/) | Easy | 1/10 | 75.5% | [ ] |
| 575 | [Distribute Candies](https://leetcode.com/problems/distribute-candies/) | Easy | 1/10 | 71.1% | [ ] |
| 2068 | [Check Whether Two Strings are Almost Equivalent](https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/) | Easy | 1/10 | 64.3% | [ ] |
| 2229 | [Check if an Array Is Consecutive](https://leetcode.com/problems/check-if-an-array-is-consecutive/) :lock: | Easy | 1/10 | 62.2% | [ ] |
| 2190 | [Most Frequent Number Following Key In an Array](https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/) | Easy | 1/10 | 59.5% | [ ] |
| 2053 | [Kth Distinct String in an Array](https://leetcode.com/problems/kth-distinct-string-in-an-array/) | Easy | 2/10 | 82.1% | [ ] |
| 2032 | [Two Out of Three](https://leetcode.com/problems/two-out-of-three/) | Easy | 2/10 | 77.6% | [ ] |
| 2085 | [Count Common Words With One Occurrence](https://leetcode.com/problems/count-common-words-with-one-occurrence/) | Easy | 2/10 | 73.4% | [ ] |
| 2273 | [Find Resultant Array After Removing Anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/) | Easy | 2/10 | 69.9% | [ ] |
| 2248 | [Intersection of Multiple Arrays](https://leetcode.com/problems/intersection-of-multiple-arrays/) | Easy | 2/10 | 68.7% | [ ] |
| 1426 | [Counting Elements](https://leetcode.com/problems/counting-elements/) :lock: | Easy | 2/10 | 60.8% | [ ] |
| 599 | [Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) | Easy | 2/10 | 59.8% | [ ] |
| 1346 | [Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/) | Easy | 2/10 | 41.8% | [ ] |
| 2094 | [Finding 3-Digit Even Numbers](https://leetcode.com/problems/finding-3-digit-even-numbers/) | Easy | 3/10 | 78.7% | [ ] |
| 1995 | [Count Special Quadruplets](https://leetcode.com/problems/count-special-quadruplets/) | Easy | 3/10 | 64.7% | [ ] |
| 594 | [Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/) | Easy | 3/10 | 64.6% | [ ] |
| 697 | [Degree of an Array](https://leetcode.com/problems/degree-of-an-array/) | Easy | 3/10 | 58.3% | [ ] |
| 953 | [Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/) | Easy | 3/10 | 55.9% | [ ] |
| 2023 | [Number of Pairs of Strings With Concatenation Equal to Target](https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/) | Medium | 4/10 | 75.4% | [ ] |
| 2225 | [Find Players With Zero or One Losses](https://leetcode.com/problems/find-players-with-zero-or-one-losses/) | Medium | 4/10 | 72.5% | [ ] |
| 2150 | [Find All Lonely Numbers in the Array](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/) | Medium | 4/10 | 63.0% | [ ] |
| 554 | [Brick Wall](https://leetcode.com/problems/brick-wall/) | Medium | 4/10 | 56.0% | [ ] |
| 1072 | [Flip Columns For Maximum Number of Equal Rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/) | Medium | 5/10 | 78.5% | [ ] |
| 1418 | [Display Table of Food Orders in a Restaurant](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/) | Medium | 5/10 | 76.3% | [ ] |
| 3071 | [Minimum Operations to Write the Letter Y on a Grid](https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/) | Medium | 5/10 | 64.5% | [ ] |
| 1452 | [People Whose List of Favorite Companies Is Not a Subset of Another List](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/) | Medium | 5/10 | 60.6% | [ ] |
| 1487 | [Making File Names Unique](https://leetcode.com/problems/making-file-names-unique/) | Medium | 5/10 | 38.7% | [ ] |
| 835 | [Image Overlap](https://leetcode.com/problems/image-overlap/) | Medium | 6/10 | 64.0% | [ ] |
| 1001 | [Grid Illumination](https://leetcode.com/problems/grid-illumination/) | Hard | 7/10 | 39.3% | [ ] |

## greedy_linear_scan

**What it is** — This pattern solves problems by making locally optimal decisions in a single left-to-right (or right-to-left) pass through the array, maintaining a small amount of running state (current max, current streak, a few tracked values). Recognize it when the answer can be built incrementally without backtracking and no subarray window is needed.

**Common steps**
1. Initialize tracking variables before the loop (e.g., `max_val`, `streak`, `result`).
2. Iterate through the array one element at a time.
3. At each position, update your running state based on the current element and the previous state.
4. Apply the greedy decision: keep, reset, or extend the current best.
5. After the loop, return the accumulated result or the final state.

**Key variations**
- Track a single running maximum/minimum (largest, second-largest, majority element).
- Track a streak or consecutive run (max consecutive ones, longest increasing subsequence).
- Two-pointer left-and-right boundary scans (shortest unsorted subarray, valid mountain array).
- Multi-pass scan (scan left for one value, scan right for another, then combine).
- Boyer-Moore voting (majority element, majority element II).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1773 | [Count Items Matching a Rule](https://leetcode.com/problems/count-items-matching-a-rule/) | Easy | 1/10 | 85.3% | [ ] |
| 1464 | [Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) | Easy | 1/10 | 83.6% | [ ] |
| 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Easy | 1/10 | 65.1% | [ ] |
| 896 | [Monotonic Array](https://leetcode.com/problems/monotonic-array/) | Easy | 1/10 | 62.3% | [ ] |
| 1213 | [Intersection of Three Sorted Arrays](https://leetcode.com/problems/intersection-of-three-sorted-arrays/) :lock: | Easy | 2/10 | 80.0% | [ ] |
| 821 | [Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/) | Easy | 2/10 | 72.8% | [ ] |
| 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | Easy | 2/10 | 66.3% | [x] |
| 243 | [Shortest Word Distance](https://leetcode.com/problems/shortest-word-distance/) :lock: | Easy | 2/10 | 66.3% | [ ] |
| 1629 | [Slowest Key](https://leetcode.com/problems/slowest-key/) | Easy | 2/10 | 59.6% | [ ] |
| 228 | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) | Easy | 2/10 | 54.2% | [ ] |
| 747 | [Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) | Easy | 2/10 | 52.4% | [ ] |
| 674 | [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/) | Easy | 2/10 | 52.0% | [ ] |
| 66 | [Plus One](https://leetcode.com/problems/plus-one/) | Easy | 2/10 | 49.9% | [ ] |
| 628 | [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/) | Easy | 2/10 | 45.9% | [ ] |
| 414 | [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) | Easy | 2/10 | 39.3% | [ ] |
| 941 | [Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/) | Easy | 2/10 | 35.2% | [ ] |
| 245 | [Shortest Word Distance III](https://leetcode.com/problems/shortest-word-distance-iii/) :lock: | Medium | 3/10 | 59.5% | [ ] |
| 717 | [1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/) | Easy | 3/10 | 49.6% | [ ] |
| 163 | [Missing Ranges](https://leetcode.com/problems/missing-ranges/) :lock: | Easy | 3/10 | 35.7% | [ ] |
| 1940 | [Longest Common Subsequence Between Sorted Arrays](https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/) :lock: | Medium | 4/10 | 81.2% | [ ] |
| 3195 | [Find the Minimum Area to Cover All Ones I](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/) | Medium | 4/10 | 78.1% | [ ] |
| 2495 | [Number of Subarrays Having Even Product](https://leetcode.com/problems/number-of-subarrays-having-even-product/) :lock: | Medium | 4/10 | 63.2% | [ ] |
| 849 | [Maximize Distance to Closest Person](https://leetcode.com/problems/maximize-distance-to-closest-person/) | Medium | 4/10 | 49.7% | [ ] |
| 1395 | [Count Number of Teams](https://leetcode.com/problems/count-number-of-teams/) | Medium | 5/10 | 70.2% | [ ] |
| 229 | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) | Medium | 5/10 | 56.1% | [ ] |
| 2171 | [Removing Minimum Number of Magic Beans](https://leetcode.com/problems/removing-minimum-number-of-magic-beans/) | Medium | 5/10 | 44.6% | [ ] |
| 581 | [Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/) | Medium | 5/10 | 38.2% | [ ] |
| 2170 | [Minimum Operations to Make the Array Alternating](https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/) | Medium | 5/10 | 35.7% | [ ] |

## matrix_simulation

**What it is** — This pattern involves iterating over a 2D grid and performing cell-by-cell operations: reading neighbors, applying transformations, or tracing a path through the matrix. Recognize it when the problem describes a grid and asks you to compute values based on each cell's position, its neighbors, or a traversal order (spiral, diagonal, etc.).

**Common steps**
1. Determine the traversal order or the set of cells to visit (row-by-row, spiral, diagonal, etc.).
2. For each cell `(r, c)`, look up its neighbors using direction arrays `dr = [-1,0,1,0]`, `dc = [0,1,0,-1]`.
3. Apply the local rule or transformation (sum neighbors, check equality, simulate movement).
4. Write results to a new output matrix (or update in-place carefully to avoid read-write conflicts).
5. Return the transformed matrix or the aggregated answer.

**Key variations**
- In-place vs. copy matrix (Game of Life requires encoding old/new state in one cell value).
- Fixed-kernel windows (3x3 smoother, hourglass sum, magic square check).
- Diagonal / anti-diagonal traversal (group cells by `r-c` or `r+c`).
- Spiral traversal (maintain four boundaries and shrink them after each direction).
- Simulation with direction changes (ball fall, rook captures, knight tour validation).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1672 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/) | Easy | 1/10 | 88.7% | [ ] |
| 832 | [Flipping an Image](https://leetcode.com/problems/flipping-an-image/) | Easy | 1/10 | 83.7% | [ ] |
| 867 | [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/) | Easy | 1/10 | 76.3% | [ ] |
| 2373 | [Largest Local Values in a Matrix](https://leetcode.com/problems/largest-local-values-in-a-matrix/) | Easy | 2/10 | 87.7% | [ ] |
| 1572 | [Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/) | Easy | 2/10 | 84.2% | [ ] |
| 1380 | [Lucky Numbers in a Matrix](https://leetcode.com/problems/lucky-numbers-in-a-matrix/) | Easy | 2/10 | 80.0% | [ ] |
| 3643 | [Flip Square Submatrix Vertically](https://leetcode.com/problems/flip-square-submatrix-vertically/) | Easy | 2/10 | 79.4% | [ ] |
| 463 | [Island Perimeter](https://leetcode.com/problems/island-perimeter/) | Easy | 2/10 | 74.4% | [ ] |
| 2643 | [Row With Maximum Ones](https://leetcode.com/problems/row-with-maximum-ones/) | Easy | 2/10 | 74.3% | [ ] |
| 2946 | [Matrix Similarity After Cyclic Shifts](https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/) | Easy | 2/10 | 74.3% | [ ] |
| 2923 | [Find Champion I](https://leetcode.com/problems/find-champion-i/) | Easy | 2/10 | 73.4% | [ ] |
| 1582 | [Special Positions in a Binary Matrix](https://leetcode.com/problems/special-positions-in-a-binary-matrix/) | Easy | 2/10 | 72.7% | [ ] |
| 999 | [Available Captures for Rook](https://leetcode.com/problems/available-captures-for-rook/) | Easy | 2/10 | 71.7% | [ ] |
| 2639 | [Find the Width of Columns of a Grid](https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/) | Easy | 2/10 | 70.4% | [ ] |
| 766 | [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/) | Easy | 2/10 | 69.7% | [ ] |
| 661 | [Image Smoother](https://leetcode.com/problems/image-smoother/) | Easy | 2/10 | 69.3% | [ ] |
| 3033 | [Modify the Matrix](https://leetcode.com/problems/modify-the-matrix/) | Easy | 2/10 | 69.1% | [ ] |
| 1886 | [Determine Whether Matrix Can Be Obtained By Rotation](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/) | Easy | 2/10 | 68.3% | [ ] |
| 1260 | [Shift 2D Grid](https://leetcode.com/problems/shift-2d-grid/) | Easy | 2/10 | 68.0% | [ ] |
| 2319 | [Check if Matrix Is X-Matrix](https://leetcode.com/problems/check-if-matrix-is-x-matrix/) | Easy | 2/10 | 66.6% | [ ] |
| 3417 | [Zigzag Grid Traversal With Skip](https://leetcode.com/problems/zigzag-grid-traversal-with-skip/) | Easy | 2/10 | 65.2% | [ ] |
| 566 | [Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/) | Easy | 2/10 | 64.9% | [ ] |
| 2133 | [Check if Every Row and Column Contains All Numbers](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/) | Easy | 2/10 | 54.1% | [ ] |
| 2125 | [Number of Laser Beams in a Bank](https://leetcode.com/problems/number-of-laser-beams-in-a-bank/) | Medium | 3/10 | 87.0% | [ ] |
| 419 | [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board/) | Medium | 3/10 | 77.5% | [ ] |
| 3127 | [Make a Square with the Same Color](https://leetcode.com/problems/make-a-square-with-the-same-color/) | Easy | 3/10 | 53.2% | [ ] |
| 3142 | [Check if Grid Satisfies Conditions](https://leetcode.com/problems/check-if-grid-satisfies-conditions/) | Easy | 3/10 | 45.2% | [ ] |
| 422 | [Valid Word Square](https://leetcode.com/problems/valid-word-square/) :lock: | Easy | 3/10 | 42.9% | [ ] |
| 2482 | [Difference Between Ones and Zeros in Row and Column](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/) | Medium | 4/10 | 84.4% | [ ] |
| 3567 | [Minimum Absolute Difference in Sliding Submatrix](https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/) | Medium | 4/10 | 78.8% | [ ] |
| 2428 | [Maximum Sum of an Hourglass](https://leetcode.com/problems/maximum-sum-of-an-hourglass/) | Medium | 4/10 | 76.3% | [ ] |
| 59 | [Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | Medium | 4/10 | 75.0% | [ ] |
| 1267 | [Count Servers that Communicate](https://leetcode.com/problems/count-servers-that-communicate/) | Medium | 4/10 | 73.5% | [ ] |
| 1222 | [Queens That Can Attack the King](https://leetcode.com/problems/queens-that-can-attack-the-king/) | Medium | 4/10 | 72.6% | [ ] |
| 1706 | [Where Will the Ball Fall](https://leetcode.com/problems/where-will-the-ball-fall/) | Medium | 4/10 | 72.3% | [ ] |
| 2711 | [Difference of Number of Distinct Values on Diagonals](https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/) | Medium | 4/10 | 68.3% | [ ] |
| 531 | [Lonely Pixel I](https://leetcode.com/problems/lonely-pixel-i/) :lock: | Medium | 4/10 | 62.7% | [ ] |
| 2596 | [Check Knight Tour Configuration](https://leetcode.com/problems/check-knight-tour-configuration/) | Medium | 4/10 | 61.1% | [ ] |
| 885 | [Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/) | Medium | 5/10 | 84.5% | [ ] |
| 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | 5/10 | 80.0% | [ ] |
| 2257 | [Count Unguarded Cells in the Grid](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/) | Medium | 5/10 | 69.0% | [ ] |
| 498 | [Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/) | Medium | 5/10 | 67.1% | [ ] |
| 3078 | [Match Alphanumerical Pattern in Matrix I](https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/) :lock: | Medium | 5/10 | 64.7% | [ ] |
| 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | 5/10 | 62.8% | [ ] |
| 2061 | [Number of Spaces Cleaning Robot Cleaned](https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/) :lock: | Medium | 5/10 | 62.8% | [ ] |
| 1424 | [Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/) | Medium | 5/10 | 58.3% | [ ] |
| 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | 5/10 | 56.7% | [ ] |
| 840 | [Magic Squares In Grid](https://leetcode.com/problems/magic-squares-in-grid/) | Medium | 5/10 | 55.2% | [ ] |
| 2018 | [Check if Word Can Be Placed In Crossword](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/) | Medium | 5/10 | 50.8% | [ ] |
| 1958 | [Check if Move is Legal](https://leetcode.com/problems/check-if-move-is-legal/) | Medium | 5/10 | 50.0% | [ ] |
| 3030 | [Find the Grid of Region Average](https://leetcode.com/problems/find-the-grid-of-region-average/) | Medium | 5/10 | 43.4% | [ ] |
| 1861 | [Rotating the Box](https://leetcode.com/problems/rotating-the-box/) | Medium | 6/10 | 82.3% | [ ] |
| 289 | [Game of Life](https://leetcode.com/problems/game-of-life/) | Medium | 6/10 | 72.6% | [ ] |
| 1914 | [Cyclically Rotating a Grid](https://leetcode.com/problems/cyclically-rotating-a-grid/) | Medium | 6/10 | 51.8% | [ ] |
| 533 | [Lonely Pixel II](https://leetcode.com/problems/lonely-pixel-ii/) :lock: | Medium | 6/10 | 48.9% | [ ] |
| 723 | [Candy Crush](https://leetcode.com/problems/candy-crush/) :lock: | Medium | 7/10 | 77.4% | [ ] |

## sorting_and_ranking

**What it is** — This pattern sorts an array (or derives a sorted order) and then uses relative rank or position to answer the question. Recognize it when the problem asks for k-th largest/smallest, rankings, relative order, or any result that depends on where elements fall once sorted.

**Common steps**
1. Sort the array (or an auxiliary copy) with a custom comparator if needed.
2. Build an index or rank map: `rank[val] = i` for each element after sorting.
3. Iterate the original (unsorted) array and look up each element's rank.
4. Use the rank to construct the answer array or apply the problem's aggregation rule.
5. Return the result, sorted again if the output order is required.

**Key variations**
- Sort with a custom key (sort by k-th column, sort by absolute value, sort by vote counts).
- Coordinate compression: replace values with their rank to reduce range (rank transform).
- Sort each sub-structure independently (sort matrix diagonals, sort each row).
- Bucket / counting sort when values are bounded (how-many-smaller via frequency prefix).
- Radix / bucket sort for O(n) maximum-gap style problems.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3667 | [Sort Array By Absolute Value](https://leetcode.com/problems/sort-array-by-absolute-value/) :lock: | Easy | 1/10 | 86.3% | [ ] |
| 2418 | [Sort the People](https://leetcode.com/problems/sort-the-people/) | Easy | 1/10 | 84.8% | [ ] |
| 1365 | [How Many Numbers Are Smaller Than the Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/) | Easy | 2/10 | 87.4% | [ ] |
| 1122 | [Relative Sort Array](https://leetcode.com/problems/relative-sort-array/) | Easy | 2/10 | 75.2% | [ ] |
| 506 | [Relative Ranks](https://leetcode.com/problems/relative-ranks/) | Easy | 2/10 | 74.6% | [ ] |
| 1030 | [Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/) | Easy | 2/10 | 74.1% | [ ] |
| 1331 | [Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/) | Easy | 2/10 | 70.8% | [ ] |
| 2545 | [Sort the Students by Their Kth Score](https://leetcode.com/problems/sort-the-students-by-their-kth-score/) | Medium | 3/10 | 86.0% | [ ] |
| 2500 | [Delete Greatest Value in Each Row](https://leetcode.com/problems/delete-greatest-value-in-each-row/) | Easy | 3/10 | 79.9% | [ ] |
| 3446 | [Sort Matrix by Diagonals](https://leetcode.com/problems/sort-matrix-by-diagonals/) | Medium | 4/10 | 84.7% | [ ] |
| 1630 | [Arithmetic Subarrays](https://leetcode.com/problems/arithmetic-subarrays/) | Medium | 4/10 | 83.7% | [ ] |
| 1329 | [Sort the Matrix Diagonally](https://leetcode.com/problems/sort-the-matrix-diagonally/) | Medium | 4/10 | 83.2% | [ ] |
| 1366 | [Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/) | Medium | 5/10 | 60.1% | [ ] |
| 2343 | [Query Kth Smallest Trimmed Number](https://leetcode.com/problems/query-kth-smallest-trimmed-number/) | Medium | 5/10 | 47.5% | [ ] |
| 3759 | [Count Elements With at Least K Greater Values](https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/) | Medium | 5/10 | 31.5% | [ ] |
| 164 | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) | Medium | 7/10 | 52.0% | [ ] |
| 2371 | [Minimize Maximum Value in a Grid](https://leetcode.com/problems/minimize-maximum-value-in-a-grid/) :lock: | Hard | 8/10 | 70.1% | [ ] |
| 2659 | [Make Array Empty](https://leetcode.com/problems/make-array-empty/) | Hard | 9/10 | 27.0% | [ ] |

## simulation

**What it is** — This pattern directly models the process described in the problem statement, step by step, without an algorithmic shortcut. Recognize it when the problem says "perform the following operations" or describes a game/machine whose rules you must faithfully replicate; the solution complexity matches the number of operations.

**Common steps**
1. Set up the initial state (array, board, variable, pointer, queue, etc.).
2. Parse or iterate through the list of operations/commands one at a time.
3. For each operation, update the state exactly as the problem describes.
4. Guard against edge cases (out-of-bounds moves, no-op commands, wrap-around).
5. After all operations are processed, extract and return the final answer from the state.

**Key variations**
- 1D array updates (apply queries, multiply/shift values, track a variable).
- 2D grid or board simulation (robot movement, tic-tac-toe, ball mechanics).
- Cycle detection to skip redundant iterations (Prison Cells After N Days).
- State-machine or rule-based simulation (reveal cards, pour water, read-N-characters).
- Multi-step validation (check that a sequence of moves produces a valid end state).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2011 | [Final Value of Variable After Performing Operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/) | Easy | 1/10 | 90.6% | [ ] |
| 657 | [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/) | Easy | 1/10 | 78.1% | [ ] |
| 2154 | [Keep Multiplying Found Values by Two](https://leetcode.com/problems/keep-multiplying-found-values-by-two/) | Easy | 1/10 | 75.0% | [ ] |
| 806 | [Number of Lines To Write String](https://leetcode.com/problems/number-of-lines-to-write-string/) | Easy | 1/10 | 72.5% | [ ] |
| 1275 | [Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) | Easy | 2/10 | 54.6% | [ ] |
| 3865 | [Reverse K Subarrays](https://leetcode.com/problems/reverse-k-subarrays/) :lock: | Medium | 4/10 | 89.4% | [ ] |
| 3653 | [XOR After Range Multiplication Queries I](https://leetcode.com/problems/xor-after-range-multiplication-queries-i/) | Medium | 4/10 | 73.3% | [ ] |
| 985 | [Sum of Even Numbers After Queries](https://leetcode.com/problems/sum-of-even-numbers-after-queries/) | Medium | 4/10 | 68.8% | [ ] |
| 1324 | [Print Words Vertically](https://leetcode.com/problems/print-words-vertically/) | Medium | 4/10 | 67.5% | [ ] |
| 874 | [Walking Robot Simulation](https://leetcode.com/problems/walking-robot-simulation/) | Medium | 4/10 | 64.6% | [ ] |
| 2201 | [Count Artifacts That Can Be Extracted](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/) | Medium | 4/10 | 57.1% | [ ] |
| 157 | [Read N Characters Given Read4](https://leetcode.com/problems/read-n-characters-given-read4/) :lock: | Easy | 4/10 | 42.6% | [ ] |
| 3400 | [Maximum Number of Matching Indices After Right Shifts](https://leetcode.com/problems/maximum-number-of-matching-indices-after-right-shifts/) :lock: | Medium | 5/10 | 84.9% | [ ] |
| 950 | [Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/) | Medium | 5/10 | 83.6% | [ ] |
| 794 | [Valid Tic-Tac-Toe State](https://leetcode.com/problems/valid-tic-tac-toe-state/) | Medium | 5/10 | 34.8% | [ ] |
| 755 | [Pour Water](https://leetcode.com/problems/pour-water/) :lock: | Medium | 6/10 | 49.0% | [ ] |
| 957 | [Prison Cells After N Days](https://leetcode.com/problems/prison-cells-after-n-days/) | Medium | 6/10 | 39.2% | [ ] |
| 158 | [Read N Characters Given read4 II - Call Multiple Times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/) :lock: | Hard | 8/10 | 43.3% | [ ] |

## sweep_line_interval

**What it is** — This pattern uses a difference array (or event-based sweep) to apply range updates in O(1) and then reconstruct the final state with a single prefix-sum pass. Recognize it when a problem applies many add/subtract operations over intervals and asks for the resulting values at each position, or when you need to count how many intervals overlap at any point.

**Common steps**
1. Create a difference array `diff` of size `n + 1` (one extra cell to safely close intervals).
2. For each interval `[l, r]` with value `v`: set `diff[l] += v` and `diff[r+1] -= v`.
3. Compute the prefix sum of `diff` to recover the actual value at every index.
4. Use the recovered array to answer the problem's queries (coverage check, max overlap, average, etc.).
5. For event-based sweeps: sort events by position, process start/end events in order, maintain a running counter or set.

**Key variations**
- Coverage check: verify every position in a range has value >= 1.
- Maximum overlap: find the position where the running sum peaks.
- 2D difference array: extend to matrix with four corner updates for rectangle range increments.
- Weighted intervals: accumulate sums rather than simple +1/-1 counts.
- Coordinate compression when interval endpoints are large sparse values.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1893 | [Check if All the Integers in a Range Are Covered](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/) | Easy | 3/10 | 51.0% | [ ] |
| 370 | [Range Addition](https://leetcode.com/problems/range-addition/) :lock: | Medium | 4/10 | 73.0% | [ ] |
| 2536 | [Increment Submatrices by One](https://leetcode.com/problems/increment-submatrices-by-one/) | Medium | 5/10 | 73.8% | [ ] |
| 1094 | [Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | 5/10 | 56.3% | [ ] |
| 2015 | [Average Height of Buildings in Each Segment](https://leetcode.com/problems/average-height-of-buildings-in-each-segment/) :lock: | Medium | 6/10 | 58.6% | [ ] |
| 1943 | [Describe the Painting](https://leetcode.com/problems/describe-the-painting/) | Medium | 6/10 | 52.2% | [ ] |
| 1674 | [Minimum Moves to Make Array Complementary](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) | Medium | 7/10 | 43.4% | [ ] |

## array_manipulation

**What it is** — This pattern modifies an array in-place using index-based tricks, often treating array positions themselves as implicit hash maps or using sign/value encoding to mark visited cells. Recognize it when the problem asks for O(1) extra space and the values are bounded by the array size, or when elements must be rearranged to their "correct" positions.

**Common steps**
1. Identify the implicit mapping: element `x` maps to index `x - 1` (or similar).
2. Walk through the array; for each element, swap or negate the value at its target index to record that `x` has been seen.
3. Make a second pass to read out the encoded information (missing number, duplicate, etc.).
4. Restore original values if needed (un-negate) or leave the array as-is if the problem allows mutation.
5. For rotation/permutation problems: apply the reverse-reversal trick or follow cycle chains.

**Key variations**
- Sign-flipping to mark visited indices (find duplicates, find disappeared numbers).
- Cyclic sort: swap each element to its correct position, then scan for mismatches.
- Reversal algorithm for array rotation (reverse whole, reverse two halves).
- Index-following to detect cycles in a permutation (Array Nesting).
- Next permutation: find rightmost ascending pair, swap with next greater, reverse suffix.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1528 | [Shuffle String](https://leetcode.com/problems/shuffle-string/) | Easy | 1/10 | 85.4% | [ ] |
| 2022 | [Convert 1D Array Into 2D Array](https://leetcode.com/problems/convert-1d-array-into-2d-array/) | Easy | 2/10 | 72.2% | [ ] |
| 448 | [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | Easy | 3/10 | 64.1% | [ ] |
| 442 | [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Medium | 4/10 | 76.9% | [ ] |
| 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | 4/10 | 44.8% | [ ] |
| 3239 | [Minimum Number of Flips to Make Binary Grid Palindromic I](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/) | Medium | 5/10 | 74.9% | [ ] |
| 565 | [Array Nesting](https://leetcode.com/problems/array-nesting/) | Medium | 5/10 | 56.6% | [ ] |
| 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | Medium | 6/10 | 45.2% | [ ] |
| 775 | [Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/) | Medium | 6/10 | 42.8% | [ ] |
| 3240 | [Minimum Number of Flips to Make Binary Grid Palindromic II](https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/) | Medium | 7/10 | 25.6% | [ ] |
| 2459 | [Sort Array by Moving Items to Empty Space](https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/) :lock: | Hard | 8/10 | 45.6% | [ ] |
| 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | Hard | 8/10 | 42.9% | [ ] |
| 927 | [Three Equal Parts](https://leetcode.com/problems/three-equal-parts/) | Hard | 8/10 | 41.3% | [ ] |

## prefix_suffix_sum

**What it is** — This pattern precomputes cumulative sums (or products) from the left and/or right so that any subarray or submatrix aggregate can be answered in O(1). Recognize it when a problem repeatedly queries "sum/product of elements from index i to j" or when you need the aggregate of everything to the left (or right) of each position.

**Common steps**
1. Build a prefix array: `pre[i] = pre[i-1] + arr[i-1]`, with `pre[0] = 0` as a base case.
2. Answer a range query `[l, r]` as `pre[r+1] - pre[l]` in O(1).
3. If both left and right context are needed, build a suffix array in a second pass.
4. For 2D prefix sums: `pre[r][c] = grid[r][c] + pre[r-1][c] + pre[r][c-1] - pre[r-1][c-1]`.
5. Combine prefix and suffix arrays to compute per-element answers (e.g., product except self).

**Key variations**
- 1D range sum queries (immutable, static array).
- 2D rectangle sum queries (matrix block sum, submatrix target sum).
- Product prefix/suffix (product of array except self, construct product matrix with modulo).
- Prefix XOR, prefix OR, or prefix GCD for bitwise/math range queries.
- Prefix frequency map combined with a hash map to count subarrays with a given sum (overlaps with subarray_counting).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | 2/10 | 72.0% | [ ] |
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | 3/10 | 62.6% | [ ] |
| 1769 | [Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/) | Medium | 4/10 | 90.1% | [ ] |
| 1314 | [Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/) | Medium | 4/10 | 76.5% | [ ] |
| 3070 | [Count Submatrices with Top-Left Element and Sum Less Than k](https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/) | Medium | 4/10 | 74.8% | [ ] |
| 304 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | Medium | 4/10 | 58.2% | [ ] |
| 3546 | [Equal Sum Grid Partition I](https://leetcode.com/problems/equal-sum-grid-partition-i/) | Medium | 4/10 | 52.8% | [ ] |
| 3212 | [Count Submatrices With Equal Frequency of X and Y](https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/) | Medium | 5/10 | 69.6% | [ ] |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | 5/10 | 68.9% | [x] |
| 1525 | [Number of Good Ways to Split a String](https://leetcode.com/problems/number-of-good-ways-to-split-a-string/) | Medium | 5/10 | 68.4% | [ ] |
| 3147 | [Taking Maximum Energy From the Mystic Dungeon](https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/) | Medium | 5/10 | 61.0% | [ ] |
| 2017 | [Grid Game](https://leetcode.com/problems/grid-game/) | Medium | 5/10 | 60.9% | [ ] |
| 2906 | [Construct Product Matrix](https://leetcode.com/problems/construct-product-matrix/) | Medium | 5/10 | 51.8% | [ ] |
| 2100 | [Find Good Days to Rob the Bank](https://leetcode.com/problems/find-good-days-to-rob-the-bank/) | Medium | 5/10 | 51.6% | [ ] |
| 825 | [Friends Of Appropriate Ages](https://leetcode.com/problems/friends-of-appropriate-ages/) | Medium | 5/10 | 49.9% | [ ] |
| 915 | [Partition Array into Disjoint Intervals](https://leetcode.com/problems/partition-array-into-disjoint-intervals/) | Medium | 5/10 | 49.5% | [ ] |
| 2121 | [Intervals Between Identical Elements](https://leetcode.com/problems/intervals-between-identical-elements/) | Medium | 5/10 | 48.0% | [ ] |
| 2055 | [Plates Between Candles](https://leetcode.com/problems/plates-between-candles/) | Medium | 5/10 | 47.5% | [ ] |
| 848 | [Shifting Letters](https://leetcode.com/problems/shifting-letters/) | Medium | 5/10 | 46.2% | [ ] |
| 2420 | [Find All Good Indices](https://leetcode.com/problems/find-all-good-indices/) | Medium | 5/10 | 40.9% | [ ] |
| 1895 | [Largest Magic Square](https://leetcode.com/problems/largest-magic-square/) | Medium | 6/10 | 75.2% | [ ] |
| 1788 | [Maximize the Beauty of the Garden](https://leetcode.com/problems/maximize-the-beauty-of-the-garden/) :lock: | Hard | 7/10 | 64.9% | [ ] |
| 548 | [Split Array with Equal Sum](https://leetcode.com/problems/split-array-with-equal-sum/) :lock: | Hard | 7/10 | 50.1% | [ ] |
| 3548 | [Equal Sum Grid Partition II](https://leetcode.com/problems/equal-sum-grid-partition-ii/) | Hard | 7/10 | 39.4% | [ ] |
| 2245 | [Maximum Trailing Zeros in a Cornered Path](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/) | Medium | 7/10 | 37.6% | [ ] |
| 3888 | [Minimum Operations to Make All Grid Elements Equal](https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/) :lock: | Hard | 8/10 | 61.9% | [ ] |
| 798 | [Smallest Rotation with Highest Score](https://leetcode.com/problems/smallest-rotation-with-highest-score/) | Hard | 8/10 | 53.7% | [ ] |
| 2132 | [Stamping the Grid](https://leetcode.com/problems/stamping-the-grid/) | Hard | 8/10 | 35.2% | [ ] |

## subarray_counting

**What it is** — This pattern counts subarrays that satisfy a condition by combining a running prefix sum with a hash map. The key insight is that `sum(i, j) = prefix[j] - prefix[i]`, so if you store prefix sums seen so far, you can check in O(1) whether the complement that would complete the target sum has already occurred. Recognize it when a problem asks "how many subarrays have sum/XOR/mod equal to k."

**Common steps**
1. Initialize a hash map `count` with `{0: 1}` to handle subarrays starting from index 0.
2. Iterate through the array, maintaining a running `prefix` value (sum, XOR, mod, etc.).
3. At each index, compute the complement: `target = prefix - k` (or the modular equivalent).
4. Add `count[target]` to the answer (this is the number of subarrays ending here with the desired property).
5. Increment `count[prefix]` by 1 and continue.

**Key variations**
- Exact sum equals k (classic prefix sum + hash map).
- Sum divisible by k (use modular prefix, handle negative mod: `((prefix % k) + k) % k`).
- Binary array with sum = k (equivalent to count of 0s and 1s).
- 2D submatrix: fix top and bottom rows, collapse columns to 1D, then apply 1D technique.
- Majority element subarrays: encode majority candidate as +1/-1, then look for prefix count.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 930 | [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) | Medium | 5/10 | 68.7% | [ ] |
| 974 | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Medium | 5/10 | 56.3% | [ ] |
| 1983 | [Widest Pair of Indices With Equal Range Sum](https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/) :lock: | Medium | 5/10 | 54.0% | [ ] |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | 5/10 | 47.3% | [ ] |
| 3737 | [Count Subarrays With Majority Element I](https://leetcode.com/problems/count-subarrays-with-majority-element-i/) | Medium | 6/10 | 65.6% | [ ] |
| 1590 | [Make Sum Divisible by P](https://leetcode.com/problems/make-sum-divisible-by-p/) | Medium | 6/10 | 42.6% | [ ] |
| 1124 | [Longest Well-Performing Interval](https://leetcode.com/problems/longest-well-performing-interval/) | Medium | 6/10 | 37.6% | [ ] |
| 1074 | [Number of Submatrices That Sum to Target](https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/) | Hard | 7/10 | 74.6% | [ ] |
| 3739 | [Count Subarrays With Majority Element II](https://leetcode.com/problems/count-subarrays-with-majority-element-ii/) | Hard | 8/10 | 45.5% | [ ] |
| 2025 | [Maximum Number of Ways to Partition an Array](https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/) | Hard | 8/10 | 35.7% | [ ] |
| 3721 | [Longest Balanced Subarray II](https://leetcode.com/problems/longest-balanced-subarray-ii/) | Hard | 8/10 | 33.7% | [ ] |

## bit_manipulation

**What it is** — This pattern uses bitwise operations (AND, OR, XOR, shifts) to encode sets compactly or to detect structural properties of numbers in O(1) per bit. Recognize it when a problem involves toggling, parity tracking, unique/missing elements, or when the number of distinct categories is small enough to represent as a bitmask.

**Common steps**
1. Identify what each bit represents (a vowel, a parity flag, a subset membership, etc.).
2. Build or update a bitmask as you scan: toggle bits with XOR (`mask ^= (1 << i)`), set with OR, clear with AND-NOT.
3. Use the mask as a hash key or directly answer parity/uniqueness queries.
4. For subarray problems, store `{mask: first_occurrence_index}` and look for a previously seen mask.
5. Check properties: `x & (x-1)` clears the lowest set bit; `x & (-x)` isolates it; `bin(x).count('1')` counts set bits.

**Key variations**
- XOR to find the unique element (all others appear twice, so they cancel out).
- Bitmask as a state key for DP or prefix tracking (vowel parity bitmask for longest substring).
- Bitmask for subset enumeration in meet-in-the-middle or brute-force solutions.
- Bitwise OR subarrays: OR is monotonically non-decreasing, so the distinct values per right endpoint are O(log(max)).
- Cinema seat allocation: represent each row as a bitmask and check forbidden patterns with AND.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1980 | [Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/) | Medium | 5/10 | 81.2% | [ ] |
| 1371 | [Find the Longest Substring Containing Vowels in Even Counts](https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/) | Medium | 6/10 | 75.6% | [ ] |
| 1386 | [Cinema Seat Allocation](https://leetcode.com/problems/cinema-seat-allocation/) | Medium | 6/10 | 44.5% | [ ] |
| 3755 | [Find Maximum Balanced XOR Subarray Length](https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/) | Medium | 7/10 | 50.9% | [ ] |
| 3171 | [Find Subarray With Bitwise OR Closest to K](https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/) | Hard | 8/10 | 31.0% | [ ] |

## math_and_combinatorics

**What it is** — This pattern solves geometric or counting problems by applying mathematical formulas rather than brute-force enumeration. Recognize it when the problem involves points in a plane, areas of shapes, counting arrangements, or any situation where a direct formula or algebraic insight eliminates the need for nested loops.

**Common steps**
1. Map the problem to a mathematical structure (e.g., axis-aligned rectangles need only x-coordinates and y-coordinates stored separately).
2. Use a hash map or set to store relevant geometric features (x-values seen, slopes, coordinate pairs).
3. Enumerate the minimal set of candidates (e.g., all pairs of x-coordinates) and check feasibility with the stored set in O(1).
4. Apply the formula to compute the answer (area = |x2-x1| * |y2-y1|, etc.).
5. Track the global minimum/maximum across all valid candidates.

**Key variations**
- Axis-aligned rectangles: store all points in a set, find matching corners by checking pairs of x-values at the same y.
- Non-axis-aligned rectangles (Minimum Area Rectangle II): group by center and radius, check perpendicularity with dot product.
- Covering all ones in a grid: find bounding box extremes by scanning row/column min and max.
- Combinatorial counting: use math.comb or Pascal's triangle when brute force would overflow time.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 939 | [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/) | Medium | 5/10 | 55.4% | [ ] |
| 963 | [Minimum Area Rectangle II](https://leetcode.com/problems/minimum-area-rectangle-ii/) | Medium | 7/10 | 55.9% | [ ] |
| 3197 | [Find the Minimum Area to Cover All Ones II](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/) | Hard | 8/10 | 63.5% | [ ] |

## meet_in_the_middle

**What it is** — This pattern splits the input into two halves, enumerates all possibilities for each half independently (often 2^(n/2) subsets), then combines the two halves efficiently using sorting and binary search or a hash map. Recognize it when brute force is O(2^n) and n is around 30-40 — too large for full enumeration but small enough that O(2^(n/2)) is feasible.

**Common steps**
1. Split the input array into a left half and a right half of roughly equal size.
2. Enumerate all 2^(n/2) subsets of the left half; store their sums (or relevant values) in a list.
3. Sort the left-half list to enable binary search.
4. Enumerate all 2^(n/2) subsets of the right half; for each, binary-search the left list for the complement that achieves the target.
5. Combine matches, being careful to avoid double-counting or off-by-one errors.

**Key variations**
- Subset sum equality: check if any partition of the array into two groups has equal average (Split Array With Same Average).
- Closest-sum target: find the pair (one from each half) whose combined value is nearest to a goal.
- Hash map instead of sort+binary-search when exact equality is needed (faster constant factor).
- Pruning: discard left-half sums that can never satisfy the constraint before storing them.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 805 | [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/) | Hard | 9/10 | 27.0% | [ ] |
