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
