# DynamicProgramming

392 problems across 15 patterns.

## linear_dp

**What it is** — Linear DP solves problems where the optimal answer at position `i` depends only on a fixed number of previous positions (e.g., `dp[i-1]`, `dp[i-2]`, or a range). Recognize this pattern when you can scan an array or sequence left-to-right and each state's answer is built from a small window of prior states. Classic signals are "maximum subarray," "minimum cost to reach here," or recurrences like Fibonacci-style counting.

**Common steps**
1. Define `dp[i]` clearly — what does it represent at index `i`? (e.g., max sum ending at `i`, min cost to reach `i`)
2. Identify the recurrence: which prior states does `dp[i]` depend on? Write the formula explicitly.
3. Handle base cases: set `dp[0]` (and `dp[1]` if needed) before the main loop.
4. Iterate left-to-right, computing `dp[i]` from the recurrence.
5. Extract the answer — it may be `dp[n-1]`, `max(dp)`, or a running aggregation.
6. Optimize space if the recurrence only looks back a fixed number of steps (use rolling variables instead of an array).

**Key variations**
- Single-value recurrence (Fibonacci, Climbing Stairs): `dp[i] = dp[i-1] + dp[i-2]`
- Subarray problems (Kadane's): track "best ending here" vs "best seen so far"
- Skip/take decisions (House Robber): `dp[i] = max(dp[i-1], dp[i-2] + val[i])`
- Cost-based traversal (Min Cost Climbing Stairs, Minimum Cost for Tickets): pick among a few jump sizes
- Circular array variants (House Robber II): run linear DP twice on two overlapping subarrays
- Multi-state linear DP (Max Product Subarray): maintain multiple parallel dp arrays (e.g., max and min ending here)

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 509 | [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | Easy | 1/10 | 74.1% | [ ] |
| 746 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy | 1/10 | 68.2% | [x] |
| 1137 | [N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | Easy | 1/10 | 63.2% | [ ] |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | 1/10 | 54.1% | [x] |
| 2393 | [Count Strictly Increasing Subarrays](https://leetcode.com/problems/count-strictly-increasing-subarrays/) :lock: | Medium | 3/10 | 71.0% | [ ] |
| 413 | [Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices/) | Medium | 3/10 | 64.8% | [ ] |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | 3/10 | 53.3% | [x] |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | Medium | 3/10 | 53.2% | [x] |
| 276 | [Paint Fence](https://leetcode.com/problems/paint-fence/) :lock: | Medium | 3/10 | 48.4% | [ ] |
| 1387 | [Sort Integers by The Power Value](https://leetcode.com/problems/sort-integers-by-the-power-value/) | Medium | 4/10 | 71.7% | [ ] |
| 1653 | [Minimum Deletions to Make String Balanced](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/) | Medium | 4/10 | 68.2% | [ ] |
| 2110 | [Number of Smooth Descent Periods of a Stock](https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/) | Medium | 4/10 | 67.7% | [ ] |
| 983 | [Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/) | Medium | 4/10 | 67.4% | [ ] |
| 2464 | [Minimum Subarrays in a Valid Split](https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/) :lock: | Medium | 4/10 | 64.7% | [ ] |
| 1014 | [Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair/) | Medium | 4/10 | 62.7% | [ ] |
| 926 | [Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/) | Medium | 4/10 | 61.9% | [ ] |
| 2606 | [Find the Substring With Maximum Cost](https://leetcode.com/problems/find-the-substring-with-maximum-cost/) | Medium | 4/10 | 57.9% | [ ] |
| 740 | [Delete and Earn](https://leetcode.com/problems/delete-and-earn/) | Medium | 4/10 | 57.2% | [x] |
| 2501 | [Longest Square Streak in an Array](https://leetcode.com/problems/longest-square-streak-in-an-array/) | Medium | 4/10 | 53.1% | [ ] |
| 213 | [House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium | 4/10 | 44.9% | [x] |
| 2036 | [Maximum Alternating Subarray Sum](https://leetcode.com/problems/maximum-alternating-subarray-sum/) :lock: | Medium | 4/10 | 40.0% | [ ] |
| 2770 | [Maximum Number of Jumps to Reach the Last Index](https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/) | Medium | 4/10 | 32.8% | [ ] |
| 1749 | [Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) | Medium | 5/10 | 71.0% | [ ] |
| 1746 | [Maximum Subarray Sum After One Operation](https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/) :lock: | Medium | 5/10 | 65.2% | [ ] |
| 1031 | [Maximum Sum of Two Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) | Medium | 5/10 | 60.8% | [ ] |
| 2327 | [Number of People Aware of a Secret](https://leetcode.com/problems/number-of-people-aware-of-a-secret/) | Medium | 5/10 | 60.8% | [ ] |
| 2140 | [Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/) | Medium | 5/10 | 60.2% | [ ] |
| 650 | [2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard/) | Medium | 5/10 | 59.3% | [ ] |
| 1262 | [Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/) | Medium | 5/10 | 57.0% | [ ] |
| 651 | [4 Keys Keyboard](https://leetcode.com/problems/4-keys-keyboard/) :lock: | Medium | 5/10 | 56.5% | [ ] |
| 2380 | [Time Needed to Rearrange a Binary String](https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/) | Medium | 5/10 | 52.9% | [ ] |
| 2369 | [Check if There is a Valid Partition For The Array](https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/) | Medium | 5/10 | 52.4% | [ ] |
| 790 | [Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/) | Medium | 5/10 | 51.4% | [ ] |
| 2052 | [Minimum Cost to Separate Sentence Into Rows](https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/) :lock: | Medium | 5/10 | 51.1% | [ ] |
| 2266 | [Count Number of Texts](https://leetcode.com/problems/count-number-of-texts/) | Medium | 5/10 | 50.2% | [ ] |
| 264 | [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) | Medium | 5/10 | 49.6% | [ ] |
| 2944 | [Minimum Number of Coins for Fruits](https://leetcode.com/problems/minimum-number-of-coins-for-fruits/) | Medium | 5/10 | 49.0% | [ ] |
| 313 | [Super Ugly Number](https://leetcode.com/problems/super-ugly-number/) | Medium | 5/10 | 46.1% | [ ] |
| 3186 | [Maximum Total Damage With Spell Casting](https://leetcode.com/problems/maximum-total-damage-with-spell-casting/) | Medium | 5/10 | 45.1% | [ ] |
| 1567 | [Maximum Length of Subarray With Positive Product](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/) | Medium | 5/10 | 44.7% | [ ] |
| 3284 | [Sum of Consecutive Subarrays](https://leetcode.com/problems/sum-of-consecutive-subarrays/) :lock: | Medium | 5/10 | 42.7% | [ ] |
| 2830 | [Maximize the Profit as the Salesman](https://leetcode.com/problems/maximize-the-profit-as-the-salesman/) | Medium | 5/10 | 38.3% | [ ] |
| 91 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | 5/10 | 37.9% | [ ] |
| 2786 | [Visit Array Positions to Maximize Score](https://leetcode.com/problems/visit-array-positions-to-maximize-score/) | Medium | 5/10 | 37.6% | [ ] |
| 418 | [Sentence Screen Fitting](https://leetcode.com/problems/sentence-screen-fitting/) :lock: | Medium | 5/10 | 36.4% | [ ] |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | 5/10 | 36.3% | [x] |
| 2919 | [Minimum Increment Operations to Make Array Beautiful](https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/) | Medium | 5/10 | 34.8% | [ ] |
| 3628 | [Maximum Number of Subsequences After One Inserting](https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/) | Medium | 5/10 | 31.9% | [ ] |
| 2771 | [Longest Non-decreasing Subarray From Two Arrays](https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/) | Medium | 5/10 | 31.2% | [ ] |
| 3434 | [Maximum Frequency After Subarray Operation](https://leetcode.com/problems/maximum-frequency-after-subarray-operation/) | Medium | 5/10 | 31.2% | [ ] |
| 1871 | [Jump Game VII](https://leetcode.com/problems/jump-game-vii/) | Medium | 5/10 | 26.5% | [ ] |
| 918 | [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) | Medium | 6/10 | 50.0% | [ ] |
| 1186 | [Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/) | Medium | 6/10 | 47.4% | [ ] |
| 2638 | [Count the Number of K-Free Subsets](https://leetcode.com/problems/count-the-number-of-k-free-subsets/) :lock: | Medium | 6/10 | 47.2% | [ ] |
| 2008 | [Maximum Earnings From Taxi](https://leetcode.com/problems/maximum-earnings-from-taxi/) | Medium | 6/10 | 46.5% | [ ] |
| 1696 | [Jump Game VI](https://leetcode.com/problems/jump-game-vi/) | Medium | 6/10 | 46.4% | [ ] |
| 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | 6/10 | 41.7% | [ ] |
| 1997 | [First Day Where You Have Been in All the Rooms](https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/) | Medium | 6/10 | 40.4% | [ ] |
| 2896 | [Apply Operations to Make Two Strings Equal](https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/) | Medium | 6/10 | 27.7% | [ ] |
| 1191 | [K-Concatenation Maximum Sum](https://leetcode.com/problems/k-concatenation-maximum-sum/) | Medium | 6/10 | 25.5% | [ ] |
| 1340 | [Jump Game V](https://leetcode.com/problems/jump-game-v/) | Hard | 7/10 | 65.0% | [ ] |
| 689 | [Maximum Sum of 3 Non-Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) | Hard | 7/10 | 59.8% | [ ] |
| 1548 | [The Most Similar Path in a Graph](https://leetcode.com/problems/the-most-similar-path-in-a-graph/) :lock: | Hard | 7/10 | 59.4% | [ ] |
| 2321 | [Maximum Score Of Spliced Array](https://leetcode.com/problems/maximum-score-of-spliced-array/) | Hard | 7/10 | 58.4% | [ ] |
| 1714 | [Sum Of Special Evenly-Spaced Elements In Array](https://leetcode.com/problems/sum-of-special-evenly-spaced-elements-in-array/) :lock: | Hard | 7/10 | 49.9% | [ ] |
| 2167 | [Minimum Time to Remove All Cars Containing Illegal Goods](https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/) | Hard | 7/10 | 41.9% | [ ] |
| 2209 | [Minimum White Tiles After Covering With Carpets](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/) | Hard | 7/10 | 38.8% | [ ] |
| 656 | [Coin Path](https://leetcode.com/problems/coin-path/) :lock: | Hard | 7/10 | 34.3% | [ ] |
| 1751 | [Maximum Number of Events That Can Be Attended II](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/) | Hard | 8/10 | 63.5% | [ ] |
| 2463 | [Minimum Total Distance Traveled](https://leetcode.com/problems/minimum-total-distance-traveled/) | Hard | 8/10 | 63.2% | [ ] |
| 1425 | [Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/) | Hard | 8/10 | 56.4% | [ ] |
| 1235 | [Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) | Hard | 8/10 | 54.7% | [ ] |
| 1388 | [Pizza With 3n Slices](https://leetcode.com/problems/pizza-with-3n-slices/) | Hard | 8/10 | 53.8% | [ ] |
| 2143 | [Choose Numbers From Two Arrays in Range](https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/) :lock: | Hard | 8/10 | 52.8% | [ ] |
| 2969 | [Minimum Number of Coins for Fruits II](https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/) :lock: | Hard | 8/10 | 47.5% | [ ] |
| 403 | [Frog Jump](https://leetcode.com/problems/frog-jump/) | Hard | 8/10 | 47.3% | [ ] |
| 2272 | [Substring With Largest Variance](https://leetcode.com/problems/substring-with-largest-variance/) | Hard | 8/10 | 46.0% | [ ] |
| 2188 | [Minimum Time to Finish the Race](https://leetcode.com/problems/minimum-time-to-finish-the-race/) | Hard | 8/10 | 43.2% | [ ] |
| 1928 | [Minimum Cost to Reach Destination in Time](https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/) | Hard | 8/10 | 41.5% | [ ] |
| 975 | [Odd Even Jump](https://leetcode.com/problems/odd-even-jump/) | Hard | 8/10 | 41.2% | [ ] |
| 2355 | [Maximum Number of Books You Can Take](https://leetcode.com/problems/maximum-number-of-books-you-can-take/) :lock: | Hard | 8/10 | 39.5% | [ ] |
| 1553 | [Minimum Number of Days to Eat N Oranges](https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/) | Hard | 8/10 | 36.2% | [ ] |
| 3041 | [Maximize Consecutive Elements in an Array After Modification](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/) | Hard | 8/10 | 33.8% | [ ] |
| 3414 | [Maximum Score of Non-overlapping Intervals](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/) | Hard | 8/10 | 31.5% | [ ] |
| 3077 | [Maximum Strength of K Disjoint Subarrays](https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/) | Hard | 8/10 | 27.8% | [ ] |
| 964 | [Least Operators to Express Number](https://leetcode.com/problems/least-operators-to-express-number/) | Hard | 9/10 | 48.5% | [ ] |
| 818 | [Race Car](https://leetcode.com/problems/race-car/) | Hard | 9/10 | 44.7% | [ ] |
| 1687 | [Delivering Boxes from Storage to Ports](https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/) | Hard | 9/10 | 39.8% | [ ] |
| 887 | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) | Hard | 9/10 | 30.1% | [ ] |
| 2945 | [Find Maximum Non-decreasing Array Length](https://leetcode.com/problems/find-maximum-non-decreasing-array-length/) | Hard | 9/10 | 18.8% | [ ] |

## probability_dp

**What it is** — Probability DP computes the likelihood of an outcome after a sequence of random events, where each step's probability depends on a previous state. Recognize it when the problem asks "what is the probability that..." after some number of moves or trials, and the transitions are well-defined (dice rolls, random walks, card draws). The state typically encodes how much of some resource remains and the probability of being in that configuration.

**Common steps**
1. Define `dp[state]` as the probability of being in that state (e.g., `dp[i][j]` = probability of being at cell `(i,j)` after `k` steps).
2. Initialize: set `dp[start_state] = 1.0`, all others to `0.0`.
3. For each step/trial, propagate probabilities: for each current state, distribute its probability mass to reachable next states weighted by transition probability.
4. After all steps, sum `dp` over the desired outcome states.
5. Watch for precision: use floating point carefully, or check if the problem allows integer counting with modular arithmetic.

**Key variations**
- Fixed number of steps with position tracking (Knight Probability): iterate step-by-step over a grid
- Sliding window / threshold stopping (New 21 Game): accumulate probabilities up to a boundary using a running window sum
- Soup servings with early stopping: recognize when probability converges and short-circuit for large inputs
- Problems that look like probability but reduce to combinatorics: verify if exact counting is possible

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1230 | [Toss Strange Coins](https://leetcode.com/problems/toss-strange-coins/) :lock: | Medium | 4/10 | 58.1% | [ ] |
| 808 | [Soup Servings](https://leetcode.com/problems/soup-servings/) | Medium | 6/10 | 59.6% | [ ] |
| 688 | [Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/) | Medium | 6/10 | 57.0% | [ ] |
| 837 | [New 21 Game](https://leetcode.com/problems/new-21-game/) | Medium | 7/10 | 52.0% | [ ] |

## grid_dp

**What it is** — Grid DP solves problems on a 2D matrix where you move between cells (typically top-to-bottom or in all directions) and the value of a cell depends on adjacent cells already computed. Recognize it when the problem involves paths, counts, or properties in a grid and movement is constrained (e.g., only right/down, or only to increasing neighbors). The state is the cell coordinates, often augmented with extra dimensions.

**Common steps**
1. Define `dp[r][c]` as the answer for the subproblem ending at cell `(r, c)` (e.g., min path cost, number of paths, max cherries).
2. Identify which prior cells feed into `dp[r][c]` based on movement rules (e.g., from `dp[r-1][c]` and `dp[r][c-1]` for top-down-only movement).
3. Initialize the boundary: fill the first row and first column (or use sentinel values) as base cases.
4. Fill the grid in topological order (row-by-row for DAG movement, or use memoized DFS for general directed graphs).
5. Handle obstacles or constraints by skipping invalid cells (set to infinity or -1).
6. Read the answer from `dp[m-1][n-1]` or aggregate across a row/column as needed.

**Key variations**
- Counting paths (Unique Paths, Out of Boundary Paths): accumulate sums, watch for modulo
- Optimization paths (Minimum Path Sum, Dungeon Game): min/max over predecessors; Dungeon Game requires reverse traversal
- Square/rectangle substructure (Maximal Square, Count Square Submatrices): `dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1`
- Longest increasing path: requires memoized DFS since movement is not strictly left-to-right
- Multi-agent simultaneous traversal (Cherry Pickup II): add a third dimension for the second agent's column
- Reverse DP (Dungeon Game): when you need to satisfy a future constraint, fill the grid from bottom-right to top-left

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 64 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Medium | 3/10 | 68.2% | [ ] |
| 62 | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | 3/10 | 66.8% | [ ] |
| 931 | [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) | Medium | 3/10 | 60.8% | [ ] |
| 1277 | [Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) | Medium | 4/10 | 80.7% | [ ] |
| 2304 | [Minimum Path Cost in a Grid](https://leetcode.com/problems/minimum-path-cost-in-a-grid/) | Medium | 4/10 | 68.1% | [ ] |
| 120 | [Triangle](https://leetcode.com/problems/triangle/) | Medium | 4/10 | 59.9% | [ ] |
| 361 | [Bomb Enemy](https://leetcode.com/problems/bomb-enemy/) :lock: | Medium | 4/10 | 52.8% | [ ] |
| 2510 | [Check if There is a Path With Equal Number of 0's And 1's](https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/) :lock: | Medium | 4/10 | 51.9% | [ ] |
| 562 | [Longest Line of Consecutive One in Matrix](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/) :lock: | Medium | 4/10 | 50.6% | [ ] |
| 3603 | [Minimum Cost Path with Alternating Directions II](https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/) | Medium | 4/10 | 44.8% | [ ] |
| 63 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | Medium | 4/10 | 44.4% | [ ] |
| 1504 | [Count Submatrices With All Ones](https://leetcode.com/problems/count-submatrices-with-all-ones/) | Medium | 5/10 | 71.0% | [ ] |
| 799 | [Champagne Tower](https://leetcode.com/problems/champagne-tower/) | Medium | 5/10 | 64.1% | [ ] |
| 2684 | [Maximum Number of Moves in a Grid](https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/) | Medium | 5/10 | 58.7% | [ ] |
| 3742 | [Maximum Path Score in a Grid](https://leetcode.com/problems/maximum-path-score-in-a-grid/) | Medium | 5/10 | 54.0% | [ ] |
| 1594 | [Maximum Non Negative Product in a Matrix](https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/) | Medium | 5/10 | 51.6% | [ ] |
| 221 | [Maximal Square](https://leetcode.com/problems/maximal-square/) | Medium | 5/10 | 50.3% | [ ] |
| 3665 | [Twisted Mirror Path Count](https://leetcode.com/problems/twisted-mirror-path-count/) | Medium | 5/10 | 48.3% | [ ] |
| 3148 | [Maximum Difference Score in a Grid](https://leetcode.com/problems/maximum-difference-score-in-a-grid/) | Medium | 5/10 | 48.0% | [ ] |
| 3418 | [Maximum Amount of Money Robot Can Earn](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/) | Medium | 5/10 | 47.8% | [ ] |
| 3332 | [Maximum Points Tourist Can Earn](https://leetcode.com/problems/maximum-points-tourist-can-earn/) | Medium | 5/10 | 47.6% | [ ] |
| 3122 | [Minimum Number of Operations to Satisfy Conditions](https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/) | Medium | 5/10 | 41.9% | [ ] |
| 3393 | [Count Paths With the Given XOR Value](https://leetcode.com/problems/count-paths-with-the-given-xor-value/) | Medium | 5/10 | 40.6% | [ ] |
| 3882 | [Minimum XOR Path in a Grid](https://leetcode.com/problems/minimum-xor-path-in-a-grid/) | Medium | 5/10 | 39.6% | [ ] |
| 1139 | [Largest 1-Bordered Square](https://leetcode.com/problems/largest-1-bordered-square/) | Medium | 6/10 | 52.1% | [ ] |
| 764 | [Largest Plus Sign](https://leetcode.com/problems/largest-plus-sign/) | Medium | 6/10 | 49.2% | [ ] |
| 576 | [Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/) | Medium | 6/10 | 48.4% | [ ] |
| 1937 | [Maximum Number of Points with Cost](https://leetcode.com/problems/maximum-number-of-points-with-cost/) | Medium | 6/10 | 41.7% | [ ] |
| 2088 | [Count Fertile Pyramids in a Land](https://leetcode.com/problems/count-fertile-pyramids-in-a-land/) | Hard | 7/10 | 66.3% | [ ] |
| 1289 | [Minimum Falling Path Sum II](https://leetcode.com/problems/minimum-falling-path-sum-ii/) | Hard | 7/10 | 63.1% | [ ] |
| 2435 | [Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/) | Hard | 7/10 | 58.8% | [ ] |
| 2912 | [Number of Ways to Reach Destination in the Grid](https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/) :lock: | Hard | 7/10 | 57.7% | [ ] |
| 2328 | [Number of Increasing Paths in a Grid](https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/) | Hard | 7/10 | 57.4% | [ ] |
| 329 | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Hard | 7/10 | 56.6% | [ ] |
| 568 | [Maximum Vacation Days](https://leetcode.com/problems/maximum-vacation-days/) :lock: | Hard | 7/10 | 46.8% | [ ] |
| 174 | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) | Hard | 7/10 | 41.3% | [ ] |
| 1411 | [Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/) | Hard | 8/10 | 80.5% | [ ] |
| 1463 | [Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii/) | Hard | 8/10 | 72.4% | [ ] |
| 3363 | [Find the Maximum Number of Fruits Collected](https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/) | Hard | 8/10 | 65.0% | [ ] |
| 3225 | [Maximum Score From Grid Operations](https://leetcode.com/problems/maximum-score-from-grid-operations/) | Hard | 8/10 | 64.8% | [ ] |
| 1444 | [Number of Ways of Cutting a Pizza](https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/) | Hard | 8/10 | 61.6% | [ ] |
| 3459 | [Length of Longest V-Shaped Diagonal Segment](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/) | Hard | 8/10 | 56.2% | [ ] |
| 3651 | [Minimum Cost Path with Teleportations](https://leetcode.com/problems/minimum-cost-path-with-teleportations/) | Hard | 8/10 | 45.6% | [ ] |
| 1301 | [Number of Paths with Max Score](https://leetcode.com/problems/number-of-paths-with-max-score/) | Hard | 8/10 | 42.4% | [ ] |
| 2267 | [ Check if There Is a Valid Parentheses String Path](https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/) | Hard | 8/10 | 40.3% | [ ] |
| 3797 | [Count Routes to Climb a Rectangular Grid](https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/) | Hard | 8/10 | 24.6% | [ ] |
| 741 | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) | Hard | 9/10 | 39.4% | [ ] |
| 1883 | [Minimum Skips to Arrive at Meeting On Time](https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/) | Hard | 9/10 | 38.5% | [ ] |
| 2713 | [Maximum Strictly Increasing Cells in a Matrix](https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/) | Hard | 9/10 | 31.4% | [ ] |
| 3257 | [Maximum Value Sum by Placing Three Rooks II](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/) | Hard | 9/10 | 26.9% | [ ] |
| 3256 | [Maximum Value Sum by Placing Three Rooks I](https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/) | Hard | 9/10 | 16.6% | [ ] |

## subsequence_dp

**What it is** — Subsequence DP finds optimal or countable subsequences (not necessarily contiguous) within one or two sequences, where the value at index `i` depends on all prior choices. Recognize it when the problem asks for the longest, shortest, or number-of ways to select elements in order from an array or string, without requiring contiguity. The canonical examples are LIS (Longest Increasing Subsequence) and LCS (Longest Common Subsequence).

**Common steps**
1. For single-sequence problems: define `dp[i]` as the answer for subsequences ending at index `i`. For two-sequence problems: define `dp[i][j]` as the answer considering the first `i` elements of sequence A and first `j` of sequence B.
2. Write the recurrence by deciding whether to include element `i` (and `j`) in the subsequence.
3. For LIS-style: `dp[i] = max(dp[j] + 1)` for all `j < i` where `arr[j] < arr[i]`.
4. For LCS-style: if elements match, `dp[i][j] = dp[i-1][j-1] + 1`; otherwise `max(dp[i-1][j], dp[i][j-1])`.
5. Initialize to base cases (empty subsequences = 0 or 1 depending on definition).
6. For LIS, optimize from O(n^2) to O(n log n) using binary search with a patience-sorting array when only the length (not reconstruction) is needed.

**Key variations**
- LIS (Longest Increasing Subsequence): classic O(n^2) or O(n log n) with binary search
- LCS (Longest Common Subsequence): 2D DP on two strings/arrays
- Counting subsequences (Distinct Subsequences, Number of LIS): track count alongside length
- Constrained subsequences (Longest Arithmetic Subsequence): use a hashmap for `dp[i][diff]`
- Reconstruction: backtrack through the dp table or store parent pointers
- Subsequence with custom ordering (Largest Divisible Subset, Best Team): sort first, then apply LIS-style DP

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1035 | [Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/) | Medium | 4/10 | 65.2% | [ ] |
| 300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | 4/10 | 59.4% | [ ] |
| 1143 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 4/10 | 59.1% | [ ] |
| 1218 | [Longest Arithmetic Subsequence of Given Difference](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/) | Medium | 4/10 | 54.3% | [ ] |
| 2826 | [Sorting Three Groups](https://leetcode.com/problems/sorting-three-groups/) | Medium | 4/10 | 43.0% | [ ] |
| 1048 | [Longest String Chain](https://leetcode.com/problems/longest-string-chain/) | Medium | 5/10 | 63.0% | [ ] |
| 2901 | [Longest Unequal Adjacent Groups Subsequence II](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/) | Medium | 5/10 | 51.4% | [ ] |
| 1626 | [Best Team With No Conflicts](https://leetcode.com/problems/best-team-with-no-conflicts/) | Medium | 5/10 | 50.7% | [ ] |
| 3825 | [Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND](https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/) | Medium | 5/10 | 50.6% | [ ] |
| 368 | [Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/) | Medium | 5/10 | 49.6% | [ ] |
| 2370 | [Longest Ideal Subsequence](https://leetcode.com/problems/longest-ideal-subsequence/) | Medium | 5/10 | 46.6% | [ ] |
| 3316 | [Find Maximum Removals From Source String](https://leetcode.com/problems/find-maximum-removals-from-source-string/) | Medium | 5/10 | 39.3% | [ ] |
| 873 | [Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/) | Medium | 6/10 | 57.5% | [ ] |
| 673 | [Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) | Medium | 6/10 | 51.9% | [ ] |
| 1027 | [Longest Arithmetic Subsequence](https://leetcode.com/problems/longest-arithmetic-subsequence/) | Medium | 6/10 | 50.0% | [ ] |
| 1458 | [Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) | Hard | 7/10 | 69.3% | [ ] |
| 1691 | [Maximum Height by Stacking Cuboids ](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/) | Hard | 7/10 | 62.0% | [ ] |
| 115 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | Hard | 7/10 | 51.8% | [ ] |
| 960 | [Delete Columns to Make Sorted III](https://leetcode.com/problems/delete-columns-to-make-sorted-iii/) | Hard | 8/10 | 72.6% | [ ] |
| 446 | [Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/) | Hard | 8/10 | 55.1% | [ ] |
| 1671 | [Minimum Number of Removals to Make Mountain Array](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/) | Hard | 8/10 | 54.8% | [ ] |
| 940 | [Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/) | Hard | 8/10 | 44.1% | [ ] |
| 1187 | [Make Array Strictly Increasing](https://leetcode.com/problems/make-array-strictly-increasing/) | Hard | 9/10 | 57.9% | [ ] |
| 2926 | [Maximum Balanced Subsequence Sum](https://leetcode.com/problems/maximum-balanced-subsequence-sum/) | Hard | 9/10 | 25.9% | [ ] |
| 3098 | [Find the Sum of Subsequence Powers](https://leetcode.com/problems/find-the-sum-of-subsequence-powers/) | Hard | 9/10 | 25.1% | [ ] |

## knapsack

**What it is** — Knapsack DP selects items from a set subject to a capacity constraint to optimize (maximize value or count ways to hit a target). Recognize it when you have a collection of items with weights/costs and the problem asks for the best selection under a budget, or the number of ways to reach a target sum. The key insight is that each item can be used once (0/1 knapsack) or unlimited times (unbounded knapsack).

**Common steps**
1. Define `dp[w]` as the best value (or number of ways) achievable with exactly (or at most) capacity `w`.
2. Initialize: `dp[0] = 0` (or 1 for counting), `dp[w] = infinity` (or 0) for `w > 0`.
3. For 0/1 knapsack, iterate items in the outer loop and capacities in the **inner loop going backwards** (to prevent reuse of the same item).
4. For unbounded knapsack (Coin Change), iterate capacities in the **inner loop going forwards** (allowing reuse).
5. For each item with weight `w` and value `v`: `dp[cap] = min/max(dp[cap], dp[cap - w] + v)` or `dp[cap] += dp[cap - w]` for counting.
6. Read the answer from `dp[target]` or `dp[capacity]`.

**Key variations**
- 0/1 knapsack (Partition Equal Subset Sum, Target Sum): each item used at most once; iterate capacity backwards
- Unbounded knapsack (Coin Change, Coin Change II): items reusable; iterate capacity forwards
- Exact target vs. at-most: adjust initialization (`dp[0]=1` for counting ways to reach exactly target)
- 2D knapsack (Ones and Zeroes): two capacity dimensions; iterate both backwards
- Bounded knapsack: each item has a limited count; use binary grouping or sliding window optimization

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 518 | [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Medium | 4/10 | 60.1% | [ ] |
| 279 | [Perfect Squares](https://leetcode.com/problems/perfect-squares/) | Medium | 4/10 | 56.5% | [ ] |
| 322 | [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | 4/10 | 48.3% | [x] |
| 2291 | [Maximum Profit From Trading Stocks](https://leetcode.com/problems/maximum-profit-from-trading-stocks/) :lock: | Medium | 4/10 | 48.2% | [ ] |
| 2431 | [Maximize Total Tastiness of Purchased Fruits](https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/) :lock: | Medium | 5/10 | 64.6% | [ ] |
| 1155 | [Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/) | Medium | 5/10 | 62.3% | [ ] |
| 1049 | [Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) | Medium | 5/10 | 59.7% | [ ] |
| 2466 | [Count Ways To Build Good Strings](https://leetcode.com/problems/count-ways-to-build-good-strings/) | Medium | 5/10 | 58.9% | [ ] |
| 377 | [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | Medium | 5/10 | 55.1% | [ ] |
| 494 | [Target Sum](https://leetcode.com/problems/target-sum/) | Medium | 5/10 | 52.2% | [ ] |
| 2787 | [Ways to Express an Integer as Sum of Powers](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/) | Medium | 5/10 | 49.8% | [ ] |
| 416 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 5/10 | 49.4% | [ ] |
| 2915 | [Length of the Longest Subsequence That Sums to Target](https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/) | Medium | 5/10 | 39.7% | [ ] |
| 474 | [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | Medium | 6/10 | 53.3% | [ ] |
| 1981 | [Minimize the Difference Between Target and Chosen Elements](https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/) | Medium | 6/10 | 36.9% | [ ] |
| 2218 | [Maximum Value of K Coins From Piles](https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/) | Hard | 7/10 | 60.4% | [ ] |
| 2585 | [Number of Ways to Earn Points](https://leetcode.com/problems/number-of-ways-to-earn-points/) | Hard | 7/10 | 59.8% | [ ] |
| 2742 | [Painting the Walls](https://leetcode.com/problems/painting-the-walls/) | Hard | 7/10 | 49.0% | [ ] |
| 3685 | [Subsequence Sum After Capping Elements](https://leetcode.com/problems/subsequence-sum-after-capping-elements/) | Medium | 7/10 | 25.3% | [ ] |
| 1449 | [Form Largest Integer With Digits That Add up to Target](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/) | Hard | 8/10 | 49.6% | [ ] |
| 879 | [Profitable Schemes](https://leetcode.com/problems/profitable-schemes/) | Hard | 8/10 | 48.3% | [ ] |
| 2518 | [Number of Great Partitions](https://leetcode.com/problems/number-of-great-partitions/) | Hard | 8/10 | 33.6% | [ ] |
| 956 | [Tallest Billboard](https://leetcode.com/problems/tallest-billboard/) | Hard | 9/10 | 51.8% | [ ] |
| 2809 | [Minimum Time to Make Array Sum At Most x](https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/) | Hard | 9/10 | 27.4% | [ ] |
| 2902 | [Count of Sub-Multisets With Bounded Sum](https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/) | Hard | 9/10 | 22.3% | [ ] |
| 3181 | [Maximum Total Reward Using Operations II](https://leetcode.com/problems/maximum-total-reward-using-operations-ii/) | Hard | 9/10 | 21.9% | [ ] |

## counting_dp

**What it is** — Counting DP counts the number of distinct ways to construct something (arrangements, sequences, structures) satisfying given constraints, modulo a prime. Recognize it when the problem asks "in how many ways..." and the answer grows exponentially without DP. The state captures how much of the structure has been built and what constraints remain active.

**Common steps**
1. Define `dp[state]` as the number of valid configurations for that state (e.g., `dp[i]` = ways to build a string of length `i`, `dp[i][j]` = ways using `i` elements with property `j`).
2. Write the recurrence by summing over all valid transitions into the current state.
3. Initialize the empty/base configuration to 1 (one way to do nothing).
4. Iterate in order of increasing state, summing contributions.
5. Apply modulo at every addition step to prevent overflow: `dp[i] = (dp[i] + dp[j]) % MOD`.
6. Read `dp[target_state]` as the answer.

**Key variations**
- Sequence counting (Count Vowels Permutation, Dice Roll Simulation): each position depends on a few prior states
- Combinatorial structure (Unique BSTs, Pascal's Triangle): Catalan-number style recurrences
- Counting with forbidden patterns: subtract invalid states or track the "bad" suffix explicitly
- Counting over a grid/path (Number of Increasing Paths): memoized DFS where each state = number of paths through that cell
- Counting partitions and distributions (K Inverse Pairs, Music Playlists): 2D DP where one dimension is the count constraint

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | Easy | 1/10 | 78.9% | [ ] |
| 119 | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) | Easy | 2/10 | 67.4% | [ ] |
| 1641 | [Count Sorted Vowel Strings](https://leetcode.com/problems/count-sorted-vowel-strings/) | Medium | 4/10 | 79.2% | [ ] |
| 750 | [Number Of Corner Rectangles](https://leetcode.com/problems/number-of-corner-rectangles/) :lock: | Medium | 4/10 | 67.9% | [ ] |
| 2189 | [Number of Ways to Build House of Cards](https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/) :lock: | Medium | 4/10 | 62.8% | [ ] |
| 1524 | [Number of Sub-arrays With Odd Sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/) | Medium | 4/10 | 55.7% | [ ] |
| 2320 | [Count Number of Ways to Place Houses](https://leetcode.com/problems/count-number-of-ways-to-place-houses/) | Medium | 4/10 | 43.9% | [ ] |
| 634 | [Find the Derangement of An Array](https://leetcode.com/problems/find-the-derangement-of-an-array/) :lock: | Medium | 4/10 | 41.7% | [ ] |
| 96 | [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | Medium | 5/10 | 63.7% | [ ] |
| 2930 | [Number of Strings Which Can Be Rearranged to Contain Substring](https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/) | Medium | 5/10 | 56.9% | [ ] |
| 2533 | [Number of Good Binary Strings](https://leetcode.com/problems/number-of-good-binary-strings/) :lock: | Medium | 5/10 | 52.9% | [ ] |
| 2222 | [Number of Ways to Select Buildings](https://leetcode.com/problems/number-of-ways-to-select-buildings/) | Medium | 5/10 | 50.9% | [ ] |
| 2400 | [Number of Ways to Reach a Position After Exactly k Steps](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/) | Medium | 5/10 | 36.9% | [ ] |
| 3129 | [Find All Possible Stable Binary Arrays I](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/) | Medium | 6/10 | 53.7% | [ ] |
| 823 | [Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors/) | Medium | 6/10 | 53.1% | [ ] |
| 1621 | [Number of Sets of K Non-Overlapping Line Segments](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/) | Medium | 6/10 | 45.9% | [ ] |
| 1866 | [Number of Ways to Rearrange Sticks With K Sticks Visible](https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/) | Hard | 7/10 | 61.2% | [ ] |
| 2147 | [Number of Ways to Divide a Long Corridor](https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/) | Hard | 7/10 | 54.6% | [ ] |
| 1955 | [Count Number of Special Subsequences](https://leetcode.com/problems/count-number-of-special-subsequences/) | Hard | 7/10 | 52.9% | [ ] |
| 1269 | [Number of Ways to Stay in the Same Place After Some Steps](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/) | Hard | 7/10 | 50.1% | [ ] |
| 1575 | [Count All Possible Routes](https://leetcode.com/problems/count-all-possible-routes/) | Hard | 8/10 | 64.8% | [ ] |
| 1692 | [Count Ways to Distribute Candies](https://leetcode.com/problems/count-ways-to-distribute-candies/) :lock: | Hard | 8/10 | 63.8% | [ ] |
| 920 | [Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists/) | Hard | 8/10 | 60.0% | [ ] |
| 3130 | [Find All Possible Stable Binary Arrays II](https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/) | Hard | 8/10 | 58.9% | [ ] |
| 2318 | [Number of Distinct Roll Sequences](https://leetcode.com/problems/number-of-distinct-roll-sequences/) | Hard | 8/10 | 58.1% | [ ] |
| 903 | [Valid Permutations for DI Sequence](https://leetcode.com/problems/valid-permutations-for-di-sequence/) | Hard | 8/10 | 56.4% | [ ] |
| 629 | [K Inverse Pairs Array](https://leetcode.com/problems/k-inverse-pairs-array/) | Hard | 8/10 | 49.0% | [ ] |
| 3082 | [Find the Sum of the Power of All Subsequences](https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/) | Hard | 8/10 | 38.3% | [ ] |
| 3154 | [Find Number of Ways to Reach the K-th Stair](https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/) | Hard | 8/10 | 37.6% | [ ] |
| 2552 | [Count Increasing Quadruplets](https://leetcode.com/problems/count-increasing-quadruplets/) | Hard | 8/10 | 34.5% | [ ] |
| 1420 | [Build Array Where You Can Find The Maximum Exactly K Comparisons](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/) | Hard | 9/10 | 65.7% | [ ] |
| 2338 | [Count the Number of Ideal Arrays](https://leetcode.com/problems/count-the-number-of-ideal-arrays/) | Hard | 9/10 | 56.9% | [ ] |
| 1569 | [Number of Ways to Reorder Array to Get Same BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/) | Hard | 9/10 | 54.1% | [ ] |
| 3725 | [Count Ways to Choose Coprime Integers from Rows](https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/) | Hard | 9/10 | 48.5% | [ ] |
| 2484 | [Count Palindromic Subsequences](https://leetcode.com/problems/count-palindromic-subsequences/) | Hard | 9/10 | 41.1% | [ ] |

## state_machine_dp

**What it is** — State machine DP models systems that move between a small, fixed set of explicit states (e.g., holding/not holding a stock, cooldown period, color choice), where the best outcome at step `i` depends on which state you were in at step `i-1`. Recognize it when the problem has mode-switching decisions — you can only do action B after doing action A, or being in state X prevents certain transitions. The dp table has one axis for position and one for state.

**Common steps**
1. Enumerate all meaningful states (e.g., for stocks: `held`, `not_held`, `cooldown`).
2. Define `dp[i][state]` as the best value after processing element `i` while in `state`.
3. Write transitions: for each state at step `i`, determine which states at step `i-1` can lead to it and at what cost.
4. Initialize step 0 for each state (often `dp[0][held] = -prices[0]`, `dp[0][not_held] = 0`).
5. Iterate forward, applying all transitions at each step.
6. Return the maximum over all "terminal" states at the last step (typically any non-held state).

**Key variations**
- Stock problems (Buy/Sell with cooldown, fee, k transactions): the core template; number of states grows with constraints
- Color/label assignment (Paint House, Paint Fence): states are the color choices; transitions forbid adjacent same colors
- Bounded transactions (Best Time IV): add a third dimension for number of transactions used
- Sequential movement with lanes (Minimum Sideway Jumps): state is the current lane
- Sequence generation with forbidden patterns (Student Attendance, Dice Roll Simulation): state encodes the recent history of choices

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 256 | [Paint House](https://leetcode.com/problems/paint-house/) :lock: | Medium | 3/10 | 64.4% | [ ] |
| 714 | [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | Medium | 5/10 | 71.9% | [ ] |
| 935 | [Knight Dialer](https://leetcode.com/problems/knight-dialer/) | Medium | 5/10 | 61.9% | [ ] |
| 1911 | [Maximum Alternating Subsequence Sum](https://leetcode.com/problems/maximum-alternating-subsequence-sum/) | Medium | 5/10 | 59.0% | [ ] |
| 1824 | [Minimum Sideway Jumps](https://leetcode.com/problems/minimum-sideway-jumps/) | Medium | 5/10 | 51.6% | [ ] |
| 309 | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | 6/10 | 62.0% | [ ] |
| 1220 | [Count Vowels Permutation](https://leetcode.com/problems/count-vowels-permutation/) | Hard | 6/10 | 61.3% | [ ] |
| 265 | [Paint House II](https://leetcode.com/problems/paint-house-ii/) :lock: | Hard | 6/10 | 57.1% | [ ] |
| 2361 | [Minimum Costs Using the Train Line](https://leetcode.com/problems/minimum-costs-using-the-train-line/) :lock: | Hard | 7/10 | 77.9% | [ ] |
| 1223 | [Dice Roll Simulation](https://leetcode.com/problems/dice-roll-simulation/) | Hard | 7/10 | 50.8% | [ ] |
| 801 | [Minimum Swaps To Make Sequences Increasing](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/) | Hard | 7/10 | 41.5% | [ ] |
| 1473 | [Paint House III](https://leetcode.com/problems/paint-house-iii/) | Hard | 8/10 | 61.2% | [ ] |
| 552 | [Student Attendance Record II](https://leetcode.com/problems/student-attendance-record-ii/) | Hard | 8/10 | 56.6% | [ ] |
| 123 | [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | Hard | 8/10 | 53.6% | [ ] |
| 188 | [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | Hard | 8/10 | 50.0% | [ ] |
| 1320 | [Minimum Distance to Type a Word Using Two Fingers](https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/) | Hard | 9/10 | 72.3% | [ ] |

## string_dp

**What it is** — String DP solves problems involving one or two strings where the answer depends on relationships between substrings or characters at specific positions. Recognize it when the problem asks to transform, match, segment, or compare strings with edit operations, wildcards, or dictionary lookups. The state typically encodes how far along each string you've processed.

**Common steps**
1. For two-string problems: create a 2D table `dp[i][j]` representing the answer for `s1[:i]` and `s2[:j]`.
2. For single-string segmentation (Word Break, Decode Ways): use 1D `dp[i]` = answer for the prefix of length `i`.
3. Write the recurrence based on whether the current characters match (or what edit operation to apply).
4. For Edit Distance: `dp[i][j] = dp[i-1][j-1]` if chars match; else `1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])`.
5. Initialize: empty string bases (`dp[0][j]`, `dp[i][0]`).
6. For segmentation, iterate over all valid splits at each position and check dictionary/pattern membership.

**Key variations**
- Edit distance family (Edit Distance, Delete Operations, Min ASCII Delete Sum): vary cost function and what operations are allowed
- Pattern matching with wildcards (Wildcard Matching, Regular Expression): handle `*` specially — it can match zero or more characters
- String segmentation (Word Break, Decode Ways): `dp[i] = OR over all j where s[j:i] is valid word`
- Interleaving / merging strings (Interleaving String): `dp[i][j]` = can we form `s3[:i+j]` from `s1[:i]` and `s2[:j]`
- Palindrome-based (Palindrome Partitioning II, Valid Palindrome III): precompute palindrome table, then apply 1D DP for cuts
- Counting string constructions (Distinct Subsequences, Decode Ways II): sum valid transitions instead of taking min/max

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 712 | [Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) | Medium | 4/10 | 71.0% | [ ] |
| 583 | [Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) | Medium | 4/10 | 65.5% | [ ] |
| 718 | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | Medium | 4/10 | 51.4% | [ ] |
| 1638 | [Count Substrings That Differ by One Character](https://leetcode.com/problems/count-substrings-that-differ-by-one-character/) | Medium | 5/10 | 72.3% | [ ] |
| 72 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | 5/10 | 60.5% | [ ] |
| 2707 | [Extra Characters in a String](https://leetcode.com/problems/extra-characters-in-a-string/) | Medium | 5/10 | 57.4% | [ ] |
| 139 | [Word Break](https://leetcode.com/problems/word-break/) | Medium | 5/10 | 49.4% | [ ] |
| 3503 | [Longest Palindrome After Substring Concatenation I](https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/) | Medium | 5/10 | 43.8% | [ ] |
| 97 | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | Medium | 6/10 | 44.0% | [ ] |
| 467 | [Unique Substrings in Wraparound String](https://leetcode.com/problems/unique-substrings-in-wraparound-string/) | Medium | 6/10 | 43.0% | [ ] |
| 2746 | [Decremental String Concatenation](https://leetcode.com/problems/decremental-string-concatenation/) | Medium | 6/10 | 27.7% | [ ] |
| 1092 | [Shortest Common Supersequence ](https://leetcode.com/problems/shortest-common-supersequence/) | Hard | 7/10 | 61.9% | [ ] |
| 2262 | [Total Appeal of A String](https://leetcode.com/problems/total-appeal-of-a-string/) | Hard | 7/10 | 56.4% | [ ] |
| 140 | [Word Break II](https://leetcode.com/problems/word-break-ii/) | Hard | 7/10 | 55.5% | [ ] |
| 1987 | [Number of Unique Good Subsequences](https://leetcode.com/problems/number-of-unique-good-subsequences/) | Hard | 7/10 | 52.3% | [ ] |
| 472 | [Concatenated Words](https://leetcode.com/problems/concatenated-words/) | Hard | 7/10 | 49.8% | [ ] |
| 1216 | [Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii/) :lock: | Hard | 7/10 | 49.2% | [ ] |
| 514 | [Freedom Trail](https://leetcode.com/problems/freedom-trail/) | Hard | 8/10 | 59.3% | [ ] |
| 1639 | [Number of Ways to Form a Target String Given a Dictionary](https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/) | Hard | 8/10 | 56.5% | [ ] |
| 1416 | [Restore The Array](https://leetcode.com/problems/restore-the-array/) | Hard | 8/10 | 46.7% | [ ] |
| 132 | [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) | Hard | 8/10 | 37.0% | [ ] |
| 2430 | [Maximum Deletions on a String](https://leetcode.com/problems/maximum-deletions-on-a-string/) | Hard | 8/10 | 35.9% | [ ] |
| 44 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | Hard | 8/10 | 31.9% | [ ] |
| 639 | [Decode Ways II](https://leetcode.com/problems/decode-ways-ii/) | Hard | 8/10 | 31.9% | [ ] |
| 3504 | [Longest Palindrome After Substring Concatenation II](https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/) | Hard | 8/10 | 18.0% | [ ] |
| 1531 | [String Compression II](https://leetcode.com/problems/string-compression-ii/) | Hard | 9/10 | 52.2% | [ ] |
| 2060 | [Check if an Original String Exists Given Two Encoded Strings](https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/) | Hard | 9/10 | 43.4% | [ ] |
| 1771 | [Maximize Palindrome Length From Subsequences](https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/) | Hard | 9/10 | 38.4% | [ ] |
| 466 | [Count The Repetitions](https://leetcode.com/problems/count-the-repetitions/) | Hard | 9/10 | 34.2% | [ ] |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard | 9/10 | 30.9% | [ ] |
| 1977 | [Number of Ways to Separate Numbers](https://leetcode.com/problems/number-of-ways-to-separate-numbers/) | Hard | 9/10 | 21.6% | [ ] |

## partition_dp

**What it is** — Partition DP splits an array or string into contiguous segments and optimizes a cost or count over all valid splits. Recognize it when the problem asks to divide a sequence into `k` parts, minimize/maximize some aggregate property of the parts, or count valid segmentations. The key transition tries all possible last-segment endpoints, making it O(n^2) or O(n^2 * k).

**Common steps**
1. Define `dp[i]` (or `dp[i][k]` with segment count) as the optimal value for the prefix ending at index `i` using at most/exactly `k` parts.
2. For each position `i`, try all previous split points `j < i`: `dp[i] = min/max over j of (dp[j] + cost(j+1, i))`.
3. Precompute any range costs (sums, max values, frequency counts) that appear inside the transition.
4. Initialize `dp[0] = 0` (cost of an empty prefix) and fill left to right.
5. For problems with a fixed number of cuts (k segments), add a second loop over `k` and fill the table row by row.
6. Optimize with the divide-and-conquer optimization or monotone queue when the cost function is concave/convex and the optimal split point is monotone.

**Key variations**
- Fixed number of partitions (Minimum Difficulty of a Job Schedule, Largest Sum of Averages): 2D DP with dimension for partition count
- Unconstrained segmentation (Word Break, Partition Array for Max Sum): try all split points with no limit on segment count
- Constrained segment properties (Palindrome Partitioning II, Minimum Substring Partition): precompute validity of each segment
- Counting valid partitions (Number of Beautiful Partitions): sum transitions instead of optimizing
- Quadrangle / divide-and-conquer optimization: applies when `cost(a,c) + cost(b,d) <= cost(a,d) + cost(b,c)` (intervals are concave)

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1043 | [Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/) | Medium | 5/10 | 77.3% | [ ] |
| 1105 | [Filling Bookcase Shelves](https://leetcode.com/problems/filling-bookcase-shelves/) | Medium | 5/10 | 68.6% | [ ] |
| 2767 | [Partition String Into Minimum Beautiful Substrings](https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/) | Medium | 5/10 | 54.1% | [ ] |
| 813 | [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages/) | Medium | 6/10 | 55.0% | [ ] |
| 1959 | [Minimum Total Space Wasted With K Resizing Operations](https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/) | Medium | 6/10 | 43.8% | [ ] |
| 3599 | [Partition Array to Minimize XOR](https://leetcode.com/problems/partition-array-to-minimize-xor/) | Medium | 6/10 | 41.3% | [ ] |
| 3144 | [Minimum Substring Partition of Equal Character Frequency](https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/) | Medium | 6/10 | 40.2% | [ ] |
| 3811 | [Number of Alternating XOR Partitions](https://leetcode.com/problems/number-of-alternating-xor-partitions/) | Medium | 6/10 | 27.0% | [ ] |
| 1335 | [Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/) | Hard | 8/10 | 59.8% | [ ] |
| 2547 | [Minimum Cost to Split an Array](https://leetcode.com/problems/minimum-cost-to-split-an-array/) | Hard | 8/10 | 44.4% | [ ] |
| 3826 | [Minimum Partition Score](https://leetcode.com/problems/minimum-partition-score/) | Hard | 8/10 | 33.9% | [ ] |
| 2911 | [Minimum Changes to Make K Semi-palindromes](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/) | Hard | 9/10 | 36.0% | [ ] |
| 2478 | [Number of Beautiful Partitions](https://leetcode.com/problems/number-of-beautiful-partitions/) | Hard | 9/10 | 33.0% | [ ] |
| 3505 | [Minimum Operations to Make Elements Within K Subarrays Equal](https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/) | Hard | 9/10 | 28.2% | [ ] |
| 3117 | [Minimum Sum of Values by Dividing Array](https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/) | Hard | 9/10 | 28.0% | [ ] |

## game_theory_dp

**What it is** — Game theory DP solves two-player zero-sum games where both players play optimally, and you need to determine the winner or the optimal score. Recognize it when two players alternate turns, each maximizing their own outcome, and the problem asks whether the first player wins or what the best achievable score is. The state encodes the current game configuration, and the value alternates between "maximize" and "minimize" perspectives.

**Common steps**
1. Define `dp[state]` as the best outcome the **current player** can achieve from that state (score difference, win/lose, etc.).
2. For each state, enumerate all valid moves the current player can make.
3. The current player picks the move that maximizes their result; the opponent will do the same on their turn, so: `dp[state] = max over moves of (value_of_move - dp[next_state])`.
4. Base cases: terminal states with no moves available (current player loses or score is 0).
5. Use memoization (top-down) or fill the table in reverse game-tree order (bottom-up).
6. The first player wins if `dp[initial_state] >= 0` (or > 0 for strict win).

**Key variations**
- Interval-based stone games (Stone Game I-VIII, Burst Balloons): state is a subarray `[l, r]`; current player takes from ends or a position within
- Minimax with boolean win/lose (Predict the Winner, Cat and Mouse): return true/false; current player wins if any move leads to opponent losing
- Nim-like take-away games (Stone Game IV): `dp[n]` = can current player win with `n` stones
- Graph-based games (Cat and Mouse): state includes both players' positions; requires careful cycle detection
- Games with variable move sets: enumerate all valid moves per state carefully (Flip Game II, Can I Win)

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 877 | [Stone Game](https://leetcode.com/problems/stone-game/) | Medium | 4/10 | 73.2% | [ ] |
| 486 | [Predict the Winner](https://leetcode.com/problems/predict-the-winner/) | Medium | 5/10 | 56.2% | [ ] |
| 294 | [Flip Game II](https://leetcode.com/problems/flip-game-ii/) :lock: | Medium | 5/10 | 52.3% | [ ] |
| 1140 | [Stone Game II](https://leetcode.com/problems/stone-game-ii/) | Medium | 6/10 | 72.8% | [ ] |
| 1690 | [Stone Game VII](https://leetcode.com/problems/stone-game-vii/) | Medium | 6/10 | 58.7% | [ ] |
| 375 | [Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) | Medium | 6/10 | 52.7% | [ ] |
| 1406 | [Stone Game III](https://leetcode.com/problems/stone-game-iii/) | Hard | 7/10 | 63.3% | [ ] |
| 1510 | [Stone Game IV](https://leetcode.com/problems/stone-game-iv/) | Hard | 7/10 | 59.6% | [ ] |
| 1872 | [Stone Game VIII](https://leetcode.com/problems/stone-game-viii/) | Hard | 7/10 | 53.9% | [ ] |
| 1563 | [Stone Game V](https://leetcode.com/problems/stone-game-v/) | Hard | 8/10 | 41.8% | [ ] |
| 1900 | [The Earliest and Latest Rounds Where Players Compete](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/) | Hard | 9/10 | 72.3% | [ ] |
| 1728 | [Cat and Mouse II](https://leetcode.com/problems/cat-and-mouse-ii/) | Hard | 10/10 | 40.3% | [ ] |
| 913 | [Cat and Mouse](https://leetcode.com/problems/cat-and-mouse/) | Hard | 10/10 | 35.2% | [ ] |
| 3283 | [Maximum Number of Moves to Kill All Pawns](https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/) | Hard | 10/10 | 33.9% | [ ] |

## interval_dp

**What it is** — Interval DP solves problems on contiguous subarrays or subsequences where the optimal answer for an interval `[l, r]` depends on answers for all smaller sub-intervals within it. Recognize it when you must consider all ways to split or combine a range — classic signals are "burst," "merge," "remove," "triangulate," or "partition a sequence optimally." The state is always `dp[l][r]` representing the best value for the subproblem on that range.

**Common steps**
1. Define `dp[l][r]` as the optimal value (max score, min cost, count of ways) for the subproblem on the interval `[l, r]`.
2. Base cases: single elements `dp[i][i]` or empty intervals `dp[i][i-1] = 0`.
3. Iterate by increasing interval **length** (not left index): for `length` from 2 to `n`, for each valid `l`, set `r = l + length - 1`.
4. For each `(l, r)`, try all split points `k` in `[l, r-1]` (or `[l+1, r]`): `dp[l][r] = min/max over k of (dp[l][k] + dp[k+1][r] + cost(l, k, r))`.
5. Be careful about the order: smaller intervals must be fully computed before larger ones.
6. The answer is `dp[0][n-1]`.

**Key variations**
- Splitting/merging with a cost (Burst Balloons, Minimum Cost to Merge Stones): the tricky part is what `cost(l, k, r)` is — for Burst Balloons it involves the "last burst" element
- Palindrome problems (Longest Palindromic Subsequence, Palindrome Partitioning III): base case `dp[i][i] = 1`; match or skip outer characters
- Optimal triangulation (Minimum Score Triangulation of Polygon): split polygon by fixing one triangle at a time
- Counting over intervals (Count Different Palindromic Subsequences, Zuma Game): sum over valid splits
- Remove/group operations (Remove Boxes, Strange Printer): state may need extra dimensions beyond just `[l, r]`

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 647 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | 4/10 | 72.8% | [x] |
| 516 | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | Medium | 5/10 | 65.3% | [ ] |
| 1039 | [Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/) | Medium | 6/10 | 67.4% | [ ] |
| 1682 | [Longest Palindromic Subsequence II](https://leetcode.com/problems/longest-palindromic-subsequence-ii/) :lock: | Medium | 6/10 | 50.3% | [ ] |
| 3040 | [Maximum Number of Operations With the Same Score II](https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/) | Medium | 6/10 | 34.2% | [ ] |
| 1312 | [Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | Hard | 7/10 | 73.9% | [ ] |
| 1547 | [Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) | Hard | 7/10 | 63.0% | [ ] |
| 1259 | [Handshakes That Don't Cross](https://leetcode.com/problems/handshakes-that-dont-cross/) :lock: | Hard | 7/10 | 59.9% | [ ] |
| 1278 | [Palindrome Partitioning III](https://leetcode.com/problems/palindrome-partitioning-iii/) | Hard | 8/10 | 62.2% | [ ] |
| 664 | [Strange Printer](https://leetcode.com/problems/strange-printer/) | Hard | 8/10 | 60.9% | [ ] |
| 2312 | [Selling Pieces of Wood](https://leetcode.com/problems/selling-pieces-of-wood/) | Hard | 8/10 | 52.9% | [ ] |
| 471 | [Encode String with Shortest Length](https://leetcode.com/problems/encode-string-with-shortest-length/) :lock: | Hard | 8/10 | 50.6% | [ ] |
| 1246 | [Palindrome Removal](https://leetcode.com/problems/palindrome-removal/) :lock: | Hard | 8/10 | 46.2% | [ ] |
| 1745 | [Palindrome Partitioning IV](https://leetcode.com/problems/palindrome-partitioning-iv/) | Hard | 8/10 | 45.5% | [ ] |
| 3018 | [Maximum Number of Removal Queries That Can Be Processed I](https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/) :lock: | Hard | 8/10 | 44.7% | [ ] |
| 1770 | [Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/) | Hard | 8/10 | 43.3% | [ ] |
| 312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | 9/10 | 63.4% | [ ] |
| 1478 | [Allocate Mailboxes](https://leetcode.com/problems/allocate-mailboxes/) | Hard | 9/10 | 56.5% | [ ] |
| 730 | [Count Different Palindromic Subsequences](https://leetcode.com/problems/count-different-palindromic-subsequences/) | Hard | 9/10 | 47.8% | [ ] |
| 1000 | [Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) | Hard | 9/10 | 46.1% | [ ] |
| 87 | [Scramble String](https://leetcode.com/problems/scramble-string/) | Hard | 9/10 | 44.5% | [ ] |
| 2019 | [The Score of Students Solving Math Expression](https://leetcode.com/problems/the-score-of-students-solving-math-expression/) | Hard | 9/10 | 34.2% | [ ] |
| 488 | [Zuma Game](https://leetcode.com/problems/zuma-game/) | Hard | 9/10 | 29.8% | [ ] |
| 546 | [Remove Boxes](https://leetcode.com/problems/remove-boxes/) | Hard | 10/10 | 49.4% | [ ] |

## tree_dp

**What it is** — Tree DP computes optimal values on rooted trees by combining solutions from child subtrees. Recognize it when the problem involves a tree and the answer at each node depends on decisions made in its subtrees (e.g., include or exclude a node, choose a color, aggregate a metric). The natural computation order is a post-order DFS: children are fully resolved before the parent is computed.

**Common steps**
1. Root the tree at node 0 (or any convenient node) and run a DFS.
2. Define `dp[node][state]` where state captures the local decision at `node` (e.g., robbed/not robbed, color assigned).
3. In the DFS, first recurse on all children to get their dp values.
4. At each node, combine children results: for each valid state at `node`, pick the best compatible states from each child.
5. Return `dp[node]` up the call stack; the root's dp holds the global answer.
6. For re-rooting problems (answers needed for every root): do a second DFS top-down, propagating the parent's contribution back down.

**Key variations**
- Include/exclude at each node (House Robber III): `dp[node] = (rob_node, skip_node)`; if robbed, children must be skipped
- Subtree aggregation (Maximum Good Subtree Score, Subtree Inversion Sum): aggregate over all subtree nodes with a sum or bitmask
- Re-rooting technique: compute answers for all possible roots in O(n) using two DFS passes
- Tree knapsack (selecting k nodes across subtrees): combine child DPs like a multi-dimensional knapsack within the DFS

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 894 | [All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees/) | Medium | 5/10 | 82.8% | [ ] |
| 337 | [House Robber III](https://leetcode.com/problems/house-robber-iii/) | Medium | 6/10 | 55.9% | [ ] |
| 3562 | [Maximum Profit from Trading Stocks with Discounts](https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/) | Hard | 9/10 | 56.6% | [ ] |
| 3544 | [Subtree Inversion Sum](https://leetcode.com/problems/subtree-inversion-sum/) | Hard | 9/10 | 44.1% | [ ] |
| 3575 | [Maximum Good Subtree Score](https://leetcode.com/problems/maximum-good-subtree-score/) | Hard | 10/10 | 45.4% | [ ] |

## bitmask_dp

**What it is** — Bitmask DP represents a subset of items as a binary integer (bitmask) and uses DP over all 2^n subsets to find an optimal assignment or traversal. Recognize it when `n` is small (typically n ≤ 20) and the problem involves assigning items to slots, visiting all nodes in a graph (TSP-style), or covering a set with subsets. The bit at position `i` being 1 means item `i` is in the current subset.

**Common steps**
1. Represent the subset of completed/assigned/visited items as an integer `mask` (0 to 2^n - 1).
2. Define `dp[mask][last]` (or just `dp[mask]`) as the best value when the items in `mask` have been handled, with `last` being the most recently added item if order matters.
3. Initialize `dp[0] = 0` (or `dp[0][start] = 0` for path problems).
4. Iterate over all masks in increasing order; for each mask, try adding any item `i` not yet in the mask: `new_mask = mask | (1 << i)`.
5. Transition: `dp[new_mask][i] = min/max(dp[new_mask][i], dp[mask][last] + cost(last, i))`.
6. Answer: `dp[(1<<n)-1]` (all items included) or aggregate over all final states.

**Key variations**
- Assignment problems (Maximum Compatibility Score, Campus Bikes II): match n workers to n jobs; state = subset of jobs assigned
- Hamiltonian path / TSP (Shortest Superstring, Find Minimum Time to Finish All Jobs): state = visited set + current position
- Coloring / painting with constraints (Painting a Grid, Student Exam Seating): encode row/column state as a bitmask
- Subset-sum over subsets (Number of Good Subsets, Stickers to Spell Word): iterate over all submasks of each mask
- Profile DP on grids (Painting a Grid With Three Different Colors): bitmask encodes the coloring of one row/column

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2992 | [Number of Self-Divisible Permutations](https://leetcode.com/problems/number-of-self-divisible-permutations/) :lock: | Medium | 5/10 | 71.8% | [ ] |
| 1947 | [Maximum Compatibility Score Sum](https://leetcode.com/problems/maximum-compatibility-score-sum/) | Medium | 5/10 | 64.4% | [ ] |
| 2184 | [Number of Ways to Build Sturdy Brick Wall](https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/) :lock: | Medium | 5/10 | 49.5% | [ ] |
| 2002 | [Maximum Product of the Length of Two Palindromic Subsequences](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/) | Medium | 6/10 | 62.5% | [ ] |
| 1066 | [Campus Bikes II](https://leetcode.com/problems/campus-bikes-ii/) :lock: | Medium | 6/10 | 55.9% | [ ] |
| 638 | [Shopping Offers](https://leetcode.com/problems/shopping-offers/) | Medium | 6/10 | 52.4% | [ ] |
| 2152 | [Minimum Number of Lines to Cover Points](https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/) :lock: | Medium | 6/10 | 43.9% | [ ] |
| 1986 | [Minimum Number of Work Sessions to Finish the Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) | Medium | 6/10 | 34.8% | [ ] |
| 3376 | [Minimum Time to Break Locks I](https://leetcode.com/problems/minimum-time-to-break-locks-i/) | Medium | 6/10 | 32.5% | [ ] |
| 2247 | [Maximum Cost of Trip With K Highways](https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/) :lock: | Hard | 7/10 | 51.1% | [ ] |
| 464 | [Can I Win](https://leetcode.com/problems/can-i-win/) | Medium | 7/10 | 31.4% | [ ] |
| 2741 | [Special Permutations](https://leetcode.com/problems/special-permutations/) | Medium | 7/10 | 29.6% | [ ] |
| 2572 | [Count the Number of Square-Free Subsets](https://leetcode.com/problems/count-the-number-of-square-free-subsets/) | Medium | 7/10 | 26.6% | [ ] |
| 1931 | [Painting a Grid With Three Different Colors](https://leetcode.com/problems/painting-a-grid-with-three-different-colors/) | Hard | 8/10 | 77.1% | [ ] |
| 1799 | [Maximize Score After N Operations](https://leetcode.com/problems/maximize-score-after-n-operations/) | Hard | 8/10 | 57.9% | [ ] |
| 2403 | [Minimum Time to Kill All Monsters](https://leetcode.com/problems/minimum-time-to-kill-all-monsters/) :lock: | Hard | 8/10 | 57.5% | [ ] |
| 1879 | [Minimum XOR Sum of Two Arrays](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/) | Hard | 8/10 | 51.1% | [ ] |
| 2172 | [Maximum AND Sum of Array](https://leetcode.com/problems/maximum-and-sum-of-array/) | Hard | 8/10 | 50.6% | [ ] |
| 1723 | [Find Minimum Time to Finish All Jobs](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/) | Hard | 8/10 | 45.7% | [ ] |
| 3533 | [Concatenated Divisibility](https://leetcode.com/problems/concatenated-divisibility/) | Hard | 8/10 | 30.9% | [ ] |
| 3530 | [Maximum Profit from Valid Topological Order in DAG](https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/) | Hard | 8/10 | 30.3% | [ ] |
| 3444 | [Minimum Increments for Target Multiples in an Array](https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/) | Hard | 8/10 | 27.7% | [ ] |
| 1617 | [Count Subtrees With Max Distance Between Cities](https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/) | Hard | 9/10 | 67.2% | [ ] |
| 1125 | [Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/) | Hard | 9/10 | 55.5% | [ ] |
| 1349 | [Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/) | Hard | 9/10 | 53.8% | [ ] |
| 3003 | [Maximize the Number of Partitions After Operations](https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/) | Hard | 9/10 | 53.4% | [ ] |
| 691 | [Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/) | Hard | 9/10 | 50.8% | [ ] |
| 1595 | [Minimum Cost to Connect Two Groups of Points](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/) | Hard | 9/10 | 50.0% | [ ] |
| 1434 | [Number of Ways to Wear Different Hats to Each Other](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) | Hard | 9/10 | 46.0% | [ ] |
| 943 | [Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/) | Hard | 9/10 | 45.4% | [ ] |
| 1815 | [Maximum Number of Groups Getting Fresh Donuts](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/) | Hard | 9/10 | 41.3% | [ ] |
| 1681 | [Minimum Incompatibility](https://leetcode.com/problems/minimum-incompatibility/) | Hard | 9/10 | 41.1% | [ ] |
| 1655 | [Distribute Repeating Integers](https://leetcode.com/problems/distribute-repeating-integers/) | Hard | 9/10 | 40.6% | [ ] |
| 1787 | [Make the XOR of All Segments Equal to Zero](https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/) | Hard | 9/10 | 40.6% | [ ] |
| 1994 | [The Number of Good Subsets](https://leetcode.com/problems/the-number-of-good-subsets/) | Hard | 9/10 | 37.1% | [ ] |
| 3801 | [Minimum Cost to Merge Sorted Lists](https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/) | Hard | 9/10 | 34.5% | [ ] |
| 1494 | [Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/) | Hard | 9/10 | 30.9% | [ ] |
| 3594 | [Minimum Time to Transport All Individuals](https://leetcode.com/problems/minimum-time-to-transport-all-individuals/) | Hard | 9/10 | 28.3% | [ ] |
| 3149 | [Find the Minimum Cost Array Permutation](https://leetcode.com/problems/find-the-minimum-cost-array-permutation/) | Hard | 9/10 | 25.6% | [ ] |
| 3287 | [Find the Maximum Sequence Value of Array](https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/) | Hard | 9/10 | 21.5% | [ ] |
| 3276 | [Select Cells in Grid With Maximum Score](https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/) | Hard | 9/10 | 15.8% | [ ] |
| 3539 | [Find Sum of Array Product of Magical Sequences](https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/) | Hard | 10/10 | 61.8% | [ ] |
| 1659 | [Maximize Grid Happiness](https://leetcode.com/problems/maximize-grid-happiness/) | Hard | 10/10 | 40.9% | [ ] |

## digit_dp

**What it is** — Digit DP counts integers in a range `[0, N]` (or `[L, R]`) satisfying a digit-level constraint (no repeating digits, sum of digits divisible by k, specific digit patterns). Recognize it when the problem asks "how many numbers from 1 to N have property X" and the property depends on individual digits. The key insight is to build the number digit by digit from most significant to least significant, tracking a "tight" flag that indicates whether the current prefix equals N's prefix.

**Common steps**
1. Convert N to its digit array.
2. Define `dp[pos][state][tight][started]` where `pos` = current digit position, `state` = the digit-constraint state (e.g., remainder, set of digits used), `tight` = are we still bounded by N's digits, `started` = have we placed a non-zero digit yet (handles leading zeros).
3. At each position, try placing digits 0 through `(tight ? N[pos] : 9)`.
4. If `tight` and we place `N[pos]`, the next state remains tight; otherwise it becomes free.
5. Memoize on `(pos, state, tight, started)` — the tight and started flags allow caching across calls.
6. For a range `[L, R]`, compute `f(R) - f(L-1)` using the standard digit DP on upper bound.

**Key variations**
- No repeated digits (Count Special Integers): state = bitmask of digits used so far
- Digit sum constraints (Count of Integers, Beautiful Integers): state = running sum or sum modulo k
- Consecutive digit constraints (Non-negative Integers without Consecutive Ones, Stepping Numbers): state = last digit placed
- Combined with string pattern matching (Find All Good Strings): state includes KMP automaton position
- Leading zero handling: use a `started` flag; before `started`, placing 0 doesn't change the digit state

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2376 | [Count Special Integers](https://leetcode.com/problems/count-special-integers/) | Hard | 7/10 | 42.5% | [ ] |
| 1012 | [Numbers With Repeated Digits](https://leetcode.com/problems/numbers-with-repeated-digits/) | Hard | 8/10 | 46.5% | [ ] |
| 1067 | [Digit Count in Range](https://leetcode.com/problems/digit-count-in-range/) :lock: | Hard | 8/10 | 46.4% | [ ] |
| 2999 | [Count the Number of Powerful Integers](https://leetcode.com/problems/count-the-number-of-powerful-integers/) | Hard | 8/10 | 46.2% | [ ] |
| 902 | [Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) | Hard | 8/10 | 45.0% | [ ] |
| 600 | [Non-negative Integers without Consecutive Ones](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/) | Hard | 8/10 | 42.3% | [ ] |
| 2719 | [Count of Integers](https://leetcode.com/problems/count-of-integers/) | Hard | 8/10 | 38.5% | [ ] |
| 2801 | [Count Stepping Numbers in Range](https://leetcode.com/problems/count-stepping-numbers-in-range/) | Hard | 8/10 | 28.3% | [ ] |
| 3621 | [Number of Integers With Popcount-Depth Equal to K I](https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/) | Hard | 9/10 | 22.6% | [ ] |
| 2827 | [Number of Beautiful Integers in the Range](https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/) | Hard | 9/10 | 22.2% | [ ] |
| 1397 | [Find All Good Strings](https://leetcode.com/problems/find-all-good-strings/) | Hard | 10/10 | 45.3% | [ ] |

## matrix_exponentiation_dp

**What it is** — Matrix exponentiation DP accelerates linear recurrences from O(n) to O(log n) by expressing the recurrence as a matrix multiplication and using fast matrix exponentiation. Recognize it when a DP recurrence involves a fixed-size state vector and the transition is the same at every step — meaning you need the value after a very large number of steps (n up to 10^18). The idea is that applying the transition matrix `n` times equals the matrix raised to the power `n`.

**Common steps**
1. Express the recurrence as a vector-matrix product: `state[i+1] = T * state[i]` where `T` is the constant transition matrix.
2. Identify the state vector (e.g., `[dp[i], dp[i-1], dp[i-2]]`) and build the transition matrix `T` that maps it to the next step.
3. Use fast matrix exponentiation (repeated squaring) to compute `T^n` in O(k^3 log n) where `k` is the matrix size.
4. Multiply `T^n` by the initial state vector to get the final state.
5. Apply modular arithmetic throughout all matrix multiplications.
6. Verify by checking small cases manually against the naive recurrence.

**Key variations**
- Simple linear recurrences (Fibonacci in O(log n)): 2x2 matrix
- Counting paths in a graph after exactly k steps: adjacency matrix raised to power k
- String transformation problems: encode character transitions as a matrix; exponentiate to count k-step transformations
- Ball-passing games (Maximize Value of Function): binary lifting — precompute jump[node][k] = node reached after 2^k passes

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2836 | [Maximize Value of Function in a Ball Passing Game](https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/) | Hard | 9/10 | 30.8% | [ ] |
| 2851 | [String Transformation](https://leetcode.com/problems/string-transformation/) | Hard | 10/10 | 27.1% | [ ] |
