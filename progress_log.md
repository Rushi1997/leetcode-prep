# Progress Log

Daily journal of problems solved, learnings, and next steps.

---

## 2026-09-23 — Day 16

**Reviews: 5**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | Maximum Depth of Binary Tree (#104) | Trees | tree_recursion | 5/10 |
| R | Merge Two Sorted Lists (#21) | Linked List | merge_sorted_lists | 5/10 |
| R | Time Based Key-Value Store (#981) | Binary Search | binary_search_timemap | 4/10 |
| R | Diameter of Binary Tree (#543) | Trees | tree_recursion | 4/10 |
| R | Balanced Binary Tree (#110) | Trees | tree_recursion | 4/10 |

**Notes:**
- Maximum Depth: first attempt used a fundamentally wrong iterative traversal — an inner `while temp.left` loop walked straight down the left spine, and the `temp.right` check only fired once on whatever node that loop stopped at, so right subtrees of the root and every intermediate node were silently skipped entirely (confirmed wrong on a right-heavy counterexample: returned 2 instead of true depth 4). Second attempt restructured to push both children per node, but the two `elif` branches for single-child nodes still checked the wrong condition (presence instead of absence), so any node with exactly one child matched no branch and got truncated like a leaf (a pure left chain of 5 nodes returned 1 instead of 5) — also had a leftover `stack.left` typo instead of `temp.left`, and no `root is None` guard. Third attempt fixed all three cleanly — verified against a left-only chain, a right-heavy tree, and a balanced tree — 5/10
- Merge Two Sorted Lists: first attempt's two `elif` branches for "one list exhausted" required both lists truthy (contradicting the point of being an elif after the both-non-None `if` already failed) — dead code, and the bodies also attached the wrong list. Second attempt changed `elif` to `if` without fixing the conditions, so the "one list remains" check (still just testing truthiness of both) fired on nearly every iteration and returned after merging only 1-2 nodes, discarding the rest (confirmed: `[1,2,4]`+`[1,3,4]` returned `[1,3,4]`). Third attempt fixed both the mutual exclusivity (elif again) and the actual exhaustion conditions (`list1==None`/`list2==None`) — verified against `[1,2,4]`+`[1,3,4]` → `[1,1,2,3,4,4]` and `[5]`+`[1,2,3]` → `[1,2,3,5]` — 5/10
- Time Based Key-Value Store: needed the data-shape question walked through first (map key → list of `[timestamp, value]` pairs, naturally sorted since `set()` calls arrive in increasing timestamp order). Recurring bugs across ~4 attempts: `self.time` not used consistently (bare `time` referenced in method bodies, `NameError`), `dict.get[key]` (indexing a method instead of calling it), `list.add()` (sets have `.add()`, not lists), indexing a not-yet-created dict key in the `else` branch (`KeyError`) before switching to `self.time[key] = [[timestamp, value]]`. The `get()` binary search itself — "find the rightmost timestamp `<= target`" — needed the full pattern explained from scratch (track a `result` candidate, keep pushing `i` right on a match instead of stopping). Final version clean — verified against the classic `set/get` interleaving example, all outputs matched — 4/10
- Diameter of Binary Tree: first attempt reused the same broken leftmost-descent iterative shape from Maximum Depth (plus the `.add()` typo again), and — worse — the whole approach was conceptually wrong for diameter specifically: it tracked one accumulating path length instead of, at every node, independently summing left-subtree height + right-subtree height (proved with a tree where `d` overcounted to 6 against a true diameter of 4). Second attempt switched to recursion but had `height()` return total node count (`1+height(l)+height(r)`) instead of actual height, and only ever checked the sum at the root, missing diameters entirely inside a subtree (classic `[1,2,3,4,5]` example gave 4 instead of 3). Third attempt fixed the height formula (`1+max(l,r)`) but still only checked the root. Needed the "update a running max as a side effect on every recursive call" pattern explained directly before the final attempt got both pieces right — verified against `[1,2,3,4,5]`→3 and a tree whose diameter doesn't pass through the root→4. Also relies on `d` being a class attribute reset fresh per LeetCode judge instantiation rather than resetting `self.d=0` explicitly inside the method — works under LeetCode's per-test-case instantiation but is fragile if the instance were reused — 4/10
- Balanced Binary Tree: first attempt had a nested `height()` function wrongly declared with a `self` param (crashes on call), referenced `self.d` without ever setting it, reassigned an unconnected local `d` inside the nested scope, and used the wrong height formula (`1+(l+r)`). Second attempt fixed all the syntax but reintroduced a subtler version of the Diameter bug: `self.d = abs(r-l)` is a plain overwrite, and since recursion is post-order, the root's own assignment always runs last and clobbers every descendant's check — functionally identical to only ever checking the root, so a tree balanced at the root but unbalanced several levels down would wrongly return `True`. Needed the fix pattern (seed `self.balanced = True`, only ever flip it to `False`, never overwrite back) given directly before the third attempt landed clean — verified against `[1,2,2,3,3,null,null,4,4]`→False and `[3,9,20,null,null,15,7]`→True — 4/10

## 2026-09-23 — Day 15

**Reviews: 3**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | Container With Most Water (#11) | Two Pointers | two_pointer_inward | 7/10 |
| R | Reverse Linked List (#206) | Linked List | reverse_linked_list | 6/10 |
| R | Invert Binary Tree (#226) | Trees | tree_traversal | 6/10 |

**Notes:**
- Container With Most Water: first attempt missed the core two-pointer-inward setup — started `i,j=0,1` (adjacent) instead of opposite ends, called `height(i)` instead of indexing `height[i]`, and passed a single product into `min()` instead of `min(height[i], height[j])`. Second attempt fixed all three cleanly: pointers start at both ends, correct indexing, moves the shorter side inward. Verified against `[1,8,6,2,5,4,8,3,7]` → 49 — 7/10
- Reverse Linked List: first attempt used `&` instead of `and` in the loop condition (crashes — `&` binds tighter than `!=`, so it tries `None & ListNode`), plus the condition also required `curr.next != None`, which dropped the last node from ever being relinked. Also left a dead, broken `swap` method above the real solution. Second attempt clean: `while curr != None`, correct pointer relinking, dead code removed. Traced `1->2->3->None` → `3->2->1->None` — 6/10
- Invert Binary Tree: first attempt (iterative, stack-based) had `.app()`/`.add()` instead of `.append()`, `while stack != None` (never terminates — a list is never literally `None`), backwards `elif` conditions (checked for the sibling child's presence instead of its absence), and `return head` referencing an undefined variable. Second attempt fixed all five cleanly — verified on a 5-node tree, inversion matched exactly, and it even handles the empty-tree case safely by accident of the loop structure — 6/10

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

## 2026-07-21 — Day 9

**Reviews**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | 3Sum (#15) | Two Pointers | two_pointer_inward | 9/10 |
| 23 | Generate Parentheses (#22) | Stack/Backtracking | backtracking | 5/10 |
| 24 | Daily Temperatures (#739) | Stack | monotonic_stack | 10/10 |
| 25 | Car Fleet (#853) | Stack | monotonic_stack | 10/10 |
| 26 | Binary Search (#704) | Binary Search | binary_search | 10/10 |
| 27 | Search a 2D Matrix (#74) | Binary Search | binary_search_2d | 9/10 |
| 28 | Koko Eating Bananas (#875) | Binary Search | binary_search_answer | 5/10 |

**Notes:**
- 3Sum: first attempt missing inner while loop; second attempt clean — reset j=i+1, k=len-1 inside loop
- Generate Parentheses: multiple attempts — elif→if, close<open not close<target, pop() not remove(), pass [] not self.res; final solve clean 5/10
- Koko Eating Bananas: first attempt had `hours=` (overwrite) and `j=mid` (infinite loop); second attempt clean — binary search on answer not input

---

## 2026-08-01 — Day 11

**Reviews: 3 | New: TBD**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | Binary Search (#704) | Binary Search | binary_search | 10/10 |
| R | Valid Parentheses (#20) | Stack | stack_matching | 7/10 |
| R | Two Sum (#1) | Hashing | two_sum_pair | 10/10 |
| 31 | Time Based Key-Value Store (#981) | Binary Search | binary_search_timemap | 7/10 |
| 32 | Reverse Linked List (#206) | Linked List | reverse_linked_list | 8/10 |
| 33 | Merge Two Sorted Lists (#21) | Linked List | merge_sorted_lists | 8/10 |
| 34 | Reorder List (#143) | Linked List | reorder_linked_list | 7/10 |
| 35 | Remove Nth Node From End (#19) | Linked List | two_pointer_gap | 8/10 |
| 36 | Copy List with Random Pointer (#138) | Linked List | hashmap_deep_copy | 5/10 |
| 37 | Add Two Numbers (#2) | Linked List | linked_list_addition | 8/10 |
| 38 | Linked List Cycle (#141) | Linked List | fast_slow_pointer | 8/10 |
| 39 | Find the Duplicate Number (#287) | Linked List | fast_slow_pointer | 7/10 |
| 40 | LRU Cache (#146) | Linked List | doubly_linked_list_hashmap | 4/10 |
| 41 | Merge K Sorted Lists (#23) | Linked List | merge_k_lists | 8/10 |
| 42 | Invert Binary Tree (#226) | Trees | tree_traversal | 8/10 |
| 43 | Maximum Depth of Binary Tree (#104) | Trees | tree_recursion | 8/10 |
| 44 | Diameter of Binary Tree (#543) | Trees | tree_recursion | 8/10 |
| 45 | Balanced Binary Tree (#110) | Trees | tree_recursion | 8/10 |

**Notes:**
- Binary Search: perfect — clean `while i<=j`, correct boundary moves
- Valid Parentheses: logic correct, crashed on closing bracket with empty stack — fix: `if not r or res[r[-1]] != j`
- Two Sum: clean single-pass hashmap, 10/10
- Time Based Key-Value Store: needed design explained (per-key list of tuples, binary search on timestamp); wrote correct solution after walkthrough. Key: save candidate when `pairs[k][0]<=timestamp`, go right to find closer match
- Reverse Linked List: first attempt advanced `n=n.next` after overwriting `n.next` — lost the rest of the list. Fixed with `nxt=n.next` save before overwrite; also fixed `while n.next!=None` → `while n!=None`
- Merge Two Sorted Lists: first attempt used `new=None` (crash on `.next`) and typo `nex`. Fixed with dummy node pattern — `curr=ListNode(0)`, `new` walks forward, return `curr.next`
- Reorder List: 3-step structure right (find middle, reverse, merge). Bugs: even-length crash (`while jump.next` → `while jump and jump.next`), wrong split (`r=start` → `r=start.next`), cycle in merge (overwriting pointer before saving next). Fix: always save `nxt_temp` and `nxt_rev` before any pointer modification
- Remove Nth From End: shadowed parameter `n` with a node variable on first attempt. Fixed with dummy node — start `left` at dummy so it stops one before the target; `left.next=left.next.next` removes it
- Copy List with Random Pointer: needed concept explained (why can't return head, why need map). Two-pass hashmap — pass 1 creates all copies, pass 2 wires next+random using map[original]=copy lookup
- Add Two Numbers: in-place approach got complicated with unequal lengths + carry. Clean pattern: `while l1 or l2 or carry`, treat missing nodes as 0, build new list with `curr.next=ListNode(s%10)`
- Linked List Cycle: first used list (O(n²)) — should be set or two pointers. Rewrote with Floyd's algorithm: slow+fast, meet = cycle, fast hits None = no cycle. O(1) space
- Find the Duplicate Number: needed concept explained (array as linked list, duplicate = cycle entry). Phase 1: slow+fast meet inside cycle. Phase 2: reset slow to nums[0], move both 1 step until they meet = duplicate
- LRU Cache: needed full solution shown — recurring bugs: missing `self` on remove/insert, bare `map` instead of `self.map`, wrong eviction logic. Key: Node class outside LRUCache, head=LRU/tail=MRU dummies, evict head.next when over cap
- Merge K Sorted Lists: merge helper solid; bug was remaining-list attachment (start never advanced). Fixed with `start.next = l1 if l1 else l2; break`. mergeKLists: start with lists[0], merge each subsequent list into res
- Invert Binary Tree: overcomplicated first attempt (building new tree, wrong Null). Key: swap in-place unconditionally `node.left, node.right = node.right, node.left`, then push non-None children. Add `if not root: return None` guard
- Maximum Depth of Binary Tree: iterative stack-length approach wrong. Recursive pattern: `if not root: return 0; return 1 + max(left, right)` — ask each subtree for its depth, add 1
- Diameter of Binary Tree: dfs returns depth upward, updates self.res = max(self.res, left+right) at each node. Two things at once: depth for parent, diameter at current node
- Balanced Binary Tree: dfs returns height or -1. Base case returns 0 (not -1). Propagate -1 before abs check. `isBalanced` = `dfs(root) != -1`

---

## 2026-07-29 — Day 10

**Reviews: 3 | New: 1**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | Valid Palindrome (#125) | Two Pointers | two_pointer_inward | 9/10 |
| R | Evaluate Reverse Polish Notation (#150) | Stack | stack_eval | 7/10 |
| R | Daily Temperatures (#739) | Stack | monotonic_stack | 10/10 |
| 29 | Find Minimum in Rotated Sorted Array (#153) | Binary Search | binary_search_rotated | 6/10 |
| 30 | Search in Rotated Sorted Array (#33) | Binary Search | binary_search_rotated | 8/10 |

**Notes:**
- Valid Palindrome: first attempt had `!` instead of `not`, `s[f]` instead of `s[j]`, `return False` at end → fixed all three, second attempt clean
- Evaluate Reverse Polish Notation: `while i<j` missed last token (should be `while i<len(tokens)`), `stack.append(t)` pushed string not int — both needed pointing out; fixed cleanly
- Daily Temperatures: perfect first attempt — monotonic stack pattern fully internalized
- Find Minimum in Rotated Sorted Array: two attempts — first had bad movement logic and broken res tracking; second had correct `nums[k]>=nums[j]` → go right, `else j=k` logic but still tracking res unnecessarily. Key: compare mid to right boundary, `return nums[i]` — no res needed
- Search in Rotated Sorted Array: correct half-detection logic (left sorted if `nums[i]<=nums[k]`); missed final boundary check on first attempt — fixed by adding `if nums[i]==target: return i` before `return -1`

---

## 2026-09-21 — Day 14

**Reviews: 2**

| # | Problem | Category | Pattern | Score |
|---|---------|----------|---------|-------|
| R | Two Sum II (#167) | Two Pointers | two_pointer_inward | 7/10 |
| R | Encode and Decode Strings (#271) | Hashing | length_prefix_encoding | 10/10 |
| R | Valid Anagram (#242) | Hashing | frequency_counting | 9/10 |
| R | Longest Repeating Character Replacement (#424) | Sliding Window | sliding_window_freq | 6/10 |

**Notes:**
- Two Sum II: first attempt wrong pattern entirely — nested binary search inside a for loop (O(n log n)), plus an infinite-loop bug (`n1=mid` never advances) and an incomplete match check (only compared against right boundary, never `mid`). Rewrote with two-pointer inward; one bug left — `i+i+1` is a no-op, should be `i+=1` — fixed clean, 7/10
- Encode and Decode Strings: clean first-pass solve with length-prefix encoding (`len#string`). Verified against 4 cases including strings containing `#` and empty strings — all passed, 10/10
- Valid Anagram: same two Day-1 bugs recurred — indexing with the character itself instead of `ord(c)-ord('a')`, and `=+1`/`=-1` (assignment, not increment). Fixed both on second attempt, verified against 4 test cases — 9/10
- Longest Repeating Character Replacement: pattern not internalized yet — needed the sliding-window concept walked through from scratch (coin/majority-count analogy). Multiple code bugs across attempts: `.add()` on a dict (set/dict mixup), `.get()` called on a value instead of the dict, backwards window length (`l-r` instead of `r-l+1`), `st.pop()` with no key, and a stale `window` variable not recomputed as `l` moved inside the `while` (caused an `IndexError`). Final version clean, all 5 tests pass — 6/10

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
