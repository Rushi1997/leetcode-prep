# SlidingWindow

98 problems across 20 patterns.

## fixed_window_sum_or_average

**What it is** — You maintain a contiguous subarray of exactly size K as it slides across the array, updating a running sum by adding the new element on the right and dropping the element that just left on the left. Recognize this pattern when a problem asks for a max, min, average, or count over all subarrays of a fixed length K.

**Common steps**
1. Compute the sum (or value) of the first K elements as the initial window.
2. Record the result for this first window (e.g., set it as the current max/min).
3. Loop from index K to the end of the array. At each step, add `arr[i]` to the window sum and subtract `arr[i - K]`.
4. Update your answer (e.g., compare new sum to running max).
5. Return the final answer after the loop ends.

**Key variations**
- Some problems want a count of windows satisfying a threshold (not just the best window).
- Some problems involve a circular array — treat the array as doubled or use modular indexing.
- Some problems add a "base" value that is always present outside the window (e.g., Grumpy Bookstore Owner), so you compute net gain of the window and add it to the base.
- Some problems flip the framing: instead of a window of size K, you pick K elements from the ends of the array, which is equivalent to finding the best window of size `n - K` in the middle.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2269 | [Find the K-Beauty of a Number](https://leetcode.com/problems/find-the-k-beauty-of-a-number/) | Easy | 1/10 | 63.3% | [ ] |
| 643 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | 1/10 | 47.7% | [x] |
| 1652 | [Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb/) | Easy | 2/10 | 79.3% | [ ] |
| 1343 | [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | Medium | 2/10 | 72.8% | [ ] |
| 2379 | [Minimum Recolors to Get K Consecutive Black Blocks](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) | Easy | 2/10 | 68.7% | [ ] |
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Medium | 2/10 | 61.9% | [ ] |
| 1176 | [Diet Plan Performance](https://leetcode.com/problems/diet-plan-performance/) :lock: | Easy | 2/10 | 56.0% | [ ] |
| 1151 | [Minimum Swaps to Group All 1's Together](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/) :lock: | Medium | 3/10 | 61.2% | [ ] |
| 2090 | [K Radius Subarray Averages](https://leetcode.com/problems/k-radius-subarray-averages/) | Medium | 3/10 | 46.2% | [ ] |
| 2134 | [Minimum Swaps to Group All 1's Together II](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/) | Medium | 4/10 | 65.6% | [ ] |
| 1052 | [Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/) | Medium | 4/10 | 64.0% | [ ] |
| 1423 | [Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | Medium | 4/10 | 57.6% | [ ] |
| 3439 | [Reschedule Meetings for Maximum Free Time I](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/) | Medium | 4/10 | 54.0% | [ ] |

## fixed_window_hashing

**What it is** — You slide a fixed-size window across an array or string and use a hash map (or hash set) to track element frequencies or membership within the current window. Recognize this pattern when the problem asks whether a fixed-size subarray has some property about duplicates, distinct values, or element counts.

**Common steps**
1. Initialize a hash map to store the frequency of each element in the first K elements.
2. Evaluate the property on the initial window and record the result.
3. Slide the window one step at a time: add `arr[i]` to the map, then remove `arr[i - K]` (decrement its count and delete the key if it reaches zero).
4. Re-evaluate the property on the updated map and update the answer.
5. Return the answer after processing all windows.

**Key variations**
- Some problems check for any duplicate within the window (use a set instead of a count map).
- Some problems require all K-length substrings to be collected into a set (e.g., checking if all binary codes of length K are present).
- Some problems compute a score based on the top-X most frequent elements in the window.
- Time-based problems group events by person and treat a one-hour sliding window over timestamps.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 219 | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Easy | 2/10 | 51.2% | [ ] |
| 3318 | [Find X-Sum of All K-Long Subarrays I](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/) | Easy | 3/10 | 76.1% | [ ] |
| 1461 | [Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) | Medium | 4/10 | 61.6% | [ ] |
| 1297 | [Maximum Number of Occurrences of a Substring](https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/) | Medium | 4/10 | 54.4% | [ ] |
| 187 | [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) | Medium | 4/10 | 53.3% | [ ] |
| 2461 | [Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) | Medium | 4/10 | 43.0% | [ ] |
| 1604 | [Alert Using Same Key-Card Three or More Times in a One Hour Period](https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/) | Medium | 5/10 | 46.2% | [ ] |

## variable_window_unique_elements

**What it is** — You expand and shrink a window dynamically to maintain the constraint that all elements inside the window are unique (no duplicates). Recognize this pattern when a problem asks for the longest subarray or substring where every element appears exactly once.

**Common steps**
1. Initialize a left pointer `l = 0`, a hash set (or frequency map), and a variable to track the best answer so far.
2. Iterate with a right pointer `r` over each element.
3. While the element at `r` already exists in the set, remove the element at `l` from the set and advance `l`.
4. Add the element at `r` to the set.
5. Update the answer using the current window size `r - l + 1` (or the current window's sum, etc.).
6. Return the best answer after `r` has visited every element.

**Key variations**
- Some problems maximize a sum rather than a length (track running sum alongside the set).
- Some problems minimize a window length (e.g., find the shortest window before a duplicate repeats).
- The uniqueness check can be on values (Longest Substring Without Repeating Characters) or on indices (Contains Duplicate II is a related idea).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2743 | [Count Substrings Without Repeating Character](https://leetcode.com/problems/count-substrings-without-repeating-character/) :lock: | Medium | 3/10 | 75.9% | [ ] |
| 1695 | [Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/) | Medium | 4/10 | 64.3% | [ ] |
| 2260 | [Minimum Consecutive Cards to Pick Up](https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/) | Medium | 4/10 | 53.7% | [ ] |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | 4/10 | 39.0% | [x] |

## fixed_window_character_frequency

**What it is** — You use a fixed-size window and compare character frequency counts between the window and a target pattern, often checking if they are equal (i.e., the window is an anagram or permutation of the target). Recognize this pattern when a problem asks if any fixed-length substring matches or contains a rearrangement of a given pattern.

**Common steps**
1. Build a frequency count map for the target pattern.
2. Build a frequency count map for the first K characters of the string (the initial window).
3. Compare the two maps; if they match, record a result.
4. Slide the window: add the new right character to the window map; remove the outgoing left character (delete key if count drops to zero).
5. Compare the maps again after each slide and record matching positions.
6. Return all recorded results.

**Key variations**
- Some problems just need a boolean (does a permutation exist?), others need all starting indices of anagrams.
- Some problems use a "match counter" instead of comparing entire maps — track how many distinct characters are currently satisfied to avoid O(26) comparison per step.
- Harder variants involve matching a list of words (each of fixed length) in any order, requiring a map-of-maps approach.
- Some problems count windows where every character appears exactly the same number of times.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1876 | [Substrings of Size Three with Distinct Characters](https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/) | Easy | 1/10 | 76.7% | [ ] |
| 1852 | [Distinct Numbers in Each Subarray](https://leetcode.com/problems/distinct-numbers-in-each-subarray/) :lock: | Medium | 3/10 | 77.3% | [ ] |
| 1100 | [Find K-Length Substrings With No Repeated Characters](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/) :lock: | Medium | 3/10 | 76.5% | [ ] |
| 2107 | [Number of Unique Flavors After Sharing K Candies](https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/) :lock: | Medium | 3/10 | 60.5% | [ ] |
| 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | 3/10 | 48.8% | [x] |
| 438 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | 4/10 | 53.7% | [ ] |
| 2067 | [Number of Equal Count Substrings](https://leetcode.com/problems/number-of-equal-count-substrings/) :lock: | Medium | 5/10 | 45.5% | [ ] |
| 30 | [Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) | Hard | 8/10 | 34.4% | [ ] |

## variable_window_bitwise_constraint

**What it is** — You use a variable-size window where the validity constraint is defined by a bitwise operation (AND, OR, XOR) on the elements in the window. Recognize this pattern when a problem restricts subarrays based on whether bitwise OR/AND reaches a threshold, or whether no two elements share a set bit.

**Common steps**
1. Initialize left pointer `l = 0` and a variable to track the current bitwise accumulation (e.g., running OR or a bitmask of used bits).
2. Expand right pointer `r` and update the bitwise accumulation by including `arr[r]`.
3. While the window violates the constraint (e.g., OR exceeds K, or two elements share a bit), shrink from the left: undo `arr[l]`'s contribution and advance `l`.
4. Once the window is valid, update the answer (window length, count, etc.).
5. Repeat until `r` reaches the end.

**Key variations**
- OR-based problems: window is valid when the running OR is at least K (find shortest) or track how the OR grows bit by bit.
- AND-based problems: unlike OR, AND can only decrease as the window grows; shrinking requires recomputing from scratch or tracking bit counts per position.
- XOR / no-shared-bits problems: maintain a bitmask of all bits currently used in the window; a new element is valid only if it shares no set bits with the current mask.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3095 | [Shortest Subarray With OR at Least K I](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/) | Easy | 2/10 | 44.5% | [ ] |
| 2401 | [Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray/) | Medium | 5/10 | 64.8% | [ ] |
| 3097 | [Shortest Subarray With OR at Least K II](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/) | Medium | 5/10 | 50.2% | [ ] |

## variable_window_at_most_k_distinct

**What it is** — You expand and shrink a window to maintain at most K distinct elements (or character types) inside it at all times. Recognize this pattern when a problem asks for the longest subarray or count of subarrays with no more than K unique values.

**Common steps**
1. Initialize left pointer `l = 0`, a frequency map, and a `distinct` counter.
2. Expand `r`: add `arr[r]` to the map; if it was not in the map before, increment `distinct`.
3. While `distinct > K`, shrink from the left: decrement `arr[l]`'s count; if its count hits zero, delete it and decrement `distinct`; advance `l`.
4. The window `[l, r]` now has at most K distinct elements. Update the answer (window size, or add `r - l + 1` to a count of valid subarrays).
5. Continue until `r` reaches the end.

**Key variations**
- Some problems fix K = 2 (two baskets, two characters), making the logic identical but the constant specific.
- Some problems count subarrays rather than find the longest window — add `r - l + 1` each step.
- Some problems require all K distinct elements to be present (at least K), which inverts the shrink condition.
- The "balance" variant tracks ratios (e.g., equal even/odd counts) instead of raw distinct counts.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3719 | [Longest Balanced Subarray I](https://leetcode.com/problems/longest-balanced-subarray-i/) | Medium | 4/10 | 65.6% | [ ] |
| 159 | [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) :lock: | Medium | 4/10 | 57.1% | [ ] |
| 904 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | 4/10 | 51.0% | [ ] |
| 340 | [Longest Substring with At Most K Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/) :lock: | Medium | 4/10 | 50.0% | [ ] |
| 1358 | [Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) | Medium | 5/10 | 73.7% | [ ] |

## variable_window_replacement_budget

**What it is** — You maintain a window where you are allowed to "change" or "replace" up to K elements to make the entire window satisfy some uniformity condition, and you want the longest such window. Recognize this pattern when a problem says you can flip, replace, or spend budget on at most K elements and asks for the maximum length of a valid subarray.

**Common steps**
1. Initialize left pointer `l = 0`, a frequency map (or count of the dominant element), and track the size of the window `r - l + 1`.
2. Expand `r`: update the frequency map with `arr[r]`. Track `max_freq` = the count of the most common element in the current window.
3. Calculate replacements needed = `(window size) - max_freq`. If this exceeds K, the window is too large.
4. Shrink from the left by one step: remove `arr[l]` from the map and advance `l`.
5. The window size never shrinks below the best answer seen so far (a classic optimization), so just keep sliding without re-shrinking repeatedly.
6. Return `r - l + 1` at the end as the maximum valid window length.

**Key variations**
- Binary array problems simplify to: count of zeros (or ones) in the window must be <= K.
- Some problems sort the window first (frequency-based problems), then use the budget to "top up" less frequent elements to match the most frequent.
- Some problems generalize to any single character (not just 0/1), requiring a per-character frequency map.
- Harder variants require the budget to be spent on increasing element values rather than replacing them (e.g., operations to equalize values within cost K).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 487 | [Max Consecutive Ones II](https://leetcode.com/problems/max-consecutive-ones-ii/) :lock: | Medium | 3/10 | 52.0% | [ ] |
| 1493 | [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | Medium | 4/10 | 71.2% | [ ] |
| 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | 4/10 | 67.6% | [ ] |
| 2024 | [Maximize the Confusion of an Exam](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/) | Medium | 5/10 | 69.9% | [ ] |
| 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | 5/10 | 59.5% | [ ] |
| 1838 | [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) | Medium | 5/10 | 44.8% | [ ] |
| 2831 | [Find the Longest Equal Subarray](https://leetcode.com/problems/find-the-longest-equal-subarray/) | Medium | 5/10 | 38.0% | [ ] |
| 2968 | [Apply Operations to Maximize Frequency Score](https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/) | Hard | 8/10 | 38.9% | [ ] |

## variable_window_product_constraint

**What it is** — You maintain a window where the product of all elements stays below a given threshold K, shrinking the window from the left whenever the product meets or exceeds K. Recognize this pattern when a problem asks you to count or find subarrays whose product (not sum) satisfies a bound.

**Common steps**
1. Initialize left pointer `l = 0`, `product = 1`, and `count = 0`.
2. Expand `r`: multiply `product` by `arr[r]`.
3. While `product >= K`, divide `product` by `arr[l]` and advance `l`.
4. The number of valid subarrays ending at `r` is `r - l + 1` (every subarray from any start in `[l, r]` to `r` is valid); add this to `count`.
5. Return `count`.

**Key variations**
- This pattern has only one primary variant (product < K); the trick is realizing that adding `r - l + 1` per step correctly counts all valid subarrays without double-counting.
- Watch for edge cases: if any single element is >= K, the window collapses to size zero and contributes zero subarrays.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 713 | [Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | Medium | 5/10 | 54.3% | [ ] |

## variable_window_pair_counting

**What it is** — You use a variable window combined with a frequency map to count the number of valid pairs (or tuples) within the current window that satisfy a given condition, updating the count incrementally as the window expands and contracts. Recognize this pattern when a problem asks you to count subarrays where the number of matching pairs inside meets a threshold.

**Common steps**
1. Initialize left pointer `l = 0`, a frequency map, a running `pairs` count, and a result counter.
2. Expand `r`: before inserting `arr[r]`, note how many existing elements in the window match it — that many new pairs are formed. Add this to `pairs`, then increment `arr[r]`'s frequency.
3. While `pairs` exceeds the allowed limit, shrink from the left: decrement the frequency of `arr[l]`, subtract the number of pairs that `arr[l]` now loses (its new count), and advance `l`.
4. The current window `[l, r]` now has exactly the allowed number of pairs or fewer. Add `r - l + 1` to the result (all subarrays ending at `r` with any left boundary in `[l, r]` are valid).
5. Return the result.

**Key variations**
- The threshold on pairs can be "at most K pairs" or "at least K pairs" (the latter uses the at-most-K trick: `atMost(K) - atMost(K-1)`).
- The pairing condition can vary: same value, values within a difference of D, etc.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2537 | [Count the Number of Good Subarrays](https://leetcode.com/problems/count-the-number-of-good-subarrays/) | Medium | 5/10 | 65.9% | [ ] |

## variable_window_condition_tracking

**What it is** — You maintain a window where validity depends on a custom sequential or structural condition (not just a simple count or sum), such as alternating signs, a specific repeating pattern, or bounded consecutive occurrences. Recognize this pattern when the window validity rule is stateful and requires tracking the relationship between adjacent elements rather than an aggregate metric.

**Common steps**
1. Initialize left pointer `l = 0` and any state variables the condition needs (e.g., count of pattern violations, last seen value, streak length).
2. Expand `r`: update the state variables to reflect including `arr[r]`.
3. While the window violates the condition, update state to remove `arr[l]`'s contribution and advance `l`.
4. The window `[l, r]` is now valid. Update the answer (max length, count of valid windows, etc.).
5. Return the answer.

**Key variations**
- Turbulent subarrays: the condition alternates between `>` and `<` between adjacent pairs; violations are detected immediately at each step.
- Semi-repetitive strings: at most one consecutive duplicate pair is allowed; shrink when a second pair appears.
- Vowels in order: all vowels must appear in non-decreasing alphabetical order and the window must contain all five.
- Fixed-bound subarrays: track the last position where a value was out of range, and compute valid counts using three pointer positions.
- Circular/rotation variants: double the array and apply a fixed-size window that tracks flips needed.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2760 | [Longest Even Odd Subarray With Threshold](https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/) | Easy | 3/10 | 32.1% | [ ] |
| 2730 | [Find the Longest Semi-Repetitive Substring](https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/) | Medium | 4/10 | 38.9% | [ ] |
| 1839 | [Longest Substring Of All Vowels in Order](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/) | Medium | 5/10 | 51.8% | [ ] |
| 978 | [Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/) | Medium | 5/10 | 49.1% | [ ] |
| 1888 | [Minimum Number of Flips to Make the Binary String Alternating](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/) | Medium | 6/10 | 53.5% | [ ] |
| 1156 | [Swap For Longest Repeated Character Substring](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/) | Medium | 6/10 | 44.5% | [ ] |
| 2444 | [Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/) | Hard | 7/10 | 69.2% | [ ] |

## variable_window_sum_constraint

**What it is** — You expand and shrink a window based on whether its sum satisfies a given constraint (e.g., sum >= target, sum <= budget, or sum equals a value). Recognize this pattern when a problem asks for the shortest, longest, or count of subarrays with a sum that meets a numeric bound.

**Common steps**
1. Initialize left pointer `l = 0`, `window_sum = 0`, and the answer variable (e.g., `min_len = infinity` or `count = 0`).
2. Expand `r`: add `arr[r]` to `window_sum`.
3. While the window satisfies the constraint (e.g., `window_sum >= target`), update the answer, then shrink from the left by subtracting `arr[l]` and advancing `l`.
4. For counting problems, add `r - l + 1` to the count before or after shrinking, depending on whether you need "at most" or "at least" semantics.
5. Return the answer after processing all of `r`.

**Key variations**
- Minimum length with sum >= target: shrink aggressively while valid and record the smallest window size.
- Maximum length with sum <= budget: expand greedily and shrink only when over budget.
- "Reduce X to zero" problems: reframe as finding the maximum subarray to keep, then the answer is `n - max_kept_length`.
- Score-based constraints: the score may be `sum * length`; these still use the same expand/shrink structure but with a more complex validity check.
- Two-pass problems: find one valid subarray, store its endpoint, then do a second pass from the other side.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3851 | [Maximum Requests Without Violating the Limit](https://leetcode.com/problems/maximum-requests-without-violating-the-limit/) :lock: | Medium | 4/10 | 65.0% | [ ] |
| 1208 | [Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) | Medium | 4/10 | 59.7% | [ ] |
| 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | 4/10 | 51.6% | [x] |
| 1658 | [Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) | Medium | 5/10 | 40.5% | [ ] |
| 2302 | [Count Subarrays With Score Less Than K](https://leetcode.com/problems/count-subarrays-with-score-less-than-k/) | Hard | 6/10 | 62.3% | [ ] |
| 1477 | [Find Two Non-overlapping Sub-arrays Each With Target Sum](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/) | Medium | 6/10 | 36.8% | [ ] |
| 2747 | [Count Zero Request Servers](https://leetcode.com/problems/count-zero-request-servers/) | Medium | 6/10 | 35.8% | [ ] |
| 2106 | [Maximum Fruits Harvested After at Most K Steps](https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/) | Hard | 8/10 | 61.0% | [ ] |

## fixed_window_on_sorted_array

**What it is** — You sort the array first, then apply a fixed-size window to exploit the sorted order — the difference between max and min in any window is simply `arr[r] - arr[l]`, and the window slides efficiently. Recognize this pattern when a problem involves ranges, differences, or "making elements consecutive/equal" and the order of elements doesn't matter for the final answer.

**Common steps**
1. Sort the array (this does not change the answer for problems where element order is irrelevant).
2. Initialize left pointer `l = 0` and the answer variable.
3. Slide a window of size K: for each `r` from 0 to `n-1`, the window is `[r - K + 1, r]` (or use two explicit pointers).
4. Compute the window's property using `arr[r] - arr[l]` (cheap because array is sorted).
5. Update the answer and slide the window forward by advancing `l` when the window exceeds size K.
6. Return the answer.

**Key variations**
- Minimum difference (e.g., min score spread across K elements): straightforward `arr[r] - arr[l]` in a K-size window.
- Maximum beauty / making array continuous: count how many elements fall within a valid range `[arr[l], arr[l] + limit]` — the answer is `K - (elements outside range)`.
- Circular or angular windows (visible points): sort angles, duplicate the array, and apply a fixed angular window.
- Interval-merging variants: sort intervals, then use a window to count how many can be merged within a budget.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1984 | [Minimum Difference Between Highest and Lowest of K Scores](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) | Easy | 2/10 | 66.3% | [ ] |
| 2779 | [Maximum Beauty of an Array After Applying Operation](https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/) | Medium | 4/10 | 58.4% | [ ] |
| 3634 | [Minimum Removals to Balance Array](https://leetcode.com/problems/minimum-removals-to-balance-array/) | Medium | 5/10 | 47.9% | [ ] |
| 2009 | [Minimum Number of Operations to Make Array Continuous](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/) | Hard | 6/10 | 51.8% | [ ] |
| 3323 | [Minimize Connected Groups by Inserting Interval](https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/) :lock: | Medium | 6/10 | 50.4% | [ ] |
| 3346 | [Maximum Frequency of an Element After Performing Operations I](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/) | Medium | 6/10 | 40.1% | [ ] |
| 1040 | [Moving Stones Until Consecutive II](https://leetcode.com/problems/moving-stones-until-consecutive-ii/) | Medium | 7/10 | 58.8% | [ ] |
| 3347 | [Maximum Frequency of an Element After Performing Operations II](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/) | Hard | 7/10 | 53.8% | [ ] |
| 683 | [K Empty Slots](https://leetcode.com/problems/k-empty-slots/) :lock: | Hard | 7/10 | 38.0% | [ ] |
| 3413 | [Maximum Coins From K Consecutive Bags](https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/) | Medium | 7/10 | 24.6% | [ ] |
| 1610 | [Maximum Number of Visible Points](https://leetcode.com/problems/maximum-number-of-visible-points/) | Hard | 8/10 | 38.1% | [ ] |

## monotonic_deque_window_extremum

**What it is** — You use a deque (double-ended queue) that maintains elements in monotonically increasing or decreasing order to efficiently query the minimum or maximum of the current sliding window in O(1) time. Recognize this pattern when a problem needs the max or min of every window of size K, or when the window's validity depends on the spread between its max and min.

**Common steps**
1. Initialize a deque (stores indices, not values), left pointer `l = 0`, and the result.
2. Expand `r`: before adding index `r` to the deque, pop from the back of the deque all indices whose values are worse than `arr[r]` (for a max-deque, pop while `arr[deque.back()] <= arr[r]`).
3. Append `r` to the back of the deque.
4. Pop from the front of the deque if the front index is outside the current window (`deque.front() < l`).
5. The front of the deque is always the index of the current window's maximum (or minimum). Use it to update the answer or check window validity.
6. Advance the window (increment `l` as needed based on your constraint).

**Key variations**
- Fixed window of size K: pop from front when `r - deque.front() >= K`.
- Variable window (abs diff <= limit): maintain two deques — one for max, one for min — and shrink from the left when `max - min > limit`.
- Equation optimization (max value of equation): rewrite the expression so one part depends only on the left element; use a max-deque over the left-dependent part.
- Budget-constrained window: the window is valid when `max + sum <= budget`; combine a deque for max with a running sum.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2762 | [Continuous Subarrays](https://leetcode.com/problems/continuous-subarrays/) | Medium | 5/10 | 58.0% | [ ] |
| 1438 | [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | Medium | 6/10 | 57.7% | [ ] |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | 7/10 | 48.7% | [ ] |
| 1499 | [Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/) | Hard | 7/10 | 45.0% | [ ] |
| 2398 | [Maximum Number of Robots Within Budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/) | Hard | 7/10 | 38.6% | [ ] |
| 3420 | [Count Non-Decreasing Subarrays After K Operations](https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/) | Hard | 8/10 | 24.3% | [ ] |

## variable_window_min_cover

**What it is** — You find the smallest window that contains all required elements (characters, values) at least once or in sufficient quantity, expanding to include requirements and shrinking once all requirements are met. Recognize this pattern when a problem asks for the minimum-length subarray or substring that satisfies a "cover all targets" condition.

**Common steps**
1. Build a `need` map from the target (how many of each character/value is required).
2. Initialize left pointer `l = 0`, a `have` map for the current window, a `formed` counter (how many distinct requirements are currently satisfied), and track the best window seen.
3. Expand `r`: add `s[r]` to `have`. If `have[s[r]] == need[s[r]]`, increment `formed`.
4. While `formed == len(need)` (all requirements met): update the best window if `r - l + 1` is smaller, then shrink from the left — decrement `have[s[l]]`, and if it drops below `need[s[l]]`, decrement `formed`; advance `l`.
5. Return the best window found (or empty string if no valid window exists).

**Key variations**
- Standard minimum window substring: match exact character counts from a pattern string.
- Balanced string replacement: the "need" is derived from a balance condition (each character should appear n/4 times); only the substring outside the window needs fixing.
- Take from both ends: equivalent to finding the largest middle window that does NOT need to contain K of each character — then the answer is `n - largest_middle`.
- Minimum window subsequence (harder): the target must appear as a subsequence (in order), not just as a set of characters — requires a two-pointer scan within the window rather than a simple count check.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2516 | [Take K of Each Character From Left and Right](https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/) | Medium | 5/10 | 51.4% | [ ] |
| 1234 | [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/) | Medium | 6/10 | 40.9% | [ ] |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | 8/10 | 47.4% | [ ] |
| 727 | [Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/) :lock: | Hard | 8/10 | 43.8% | [ ] |

## fixed_window_bucket_sort

**What it is** — You use fixed-size buckets alongside a sliding window to detect whether any two elements within a window of size K are within a value distance of T in O(n) time, bypassing the need to compare every pair. Recognize this pattern when a problem asks about "nearby" elements satisfying both an index constraint and a value constraint simultaneously.

**Common steps**
1. Define bucket width as `t + 1` (so any two elements in the same bucket differ by at most T).
2. Maintain a hash map of buckets, each storing at most one element (the last element placed in that bucket).
3. For each new element `num`, compute its bucket ID as `num // (t + 1)` (handle negatives carefully).
4. Check: (a) the same bucket already has an element (automatically within distance T), or (b) the neighboring buckets (`bucket_id - 1`, `bucket_id + 1`) have an element within distance T.
5. If a match is found, return true. Otherwise, add the current element to its bucket.
6. Remove the element that is sliding out of the window (the one at index `i - k`) from its bucket.

**Key variations**
- This pattern has essentially one canonical problem (Contains Duplicate III); the key insight is that bucket sort reduces the value comparison from O(K) to O(1) per element.
- A sorted set (e.g., a balanced BST or SortedList) is an alternative approach for the same problem, using `floor` and `ceiling` queries instead of buckets.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 220 | [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) | Hard | 7/10 | 24.7% | [ ] |

## exact_k_via_at_most_k_difference

**What it is** — When counting subarrays with exactly K of something (K distinct values, K odd numbers, etc.), you cannot directly use a shrinking window because the window can be both too small and too large. The trick is: `count(exactly K) = count(at most K) - count(at most K-1)`, letting you reuse a simpler "at most K" sliding window twice. Recognize this pattern when a problem asks to count subarrays with exactly K occurrences of something.

**Common steps**
1. Write a helper function `atMost(k)` that counts subarrays with at most K of the target property using a standard variable sliding window.
2. Inside `atMost(k)`: use left pointer `l = 0`, a frequency map or counter, and a result variable.
3. Expand `r`: update the counter for the new element.
4. While the constraint is violated (more than K), shrink from the left and advance `l`.
5. Add `r - l + 1` to the result (all subarrays ending at `r` with any valid left boundary).
6. Return `atMost(k) - atMost(k - 1)` as the final answer.

**Key variations**
- Counting nice subarrays with exactly K odd numbers: apply the trick directly on odd-element count.
- Subarrays with exactly K distinct integers: apply the trick on distinct-value count.
- Harder variants combine this with prefix sums or binary search to count subarrays ending at each position efficiently.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1248 | [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) | Medium | 5/10 | 75.0% | [ ] |
| 992 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Hard | 7/10 | 68.0% | [ ] |
| 3261 | [Count Substrings That Satisfy K-Constraint II](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/) | Hard | 9/10 | 23.5% | [ ] |

## fixed_window_order_statistic

**What it is** — You slide a fixed-size window and need to efficiently query rank-based statistics (median, Xth smallest, Xth largest) for each window position, requiring a data structure that supports O(log K) insertions, deletions, and order-statistic queries. Recognize this pattern when a problem asks for a percentile, rank, or sorted-position value within each window.

**Common steps**
1. Choose the right data structure: two heaps (max-heap for lower half, min-heap for upper half) for median; a sorted list or balanced BST for arbitrary rank queries.
2. Populate the structure with the first K elements and compute the initial answer.
3. For each new position, insert the incoming element into the structure (maintaining the balance or sorted property).
4. Remove the outgoing element (the one that just left the window) — this is the hardest step; lazy deletion or direct removal depending on the structure.
5. Query the structure for the required statistic (e.g., top of the min-heap for the median, or Xth element in a sorted list).
6. Record the result and continue until all windows are processed.

**Key variations**
- Sliding window median: maintain two heaps of equal size (or differ by 1); the median is the top of one or average of both tops.
- Sliding window Xth smallest: use a sorted list (e.g., Python's `SortedList`) and index directly into it.
- Top-X frequency sum (X-Sum): combine a frequency map with a sorted structure to track which elements are in the top X by frequency.
- Operations to equalize: sort the window, find the median, compute the total absolute deviation from the median.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2653 | [Sliding Subarray Beauty](https://leetcode.com/problems/sliding-subarray-beauty/) | Medium | 6/10 | 36.9% | [ ] |
| 3422 | [Minimum Operations to Make Subarray Elements Equal](https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/) :lock: | Medium | 7/10 | 46.3% | [ ] |
| 3321 | [Find X-Sum of All K-Long Subarrays II](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/) | Hard | 8/10 | 41.1% | [ ] |
| 480 | [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) | Hard | 9/10 | 39.0% | [ ] |

## monotonic_deque_prefix_sum

**What it is** — You combine a prefix sum array with a monotonic deque to find the shortest subarray whose sum is at least K, where the array may contain negative numbers (ruling out a simple two-pointer approach). Recognize this pattern when elements can be negative and you need min/max length subarrays with a sum constraint.

**Common steps**
1. Compute the prefix sum array `P` where `P[i] = arr[0] + ... + arr[i-1]` and `P[0] = 0`.
2. Initialize a monotonically increasing deque (stores indices into `P`) and the answer as infinity.
3. For each index `r` from 0 to n: while the deque is non-empty and `P[r] - P[deque.front()] >= K`, update the answer with `r - deque.front()` and pop from the front (we found the best use of that left endpoint).
4. While the deque is non-empty and `P[r] <= P[deque.back()]`, pop from the back (the back index can never be a better left endpoint than `r` for any future right endpoint).
5. Append `r` to the deque.
6. Return the answer (or -1 if no valid subarray was found).

**Key variations**
- This is primarily a single-problem pattern; the key insight is that negative numbers break the monotone-sum property needed for a plain two-pointer, so a deque over prefix sums restores efficiency.
- Similar prefix-sum + deque ideas appear in problems involving maximum sum subarrays with length constraints.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 862 | [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | Hard | 8/10 | 32.8% | [ ] |

## fixed_window_greedy_flip

**What it is** — You use a fixed-size window to simulate bit flips greedily: whenever you encounter a bit that needs to change, you flip the entire window starting at that position, tracking cumulative flips with a difference array or a running counter to avoid re-processing each element. Recognize this pattern when you must flip contiguous blocks of size K and want the minimum number of flips.

**Common steps**
1. Initialize a `flip_count` variable (or a difference array) to track how many flips cover the current position, and a result counter.
2. Iterate index `i` from 0 to `n - 1`. Determine the current effective value of `arr[i]` by checking whether the running flip parity (even or odd) changes its value.
3. If the current position needs to be flipped (effective value != target), and `i + K > n`, return -1 (impossible).
4. Otherwise, increment the result counter, record a flip starting at `i` (set `flip[i] = 1` or increment a running toggle), and update the running flip count.
5. When `i >= K`, undo the flip that started K positions ago (subtract `flip[i - K]` from the running count).
6. Return the result count.

**Key variations**
- This pattern is primarily captured by one canonical problem (Minimum Number of K Consecutive Bit Flips); the greedy correctness relies on the fact that each position should be flipped at most once.
- The difference array trick (marking flip starts and reconstructing the parity via prefix sum) is the key optimization over a naive O(nK) simulation.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 995 | [Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/) | Hard | 8/10 | 62.3% | [ ] |

## rolling_hash_window

**What it is** — You use polynomial hashing to represent a fixed-size window as a numeric hash value, updating it in O(1) as the window slides (subtract the outgoing element's contribution, multiply, add the incoming element). Recognize this pattern when a problem requires detecting or comparing substrings by content at scale, where naive comparison would be too slow.

**Common steps**
1. Choose a base (e.g., 31 or a prime) and a modulus (a large prime) to reduce collision risk.
2. Compute the hash of the first window of size K using: `hash = (hash * base + char_value) % mod` for each character.
3. Slide the window: remove the leftmost character's contribution (`hash = (hash - char_value * base^(K-1)) % mod`) then add the new rightmost character (`hash = (hash * base + new_char) % mod`).
4. Store hashes in a set or map; if the current hash matches a previously seen hash, verify with a direct string comparison to confirm (handle collisions).
5. Record the result (e.g., all starting positions of matching windows, or whether a repeated hash exists).

**Key variations**
- Detecting repeated substrings: insert each window hash into a set and flag duplicates.
- Matching against a target hash: compute the target hash once and compare each window hash to it directly.
- Reverse-direction hashing: some problems (Find Substring With Given Hash Value) require computing hashes right-to-left because the hash function depends on future characters, so you process the string from right to left.
- Double hashing (two different mod values) reduces collision probability for high-stakes problems.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2524 | [Maximum Frequency Score of a Subarray](https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/) :lock: | Hard | 8/10 | 36.6% | [ ] |
| 2156 | [Find Substring With Given Hash Value](https://leetcode.com/problems/find-substring-with-given-hash-value/) | Hard | 8/10 | 26.2% | [ ] |
