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

**Notes:**
- Valid Sudoku: understood structure but didn't complete — review 2026-07-17
- Encode and Decode: encode clean; decode had one bug (`s[i]` instead of `s[j]` in inner while loop)
- Valid Palindrome (#125): first attempt had inverted isalnum logic; second attempt clean 9/10
- Two Sum II (#167): first attempt used binary search (too complex); second attempt two pointers clean, one typo `j-=i` vs `j-=1` → 8/10
