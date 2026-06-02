# Greedy

331 problems across 14 patterns.

## stock_trading

**What it is** — Stock trading problems ask you to maximize profit (or minimize loss) over a sequence of prices, where you decide when to buy and sell. The greedy insight is that in single-transaction problems you track the running minimum price, and in multi-transaction problems every upward price move is independently profitable so you collect each positive difference.

**Common steps**
1. Determine the constraint: one transaction, unlimited, or k transactions.
2. For one transaction: track `min_price` seen so far; at each step compute `price - min_price` and update `max_profit`.
3. For unlimited transactions: scan consecutive pairs; accumulate `price[i+1] - price[i]` whenever it is positive.
4. Return the accumulated profit (0 if never profitable).

**Key variations**
- Single buy/sell (LC 121): one pass tracking running minimum.
- Unlimited transactions (LC 122): sum all positive daily deltas; no state needed beyond the previous price.
- Cooldown / transaction fee variants: these shift from pure greedy to DP.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | 2/10 | 56.7% | [x] |
| 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium | 3/10 | 71.0% | [ ] |

## greedy_sorting

**What it is** — These problems become tractable once you sort the input (or sort by a derived key), after which the optimal greedy choice at each position is obvious and locally verifiable. Recognise this pattern when the relative order of elements is the only thing standing between you and a simple linear scan.

**Common steps**
1. Identify the sorting key (raw values, differences, negatives first, custom comparator, etc.).
2. Sort the array (or use a frequency-sorted structure) in the required order.
3. Iterate linearly and apply the greedy rule (take, skip, pair, assign) at each position.
4. Accumulate the answer (count, sum, boolean flag).
5. Handle edge cases: ties in the sort key, even/odd parity, or leftover elements.

**Key variations**
- Pair adjacent elements after sorting (array partition, minimise difference).
- Sort descending then apply buy-every-third or similar discount rules.
- Sort by a composite key (value + label, or value + degree) for constrained selection.
- Custom comparator sort to form the lexicographically largest/smallest concatenation.
- Sort plus a second pass to greedily fix constraint violations (increment to unique, etc.).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2037 | [Minimum Number of Moves to Seat Everyone](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/) | Easy | 1/10 | 87.2% | [ ] |
| 2706 | [Buy Two Chocolates](https://leetcode.com/problems/buy-two-chocolates/) | Easy | 1/10 | 68.4% | [ ] |
| 561 | [Array Partition](https://leetcode.com/problems/array-partition/) | Easy | 2/10 | 81.7% | [ ] |
| 3074 | [Apple Redistribution into Boxes](https://leetcode.com/problems/apple-redistribution-into-boxes/) | Easy | 2/10 | 78.5% | [ ] |
| 3684 | [Maximize Sum of At Most K Distinct Elements](https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/) | Easy | 2/10 | 77.0% | [ ] |
| 1403 | [Minimum Subsequence in Non-Increasing Order](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/) | Easy | 2/10 | 73.7% | [ ] |
| 3745 | [Maximize Expression of Three Elements](https://leetcode.com/problems/maximize-expression-of-three-elements/) | Easy | 2/10 | 72.6% | [ ] |
| 1196 | [How Many Apples Can You Put into the Basket](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/) :lock: | Easy | 2/10 | 67.1% | [ ] |
| 1708 | [Largest Subarray Length K](https://leetcode.com/problems/largest-subarray-length-k/) :lock: | Easy | 2/10 | 65.8% | [ ] |
| 2231 | [Largest Number After Digit Swaps by Parity](https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/) | Easy | 2/10 | 65.3% | [ ] |
| 2144 | [Minimum Cost of Buying Candies With Discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/) | Easy | 2/10 | 62.8% | [ ] |
| 976 | [Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/) | Easy | 2/10 | 62.2% | [ ] |
| 1561 | [Maximum Number of Coins You Can Get](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/) | Medium | 3/10 | 84.8% | [ ] |
| 1833 | [Maximum Ice Cream Bars](https://leetcode.com/problems/maximum-ice-cream-bars/) | Medium | 3/10 | 74.3% | [ ] |
| 3730 | [Maximum Calories Burnt from Jumps](https://leetcode.com/problems/maximum-calories-burnt-from-jumps/) :lock: | Medium | 3/10 | 72.4% | [ ] |
| 1433 | [Check If a String Can Break Another String](https://leetcode.com/problems/check-if-a-string-can-break-another-string/) | Medium | 3/10 | 71.0% | [ ] |
| 3627 | [Maximum Median Sum of Subsequences of Size 3](https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/) | Medium | 3/10 | 65.1% | [ ] |
| 3572 | [Maximize Y‑Sum by Picking a Triplet of Distinct X‑Values](https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/) | Medium | 3/10 | 63.4% | [ ] |
| 1005 | [Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/) | Easy | 3/10 | 53.8% | [ ] |
| 2966 | [Divide Array Into Arrays With Max Difference](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/) | Medium | 4/10 | 79.0% | [ ] |
| 2285 | [Maximum Total Importance of Roads](https://leetcode.com/problems/maximum-total-importance-of-roads/) | Medium | 4/10 | 69.1% | [ ] |
| 2279 | [Maximum Bags With Full Capacity of Rocks](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/) | Medium | 4/10 | 68.1% | [ ] |
| 1846 | [Maximum Element After Decreasing and Rearranging](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/) | Medium | 4/10 | 65.7% | [ ] |
| 1090 | [Largest Values From Labels](https://leetcode.com/problems/largest-values-from-labels/) | Medium | 4/10 | 64.3% | [ ] |
| 3727 | [Maximum Alternating Sum of Squares](https://leetcode.com/problems/maximum-alternating-sum-of-squares/) | Medium | 4/10 | 61.5% | [ ] |
| 945 | [Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/) | Medium | 4/10 | 60.7% | [ ] |
| 2679 | [Sum in a Matrix](https://leetcode.com/problems/sum-in-a-matrix/) | Medium | 4/10 | 60.6% | [ ] |
| 1509 | [Minimum Difference Between Largest and Smallest Value in Three Moves](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/) | Medium | 4/10 | 59.2% | [ ] |
| 3075 | [Maximize Happiness of Selected Children](https://leetcode.com/problems/maximize-happiness-of-selected-children/) | Medium | 4/10 | 58.7% | [ ] |
| 826 | [Most Profit Assigning Work](https://leetcode.com/problems/most-profit-assigning-work/) | Medium | 4/10 | 56.2% | [ ] |
| 2126 | [Destroying Asteroids](https://leetcode.com/problems/destroying-asteroids/) | Medium | 4/10 | 53.5% | [ ] |
| 3496 | [Maximize Score After Pair Deletions](https://leetcode.com/problems/maximize-score-after-pair-deletions/) :lock: | Medium | 4/10 | 52.6% | [ ] |
| 1968 | [Array With Elements Not Equal to Average of Neighbors](https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/) | Medium | 4/10 | 50.7% | [ ] |
| 2587 | [Rearrange Array to Maximize Prefix Score](https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/) | Medium | 4/10 | 42.8% | [ ] |
| 274 | [H-Index](https://leetcode.com/problems/h-index/) | Medium | 4/10 | 41.4% | [ ] |
| 1465 | [Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/) | Medium | 4/10 | 41.4% | [ ] |
| 406 | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | Medium | 5/10 | 74.7% | [ ] |
| 969 | [Pancake Sorting](https://leetcode.com/problems/pancake-sorting/) | Medium | 5/10 | 71.8% | [ ] |
| 1536 | [Minimum Swaps to Arrange a Binary Grid](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/) | Medium | 5/10 | 70.1% | [ ] |
| 1798 | [Maximum Number of Consecutive Values You Can Make](https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/) | Medium | 5/10 | 64.0% | [ ] |
| 3397 | [Maximum Number of Distinct Elements After Operations](https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/) | Medium | 5/10 | 52.2% | [ ] |
| 2567 | [Minimum Score by Changing Two Elements](https://leetcode.com/problems/minimum-score-by-changing-two-elements/) | Medium | 5/10 | 49.9% | [ ] |
| 3107 | [Minimum Operations to Make Median of Array Equal to K](https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/) | Medium | 5/10 | 47.9% | [ ] |
| 3780 | [Maximum Sum of Three Numbers Divisible by Three](https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/) | Medium | 5/10 | 47.7% | [ ] |
| 3732 | [Maximum Product of Three Elements After One Replacement](https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/) | Medium | 5/10 | 47.5% | [ ] |
| 179 | [Largest Number](https://leetcode.com/problems/largest-number/) | Medium | 5/10 | 43.0% | [ ] |
| 2497 | [Maximum Star Sum of a Graph](https://leetcode.com/problems/maximum-star-sum-of-a-graph/) | Medium | 5/10 | 42.3% | [ ] |
| 3424 | [Minimum Cost to Make Arrays Identical](https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/) | Medium | 5/10 | 37.8% | [ ] |
| 3301 | [Maximize the Total Height of Unique Towers](https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/) | Medium | 5/10 | 37.4% | [ ] |
| 2098 | [Subsequence of Size K With the Largest Even Sum](https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/) :lock: | Medium | 5/10 | 35.6% | [ ] |
| 1727 | [Largest Submatrix With Rearrangements](https://leetcode.com/problems/largest-submatrix-with-rearrangements/) | Medium | 6/10 | 80.2% | [ ] |
| 1402 | [Reducing Dishes](https://leetcode.com/problems/reducing-dishes/) | Hard | 6/10 | 76.7% | [ ] |
| 1589 | [Maximum Sum Obtained of Any Permutation](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) | Medium | 6/10 | 40.8% | [ ] |
| 2007 | [Find Original Array From Doubled Array](https://leetcode.com/problems/find-original-array-from-doubled-array/) | Medium | 6/10 | 40.8% | [ ] |
| 3207 | [Maximum Points After Enemy Battles](https://leetcode.com/problems/maximum-points-after-enemy-battles/) | Medium | 6/10 | 33.3% | [ ] |
| 3457 | [Eat Pizzas!](https://leetcode.com/problems/eat-pizzas/) | Medium | 6/10 | 33.3% | [ ] |
| 3645 | [Maximum Total from Optimal Activation Order](https://leetcode.com/problems/maximum-total-from-optimal-activation-order/) | Medium | 6/10 | 33.3% | [ ] |
| 3752 | [Lexicographically Smallest Negated Permutation that Sums to Target](https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/) | Medium | 6/10 | 31.2% | [ ] |
| 2931 | [Maximum Spending After Buying Items](https://leetcode.com/problems/maximum-spending-after-buying-items/) | Hard | 7/10 | 61.1% | [ ] |
| 324 | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) | Medium | 7/10 | 37.4% | [ ] |
| 3854 | [Minimum Operations to Make Array Parity Alternating](https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/) | Medium | 7/10 | 17.0% | [ ] |
| 2263 | [Make Array Non-decreasing or Non-increasing](https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/) :lock: | Hard | 8/10 | 65.5% | [ ] |
| 2561 | [Rearranging Fruits](https://leetcode.com/problems/rearranging-fruits/) | Hard | 8/10 | 57.3% | [ ] |

## digit_construction

**What it is** — Digit construction problems ask you to build, modify, or remap the digits of a number to achieve an extremal (largest, smallest, most palindromic, etc.) result. The greedy insight is to process digits from the most significant position first and make the locally best swap or replacement at the first opportunity, then stop — changing an earlier digit dominates changing any later one.

**Common steps**
1. Convert the number to a list or string of its digits for easy manipulation.
2. Decide the direction: scan left-to-right for maximization (replace the first digit that can be improved), right-to-left for minimization.
3. At each position, check whether applying the allowed operation (remap, swap, delete, insert) strictly improves the current digit.
4. Apply the operation at the first beneficial position and stop (one-shot greedy) — or continue if the operation has unlimited uses.
5. Reconstruct the number from the modified digit list and return it.

**Key variations**
- Single remap of all occurrences of one digit (max/min difference).
- Remove exactly one digit to maximise the remaining number.
- Insert a digit at the optimal position.
- Replace a contiguous substring greedily from the left.
- Repeatedly apply an operation (monotone increasing digits requires a backward pass).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2160 | [Minimum Sum of Four Digit Number After Splitting Digits](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/) | Easy | 1/10 | 86.3% | [ ] |
| 1323 | [Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/) | Easy | 1/10 | 84.5% | [ ] |
| 2864 | [Maximum Odd Binary Number](https://leetcode.com/problems/maximum-odd-binary-number/) | Easy | 1/10 | 82.9% | [ ] |
| 2566 | [Maximum Difference by Remapping a Digit](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/) | Easy | 2/10 | 76.1% | [ ] |
| 2578 | [Split With Minimum Sum](https://leetcode.com/problems/split-with-minimum-sum/) | Easy | 2/10 | 73.5% | [ ] |
| 1736 | [Latest Time by Replacing Hidden Digits](https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/) | Easy | 2/10 | 43.8% | [ ] |
| 2259 | [Remove Digit From Number to Maximize Result](https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/) | Easy | 3/10 | 48.5% | [ ] |
| 1663 | [Smallest String With A Given Numeric Value](https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/) | Medium | 4/10 | 67.4% | [ ] |
| 3723 | [Maximize Sum of Squares of Digits](https://leetcode.com/problems/maximize-sum-of-squares-of-digits/) | Medium | 4/10 | 59.0% | [ ] |
| 1881 | [Maximum Value after Insertion](https://leetcode.com/problems/maximum-value-after-insertion/) | Medium | 4/10 | 39.4% | [ ] |
| 484 | [Find Permutation](https://leetcode.com/problems/find-permutation/) :lock: | Medium | 5/10 | 66.9% | [ ] |
| 738 | [Monotone Increasing Digits](https://leetcode.com/problems/monotone-increasing-digits/) | Medium | 5/10 | 49.6% | [ ] |
| 1053 | [Previous Permutation With One Swap](https://leetcode.com/problems/previous-permutation-with-one-swap/) | Medium | 5/10 | 49.2% | [ ] |
| 1432 | [Max Difference You Can Get From Changing an Integer](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/) | Medium | 5/10 | 48.7% | [ ] |
| 2457 | [Minimum Addition to Make Integer Beautiful](https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/) | Medium | 5/10 | 38.7% | [ ] |
| 2844 | [Minimum Operations to Make a Special Number](https://leetcode.com/problems/minimum-operations-to-make-a-special-number/) | Medium | 5/10 | 38.5% | [ ] |
| 1946 | [Largest Number After Mutating Substring](https://leetcode.com/problems/largest-number-after-mutating-substring/) | Medium | 5/10 | 38.1% | [ ] |
| 2384 | [Largest Palindromic Number](https://leetcode.com/problems/largest-palindromic-number/) | Medium | 5/10 | 37.1% | [ ] |
| 2847 | [Smallest Number With Given Digit Product](https://leetcode.com/problems/smallest-number-with-given-digit-product/) :lock: | Medium | 6/10 | 43.6% | [ ] |
| 3720 | [Lexicographically Smallest Permutation Greater Than Target](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/) | Medium | 7/10 | 26.7% | [ ] |
| 1363 | [Largest Multiple of Three](https://leetcode.com/problems/largest-multiple-of-three/) | Hard | 8/10 | 33.2% | [ ] |
| 3348 | [Smallest Divisible Digit Product II](https://leetcode.com/problems/smallest-divisible-digit-product-ii/) | Hard | 9/10 | 14.6% | [ ] |

## greedy_counting

**What it is** — Greedy counting problems require you to count frequencies or track running tallies to make optimal decisions without looking ahead. The key observation is that the structure of the problem (character frequencies, parenthesis balance, group sizes) directly determines the minimum operations or maximum items, and a simple frequency-based rule gives the global optimum.

**Common steps**
1. Count element frequencies using a hash map or counter.
2. Sort or process the frequencies in a specific order (ascending for removal, descending for selection).
3. Apply a greedy rule at each step (remove the least frequent element first, fill groups greedily, pair complementary characters).
4. Track any running balance or remainder that carries over between steps.
5. Return the accumulated count of operations or the size of the result.

**Key variations**
- Frequency-based removal (remove least frequent to reduce distinct count by half).
- Group filling: divide elements into fixed-size groups greedily (hand of straights, consecutive subsequences).
- Parenthesis balancing: count unmatched opens and closes in one pass.
- Binary string alternation: count mismatches with both possible patterns and take the minimum.
- Pair-matching with a hash map (palindrome construction from two-letter words).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1221 | [Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/) | Easy | 1/10 | 87.4% | [ ] |
| 2600 | [K Items With the Maximum Sum](https://leetcode.com/problems/k-items-with-the-maximum-sum/) | Easy | 1/10 | 60.2% | [ ] |
| 3545 | [Minimum Deletions for At Most K Distinct Characters](https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/) | Easy | 2/10 | 73.1% | [ ] |
| 1758 | [Minimum Changes To Make Alternating Binary String](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/) | Easy | 2/10 | 67.8% | [ ] |
| 409 | [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) | Easy | 2/10 | 56.0% | [ ] |
| 3487 | [Maximum Unique Subarray Sum After Deletion](https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/) | Easy | 2/10 | 40.5% | [ ] |
| 921 | [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/) | Medium | 3/10 | 74.4% | [ ] |
| 1338 | [Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/) | Medium | 3/10 | 69.4% | [ ] |
| 2554 | [Maximum Number of Integers to Choose From a Range I](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/) | Medium | 3/10 | 68.0% | [ ] |
| 1481 | [Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/) | Medium | 3/10 | 63.8% | [ ] |
| 1963 | [Minimum Number of Swaps to Make the String Balanced](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/) | Medium | 4/10 | 78.0% | [ ] |
| 1111 | [Maximum Nesting Depth of Two Valid Parentheses Strings](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) | Medium | 4/10 | 71.9% | [ ] |
| 3228 | [Maximum Number of Operations to Move Ones to the End](https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/) | Medium | 4/10 | 67.1% | [ ] |
| 3192 | [Minimum Operations to Make Binary Array Elements Equal to One II](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/) | Medium | 4/10 | 65.1% | [ ] |
| 2244 | [Minimum Rounds to Complete All Tasks](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/) | Medium | 4/10 | 63.3% | [ ] |
| 2038 | [Remove Colored Pieces if Both Neighbors are the Same Color](https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/) | Medium | 4/10 | 63.1% | [ ] |
| 2870 | [Minimum Number of Operations to Make Array Empty](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/) | Medium | 4/10 | 62.1% | [ ] |
| 1647 | [Minimum Deletions to Make Character Frequencies Unique](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/) | Medium | 4/10 | 61.5% | [ ] |
| 1007 | [Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) | Medium | 4/10 | 56.5% | [ ] |
| 3085 | [Minimum Deletions to Make String K-Special](https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/) | Medium | 5/10 | 67.1% | [ ] |
| 1296 | [Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/) | Medium | 5/10 | 59.2% | [ ] |
| 846 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Medium | 5/10 | 57.9% | [ ] |
| 1775 | [Equal Sum Arrays With Minimum Number of Operations](https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/) | Medium | 5/10 | 54.5% | [ ] |
| 1541 | [Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/) | Medium | 5/10 | 53.5% | [ ] |
| 2131 | [Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/) | Medium | 5/10 | 53.5% | [ ] |
| 3119 | [Maximum Number of Potholes That Can Be Fixed](https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/) :lock: | Medium | 5/10 | 53.4% | [ ] |
| 1054 | [Distant Barcodes](https://leetcode.com/problems/distant-barcodes/) | Medium | 5/10 | 48.9% | [ ] |
| 3868 | [Minimum Cost to Equalize Arrays Using Swaps](https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/) | Medium | 5/10 | 48.5% | [ ] |
| 3002 | [Maximum Size of a Set After Removals](https://leetcode.com/problems/maximum-size-of-a-set-after-removals/) | Medium | 5/10 | 46.3% | [ ] |
| 1864 | [Minimum Number of Swaps to Make the Binary String Alternating](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/) | Medium | 5/10 | 43.9% | [ ] |
| 678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Medium | 5/10 | 40.1% | [ ] |
| 1733 | [Minimum Number of People to Teach](https://leetcode.com/problems/minimum-number-of-people-to-teach/) | Medium | 6/10 | 67.4% | [ ] |
| 659 | [Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/) | Medium | 6/10 | 52.1% | [ ] |
| 954 | [Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/) | Medium | 6/10 | 39.8% | [ ] |
| 2856 | [Minimum Array Length After Pair Removals](https://leetcode.com/problems/minimum-array-length-after-pair-removals/) | Medium | 6/10 | 27.4% | [ ] |
| 2350 | [Shortest Impossible Sequence of Rolls](https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/) | Hard | 7/10 | 69.1% | [ ] |
| 135 | [Candy](https://leetcode.com/problems/candy/) | Hard | 7/10 | 48.4% | [ ] |
| 2910 | [Minimum Number of Groups to Create a Valid Assignment](https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/) | Medium | 7/10 | 25.2% | [ ] |
| 2499 | [Minimum Total Cost to Make Arrays Unequal](https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/) | Hard | 8/10 | 41.3% | [ ] |

## task_assignment

**What it is** — Task assignment problems ask you to pair workers/machines/slots with tasks to optimise a global objective (minimise time, maximise value, or satisfy capacity constraints). The greedy insight is to sort both workers and tasks and match them in a specific order — biggest task to biggest worker, or smallest task to smallest worker — depending on whether you are maximising or minimising.

**Common steps**
1. Sort tasks by the relevant attribute (difficulty, duration, value).
2. Sort workers/resources by capacity (or derive their capacity).
3. Match tasks to workers using the appropriate greedy pairing strategy (largest-to-largest for maximisation, smallest-to-smallest for minimisation, or fill slots round-robin for keyboard-mapping style problems).
4. Track the running total (time used, profit earned, pushes needed) as you assign.
5. Return the accumulated result; check for impossible cases (task exceeds all worker capacities).

**Key variations**
- One-to-one matching (assign each task to exactly one worker).
- Many-to-one matching (fill workers up to capacity, e.g., keyboard key slots of size 8).
- Cooldown-constrained scheduling (Task Scheduler): use frequency of most common task to determine idle slots.
- Energy/threshold ordering: sort by `(actual - minimum)` difference to ensure sufficient starting energy.
- Parallel workers with identical machines (minimum completion time requires pairing max job with max worker).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1282 | [Group the People Given the Group Size They Belong To](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/) | Medium | 2/10 | 87.5% | [ ] |
| 1710 | [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/) | Easy | 2/10 | 74.8% | [ ] |
| 3014 | [Minimum Number of Pushes to Type Word I](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/) | Easy | 2/10 | 67.1% | [ ] |
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy | 2/10 | 54.9% | [ ] |
| 2335 | [Minimum Amount of Time to Fill Cups](https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/) | Easy | 3/10 | 60.2% | [ ] |
| 3016 | [Minimum Number of Pushes to Type Word II](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/) | Medium | 4/10 | 80.0% | [ ] |
| 2268 | [Minimum Number of Keypresses](https://leetcode.com/problems/minimum-number-of-keypresses/) :lock: | Medium | 4/10 | 71.4% | [ ] |
| 2895 | [Minimum Processing Time](https://leetcode.com/problems/minimum-processing-time/) | Medium | 4/10 | 70.3% | [ ] |
| 2323 | [Find Minimum Time to Finish All Jobs II](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/) :lock: | Medium | 4/10 | 66.1% | [ ] |
| 3476 | [Maximize Profit from Task Assignment](https://leetcode.com/problems/maximize-profit-from-task-assignment/) :lock: | Medium | 4/10 | 65.5% | [ ] |
| 3189 | [Minimum Moves to Get a Peaceful Board](https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/) :lock: | Medium | 5/10 | 75.8% | [ ] |
| 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | 5/10 | 63.0% | [x] |
| 3767 | [Maximize Points After Choosing K Tasks](https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/) | Medium | 5/10 | 60.0% | [ ] |
| 1057 | [Campus Bikes](https://leetcode.com/problems/campus-bikes/) :lock: | Medium | 5/10 | 59.1% | [ ] |
| 2365 | [Task Scheduler II](https://leetcode.com/problems/task-scheduler-ii/) | Medium | 5/10 | 54.8% | [ ] |
| 1953 | [Maximum Number of Weeks for Which You Can Work](https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/) | Medium | 6/10 | 42.5% | [ ] |
| 1665 | [Minimum Initial Energy to Finish Tasks](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/) | Hard | 7/10 | 60.9% | [ ] |
| 358 | [Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) :lock: | Hard | 7/10 | 40.0% | [ ] |
| 1199 | [Minimum Time to Build Blocks](https://leetcode.com/problems/minimum-time-to-build-blocks/) :lock: | Hard | 8/10 | 46.6% | [ ] |

## greedy_simulation

**What it is** — Greedy simulation problems require you to step through a process sequentially, making the locally optimal decision at each step rather than planning ahead. You recognise this pattern when each action permanently modifies a state (array values, a balance counter, a pointer position) and the best action at each position is self-evident given the current state — no backtracking is needed.

**Common steps**
1. Initialize any necessary state variables (running balance, pointer, current max, cost accumulator).
2. Iterate through the sequence one element at a time.
3. At each position, apply the greedy rule: perform the minimum forced operation, take the best available action, or skip if the constraint is already satisfied.
4. Update state variables to reflect the action taken.
5. After the full iteration, return the accumulated cost, count, or the modified structure.

**Key variations**
- Minimum increments to make a sequence strictly increasing (process left to right, bump each element above the previous).
- Flip-based problems: flip a window starting at each 0, track flips with a running XOR or difference array.
- Wiggle/zigzag arrangement: swap adjacent pairs whenever the pattern is violated.
- Simulating game rules (Dota Senate, Lemonade Change): use queues or counters to model each turn.
- Grid/matrix simulation: apply row or column operations in a fixed greedy order (highest bit first for Score After Flipping Matrix).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1827 | [Minimum Operations to Make the Array Increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/) | Easy | 1/10 | 82.0% | [ ] |
| 1974 | [Minimum Time to Type Word Using Special Typewriter](https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/) | Easy | 2/10 | 78.7% | [ ] |
| 3402 | [Minimum Operations to Make Columns Strictly Increasing](https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/) | Easy | 2/10 | 72.7% | [ ] |
| 2900 | [Longest Unequal Adjacent Groups Subsequence I](https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/) | Easy | 2/10 | 67.0% | [ ] |
| 3633 | [Earliest Finish Time for Land and Water Rides I](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/) | Easy | 2/10 | 62.1% | [ ] |
| 860 | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) | Easy | 2/10 | 59.1% | [ ] |
| 495 | [Teemo Attacking](https://leetcode.com/problems/teemo-attacking/) | Easy | 2/10 | 57.7% | [ ] |
| 807 | [Max Increase to Keep City Skyline](https://leetcode.com/problems/max-increase-to-keep-city-skyline/) | Medium | 3/10 | 86.4% | [ ] |
| 2383 | [Minimum Hours of Training to Win a Competition](https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/) | Easy | 3/10 | 42.6% | [ ] |
| 605 | [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) | Easy | 3/10 | 29.1% | [ ] |
| 1605 | [Find Valid Matrix Given Row and Column Sums](https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/) | Medium | 4/10 | 82.6% | [ ] |
| 861 | [Score After Flipping Matrix](https://leetcode.com/problems/score-after-flipping-matrix/) | Medium | 4/10 | 80.3% | [ ] |
| 1529 | [Minimum Suffix Flips](https://leetcode.com/problems/minimum-suffix-flips/) | Medium | 4/10 | 73.9% | [ ] |
| 1899 | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Medium | 4/10 | 69.0% | [ ] |
| 280 | [Wiggle Sort](https://leetcode.com/problems/wiggle-sort/) :lock: | Medium | 4/10 | 68.4% | [ ] |
| 1578 | [Minimum Time to Make Rope Colorful](https://leetcode.com/problems/minimum-time-to-make-rope-colorful/) | Medium | 4/10 | 65.2% | [ ] |
| 3810 | [Minimum Operations to Reach Target Array](https://leetcode.com/problems/minimum-operations-to-reach-target-array/) | Medium | 4/10 | 63.5% | [ ] |
| 2214 | [Minimum Health to Beat Game](https://leetcode.com/problems/minimum-health-to-beat-game/) :lock: | Medium | 4/10 | 58.8% | [ ] |
| 2957 | [Remove Adjacent Almost-Equal Characters](https://leetcode.com/problems/remove-adjacent-almost-equal-characters/) | Medium | 4/10 | 53.6% | [ ] |
| 376 | [Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/) | Medium | 4/10 | 49.4% | [ ] |
| 1253 | [Reconstruct a 2-Row Binary Matrix](https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/) | Medium | 4/10 | 48.9% | [ ] |
| 624 | [Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays/) | Medium | 4/10 | 45.6% | [ ] |
| 3191 | [Minimum Operations to Make Binary Array Elements Equal to One I](https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/) | Medium | 5/10 | 80.4% | [ ] |
| 769 | [Max Chunks To Make Sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/) | Medium | 5/10 | 64.1% | [ ] |
| 2498 | [Frog Jump II](https://leetcode.com/problems/frog-jump-ii/) | Medium | 5/10 | 62.2% | [ ] |
| 3796 | [Find Maximum Value in a Constrained Sequence](https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/) | Medium | 5/10 | 62.1% | [ ] |
| 2087 | [Minimum Cost Homecoming of a Robot in a Grid](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/) | Medium | 5/10 | 51.8% | [ ] |
| 2216 | [Minimum Deletions to Make Array Beautiful](https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/) | Medium | 5/10 | 49.9% | [ ] |
| 649 | [Dota2 Senate](https://leetcode.com/problems/dota2-senate/) | Medium | 5/10 | 49.8% | [ ] |
| 1144 | [Decrease Elements To Make Array Zigzag](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/) | Medium | 5/10 | 49.1% | [ ] |
| 2789 | [Largest Element in an Array after Merge Operations](https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/) | Medium | 5/10 | 47.9% | [ ] |
| 3587 | [Minimum Adjacent Swaps to Alternate Parity](https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/) | Medium | 5/10 | 42.4% | [ ] |
| 2892 | [Minimizing Array After Replacing Pairs With Their Product](https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/) :lock: | Medium | 5/10 | 40.7% | [ ] |
| 3724 | [Minimum Operations to Transform Array](https://leetcode.com/problems/minimum-operations-to-transform-array/) | Medium | 5/10 | 39.8% | [ ] |
| 334 | [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | Medium | 5/10 | 39.3% | [ ] |
| 665 | [Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/) | Medium | 5/10 | 25.4% | [ ] |
| 2599 | [Make the Prefix Sum Non-negative](https://leetcode.com/problems/make-the-prefix-sum-non-negative/) :lock: | Medium | 6/10 | 51.9% | [ ] |
| 2871 | [Split Array Into Maximum Number of Subarrays](https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/) | Medium | 6/10 | 42.5% | [ ] |
| 3776 | [Minimum Moves to Balance Circular Array](https://leetcode.com/problems/minimum-moves-to-balance-circular-array/) | Medium | 6/10 | 40.3% | [ ] |
| 3511 | [Make a Positive Array](https://leetcode.com/problems/make-a-positive-array/) :lock: | Medium | 6/10 | 35.7% | [ ] |
| 3781 | [Maximum Score After Binary Swaps](https://leetcode.com/problems/maximum-score-after-binary-swaps/) | Medium | 6/10 | 35.2% | [ ] |
| 2811 | [Check if it is Possible to Split Array](https://leetcode.com/problems/check-if-it-is-possible-to-split-array/) | Medium | 6/10 | 34.5% | [ ] |
| 3576 | [Transform Array to All Equal Elements](https://leetcode.com/problems/transform-array-to-all-equal-elements/) | Medium | 6/10 | 33.2% | [ ] |
| 2202 | [Maximize the Topmost Element After K Moves](https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/) | Medium | 6/10 | 24.1% | [ ] |
| 1488 | [Avoid Flood in The City](https://leetcode.com/problems/avoid-flood-in-the-city/) | Medium | 7/10 | 39.0% | [ ] |
| 3891 | [Minimum Increase to Maximize Special Indices](https://leetcode.com/problems/minimum-increase-to-maximize-special-indices/) | Medium | 7/10 | 19.5% | [ ] |
| 1703 | [Minimum Adjacent Swaps for K Consecutive Ones](https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/) | Hard | 8/10 | 42.2% | [ ] |
| 3785 | [Minimum Swaps to Avoid Forbidden Values](https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/) | Hard | 8/10 | 30.6% | [ ] |

## gas_station

**What it is** — The gas station pattern solves circular-tour problems where you must find a starting position that allows you to complete a full loop given local surplus/deficit at each stop. The key insight is that if the total gas is at least total cost then a valid starting point always exists, and you can identify it in a single pass by resetting your candidate start whenever your running tank goes negative.

**Common steps**
1. Compute the net gain at each station: `net[i] = gas[i] - cost[i]`.
2. Check feasibility: if `sum(net) < 0`, return -1 (no valid start exists).
3. Scan left to right, accumulating a running `tank` total and tracking `candidate_start`.
4. Whenever `tank < 0`, reset `tank = 0` and set `candidate_start = i + 1`.
5. Return `candidate_start` (the reset point is provably the only viable start).

**Key variations**
- Standard single-start circular tour (LC 134).
- Extensions requiring minimum cost or multiple vehicles follow the same feasibility check but add a secondary objective.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | Medium | 5/10 | 47.9% | [ ] |

## two_pointer_greedy

**What it is** — Two-pointer greedy problems place one pointer at each end (or at two strategic positions) of a sorted or structured sequence and decide at each step which pointer to move inward based on a greedy comparison. This avoids the O(n²) brute force and works because moving the suboptimal pointer can only hurt the objective, so the optimal pointer should stay fixed until the other catches up.

**Common steps**
1. Sort the input (if not already sorted) so the two extremes are well-defined.
2. Initialize `left = 0` and `right = n - 1`.
3. At each iteration, evaluate the current pair and record the contribution to the answer (max distance, minimum operations, boat count, etc.).
4. Apply the greedy rule to advance one pointer: move the pointer whose value is less promising (e.g., move `left` if `arr[left] + arr[right] <= limit`).
5. Repeat until the pointers meet; return the accumulated answer.

**Key variations**
- Pairing lightest with heaviest (Boats to Save People): fill each boat greedily.
- Matching two independent arrays (Advantage Shuffle in exchange_argument): sort both, use pointer on the opponent's sorted array.
- Shortest way to form a string: advance a pointer over the source for each character of the target.
- Bag of Tokens: spend the cheapest token for power, sell the most expensive for score.
- Finding the two extreme indices (min, max) and choosing the cheaper removal direction.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2078 | [Two Furthest Houses With Different Colors](https://leetcode.com/problems/two-furthest-houses-with-different-colors/) | Easy | 1/10 | 71.8% | [ ] |
| 942 | [DI String Match](https://leetcode.com/problems/di-string-match/) | Easy | 2/10 | 81.0% | [ ] |
| 881 | [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | Medium | 4/10 | 61.7% | [ ] |
| 2091 | [Removing Minimum and Maximum From Array](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/) | Medium | 4/10 | 56.4% | [ ] |
| 2340 | [Minimum Adjacent Swaps to Make a Valid Array](https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/) :lock: | Medium | 5/10 | 72.2% | [ ] |
| 1564 | [Put Boxes Into the Warehouse I](https://leetcode.com/problems/put-boxes-into-the-warehouse-i/) :lock: | Medium | 5/10 | 67.5% | [ ] |
| 2938 | [Separate Black and White Balls](https://leetcode.com/problems/separate-black-and-white-balls/) | Medium | 5/10 | 63.9% | [ ] |
| 1055 | [Shortest Way to Form String](https://leetcode.com/problems/shortest-way-to-form-string/) :lock: | Medium | 5/10 | 61.6% | [ ] |
| 948 | [Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/) | Medium | 5/10 | 59.6% | [ ] |
| 1580 | [Put Boxes Into the Warehouse II](https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/) :lock: | Medium | 6/10 | 65.9% | [ ] |
| 2868 | [The Wording Game](https://leetcode.com/problems/the-wording-game/) :lock: | Hard | 7/10 | 55.9% | [ ] |
| 1537 | [Get the Maximum Score](https://leetcode.com/problems/get-the-maximum-score/) | Hard | 7/10 | 41.1% | [ ] |
| 2332 | [The Latest Time to Catch a Bus](https://leetcode.com/problems/the-latest-time-to-catch-a-bus/) | Medium | 7/10 | 30.0% | [ ] |
| 3086 | [Minimum Moves to Pick K Ones](https://leetcode.com/problems/minimum-moves-to-pick-k-ones/) | Hard | 9/10 | 21.4% | [ ] |

## greedy_math

**What it is** — Greedy math problems have an answer that follows directly from a mathematical or number-theoretic observation, so the optimal strategy can be expressed as a formula or a short computation rather than a full search. Recognise this pattern when the problem involves divisibility, bit manipulation, sums, or GCDs and a closed-form rule provably yields the best outcome.

**Common steps**
1. Identify the mathematical structure (modular arithmetic, bit properties, Fibonacci representation, greedy coin-change style argument).
2. Derive or recall the greedy rule that follows from that structure (e.g., always subtract the largest valid value, or always flip bits greedily from the highest position).
3. Apply the rule in a loop or a single formula, updating the running state (remaining target, current number, remaining budget).
4. Handle edge cases: parity constraints, impossibility conditions, or the difference between floor and ceiling divisions.
5. Return the computed count, sum, or constructed value.

**Key variations**
- Greedy coin/denomination change (Fibonacci numbers, deci-binary decomposition): always take the largest valid piece.
- Bit manipulation greedy (max XOR, minimize OR): process bits from most significant to least significant.
- Array equalization with a single operation type (minimum operations to make array equal II): derive the formula from the sum difference.
- Integer replacement / broken calculator: work backwards from the target, applying inverse operations greedily.
- Patching array: maintain the furthest reachable number and greedily add the smallest missing value.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1689 | [Partitioning Into Minimum Number Of Deci-Binary Numbers](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/) | Medium | 1/10 | 90.5% | [ ] |
| 2656 | [Maximum Sum With Exactly K Elements ](https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/) | Easy | 1/10 | 80.6% | [ ] |
| 2224 | [Minimum Number of Operations to Convert Time](https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/) | Easy | 2/10 | 66.4% | [ ] |
| 1013 | [Partition Array Into Three Parts With Equal Sum](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/) | Easy | 2/10 | 42.7% | [ ] |
| 1785 | [Minimum Elements to Add to Form a Given Sum](https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/) | Medium | 3/10 | 45.1% | [ ] |
| 3849 | [Maximum Bitwise XOR After Rearrangement](https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/) | Medium | 4/10 | 71.2% | [ ] |
| 2436 | [Minimum Split Into Subarrays With GCD Greater Than One](https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/) :lock: | Medium | 4/10 | 70.3% | [ ] |
| 2358 | [Maximum Number of Groups Entering a Competition](https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/) | Medium | 4/10 | 68.6% | [ ] |
| 1753 | [Maximum Score From Removing Stones](https://leetcode.com/problems/maximum-score-from-removing-stones/) | Medium | 4/10 | 68.5% | [ ] |
| 1975 | [Maximum Matrix Sum](https://leetcode.com/problems/maximum-matrix-sum/) | Medium | 4/10 | 67.5% | [ ] |
| 2971 | [Find Polygon With the Largest Perimeter](https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/) | Medium | 4/10 | 65.5% | [ ] |
| 1247 | [Minimum Swaps to Make Strings Equal](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/) | Medium | 4/10 | 65.3% | [ ] |
| 1414 | [Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/) | Medium | 4/10 | 65.0% | [ ] |
| 3689 | [Maximum Total Subarray Value I](https://leetcode.com/problems/maximum-total-subarray-value-i/) | Medium | 4/10 | 64.4% | [ ] |
| 2829 | [Determine the Minimum Sum of a k-avoiding Array](https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/) | Medium | 4/10 | 60.8% | [ ] |
| 781 | [Rabbits in Forest](https://leetcode.com/problems/rabbits-in-forest/) | Medium | 4/10 | 58.1% | [ ] |
| 2139 | [Minimum Moves to Reach Target Score](https://leetcode.com/problems/minimum-moves-to-reach-target-score/) | Medium | 4/10 | 52.4% | [ ] |
| 2918 | [Minimum Equal Sum of Two Arrays After Replacing Zeros](https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/) | Medium | 4/10 | 50.2% | [ ] |
| 1936 | [Add Minimum Number of Rungs](https://leetcode.com/problems/add-minimum-number-of-rungs/) | Medium | 4/10 | 44.0% | [ ] |
| 2178 | [Maximum Split of Positive Even Integers](https://leetcode.com/problems/maximum-split-of-positive-even-integers/) | Medium | 5/10 | 59.7% | [ ] |
| 2952 | [Minimum Number of Coins to be Added](https://leetcode.com/problems/minimum-number-of-coins-to-be-added/) | Medium | 5/10 | 58.1% | [ ] |
| 991 | [Broken Calculator](https://leetcode.com/problems/broken-calculator/) | Medium | 5/10 | 56.1% | [ ] |
| 2601 | [Prime Subtraction Operation](https://leetcode.com/problems/prime-subtraction-operation/) | Medium | 5/10 | 55.6% | [ ] |
| 2745 | [Construct the Longest New String](https://leetcode.com/problems/construct-the-longest-new-string/) | Medium | 5/10 | 54.8% | [ ] |
| 3091 | [Apply Operations to Make Sum of Array Greater Than or Equal to k](https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/) | Medium | 5/10 | 44.3% | [ ] |
| 3800 | [Minimum Cost to Make Two Binary Strings Equal](https://leetcode.com/problems/minimum-cost-to-make-two-binary-strings-equal/) | Medium | 5/10 | 39.0% | [ ] |
| 397 | [Integer Replacement](https://leetcode.com/problems/integer-replacement/) | Medium | 5/10 | 37.5% | [ ] |
| 3789 | [Minimum Cost to Acquire Required Items](https://leetcode.com/problems/minimum-cost-to-acquire-required-items/) | Medium | 5/10 | 34.9% | [ ] |
| 2541 | [Minimum Operations to Make Array Equal II](https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/) | Medium | 5/10 | 33.1% | [ ] |
| 1058 | [Minimize Rounding Error to Meet Target](https://leetcode.com/problems/minimize-rounding-error-to-meet-target/) :lock: | Medium | 6/10 | 45.9% | [ ] |
| 910 | [Smallest Range II](https://leetcode.com/problems/smallest-range-ii/) | Medium | 6/10 | 37.9% | [ ] |
| 3588 | [Find Maximum Area of a Triangle](https://leetcode.com/problems/find-maximum-area-of-a-triangle/) | Medium | 6/10 | 29.4% | [ ] |
| 3326 | [Minimum Division Operations to Make Array Non Decreasing](https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/) | Medium | 6/10 | 29.2% | [ ] |
| 2195 | [Append K Integers With Minimal Sum](https://leetcode.com/problems/append-k-integers-with-minimal-sum/) | Medium | 6/10 | 27.0% | [ ] |
| 3858 | [Minimum Bitwise OR From Grid](https://leetcode.com/problems/minimum-bitwise-or-from-grid/) | Medium | 6/10 | 26.8% | [ ] |
| 2708 | [Maximum Strength of a Group](https://leetcode.com/problems/maximum-strength-of-a-group/) | Medium | 6/10 | 25.7% | [ ] |
| 3068 | [Find the Maximum Sum of Node Values](https://leetcode.com/problems/find-the-maximum-sum-of-node-values/) | Hard | 7/10 | 69.4% | [ ] |
| 3666 | [Minimum Operations to Equalize Binary String](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/) | Hard | 7/10 | 45.1% | [ ] |
| 1648 | [Sell Diminishing-Valued Colored Balls](https://leetcode.com/problems/sell-diminishing-valued-colored-balls/) | Medium | 7/10 | 30.2% | [ ] |
| 2939 | [Maximum Xor Product](https://leetcode.com/problems/maximum-xor-product/) | Medium | 7/10 | 29.8% | [ ] |
| 2967 | [Minimum Cost to Make Array Equalindromic](https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/) | Medium | 7/10 | 23.5% | [ ] |
| 1183 | [Maximum Number of Ones](https://leetcode.com/problems/maximum-number-of-ones/) :lock: | Hard | 8/10 | 70.6% | [ ] |
| 330 | [Patching Array](https://leetcode.com/problems/patching-array/) | Hard | 8/10 | 54.3% | [ ] |
| 2897 | [Apply Operations on Array to Maximize Sum of Squares](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/) | Hard | 8/10 | 44.6% | [ ] |
| 517 | [Super Washing Machines](https://leetcode.com/problems/super-washing-machines/) | Hard | 8/10 | 44.3% | [ ] |
| 1330 | [Reverse Subarray To Maximize Array Value](https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/) | Hard | 8/10 | 43.9% | [ ] |
| 3022 | [Minimize OR of Remaining Elements Using Operations](https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/) | Hard | 8/10 | 30.2% | [ ] |
| 2835 | [Minimum Operations to Form Subsequence With Target Sum](https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/) | Hard | 9/10 | 32.5% | [ ] |
| 3139 | [Minimum Cost to Equalize Array](https://leetcode.com/problems/minimum-cost-to-equalize-array/) | Hard | 9/10 | 18.8% | [ ] |

## jump_game

**What it is** — Jump game problems ask whether you can reach a target (or how few jumps it takes) when each position tells you how far you can jump from there. The greedy insight is to track the furthest position reachable so far: if you are still within that reach, you can always extend it; if the current position exceeds the reach, the target is unreachable. For minimum jumps, greedily use the jump that extends your reach the most before you are forced to jump.

**Common steps**
1. Initialize `max_reach = 0` (furthest position reachable), `jumps = 0`, `current_end = 0` (end of current jump level).
2. Iterate through positions `0` to `n-2`.
3. Update `max_reach = max(max_reach, i + nums[i])` at each position.
4. When `i == current_end`, you must jump: increment `jumps`, set `current_end = max_reach`.
5. If at any point `max_reach < i`, the target is unreachable; otherwise return `jumps` (or `True` for reachability).

**Key variations**
- Reachability only (LC 55): return `max_reach >= n - 1` after a single pass.
- Minimum jumps (LC 45): count jumps whenever the current level boundary is crossed.
- Interval covering (Video Stitching, Minimum Taps): sort intervals by start, then greedily extend coverage with the interval that reaches furthest.
- Refueling stops (LC 871): use a max-heap to retroactively pick the largest refuel seen so far whenever you run out of fuel.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2027 | [Minimum Moves to Convert String](https://leetcode.com/problems/minimum-moves-to-convert-string/) | Easy | 2/10 | 57.9% | [ ] |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | 4/10 | 40.8% | [ ] |
| 1024 | [Video Stitching](https://leetcode.com/problems/video-stitching/) | Medium | 5/10 | 52.7% | [ ] |
| 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | 5/10 | 42.8% | [ ] |
| 3282 | [Reach End of Array With Max Score](https://leetcode.com/problems/reach-end-of-array-with-max-score/) | Medium | 6/10 | 33.6% | [ ] |
| 1326 | [Minimum Number of Taps to Open to Water a Garden](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) | Hard | 7/10 | 51.0% | [ ] |
| 871 | [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | Hard | 8/10 | 41.4% | [ ] |

## activity_selection

**What it is** — Activity selection (also called interval scheduling) is the classic greedy problem of choosing the maximum number of non-overlapping activities (or the minimum number of "arrows" to cover all of them). The fundamental insight is to always select the activity that ends earliest, because it leaves the most room for future activities — this is a provably optimal exchange argument.

**Common steps**
1. Sort intervals by their end time (ascending).
2. Initialize `last_end = -infinity` and `count = 0`.
3. Iterate through the sorted intervals: if `interval.start >= last_end`, select this interval, update `last_end = interval.end`, and increment `count`.
4. Skip any interval that overlaps with the last selected one.
5. Return `count` (for maximum selections) or `n - count` (for minimum removals to make non-overlapping).

**Key variations**
- Maximum non-overlapping intervals (LC 435, 646): sort by end, count greedily selected intervals.
- Minimum arrows to burst balloons (LC 452): every new arrow is needed only when the current balloon starts after the last arrow position.
- Attend maximum events (LC 1353): use a min-heap of end times to always attend the earliest-ending available event each day.
- Earliest full bloom (LC 2136): sort by bloom time descending; greedily plant longest-blooming flowers first to minimise total wait.
- Course Schedule III (LC 630): use a max-heap to greedily swap out the longest course taken when the deadline is exceeded.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 646 | [Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) | Medium | 4/10 | 61.7% | [ ] |
| 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | 4/10 | 61.4% | [ ] |
| 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | 4/10 | 57.1% | [x] |
| 1921 | [Eliminate Maximum Number of Monsters](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/) | Medium | 5/10 | 51.1% | [ ] |
| 1353 | [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) | Medium | 6/10 | 39.0% | [ ] |
| 2136 | [Earliest Possible Day of Full Bloom](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/) | Hard | 7/10 | 71.2% | [ ] |
| 630 | [Course Schedule III](https://leetcode.com/problems/course-schedule-iii/) | Hard | 7/10 | 41.6% | [ ] |

## greedy_string

**What it is** — Greedy string problems ask you to construct, modify, or partition a string to achieve a lexicographic or structural objective with the fewest operations. The greedy insight is to process characters left to right and make the locally best character-level decision at each position, exploiting the fact that earlier positions dominate lexicographic order or structural validity.

**Common steps**
1. Determine the objective: minimise lexicographic order, maximise it, or satisfy a structural constraint (no three consecutive same characters, valid parentheses, etc.).
2. Iterate over the string from left to right (or right to left for suffix-based problems).
3. At each position, apply the greedy rule: choose the smallest (or largest) valid character, skip/merge if a constraint would be violated, or count the operation forced by the current character.
4. Track any necessary state (remaining budget, last character used, frequency counts, open parenthesis balance).
5. Build the result character by character or return the accumulated operation count.

**Key variations**
- Lexicographically smallest/largest construction with a constraint (no palindrome substrings, no triple repeats).
- Minimum deletions or operations to satisfy a pattern (alternating, anti-palindrome, sorted columns).
- Partition into minimum substrings satisfying a value or uniqueness constraint.
- Break/modify exactly one substring or character to achieve a lexicographic goal.
- Two-string merge choosing the lexicographically larger character at each step (LC 1754).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1903 | [Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string/) | Easy | 1/10 | 67.3% | [ ] |
| 3216 | [Lexicographically Smallest String After a Swap](https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/) | Easy | 2/10 | 54.6% | [ ] |
| 2405 | [Optimal Partition of String](https://leetcode.com/problems/optimal-partition-of-string/) | Medium | 4/10 | 78.4% | [ ] |
| 3106 | [Lexicographically Smallest String After Operations With Constraint](https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/) | Medium | 4/10 | 62.8% | [ ] |
| 3675 | [Minimum Operations to Transform String](https://leetcode.com/problems/minimum-operations-to-transform-string/) | Medium | 4/10 | 61.9% | [ ] |
| 1328 | [Break a Palindrome](https://leetcode.com/problems/break-a-palindrome/) | Medium | 4/10 | 51.6% | [ ] |
| 2645 | [Minimum Additions to Make Valid String](https://leetcode.com/problems/minimum-additions-to-make-valid-string/) | Medium | 4/10 | 51.0% | [ ] |
| 2522 | [Partition String Into Substrings With Values at Most K](https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/) | Medium | 4/10 | 47.7% | [ ] |
| 1405 | [Longest Happy String](https://leetcode.com/problems/longest-happy-string/) | Medium | 5/10 | 65.5% | [ ] |
| 2712 | [Minimum Cost to Make All Characters Equal](https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/) | Medium | 5/10 | 54.3% | [ ] |
| 1754 | [Largest Merge Of Two Strings](https://leetcode.com/problems/largest-merge-of-two-strings/) | Medium | 5/10 | 53.9% | [ ] |
| 2311 | [Longest Binary Subsequence Less Than or Equal to K](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/) | Medium | 5/10 | 52.8% | [ ] |
| 3035 | [Maximum Palindromes After Operations](https://leetcode.com/problems/maximum-palindromes-after-operations/) | Medium | 5/10 | 46.4% | [ ] |
| 984 | [String Without AAA or BBB](https://leetcode.com/problems/string-without-aaa-or-bbb/) | Medium | 5/10 | 45.2% | [ ] |
| 2734 | [Lexicographically Smallest String After Substring Operation](https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/) | Medium | 5/10 | 34.9% | [ ] |
| 955 | [Delete Columns to Make Sorted II](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/) | Medium | 6/10 | 49.7% | [ ] |
| 1702 | [Maximum Binary String After Change](https://leetcode.com/problems/maximum-binary-string-after-change/) | Medium | 6/10 | 47.6% | [ ] |
| 2116 | [Check if a Parentheses String Can Be Valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/) | Medium | 6/10 | 45.1% | [ ] |
| 555 | [Split Concatenated Strings](https://leetcode.com/problems/split-concatenated-strings/) :lock: | Medium | 6/10 | 43.6% | [ ] |
| 3081 | [Replace Question Marks in String to Minimize Its Value](https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/) | Medium | 6/10 | 29.2% | [ ] |
| 3088 | [Make String Anti-palindrome](https://leetcode.com/problems/make-string-anti-palindrome/) :lock: | Hard | 7/10 | 46.1% | [ ] |
| 1585 | [Check If String Is Transformable With Substring Sort Operations](https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/) | Hard | 8/10 | 51.6% | [ ] |
| 2472 | [Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/) | Hard | 8/10 | 44.6% | [ ] |
| 2663 | [Lexicographically Smallest Beautiful String](https://leetcode.com/problems/lexicographically-smallest-beautiful-string/) | Hard | 8/10 | 38.1% | [ ] |
| 321 | [Create Maximum Number](https://leetcode.com/problems/create-maximum-number/) | Hard | 9/10 | 35.3% | [ ] |
| 420 | [Strong Password Checker](https://leetcode.com/problems/strong-password-checker/) | Hard | 10/10 | 15.7% | [ ] |

## interval_scheduling

**What it is** — Interval scheduling problems deal with a set of intervals and ask you to merge them, count overlaps, partition them into groups, or cover points optimally. The unifying greedy strategy is to sort by one endpoint (start or end) and then sweep through, maintaining just enough state (current merged interval, active count, last covered point) to make each decision in O(1).

**Common steps**
1. Sort intervals by start time (or end time, depending on the sub-problem).
2. Initialize result structure (merged list, group count, point counter).
3. Sweep through sorted intervals one by one.
4. At each interval, decide: merge with the previous (if overlapping), open a new group (if no available group), or record a new covered segment.
5. Update state (extend the current interval's end, increment/decrement active count) and add to the result when a segment closes.

**Key variations**
- Merge overlapping intervals (LC 56): sort by start, extend end greedily.
- Count simultaneous meetings / minimum rooms (LC 253, 2406): use a min-heap of end times or a sweep-line event counter.
- Insert a new interval into a sorted list (LC 57): binary search for position, then merge.
- Maximum non-overlapping subarrays with a given property (LC 1546): combine prefix-sum with a greedy "take as early as possible" scan.
- Non-overlapping substrings or intervals with complex containment rules (LC 1520, 3557): sort by end, greedily extend coverage without backtracking.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 252 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) :lock: | Easy | 2/10 | 59.4% | [ ] |
| 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | 4/10 | 81.9% | [ ] |
| 2294 | [Partition Array Such That Maximum Difference Is K](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/) | Medium | 4/10 | 81.8% | [ ] |
| 3111 | [Minimum Rectangles to Cover Points](https://leetcode.com/problems/minimum-rectangles-to-cover-points/) | Medium | 4/10 | 63.8% | [ ] |
| 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | 4/10 | 51.7% | [x] |
| 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) :lock: | Medium | 5/10 | 52.7% | [ ] |
| 2086 | [Minimum Number of Food Buckets to Feed the Hamsters](https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/) | Medium | 5/10 | 48.3% | [ ] |
| 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | 5/10 | 45.1% | [x] |
| 759 | [Employee Free Time](https://leetcode.com/problems/employee-free-time/) :lock: | Hard | 6/10 | 72.9% | [ ] |
| 2406 | [Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) | Medium | 6/10 | 63.6% | [ ] |
| 3440 | [Reschedule Meetings for Maximum Free Time II](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/) | Medium | 6/10 | 60.4% | [ ] |
| 1546 | [Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/) | Medium | 6/10 | 48.9% | [ ] |
| 3557 | [Find Maximum Number of Non Intersecting Substrings](https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/) | Medium | 6/10 | 30.7% | [ ] |
| 3362 | [Zero Array Transformation III](https://leetcode.com/problems/zero-array-transformation-iii/) | Medium | 7/10 | 54.8% | [ ] |
| 3458 | [Select K Disjoint Special Substrings](https://leetcode.com/problems/select-k-disjoint-special-substrings/) | Medium | 7/10 | 19.3% | [ ] |
| 757 | [Set Intersection Size At Least Two](https://leetcode.com/problems/set-intersection-size-at-least-two/) | Hard | 8/10 | 58.0% | [ ] |
| 1520 | [Maximum Number of Non-Overlapping Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) | Hard | 8/10 | 42.1% | [ ] |
| 2589 | [Minimum Time to Complete All Tasks](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/) | Hard | 8/10 | 40.4% | [ ] |
| 3244 | [Shortest Distance After Road Addition Queries II](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/) | Hard | 8/10 | 26.7% | [ ] |

## exchange_argument

**What it is** — Exchange argument problems require you to find the optimal ordering or assignment of elements by proving that swapping any two adjacent out-of-order elements improves (or does not worsen) the objective. Once you identify the pairwise comparison that defines "better order," sorting by that comparator gives the global optimum. This is the rigorous justification behind many greedy sorting strategies.

**Common steps**
1. Hypothesize a comparator: define when element A should come before element B.
2. Prove the exchange argument: show that swapping A and B when B precedes A improves the objective (e.g., reduces cost, increases profit).
3. Sort the elements using that comparator.
4. Apply any secondary greedy step needed after sorting (e.g., binary search for matching, take top-k, or accumulate a running value).
5. Return the optimised total.

**Key variations**
- Minimise product sum: sort one array ascending, the other descending, then pair them.
- Two-city scheduling: sort by `cost_A - cost_B` and send the first half to city A.
- Advantage shuffle: sort both arrays; for each opponent value, assign the smallest value that can beat it (binary search on your sorted array).
- Weighted scheduling with deadlines: sort by deadline or by a ratio like `damage / time` to minimise total damage taken.
- Multi-item knapsack with exchange: greedily swap out included items to improve a secondary metric (Maximum Elegance LC 2813).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1874 | [Minimize Product Sum of Two Arrays](https://leetcode.com/problems/minimize-product-sum-of-two-arrays/) :lock: | Medium | 3/10 | 89.9% | [ ] |
| 1029 | [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/) | Medium | 4/10 | 68.5% | [ ] |
| 2548 | [Maximum Price to Fill a Bag](https://leetcode.com/problems/maximum-price-to-fill-a-bag/) :lock: | Medium | 4/10 | 64.6% | [ ] |
| 1686 | [Stone Game VI](https://leetcode.com/problems/stone-game-vi/) | Medium | 5/10 | 60.6% | [ ] |
| 3218 | [Minimum Cost for Cutting Cake I](https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/) | Medium | 5/10 | 58.5% | [ ] |
| 870 | [Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/) | Medium | 5/10 | 54.5% | [ ] |
| 2611 | [Mice and Cheese](https://leetcode.com/problems/mice-and-cheese/) | Medium | 6/10 | 48.7% | [ ] |
| 2551 | [Put Marbles in Bags](https://leetcode.com/problems/put-marbles-in-bags/) | Hard | 7/10 | 72.1% | [ ] |
| 3219 | [Minimum Cost for Cutting Cake II](https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/) | Hard | 7/10 | 55.2% | [ ] |
| 3273 | [Minimum Amount of Damage Dealt to Bob](https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/) | Hard | 7/10 | 39.7% | [ ] |
| 2449 | [Minimum Number of Operations to Make Arrays Similar](https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/) | Hard | 8/10 | 61.4% | [ ] |
| 2366 | [Minimum Replacements to Sort the Array](https://leetcode.com/problems/minimum-replacements-to-sort-the-array/) | Hard | 8/10 | 53.1% | [ ] |
| 2412 | [Minimum Money Required Before Transactions](https://leetcode.com/problems/minimum-money-required-before-transactions/) | Hard | 8/10 | 42.0% | [ ] |
| 3547 | [Maximum Sum of Edge Values in a Graph](https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/) | Hard | 8/10 | 36.4% | [ ] |
| 2813 | [Maximum Elegance of a K-Length Subsequence](https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/) | Hard | 8/10 | 28.7% | [ ] |
