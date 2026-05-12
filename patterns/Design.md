# Design

83 problems across 20 patterns.

## hashmap_index_lookup

**What it is** — This pattern uses a hash map to store and retrieve data by key in O(1) time, often mapping identifiers to values, timestamps, or lists of positions. Recognize it when a problem asks you to design a class that records events and later answers queries about them (e.g., "was this seen recently?", "what is the average for this route?").

**Common steps**
1. Identify the key (user ID, word, route, etc.) and the value to store (timestamp, count, list of indices, running sum + count).
2. Choose the right map structure: `dict` for single values, `defaultdict(list)` for multiple values per key.
3. On each `record`/`add` call, insert or update the map entry.
4. On each `query` call, look up the key and compute the answer from stored data (e.g., average = sum / count, min distance between index pairs).
5. Handle edge cases: key not present, empty lists, duplicate entries.

**Key variations**
- Single value per key (rate limiter, authentication tokens) vs. list of values per key (word positions, check-in/check-out pairs).
- Query is a direct lookup (Logger Rate Limiter) vs. requires iteration or math over stored values (Underground System averages, Shortest Word Distance).
- Secondary index needed: some problems require a sorted structure (Leaderboard uses a sorted score map alongside a name→score map).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 359 | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) :lock: | Easy | 1/10 | 76.8% | [ ] |
| 3242 | [Design Neighbor Sum Service](https://leetcode.com/problems/design-neighbor-sum-service/) | Easy | 1/10 | 76.5% | [ ] |
| 1570 | [Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors/) :lock: | Medium | 2/10 | 89.9% | [ ] |
| 535 | [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/) | Medium | 2/10 | 86.6% | [ ] |
| 1244 | [Design A Leaderboard](https://leetcode.com/problems/design-a-leaderboard/) :lock: | Medium | 3/10 | 68.1% | [ ] |
| 1357 | [Apply Discount Every n Orders](https://leetcode.com/problems/apply-discount-every-n-orders/) | Medium | 3/10 | 65.6% | [ ] |
| 244 | [Shortest Word Distance II](https://leetcode.com/problems/shortest-word-distance-ii/) :lock: | Medium | 3/10 | 62.9% | [ ] |
| 1396 | [Design Underground System](https://leetcode.com/problems/design-underground-system/) | Medium | 4/10 | 74.5% | [ ] |
| 1865 | [Finding Pairs With a Certain Sum](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/) | Medium | 4/10 | 61.6% | [ ] |
| 635 | [Design Log Storage System](https://leetcode.com/problems/design-log-storage-system/) :lock: | Medium | 4/10 | 59.6% | [ ] |
| 1797 | [Design Authentication Manager](https://leetcode.com/problems/design-authentication-manager/) | Medium | 4/10 | 58.6% | [ ] |
| 2013 | [Detect Squares](https://leetcode.com/problems/detect-squares/) | Medium | 5/10 | 52.5% | [ ] |

## sliding_window_stream

**What it is** — This pattern processes an incoming stream of values and answers queries about a fixed-size or time-bounded recent window. Recognize it when data arrives one element at a time and queries ask about only the last N elements or events within the last T seconds.

**Common steps**
1. Decide on the underlying container: a fixed-size array (circular buffer) for count-based windows, or a `deque`/sorted list for time-based windows.
2. On each incoming element, add it to the window and evict stale entries (index out of range, or timestamp too old).
3. Maintain a running aggregate (sum, count, prefix pointer) so queries are O(1) rather than recomputing from scratch.
4. On query, return the aggregate directly or compute it from the current window contents.
5. Handle the pointer wrap-around correctly when using a circular buffer.

**Key variations**
- Fixed-count window (Moving Average: always last N elements) vs. time-based window (Hit Counter: events within last 300 seconds).
- Ordered stream gap-filling (Design an Ordered Stream: fill slots and advance a pointer when consecutive entries are complete).
- Longest prefix tracking (Longest Uploaded Prefix: find the furthest contiguous chunk uploaded so far).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1656 | [Design an Ordered Stream](https://leetcode.com/problems/design-an-ordered-stream/) | Easy | 2/10 | 82.6% | [ ] |
| 346 | [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) :lock: | Easy | 2/10 | 80.2% | [ ] |
| 362 | [Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) :lock: | Medium | 4/10 | 69.7% | [ ] |
| 2424 | [Longest Uploaded Prefix](https://leetcode.com/problems/longest-uploaded-prefix/) | Medium | 4/10 | 55.0% | [ ] |

## data_structure_simulation

**What it is** — This pattern asks you to implement a well-known data structure or system from scratch using only more primitive building blocks (arrays, linked lists, queues). Recognize it when a problem says "implement X without using X" or "design a class that supports these operations" and the operations map directly to a classic structure.

**Common steps**
1. Identify which classic structure is being simulated (stack, queue, linked list, hash map, etc.) and which primitive you must use instead.
2. Choose a representation: one array/list for simple cases, two stacks for amortized queue simulation, a list of nodes for linked lists.
3. Implement each required operation, thinking carefully about which end of your primitive to push/pop from.
4. For amortized designs (queue from two stacks), transfer elements lazily only when the output side is empty.
5. Track auxiliary state (size, top pointer, tail pointer) as separate fields so each operation stays O(1) or amortized O(1).
6. Test boundary conditions: empty structure, single element, max capacity.

**Key variations**
- Simulating one structure with another (stack↔queue) vs. building a structure from scratch (Design HashMap, Design Linked List).
- Operations with side effects beyond the core structure (Stack With Increment applies lazy increments; Browser History has forward/back pointers).
- Grid/2D simulation (Subrectangle Queries stores updates lazily and applies them on read vs. eagerly updating all cells).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1476 | [Subrectangle Queries](https://leetcode.com/problems/subrectangle-queries/) | Medium | 2/10 | 86.3% | [ ] |
| 225 | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Easy | 2/10 | 69.8% | [ ] |
| 232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | 2/10 | 69.7% | [x] |
| 2043 | [Simple Bank System](https://leetcode.com/problems/simple-bank-system/) | Medium | 2/10 | 69.7% | [ ] |
| 705 | [Design HashSet](https://leetcode.com/problems/design-hashset/) | Easy | 2/10 | 68.0% | [ ] |
| 706 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) | Easy | 2/10 | 66.5% | [ ] |
| 1472 | [Design Browser History](https://leetcode.com/problems/design-browser-history/) | Medium | 3/10 | 78.3% | [ ] |
| 1381 | [Design a Stack With Increment Operation](https://leetcode.com/problems/design-a-stack-with-increment-operation/) | Medium | 4/10 | 79.9% | [ ] |
| 2408 | [Design SQL](https://leetcode.com/problems/design-sql/) :lock: | Medium | 4/10 | 64.4% | [ ] |
| 2241 | [Design an ATM Machine](https://leetcode.com/problems/design-an-atm-machine/) | Medium | 4/10 | 45.0% | [ ] |
| 707 | [Design Linked List](https://leetcode.com/problems/design-linked-list/) | Medium | 5/10 | 30.2% | [ ] |
| 2296 | [Design a Text Editor](https://leetcode.com/problems/design-a-text-editor/) | Hard | 7/10 | 50.5% | [ ] |

## iterator_design

**What it is** — This pattern wraps one or more underlying collections behind a unified `hasNext()` / `next()` interface, often with added behavior like peeking ahead, interleaving sources, or decoding compressed formats. Recognize it when a problem provides an existing iterator or nested structure and asks you to wrap or extend it.

**Common steps**
1. Store references to all underlying iterators or a pointer into the source data.
2. Implement `hasNext()` by checking whether any source still has unconsumed elements (may require advancing internal state).
3. Implement `next()` to return the current element and advance the pointer; use a queue or buffer if elements must be pre-fetched.
4. For peeking: cache the next value in a variable on the first call to `peek()` and consume it on the next call to `next()`.
5. For interleaving (Zigzag): use a round-robin index to cycle through multiple iterators, skipping exhausted ones.
6. For compressed/encoded formats (RLE, compressed string): decode lazily — only expand the next run when the buffer empties.

**Key variations**
- Single source with lookahead (Peeking Iterator) vs. multiple interleaved sources (Zigzag Iterator).
- Flat compressed sequence (RLE Iterator, Compressed String Iterator) vs. arbitrarily nested structure (Flatten Nested List Iterator — needs a stack to unwrap nesting).
- 2D structure flattening (Flatten 2D Vector: advance row when current row is exhausted).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 281 | [Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/) :lock: | Medium | 3/10 | 67.0% | [ ] |
| 604 | [Design Compressed String Iterator](https://leetcode.com/problems/design-compressed-string-iterator/) :lock: | Easy | 3/10 | 40.4% | [ ] |
| 284 | [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/) | Medium | 4/10 | 61.5% | [ ] |
| 900 | [RLE Iterator](https://leetcode.com/problems/rle-iterator/) | Medium | 4/10 | 59.2% | [ ] |
| 251 | [Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector/) :lock: | Medium | 4/10 | 50.5% | [ ] |
| 341 | [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) | Medium | 5/10 | 65.7% | [ ] |

## pool_slot_management

**What it is** — This pattern manages a finite pool of resources (phone numbers, seats, IDs) supporting allocation and release operations, with the goal of always returning an available resource efficiently. Recognize it when a problem has a fixed universe of items and requires O(1) or O(log n) get/release with no duplicates.

**Common steps**
1. Initialize the pool: store all available resources in a set or queue for O(1) access.
2. On `get`: return any available resource (pop from the set/queue) and mark it as allocated in a separate "in-use" set.
3. On `check(x)`: look up x in the in-use set to determine availability.
4. On `release(x)`: move x from in-use back to the available pool.
5. Handle invalid operations: releasing an unallocated resource or getting from an empty pool.

**Key variations**
- Pool with arbitrary ordering (any available is fine — use a set) vs. ordered allocation (always the smallest — use a min-heap).
- Pool with additional metadata per slot (e.g., owner, timestamp).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 379 | [Design Phone Directory](https://leetcode.com/problems/design-phone-directory/) :lock: | Medium | 4/10 | 53.2% | [ ] |

## game_board_simulation

**What it is** — This pattern simulates state changes on a bounded 2D grid or board over a sequence of moves or turns, typically requiring efficient win-condition checking or collision detection. Recognize it when there is a grid with discrete positions, turns/moves, and a victory or failure condition.

**Common steps**
1. Represent the board state: a 2D array for cell contents, plus per-row, per-column, and per-diagonal counters for fast win detection.
2. On each `move(row, col, player)`: update the cell, increment the corresponding row/col/diagonal counters for that player.
3. Check win condition after each move: if any counter reaches the board size N, the current player wins.
4. For movement-based games (Snake): use a deque to represent the snake body — append head at front, pop tail when not eating food.
5. Maintain a set of food positions or occupied cells for O(1) collision detection.

**Key variations**
- Static placement game with win condition (Tic-Tac-Toe: check row/col/diagonal sums) vs. continuous movement game (Snake: deque for body, collision against walls and self).
- Fixed small board vs. parameterized N×N board.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 348 | [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/) :lock: | Medium | 4/10 | 58.8% | [ ] |
| 353 | [Design Snake Game](https://leetcode.com/problems/design-snake-game/) :lock: | Medium | 5/10 | 40.0% | [ ] |

## circular_buffer_design

**What it is** — This pattern implements a fixed-capacity queue or deque backed by a pre-allocated array, using head and tail pointers that wrap around using modular arithmetic. Recognize it when a problem asks for a queue with bounded capacity and O(1) enqueue/dequeue from one or both ends.

**Common steps**
1. Allocate an array of size `capacity` and initialize `head = 0`, `tail = 0`, `size = 0`.
2. For `enqueue` (rear): place the element at `tail`, then advance `tail = (tail + 1) % capacity`, increment `size`.
3. For `dequeue` (front): read element at `head`, advance `head = (head + 1) % capacity`, decrement `size`.
4. For deque operations (front insert): move head backward `head = (head - 1 + capacity) % capacity` before placing element.
5. Use `size == 0` for empty check and `size == capacity` for full check; avoid conflating head == tail for both states.
6. For Front Middle Back Queue: maintain two halves using two deques, rebalancing after each operation to keep sizes equal (or left one larger by at most one).

**Key variations**
- Single-ended circular queue (Design Circular Queue) vs. double-ended (Design Circular Deque).
- Middle-access queue (Design Front Middle Back Queue) requires two deques and a rebalancing step after each push/pop.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 622 | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | Medium | 4/10 | 54.6% | [ ] |
| 641 | [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) | Medium | 5/10 | 64.7% | [ ] |
| 1670 | [Design Front Middle Back Queue](https://leetcode.com/problems/design-front-middle-back-queue/) | Medium | 5/10 | 57.9% | [ ] |

## string_serialization

**What it is** — This pattern encodes a list of strings (or other data) into a single flat string and decodes it back losslessly, requiring a self-delimiting format that handles arbitrary characters including the delimiter itself. Recognize it when a problem asks you to design encode/decode functions that must survive round-trips through a medium that only accepts a single string.

**Common steps**
1. Choose an encoding scheme: length-prefix (store `len#data` for each string) or escape-based (escape any occurrence of the delimiter in data).
2. For encoding: for each string, write its length, a separator character (e.g., `#`), and then the raw string bytes.
3. For decoding: read characters until the separator, parse the length, then slice exactly that many characters as the next string; repeat.
4. Ensure the scheme handles empty strings and strings containing the separator character correctly.
5. For encryption variants: use a prebuilt lookup table and handle ambiguous multi-character mappings with backtracking or a trie.

**Key variations**
- Simple lossless codec (Encode and Decode Strings: length-prefix removes ambiguity entirely) vs. encryption with collision handling (Encrypt and Decrypt Strings: multiple plaintexts may map to the same ciphertext, requiring counting all possibilities).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) :lock: | Medium | 4/10 | 51.5% | [ ] |
| 2227 | [Encrypt and Decrypt Strings](https://leetcode.com/problems/encrypt-and-decrypt-strings/) | Hard | 7/10 | 38.3% | [ ] |

## binary_search_on_versioned_data

**What it is** — This pattern stores a history of (timestamp, value) pairs per key and uses binary search to answer range or point queries efficiently. Recognize it when a problem involves timestamped writes and asks for the most recent value at or before a given time, or for aggregate counts over a time range.

**Common steps**
1. Use a `defaultdict(list)` mapping each key to a sorted list of `(timestamp, value)` pairs.
2. On each `set` or `record` call, append `(timestamp, value)` to the key's list (timestamps are guaranteed non-decreasing, so the list stays sorted automatically).
3. On each `get` or `query` call, use `bisect_right(timestamps_list, target_time) - 1` to find the index of the largest timestamp ≤ target.
4. If the index is -1, no valid entry exists; otherwise return the value at that index.
5. For range-count queries (Range Frequency Queries, Tweet Counts), use `bisect_right(end) - bisect_left(start)` to count entries in a window.
6. For snapshot arrays (Snapshot Array): treat each `snap_id` as a timestamp; store per-index histories and binary-search on snap_id at query time.

**Key variations**
- Point query (most recent value ≤ T) vs. range count (how many events in [T1, T2]).
- Per-key history (Time Based Key-Value Store) vs. per-index snapshot history (Snapshot Array).
- Fixed-frequency bucketing (Tweet Counts: bucket by hour/day/minute) vs. exact timestamp lookup.
- Majority element verification over ranges (Online Majority Element): binary search to count occurrences, then verify the candidate exceeds half the range length.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2080 | [Range Frequency Queries](https://leetcode.com/problems/range-frequency-queries/) | Medium | 4/10 | 42.9% | [ ] |
| 981 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | 5/10 | 49.9% | [ ] |
| 1348 | [Tweet Counts Per Frequency](https://leetcode.com/problems/tweet-counts-per-frequency/) | Medium | 5/10 | 46.1% | [ ] |
| 3709 | [Design Exam Scores Tracker](https://leetcode.com/problems/design-exam-scores-tracker/) | Medium | 6/10 | 44.1% | [ ] |
| 3508 | [Implement Router](https://leetcode.com/problems/implement-router/) | Medium | 6/10 | 39.1% | [ ] |
| 1146 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | 6/10 | 36.7% | [ ] |
| 1157 | [Online Majority Element In Subarray](https://leetcode.com/problems/online-majority-element-in-subarray/) | Hard | 8/10 | 40.3% | [ ] |

## tree_structure_design

**What it is** — This pattern implements operations on an explicit tree (parent-child relationships stored as a graph) supporting queries like "find ancestor," "lock/unlock a node," or "find subtree members." Recognize it when nodes have parent pointers and operations must propagate up or down the tree.

**Common steps**
1. Build an adjacency list for children and a parent map from the input.
2. On lock/unlock: check all ancestors (walk up via parent map) for conflicts, then check all descendants (BFS/DFS down via children map).
3. Use a set to track locked nodes for O(1) membership checks.
4. For subtree queries, perform BFS/DFS from the target node using the children adjacency list.
5. Return results based on whether the operation is valid (no conflicts in ancestors or descendants).

**Key variations**
- Lock/unlock with conflict detection requires both upward (ancestor) and downward (descendant) traversal.
- Read-only subtree queries (sum, count) vs. write operations that modify state along the path.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1993 | [Operations on Tree](https://leetcode.com/problems/operations-on-tree/) | Medium | 6/10 | 45.2% | [ ] |

## bitset_design

**What it is** — This pattern implements a fixed-size bit array supporting bulk operations (flip all bits, set/unset individual bits, count set bits) in O(1) or O(n/64) time using lazy flags to avoid iterating every bit. Recognize it when a problem asks you to design a structure with a "flip all" or "complement" operation alongside individual bit reads/writes.

**Common steps**
1. Store the bits in an array (list of booleans or integers) of size `size`.
2. Maintain a `flipped` boolean flag to represent a global complement without touching every element.
3. On `flip(idx)`: toggle `arr[idx]`; on `flipAll()`: toggle the `flipped` flag and swap your `count` to `size - count`.
4. On `get(idx)`: return `arr[idx] XOR flipped` to account for the global flip.
5. Track `count` (number of 1s in the logical view) as a running variable, updating it on each individual set/unset/flip operation.
6. For `toString()`: iterate all indices and apply the XOR with the flipped flag.

**Key variations**
- Single bulk flip flag (Design Bitset) is the primary variation; more advanced problems might support range flips requiring a segment tree or BIT instead of a single flag.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2166 | [Design Bitset](https://leetcode.com/problems/design-bitset/) | Medium | 6/10 | 32.7% | [ ] |

## interval_management

**What it is** — This pattern maintains a dynamic set of intervals, supporting insertion of new intervals and queries about overlap, coverage, or optimal placement. Recognize it when a problem involves booking time ranges, seating positions, or merging incoming segments into a canonical disjoint-interval representation.

**Common steps**
1. Store intervals in a sorted structure (sorted list, balanced BST via `SortedList`, or just a list that you keep sorted).
2. On `add(start, end)`: find all existing intervals that overlap with or are adjacent to [start, end] using binary search on start points.
3. Merge overlapping intervals: the new interval's merged start = min(start, overlapping_start), merged end = max(end, overlapping_end); remove the absorbed intervals.
4. Insert the merged interval back into the sorted structure.
5. For booking/conflict detection (My Calendar II): maintain a second list of "double-booked" regions; a new booking is invalid if it overlaps any double-booked region.
6. For seat placement (Exam Room): track gaps between seated neighbors and always pick the gap that maximizes the minimum distance.

**Key variations**
- Merge-only stream (Data Stream as Disjoint Intervals: always merge, answer total coverage queries).
- Overlap-level counting (My Calendar II: allow up to 2 overlaps, reject on 3rd).
- Optimal placement under a distance metric (Exam Room: always seat at the midpoint of the largest gap).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 731 | [My Calendar II](https://leetcode.com/problems/my-calendar-ii/) | Medium | 5/10 | 63.1% | [ ] |
| 352 | [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) | Hard | 7/10 | 60.1% | [ ] |
| 855 | [Exam Room](https://leetcode.com/problems/exam-room/) | Medium | 7/10 | 43.4% | [ ] |

## randomized_data_structure

**What it is** — This pattern combines a hash map with an array to achieve O(1) insert, delete, and uniform random access — operations that no single standard structure supports simultaneously. Recognize it when a problem requires all three: add, remove, and getRandom in O(1).

**Common steps**
1. Maintain a list (`arr`) for index-based random access and a dict (`idx_map`) mapping value → index in the list.
2. On `insert(val)`: if val not in map, append to list and store its index in the map.
3. On `remove(val)`: to avoid O(n) list deletion, swap val with the last element in the list, update the last element's index in the map, pop the list's last element, and remove val from the map.
4. On `getRandom()`: return `arr[random.randint(0, len(arr) - 1)]`.
5. For duplicates allowed: map each value to a **set** of indices rather than a single index; on removal, pick any index from the set to swap.

**Key variations**
- No duplicates (Insert Delete GetRandom O(1): map value → single index) vs. duplicates allowed (variant: map value → set of indices).
- Sparse matrix random flip (Random Flip Matrix): treat the unfilled cells as a virtual array and use a remapping dict to handle swaps in a huge sparse space without allocating the full matrix.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 380 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | 5/10 | 55.4% | [ ] |
| 519 | [Random Flip Matrix](https://leetcode.com/problems/random-flip-matrix/) | Medium | 6/10 | 45.8% | [ ] |
| 381 | [Insert Delete GetRandom O(1) - Duplicates allowed](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) | Hard | 8/10 | 36.6% | [ ] |

## heap_with_hashmap

**What it is** — This pattern uses a heap (priority queue) for efficient min/max access and a hash map for O(1) lookup and index tracking, enabling structures that need both ranked access and keyed retrieval. Recognize it when a problem requires "get the top-ranked item" alongside "update or delete a specific item by key."

**Common steps**
1. Maintain a min-heap (or max-heap via negation) of `(priority, key)` tuples for ordered access.
2. Maintain a dict mapping `key → current priority` for O(1) lookups and validity checks.
3. Use **lazy deletion**: when a priority changes, push the new `(priority, key)` onto the heap without removing the old entry. Mark old entries as stale by comparing heap top's priority to the dict.
4. On `pop` / `top`: skip and discard any heap entry where `heap[0].priority != dict[key]` (stale entry).
5. For multi-attribute ranking (Design Twitter, Food Rating System): use tuples `(-priority, name, key)` to encode tiebreaking directly in heap comparison.
6. For "all items at the same priority" queries: maintain a secondary dict `priority → set of keys`.

**Key variations**
- Single scalar priority (Smallest Number in Infinite Set, Stock Price Fluctuation) vs. multi-attribute priority with tiebreaking (Design Twitter: most recent, Food Rating: alphabetical name).
- Updates to existing keys require lazy deletion (push new entry, ignore stale pops) unless you can afford rebuilding the heap.
- Some problems need both a min-heap and a max-heap simultaneously (Stock Price Fluctuation: track both min and max prices).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2336 | [Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set/) | Medium | 4/10 | 70.6% | [ ] |
| 3391 | [Design a 3D Binary Matrix with Efficient Layer Tracking](https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/) :lock: | Medium | 5/10 | 66.2% | [ ] |
| 2349 | [Design a Number Container System](https://leetcode.com/problems/design-a-number-container-system/) | Medium | 5/10 | 57.1% | [ ] |
| 2353 | [Design a Food Rating System](https://leetcode.com/problems/design-a-food-rating-system/) | Medium | 5/10 | 52.9% | [ ] |
| 2034 | [Stock Price Fluctuation ](https://leetcode.com/problems/stock-price-fluctuation/) | Medium | 6/10 | 49.0% | [ ] |
| 3408 | [Design Task Manager](https://leetcode.com/problems/design-task-manager/) | Medium | 6/10 | 48.9% | [ ] |
| 355 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | 6/10 | 44.6% | [ ] |
| 3815 | [Design Auction System](https://leetcode.com/problems/design-auction-system/) | Medium | 6/10 | 42.1% | [ ] |
| 1500 | [Design a File Sharing System](https://leetcode.com/problems/design-a-file-sharing-system/) :lock: | Medium | 6/10 | 41.7% | [ ] |
| 2254 | [Design Video Sharing Platform](https://leetcode.com/problems/design-video-sharing-platform/) :lock: | Hard | 7/10 | 64.1% | [ ] |
| 2102 | [Sequentially Ordinal Rank Tracker](https://leetcode.com/problems/sequentially-ordinal-rank-tracker/) | Hard | 7/10 | 61.4% | [ ] |
| 1912 | [Design Movie Rental System](https://leetcode.com/problems/design-movie-rental-system/) | Hard | 8/10 | 62.3% | [ ] |
| 716 | [Max Stack](https://leetcode.com/problems/max-stack/) :lock: | Hard | 8/10 | 46.0% | [ ] |
| 1172 | [Dinner Plate Stacks](https://leetcode.com/problems/dinner-plate-stacks/) | Hard | 8/10 | 33.6% | [ ] |
| 1825 | [Finding MK Average](https://leetcode.com/problems/finding-mk-average/) | Hard | 9/10 | 38.7% | [ ] |

## cache_design

**What it is** — This pattern implements a bounded cache that evicts entries according to a policy (Least Recently Used or Least Frequently Used) when capacity is exceeded. Recognize it when a problem asks for O(1) get and put with an eviction policy based on access history.

**Common steps**
1. Use an `OrderedDict` (Python) or a doubly-linked list + hash map to track access order in O(1).
2. On `get(key)`: if key exists, move it to the "most recently used" end and return its value; otherwise return -1.
3. On `put(key, value)`: if key exists, update its value and move it to the MRU end. If key is new and cache is at capacity, evict the LRU entry (the front/tail of the ordered structure), then insert the new entry at the MRU end.
4. For LFU: also maintain a `freq → doubly-linked list` map and track the current minimum frequency. On each access, move the key from its current frequency bucket to the `freq + 1` bucket and update min_freq accordingly.
5. Always update `min_freq = 1` on a fresh `put` for LFU.

**Key variations**
- LRU (evict least recently accessed): one `OrderedDict` suffices, ordering by recency.
- LFU (evict least frequently accessed, with recency as tiebreaker): requires both a `key → freq` map and a `freq → OrderedDict` map, plus a `min_freq` variable.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | 6/10 | 47.3% | [ ] |
| 460 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | 8/10 | 49.1% | [ ] |

## graph_shortest_path_design

**What it is** — This pattern designs a graph data structure that supports dynamic edge additions and on-demand shortest-path queries, typically using Dijkstra's algorithm run at query time. Recognize it when a problem asks you to build a weighted directed graph with an `addEdge` method and a `shortestPath` query.

**Common steps**
1. Store the graph as an adjacency list: `dict[node] = list of (neighbor, weight)` pairs.
2. On `addEdge(u, v, w)`: append `(v, w)` to `adj[u]`.
3. On `shortestPath(src, dst)`: run Dijkstra from `src` using a min-heap of `(dist, node)`.
4. Maintain a `dist` array initialized to infinity; set `dist[src] = 0` and push `(0, src)` onto the heap.
5. Pop the minimum-distance node, skip if already finalized, otherwise relax all its outgoing edges and push updated distances.
6. Return `dist[dst]` if reached, else -1.

**Key variations**
- Single query per call (run full Dijkstra each time) vs. multiple queries (consider caching or preprocessing with all-pairs shortest paths if the graph is small).
- Directed vs. undirected edges; presence of negative weights would require Bellman-Ford instead of Dijkstra.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2642 | [Design Graph With Shortest Path Calculator](https://leetcode.com/problems/design-graph-with-shortest-path-calculator/) | Hard | 7/10 | 65.1% | [ ] |

## spreadsheet_formula_design

**What it is** — This pattern implements a spreadsheet where cells hold either literal values or formulas referencing other cells, requiring dependency tracking and propagation when a cell's value changes. Recognize it when a problem has cells that reference each other and asks you to evaluate or sum cell values.

**Common steps**
1. Store a `values` dict mapping cell name → current integer value.
2. For formula cells: store the formula (list of contributing cells and ranges) separately.
3. On `set(cell, value)`: update the cell's stored value directly; if any other cell's formula references this cell, recompute those cells (dependency propagation).
4. On `get(cell)`: return the stored value; if it's a formula cell, sum up all referenced cells' current values.
5. For circular dependency detection: do a DFS to check if setting a cell would create a cycle before committing the change.
6. Use topological ordering to recompute all dependent cells in the correct order after an update.

**Key variations**
- Simple value storage with range sums (Design Spreadsheet: no circular refs, direct lookup) vs. full formula evaluation with dependency graphs and cycle detection (Design Excel Sum Formula: recursive DFS recomputation).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3484 | [Design Spreadsheet](https://leetcode.com/problems/design-spreadsheet/) | Medium | 5/10 | 74.2% | [ ] |
| 631 | [Design Excel Sum Formula](https://leetcode.com/problems/design-excel-sum-formula/) :lock: | Hard | 9/10 | 39.8% | [ ] |

## sqrt_decomposition_design

**What it is** — This pattern divides a sequence into blocks of size √n, maintaining each block in a structure that supports O(√n) insert, delete, and rank queries — useful when you need faster-than-O(n) operations that a simple array can't provide but don't need the full complexity of a balanced BST. Recognize it when a problem requires moving elements to the front/back while also supporting positional access.

**Common steps**
1. Divide the sequence into blocks of size √n; store each block as a sorted list or deque.
2. On `fetch(k)` (bring element at position k to the front): find which block contains position k by iterating block sizes, remove the element from that block, and prepend it to the first block.
3. After each insertion into the first block, rebalance: if any block exceeds 2√n in size, split it; if adjacent blocks are both under √n/2, merge them.
4. On `get(k)`: compute the global position by summing block sizes and indexing into the correct block.
5. Keep block sizes roughly equal to maintain O(√n) per operation across all n operations.

**Key variations**
- MRU queue (Design Most Recently Used Queue: fetch + move-to-front) is the primary application; more general √-decomposition problems may support insertions/deletions anywhere.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1756 | [Design Most Recently Used Queue](https://leetcode.com/problems/design-most-recently-used-queue/) :lock: | Medium | 7/10 | 78.3% | [ ] |

## frequency_tracking_data_structure

**What it is** — This pattern maintains a running count of how often each element has been seen and answers queries about elements with specific frequencies (the most frequent, all at min frequency, first unique, etc.) in O(1) time. Recognize it when a problem streams elements and asks you to retrieve items by their occurrence count at any moment.

**Common steps**
1. Maintain a `freq` dict mapping element → current count.
2. Maintain a `group` dict (or list of sets) mapping count → set/ordered-set of elements with that count.
3. Track `max_freq` (or `min_freq`) as a running variable updated on each insert.
4. On `push(val)`: increment `freq[val]`, move val from `group[old_freq]` to `group[new_freq]`, update `max_freq` if needed.
5. On `pop()`: retrieve any element from `group[max_freq]`; decrement its count and move it to `group[max_freq - 1]`; if `group[max_freq]` becomes empty, decrement `max_freq`.
6. For "first unique" queries: also maintain an insertion-order structure (deque or linked list) per frequency bucket so you can retrieve the oldest element at a given frequency.

**Key variations**
- Max frequency stack with recency tiebreak (Maximum Frequency Stack: among all elements at max freq, return most recently pushed — use a stack per frequency).
- First unique number (First Unique Number: return the oldest element with frequency exactly 1 — use a deque to track insertion order alongside freq dict).
- All O(1) operations on any key (All O`one Data Structure: increment/decrement any key's count and retrieve min/max count keys — use a doubly-linked list of frequency nodes).
- Full statistics tracking (Design an Array Statistics Tracker: maintain min, max, mean, median, mode simultaneously — requires multiple structures).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1429 | [First Unique Number](https://leetcode.com/problems/first-unique-number/) :lock: | Medium | 6/10 | 57.5% | [ ] |
| 895 | [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) | Hard | 7/10 | 66.8% | [ ] |
| 432 | [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) | Hard | 8/10 | 44.2% | [ ] |
| 3369 | [Design an Array Statistics Tracker ](https://leetcode.com/problems/design-an-array-statistics-tracker/) :lock: | Hard | 9/10 | 35.7% | [ ] |

## skiplist_design

**What it is** — This pattern implements a skip list: a probabilistic layered linked list where each node appears in successively sparser "express lanes," enabling O(log n) average-case search, insert, and delete without the rotations required by balanced BSTs. Recognize it when a problem asks you to implement a sorted dynamic set with all three operations from scratch.

**Common steps**
1. Define a `Node` class with a `val` field and a `next` list of length `level`, where `next[i]` points to the next node at level i.
2. Initialize a sentinel `head` node at the maximum level with val = -infinity; `MAX_LEVEL` is typically 16–32 and `P = 0.5`.
3. For `search(target)`: start at `head` at the top level; at each level, advance forward while `curr.next[level].val < target`; drop down a level when you can't advance; return true if `curr.next[0].val == target`.
4. For `add(num)`: do the same traversal but record the last node visited at each level in an `update[]` array. Randomly generate a new node's level (`randomLevel()`). Create the new node and splice it in at each level using `update[i]`.
5. For `erase(num)`: find `update[]` as in add, verify the target exists at level 0, then unlink it from each level where it appears.
6. `randomLevel()`: start at 1, keep incrementing while `random() < P` and level `< MAX_LEVEL`.

**Key variations**
- Standard skip list with duplicates allowed vs. set semantics (erase only one copy).
- Level probability P and MAX_LEVEL choices affect constant factors but not asymptotic complexity.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1206 | [Design Skiplist](https://leetcode.com/problems/design-skiplist/) | Hard | 8/10 | 59.6% | [ ] |
