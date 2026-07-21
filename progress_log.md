# Progress Log

Daily journal of problems solved, learnings, and next steps.

---

## 2026-07-08 — Day 1

**Problems solved: 3**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| 1 | Contains Duplicate (#217) | Hashing | set_lookup | 9/10 |
| 2 | Valid Anagram (#242) | Hashing | frequency_counting | 4/10 |
| 3 | Two Sum (#1) | Hashing | two_sum_pair | 2/10 |

**Python syntax mistakes to remember:**
- `ord(c)` converts character → integer (`ord('a') == 97`). `chr(n)` is the reverse (integer → character). Used `chr` when you needed `ord` in Valid Anagram
- `i += 1` increments. `i=+1` just sets i to 1 every time — NOT the same thing
- `enumerate(nums)` gives `(index, value)` pairs — use this instead of tracking `i` manually

**Patterns learned:**
- set_lookup: `seen = set()` → `if x in seen: return True` → `seen.add(x)`
- frequency_counting: 26-slot array (`ord(c) - 97` as index), or just `Counter(s) == Counter(t)`
- two_sum_pair: single-pass hashmap — store `{num: index}`, check if complement exists before adding

---

## 2026-07-09 — Day 2

**Problems solved: 3**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| 4 | Group Anagrams (#49) | Hashing | grouping_by_key | 5/10 |
| 5 | Top K Frequent Elements (#347) | Hashing | top_k_frequent | 3/10 |
| 6 | Product of Array Except Self (#238) | Arrays | prefix_suffix_products | 4/10 |

**Python learned:**
- `defaultdict(list)` — auto-creates empty list for new keys, no need to check `if key in d`
- Don't shadow built-ins: avoid naming variables `map`, `str`, `list`
- `[[] for _ in range(n)]` — list of empty lists (bucket array)
- `heapq.nlargest(k, iterable, key=lambda x: count[x])` — top k by custom key

**Patterns learned:**
- grouping_by_key: `"".join(sorted(word))` as key, `defaultdict(list)` to group
- top_k_frequent: bucket sort — use frequency as index, read buckets high to low → O(n)
- prefix_suffix_products: two passes — right to left stores suffix, left to right multiplies in prefix. Reset `a=1` between passes, use `*=` not `=`

---

## 2026-07-10 — Day 3

**Reviews: 2**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | Two Sum (#1) | Hashing | two_sum_pair | 6/10 |
| R | Top K Frequent Elements (#347) — bucket sort | Hashing | top_k_frequent | 4/10 |

**Notes:**
- Two Sum: still using `num != target-num` guard — drop it. Single-pass handles duplicates naturally
- Top K Frequent: needed full solution shown — bucket sort not internalized yet, on review for 2026-07-17
- Two Sum review (2026-07-17): 8/10 — pattern solid, review due 2026-07-31
- Top K Frequent review (2026-07-17): 8/10 — bucket sort clicked on second attempt, review due 2026-08-17
- Valid Sudoku review (2026-07-17): 8/10 — recurring bugs: init sets inside loop, checking list not set[i]; final solve clean
- Longest Consecutive Sequence review (2026-07-17): pending

---

## 2026-07-17 — Day 6

**Reviews: 3 | New: 1**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | Two Sum (#1) | Hashing | two_sum_pair | 8/10 |
| R | Top K Frequent Elements (#347) | Hashing | top_k_frequent | 8/10 |
| R | Valid Sudoku (#36) | Hashing | multi_set_validation | 8/10 |
| 16 | Longest Substring Without Repeating Characters (#3) | Sliding Window | sliding_window_set | 5/10 |

**Notes:**
- Two Sum: first attempt used list instead of dict; second attempt clean single-pass hashmap
- Top K Frequent: bucket indexing wrong on first attempt; clicked on second attempt
- Valid Sudoku: recurring bug — init sets inside loop and checking list not set[i]; clean after guidance
- Longest Substring: two pointer approach on first attempt (wrong); sliding window clean on second attempt

---

## 2026-07-18 — Day 7

**Reviews**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | Valid Anagram (#242) | Hashing | frequency_counting | 6/10 |
| R | Group Anagrams (#49) | Hashing | grouping_by_key | 10/10 |
| R | Longest Consecutive Sequence (#128) | Hashing | consecutive_sequence | 9/10 |

**Notes:**
- Valid Anagram: approach correct (26-slot array); syntax bugs — `[0].len(26)` → `[0]*26`, `i-'a'` → `ord(i)-ord('a')`
- Group Anagrams: clean first attempt — 10/10
- Longest Consecutive Sequence: infinite loop on first attempt (num not moving); clean on second attempt — 9/10

---

## 2026-07-20 — Day 8

**New: 1**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| 17 | Longest Repeating Character Replacement (#424) | Sliding Window | sliding_window_freq | 3/10 |
| 18 | Permutation in String (#567) | Sliding Window | fixed_window_freq | 6/10 |
| 19 | Minimum Window Substring (#76) | Sliding Window | sliding_window_counter | 5/10 |
| 20 | Valid Parentheses (#20) | Stack | stack_matching | 9/10 |
| 21 | Min Stack (#155) | Stack | two_stack_min | 9/10 |
| 22 | Evaluate Reverse Polish Notation (#150) | Stack | stack_eval | 10/10 |

**Notes:**
- Longest Repeating Character Replacement: first attempt copied solution; second attempt from memory — window length `r-l` should be `r-l+1`, `count.values()+1` is wrong — should be `max(count.values())`
- Key formula: `(r - l + 1) - max(count.values()) > k` → window invalid
- Permutation in String: first attempt wrong window logic; understood fixed-window pattern after walkthrough — 6/10
- Minimum Window Substring: multiple attempts — order of ops in while loop was key. Pattern: sliding window with two Counters, track `have` vs `need`. Expand right until all chars satisfied, then trim from left until a required char drops below needed count, recording min window each time before trimming.
- Valid Parentheses: multiple attempts — bidirectional dict caused bugs; fixed with opening→closing dict and looking up `res[r[-1]]` not `res[c]`
- Min Stack: first attempt had indentation/self bugs; second attempt clean — push min to minStack every time, pop both stacks together

---

## 2026-07-13 — Day 4

**Reviews: 1 | New: 1**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | Product of Array Except Self (#238) | Arrays | prefix_suffix_products | 5/10 |
| 7 | Longest Consecutive Sequence (#128) | Hashing | consecutive_sequence | 8/10 |

**Notes:**
- Product of Array Except Self: remembered two-pass structure; bug was `=` instead of `*=` in second pass
- Longest Consecutive Sequence: took 3 attempts — fixed set syntax and variable names on attempt 2, added start-of-sequence guard and `length=1` on attempt 3; clean solve
- Key pattern: `if (i-1) in a: continue` skips non-starts → keeps it O(n). Extend rightward with `while (i+1) in a`

---

## 2026-07-14 — Day 5

**New: 2**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| 8 | Valid Sudoku (#36) | Hashing | multi_set_validation | incomplete — queued for review |
| 9 | Encode and Decode Strings (#271) | Hashing | length_prefix_encoding | 8/10 |
| 10 | Valid Palindrome (#125) | Two Pointers | two_pointer_inward | 9/10 |
| 11 | Two Sum II (#167) | Two Pointers | two_pointer_inward | 8/10 |
| 12 | 3Sum (#15) | Two Pointers | two_pointer_inward | 7/10 |
| 13 | Container With Most Water (#11) | Two Pointers | two_pointer_inward | 10/10 |
| 14 | Best Time to Buy and Sell Stock (#121) | Sliding Window | min_tracking | 7/10 |
| 15 | Longest Substring Without Repeating Characters (#3) | Sliding Window | sliding_window_set | 5/10 |

**Notes:**
- Valid Sudoku: understood structure but didn't complete — review 2026-07-17
- Encode and Decode: encode clean; decode had one bug (`s[i]` instead of `s[j]` in inner while loop)
- Valid Palindrome (#125): first attempt had inverted isalnum logic; second attempt clean 9/10
- Two Sum II (#167): first attempt used binary search (too complex); second attempt two pointers clean, one typo `j-=i` vs `j-=1` → 8/10
- 3Sum (#15): took 3 attempts — missing two-pointer loop, then missing dup skip after match; final solve clean 7/10
- Container With Most Water (#11): first attempt infinite loop on equal heights; second attempt clean 10/10
