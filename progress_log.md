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

## Problems to redo
- Move Zeroes (#283) — review done 2026-05-11
