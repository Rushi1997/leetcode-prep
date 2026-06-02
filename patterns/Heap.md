# Heap

66 problems across 13 patterns.

## top_k_frequent

**What it is** — Count the frequency of each element using a hash map, then use a min-heap of size K to track the K most frequent items. When the heap exceeds size K, pop the minimum-frequency element so only the top K remain. Recognize this pattern when the problem asks for the K most/least common elements in a collection.

**Common steps**
1. Build a frequency map (hash map from element to count).
2. Initialize a min-heap (keyed on frequency).
3. Push each (frequency, element) pair onto the heap.
4. If heap size exceeds K, pop the smallest frequency element.
5. After processing all elements, extract remaining heap entries — these are the top K.
6. Return results, sorting if order matters (e.g., lexicographic for words).

**Key variations**
- Simple integer elements vs. string elements (strings need secondary sort by lexicographic order when frequencies tie).
- Returning the elements themselves vs. returning their frequencies.
- Aggregating scores across multiple criteria before ranking (e.g., Reward Top K Students uses positive/negative word lists).
- Streaming input vs. batch input.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1086 | [High Five](https://leetcode.com/problems/high-five/) :lock: | Easy | 2/10 | 74.2% | [ ] |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | 4/10 | 66.3% | [x] |
| 692 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | Medium | 4/10 | 60.1% | [ ] |
| 2512 | [Reward Top K Students](https://leetcode.com/problems/reward-top-k-students/) | Medium | 4/10 | 47.0% | [ ] |

## kth_element

**What it is** — Find the K-th smallest or largest element in a dataset without fully sorting it. A min-heap of size K maintains the K largest elements seen so far; the heap root is always the K-th largest. Recognize this when asked for a single ranked element (not the full top-K list) or when elements arrive one at a time.

**Common steps**
1. Initialize a min-heap.
2. Push elements one by one onto the heap.
3. If heap size exceeds K, pop the minimum (this discards elements smaller than the current K-th largest).
4. After all elements are processed, the heap root is the K-th largest element.
5. For K-th smallest, use a max-heap of size K instead (negate values in Python).
6. For multi-dimensional problems (e.g., closest points), key the heap on the computed metric (e.g., squared distance).

**Key variations**
- Static array vs. online stream (Kth Largest in a Stream requires maintaining the heap across calls).
- Numeric values vs. string-encoded integers (require custom comparator or conversion).
- 1D values vs. 2D coordinates (key on distance instead of value directly).
- Grid problems where the K-th element requires scanning a 2D space (Get Biggest Three Rhombus Sums).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 703 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | 2/10 | 61.0% | [x] |
| 2099 | [Find Subsequence of Length K With the Largest Sum](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/) | Easy | 2/10 | 57.4% | [ ] |
| 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | 4/10 | 69.0% | [x] |
| 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | 4/10 | 68.9% | [x] |
| 3275 | [K-th Nearest Obstacle Queries](https://leetcode.com/problems/k-th-nearest-obstacle-queries/) | Medium | 4/10 | 49.0% | [ ] |
| 1985 | [Find the Kth Largest Integer in the Array](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/) | Medium | 4/10 | 47.9% | [ ] |
| 1878 | [Get Biggest Three Rhombus Sums in a Grid](https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/) | Medium | 7/10 | 71.4% | [ ] |

## design_priority_queue

**What it is** — Build a data structure that supports efficient insert and extract-min/max operations, typically wrapping a heap to satisfy a custom API contract. Recognize this pattern when a design problem asks for O(log n) reservation, release, or priority-based retrieval with persistent state across method calls.

**Common steps**
1. Identify the priority key (e.g., seat number, event priority, timestamp).
2. Pre-populate the heap with all available items at initialization if the universe is fixed.
3. For `reserve`/`acquire`: pop the heap root (best available item).
4. For `release`/`free`: push the item back onto the heap.
5. Handle edge cases such as double-release or querying when the heap is empty.
6. Return the popped value (or a computed result) as the API response.

**Key variations**
- Fixed universe of items (pre-populate at init) vs. dynamically added items.
- Min-heap for smallest-first allocation (seat numbers) vs. max-heap for highest-priority-first (event manager).
- Simple integer keys vs. composite keys with tie-breaking rules.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1845 | [Seat Reservation Manager](https://leetcode.com/problems/seat-reservation-manager/) | Medium | 3/10 | 67.2% | [ ] |
| 3885 | [Design Event Manager](https://leetcode.com/problems/design-event-manager/) | Medium | 6/10 | 50.8% | [ ] |

## heap_simulation

**What it is** — Repeatedly extract the most extreme element from a collection, transform it according to problem rules, and reinsert it. The heap maintains sorted order after each mutation so the next operation always targets the correct element. Recognize this when a problem says "repeat K times: pick min/max, apply operation, put back."

**Common steps**
1. Heapify the initial array (min or max heap depending on the operation).
2. For each of the K rounds: pop the root, apply the transformation (e.g., halve, multiply, mark neighbors).
3. Push the transformed value back onto the heap.
4. Accumulate any running total or side effect required by the problem.
5. After all rounds, read the answer from the heap or the accumulator.
6. For Hard variants: batch operations using math (modular exponentiation) to avoid simulating each step individually.

**Key variations**
- Transformation is simple arithmetic (halve, multiply) vs. complex (mark neighbors, merge pairs).
- Fixed K rounds vs. "repeat until condition is met."
- Need to track element identities (indices) alongside values for tie-breaking or neighbor lookups.
- Hard variants require detecting cycles or using math to skip redundant simulation steps.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3264 | [Final Array State After K Multiplication Operations I](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/) | Easy | 1/10 | 86.9% | [ ] |
| 2974 | [Minimum Number Game](https://leetcode.com/problems/minimum-number-game/) | Easy | 1/10 | 85.5% | [ ] |
| 3507 | [Minimum Pair Removal to Sort Array I](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/) | Easy | 2/10 | 65.2% | [ ] |
| 2593 | [Find Score of an Array After Marking All Elements](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/) | Medium | 5/10 | 64.5% | [ ] |
| 3080 | [Mark Elements on Array by Performing Queries](https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/) | Medium | 5/10 | 49.3% | [ ] |
| 3092 | [Most Frequent IDs](https://leetcode.com/problems/most-frequent-ids/) | Medium | 5/10 | 42.7% | [ ] |
| 3510 | [Minimum Pair Removal to Sort Array II](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/) | Hard | 8/10 | 39.0% | [ ] |
| 3266 | [Final Array State After K Multiplication Operations II](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/) | Hard | 9/10 | 13.3% | [ ] |

## greedy_max_heap

**What it is** — Use a max-heap to always greedily act on the largest element available, because taking from/modifying the maximum at each step leads to the globally optimal result. Recognize this when the problem says "repeatedly pick the largest" and the greedy choice is provably optimal (e.g., reducing the maximum reduces total sum fastest).

**Common steps**
1. Negate all values and push onto a min-heap (Python's `heapq` is a min-heap, so negate to simulate max-heap).
2. For each of K operations: pop the max (smallest negated value), apply the required transformation.
3. Push the transformed value back (negated if it re-enters the heap).
4. Track any required running sum, count, or constructed output.
5. After K operations (or when a termination condition is met), return the answer.
6. For construction problems (Reorganize String), always place the most frequent remaining character that does not violate the constraint.

**Key variations**
- Fixed K operations vs. operate until a condition holds.
- Numeric reduction (halve, take floor sqrt) vs. string construction (interleave characters by frequency).
- Problems that require working backwards from the target using a max-heap (Construct Target Array).
- Minimizing deviation by normalizing elements first (all odd → multiply by 2, then only divide evens).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2558 | [Take Gifts From the Richest Pile](https://leetcode.com/problems/take-gifts-from-the-richest-pile/) | Easy | 1/10 | 75.5% | [ ] |
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | 1/10 | 66.5% | [x] |
| 1962 | [Remove Stones to Minimize the Total](https://leetcode.com/problems/remove-stones-to-minimize-the-total/) | Medium | 4/10 | 65.7% | [ ] |
| 2530 | [Maximal Score After Applying K Operations](https://leetcode.com/problems/maximal-score-after-applying-k-operations/) | Medium | 4/10 | 64.1% | [ ] |
| 2208 | [Minimum Operations to Halve Array Sum](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/) | Medium | 4/10 | 50.1% | [ ] |
| 2182 | [Construct String With Repeat Limit](https://leetcode.com/problems/construct-string-with-repeat-limit/) | Medium | 5/10 | 70.8% | [ ] |
| 767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | Medium | 5/10 | 57.1% | [ ] |
| 1792 | [Maximum Average Pass Ratio](https://leetcode.com/problems/maximum-average-pass-ratio/) | Medium | 6/10 | 74.1% | [ ] |
| 1675 | [Minimize Deviation in Array](https://leetcode.com/problems/minimize-deviation-in-array/) | Hard | 8/10 | 54.0% | [ ] |
| 1354 | [Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) | Hard | 8/10 | 37.0% | [ ] |

## greedy_min_heap

**What it is** — Use a min-heap to greedily act on the smallest element available, because merging or modifying the cheapest/smallest items at each step minimizes total cost. Recognize this when combining two smallest elements produces a new element that must also be considered (Huffman-coding style), or when you want to defer using expensive resources as long as possible.

**Common steps**
1. Push all initial elements onto a min-heap.
2. Pop the one or two smallest elements required by the operation.
3. Compute the new element (e.g., sum, product, combined cost) and push it back if needed.
4. Accumulate the cost or result of each operation.
5. Repeat until the heap satisfies the termination condition (size, threshold value, etc.).
6. For problems with expiration (Maximum Number of Eaten Apples), also track item deadlines and lazily discard expired entries.

**Key variations**
- Merging two smallest elements into one (connect sticks, eliminate bacterial strains).
- Increments to minimize/maximize a product — always increment the smallest element.
- Lazy deletion: items have deadlines; pop and discard expired items before using the heap root.
- Lexicographic constraints combined with frequency (remove stars to get lexicographically minimum string).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1167 | [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) :lock: | Medium | 4/10 | 71.9% | [ ] |
| 3066 | [Minimum Operations to Exceed Threshold Value II](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/) | Medium | 4/10 | 45.8% | [ ] |
| 1642 | [Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/) | Medium | 5/10 | 50.8% | [ ] |
| 2233 | [Maximum Product After K Increments](https://leetcode.com/problems/maximum-product-after-k-increments/) | Medium | 5/10 | 44.0% | [ ] |
| 3170 | [Lexicographically Minimum String After Removing Stars](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/) | Medium | 6/10 | 50.9% | [ ] |
| 1705 | [Maximum Number of Eaten Apples](https://leetcode.com/problems/maximum-number-of-eaten-apples/) | Medium | 6/10 | 43.2% | [ ] |
| 3711 | [Maximum Transactions Without Negative Balance](https://leetcode.com/problems/maximum-transactions-without-negative-balance/) :lock: | Medium | 7/10 | 46.3% | [ ] |
| 2333 | [Minimum Sum of Squared Difference](https://leetcode.com/problems/minimum-sum-of-squared-difference/) | Medium | 7/10 | 26.8% | [ ] |
| 3506 | [Find Time Required to Eliminate Bacterial Strains](https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/) :lock: | Hard | 8/10 | 61.4% | [ ] |

## two_heaps

**What it is** — Maintain two heaps simultaneously — a max-heap for the lower half of values and a min-heap for the upper half — so that the median (or boundary between two groups) is always accessible in O(1). Recognize this when a problem requires dynamic insertion and repeated queries for the middle value of a growing dataset, or when buy/sell orders must be matched at a boundary price.

**Common steps**
1. Initialize a max-heap `lo` (negate values) for the smaller half and a min-heap `hi` for the larger half.
2. When inserting a new element: push to `lo` if it is <= current max of `lo`, otherwise push to `hi`.
3. Rebalance: ensure `len(lo) - len(hi)` is at most 1 (or 0 for equal-size), moving elements between heaps as needed.
4. The median is the root of `lo` (if sizes differ) or the average of both roots (if sizes are equal).
5. For order-matching problems: match orders from both heaps while the best buy price >= best sell price, decrementing quantities accordingly.

**Key variations**
- Streaming median: new numbers arrive one at a time (Find Median from Data Stream).
- Order book matching: two heaps represent buy orders (max-heap) and sell orders (min-heap) with quantity tracking (Number of Orders in the Backlog).
- Fixed vs. sliding window median (sliding window adds lazy deletion complexity).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1801 | [Number of Orders in the Backlog](https://leetcode.com/problems/number-of-orders-in-the-backlog/) | Medium | 5/10 | 53.9% | [ ] |
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | 8/10 | 54.4% | [x] |

## heap_sort_greedy

**What it is** — Sort items by one criterion, then use a heap on a second criterion to efficiently pick the best K items under a combined constraint. Recognize this when you must fix one variable (sort by it) to make greedy choices tractable on a second variable, often seen in "maximize/minimize a score subject to choosing exactly K items."

**Common steps**
1. Sort the input by the "fixed" criterion (e.g., minimum speed, profit threshold, weight).
2. Iterate through sorted items; for each item, push the "variable" criterion value onto a max-heap (or min-heap).
3. If the heap exceeds K elements, pop the worst one to maintain only the best K.
4. Compute the current answer using the heap's aggregate (e.g., sum of top-K values times current item's other attribute).
5. Track the global best answer across all iterations.
6. For problems like IPO, use a min-heap on capital to unlock projects as budget grows, then greedily pick max-profit from unlocked projects.

**Key variations**
- Maximize sum of K largest values paired with current item's multiplier (Maximum Subsequence Score, Maximum Performance of a Team).
- Unlock items progressively as a resource grows, then greedy pick from unlocked set (IPO).
- Select at most K elements from sub-groups with constraints (Choose K Elements With Maximum Sum).
- Minimize cost of K workers by iterating on a ratio constraint (Minimum Cost to Hire K Workers — sort by wage/quality ratio).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3763 | [Maximum Total Sum with Threshold Constraints](https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/) :lock: | Medium | 5/10 | 82.2% | [ ] |
| 3462 | [Maximum Sum With at Most K Elements](https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/) | Medium | 5/10 | 60.7% | [ ] |
| 2542 | [Maximum Subsequence Score](https://leetcode.com/problems/maximum-subsequence-score/) | Medium | 6/10 | 54.6% | [ ] |
| 3478 | [Choose K Elements With Maximum Sum](https://leetcode.com/problems/choose-k-elements-with-maximum-sum/) | Medium | 6/10 | 33.7% | [ ] |
| 502 | [IPO](https://leetcode.com/problems/ipo/) | Hard | 7/10 | 53.5% | [ ] |
| 1383 | [Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/) | Hard | 8/10 | 47.8% | [ ] |
| 857 | [Minimum Cost to Hire K Workers](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/) | Hard | 9/10 | 63.6% | [ ] |

## task_scheduling

**What it is** — Simulate a CPU or server scheduler where tasks arrive over time and must be assigned to the best available resource according to a priority rule. A min-heap of free resources and a min-heap of in-progress tasks (keyed on completion time) together let you efficiently advance time and make assignments. Recognize this when problems describe machines/servers processing jobs with start times, durations, and tie-breaking rules.

**Common steps**
1. Sort tasks/arrivals by start time (or arrival time).
2. Initialize a min-heap of available resources (e.g., server indices, chair numbers).
3. Initialize a min-heap of busy resources keyed on (finish_time, resource_id).
4. For each arriving task: pop all resources from the busy heap whose finish_time <= current time and push them back to the available heap.
5. Assign the arriving task to the best available resource (pop from available heap); if none are free, advance time to the earliest finish_time and free that resource first.
6. Push the newly busy resource (finish_time + duration, resource_id) onto the busy heap, and record the assignment.

**Key variations**
- Identical resources (chairs, threads) vs. heterogeneous resources with different speeds.
- Tie-breaking by resource index (smallest index wins) vs. longest-waiting task first.
- Multiple queues: tasks flow through stages (left bank → right bank in Time to Cross a Bridge).
- Tracking which resource handled the most tasks, not just assignments (Find Servers That Handled Most Number of Requests).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1942 | [The Number of the Smallest Unoccupied Chair](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/) | Medium | 6/10 | 60.3% | [ ] |
| 1834 | [Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) | Medium | 6/10 | 47.6% | [ ] |
| 2462 | [Total Cost to Hire K Workers](https://leetcode.com/problems/total-cost-to-hire-k-workers/) | Medium | 6/10 | 43.6% | [ ] |
| 1882 | [Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/) | Medium | 7/10 | 41.9% | [ ] |
| 2402 | [Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/) | Hard | 8/10 | 51.5% | [ ] |
| 1606 | [Find Servers That Handled Most Number of Requests](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/) | Hard | 9/10 | 45.4% | [ ] |
| 2532 | [Time to Cross a Bridge](https://leetcode.com/problems/time-to-cross-a-bridge/) | Hard | 9/10 | 44.3% | [ ] |

## merge_k_sorted

**What it is** — Merge K sorted sequences into one sorted output by always extending from whichever sequence currently has the smallest available element. A min-heap of size K tracks the current front of each sequence, giving O(N log K) total time instead of O(NK). Recognize this when input is K pre-sorted lists and you need a globally sorted result or the smallest range covering all lists.

**Common steps**
1. Push the first element of each of the K lists onto a min-heap as (value, list_index, element_index).
2. Pop the minimum element from the heap — this is the next element in the merged output.
3. If the popped element's list has a next element, push it onto the heap.
4. Repeat until the heap is empty.
5. For "smallest range" problems: track the current max across all list fronts alongside the heap min, updating the best range whenever a new element is popped.

**Key variations**
- Merge into a single linked list or array (Merge k Sorted Lists).
- Find the smallest window [min, max] that contains at least one element from each list (Smallest Range Covering Elements from K Lists — requires tracking the current max explicitly).
- The K sequences are virtual/implicit rather than materialized arrays.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | 7/10 | 59.5% | [ ] |
| 632 | [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Hard | 8/10 | 70.1% | [ ] |

## k_way_merge

**What it is** — Enumerate candidate solutions in sorted order using a heap over an implicit sorted space, without generating all candidates explicitly. Push the smallest candidate into the heap, and when popping it, generate its neighbors (the next candidates derived from it) and push those. Recognize this when candidates can be ordered but generating all of them upfront is too expensive.

**Common steps**
1. Define the initial candidate (e.g., pair with smallest indices, smallest subset sum) and push it onto a min-heap.
2. Use a visited set to avoid pushing duplicate candidates.
3. Pop the minimum candidate; if K answers have been found, stop.
4. Generate neighbor candidates by incrementing one index/dimension at a time and push each unvisited neighbor.
5. Repeat until K candidates have been extracted from the heap.
6. For matrix problems, the "neighbors" of (row, col) are (row+1, col) and (row, col+1) in a sorted-row matrix.

**Key variations**
- K smallest pairs from two sorted arrays (Find K Pairs with Smallest Sums — neighbors are (i+1, j) and (i, j+1)).
- K-th smallest sum from K sorted rows of a matrix (reduce pairwise: merge two rows at a time).
- K-th largest sum of a subset (Find the K-Sum of an Array — transform to finding K-th smallest among all subset sums using a sorted array of non-negatives).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Medium | 6/10 | 41.8% | [ ] |
| 1439 | [Find the Kth Smallest Sum of a Matrix With Sorted Rows](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) | Hard | 8/10 | 62.3% | [ ] |
| 2386 | [Find the K-Sum of an Array](https://leetcode.com/problems/find-the-k-sum-of-an-array/) | Hard | 9/10 | 41.3% | [ ] |

## sweep_line_heap

**What it is** — Process events (interval starts and ends, building edges, water boundaries) in sorted order along one axis, using a heap to efficiently query or maintain the active set at each event point. The heap holds currently "open" intervals or heights, and elements are lazily removed when the sweep line passes their endpoint. Recognize this when intervals or geometric structures must be queried at arbitrary points along a sorted axis.

**Common steps**
1. Convert the input into events (start events and end events) sorted by position/time.
2. Initialize a max-heap (or min-heap) to represent the currently active set.
3. Process events in order: on a start event, push the relevant value (e.g., building height, interval length) onto the heap.
4. On an end event (or before answering a query), lazily pop expired entries from the heap top until the top is still valid.
5. Record the answer at each query point using the current heap top.
6. For offline query problems (Minimum Interval to Include Each Query), sort queries too and process them interleaved with events.

**Key variations**
- Skyline problem: events are building left/right edges; track current max height and emit output when it changes.
- Trapping Rain Water II: BFS/Dijkstra-style from the boundary inward, using a min-heap on boundary height.
- Offline interval queries: sort queries by value, sweep sorted intervals, use heap to find the shortest active interval covering each query point.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 407 | [Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) | Hard | 8/10 | 64.1% | [ ] |
| 1851 | [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Hard | 8/10 | 54.3% | [ ] |
| 218 | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | Hard | 9/10 | 45.3% | [ ] |

## sliding_window_heap

**What it is** — Combine a sliding window over an array with a heap to efficiently track the minimum or maximum within the current window, or to maintain a fixed-size optimal subset as the window moves. Elements that fall outside the window boundary are lazily discarded from the heap using their stored index. Recognize this when the problem asks for an optimal value (min/max/sum) over every contiguous subarray of a fixed or variable size.

**Common steps**
1. Determine the window size or the condition that defines when the window shrinks.
2. Push (value, index) tuples onto the heap as the right pointer advances.
3. Before reading the heap top, pop all entries whose index is outside the current valid window (lazy deletion).
4. The heap top is the answer for the current window position.
5. Advance the left/right pointers and repeat.
6. For "split array" variants, precompute prefix heaps from both ends, then combine at each split point.

**Key variations**
- Fixed window size (classic sliding window maximum/minimum).
- Variable window defined by a constraint (sum, cost) rather than fixed length.
- Split-point optimization: precompute the best K-element subset for the prefix ending at each index and suffix starting at each index, then sweep split points (Minimum Difference in Sums After Removal of Elements).
- Multiple subarrays with minimum cost chosen greedily using a heap that tracks the cheapest subarray starts (Divide an Array Into Subarrays With Minimum Cost II).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2163 | [Minimum Difference in Sums After Removal of Elements](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/) | Hard | 8/10 | 69.7% | [ ] |
| 3013 | [Divide an Array Into Subarrays With Minimum Cost II](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/) | Hard | 9/10 | 54.7% | [ ] |
