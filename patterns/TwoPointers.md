# TwoPointers

107 problems across 14 patterns.

## partition

**What it is** — The partition pattern uses two pointers to divide an array in-place into groups based on a condition (e.g., even/odd, zeros/non-zeros, less/greater than pivot) without requiring extra space. Recognize it when a problem asks you to rearrange elements into distinct sections while maintaining O(1) space. The classic example is Dutch National Flag (3-way partition).

**Common steps**
1. Define the condition that separates the two (or three) groups.
2. Initialize a "write" pointer (or left/right boundary pointers) at the start/end of the array.
3. Scan with a "read" pointer from left to right.
4. If the current element belongs in the left group, swap it to the write pointer's position and advance both pointers.
5. If it belongs in the right group, swap with the right boundary and shrink the boundary (do NOT advance the read pointer yet).
6. Repeat until the read pointer crosses the right boundary.

**Key variations**
- Two-group vs. three-group (Dutch National Flag / Sort Colors) — three-group needs a third `mid` pointer.
- Stable vs. unstable — some problems require relative order to be preserved, which may require extra space or a different traversal direction.
- Pivot-based vs. predicate-based — pivot problems fix a value; predicate problems use a boolean condition (even, zero, sign).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) | Easy | 2/10 | 76.5% | [ ] |
| 922 | [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/) | Easy | 2/10 | 71.3% | [ ] |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | 2/10 | 63.8% | [x] |
| 2161 | [Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/) | Medium | 3/10 | 89.8% | [ ] |
| 2149 | [Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/) | Medium | 3/10 | 84.6% | [ ] |
| 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | 4/10 | 69.6% | [ ] |

## in_place_array_modification

**What it is** — This pattern modifies an array or string in-place using two pointers: a slow "write" pointer that tracks where the next valid result goes, and a fast "read" pointer that scans ahead. Recognize it when a problem says "do it in-place" and you need to filter, compress, or restructure elements without allocating a new data structure.

**Common steps**
1. Initialize a write pointer `w = 0` (or at one end) and a read pointer `r = 0` (or at the other end).
2. Advance the read pointer through each element.
3. Apply the problem's condition to decide whether the current element is "valid" or "should be kept."
4. If valid, copy/write the element at the write pointer's position and advance the write pointer.
5. If invalid, skip the element (only advance the read pointer).
6. After the loop, `w` marks the new logical end of the array; return it or use it to truncate.

**Key variations**
- Removal/filtering — skip elements matching a value (Remove Element, Remove Duplicates).
- Reversal — one pointer starts at each end and they swap toward the middle (Reverse String, Reverse Vowels).
- Compression — consecutive runs of the same character are collapsed (String Compression).
- Two-pass reversal — reverse the whole string, then reverse individual words (Reverse Words in a String II).
- Allow-k-duplicates — keep up to k copies by comparing write pointer with write pointer minus k (Remove Duplicates II).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | 1/10 | 80.8% | [ ] |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | Easy | 1/10 | 61.7% | [ ] |
| 3823 | [Reverse Letters Then Special Characters in a String](https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/) | Easy | 2/10 | 82.0% | [ ] |
| 2460 | [Apply Operations to an Array](https://leetcode.com/problems/apply-operations-to-an-array/) | Easy | 2/10 | 74.7% | [ ] |
| 917 | [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/) | Easy | 2/10 | 68.4% | [ ] |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | 2/10 | 62.7% | [ ] |
| 345 | [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | Easy | 2/10 | 61.2% | [ ] |
| 1089 | [Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/) | Easy | 3/10 | 53.6% | [ ] |
| 80 | [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | Medium | 4/10 | 64.6% | [ ] |
| 443 | [String Compression](https://leetcode.com/problems/string-compression/) | Medium | 4/10 | 59.9% | [ ] |
| 186 | [Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/) :lock: | Medium | 4/10 | 56.7% | [ ] |
| 1750 | [Minimum Length of String After Deleting Similar Ends](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/) | Medium | 5/10 | 56.1% | [ ] |
| 1574 | [Shortest Subarray to be Removed to Make Array Sorted](https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/) | Medium | 6/10 | 51.3% | [ ] |

## sorted_array_merge

**What it is** — This pattern processes two sorted sequences simultaneously by maintaining one pointer per sequence and advancing the pointer that currently holds the smaller (or more relevant) value. Recognize it when you need to combine, intersect, or compare two already-sorted arrays or strings in a single linear pass.

**Common steps**
1. Initialize pointer `i = 0` for the first sequence and `j = 0` for the second.
2. While both pointers are in bounds, compare the elements at `i` and `j`.
3. Process (write, count, or record) the smaller/equal element and advance that pointer.
4. When one sequence is exhausted, append or process the remaining elements from the other.
5. If writing into one of the input arrays (e.g., Merge Sorted Array), iterate from the back to avoid overwriting unread data.

**Key variations**
- Merge into new array vs. merge in-place from the back (Merge Sorted Array).
- Find intersection/common value — advance both pointers only when elements match (Minimum Common Value).
- Squaring before merging — squares of a sorted array can produce a new sorted array by comparing from both ends (Squares of a Sorted Array).
- Run-length encoded inputs — advance whichever run is exhausted first, then handle partial runs (Product of Two Run-Length Encoded Arrays).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1768 | [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | Easy | 1/10 | 82.1% | [ ] |
| 2570 | [Merge Two 2D Arrays by Summing Values](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/) | Easy | 2/10 | 81.7% | [ ] |
| 977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Easy | 2/10 | 73.7% | [ ] |
| 2540 | [Minimum Common Value](https://leetcode.com/problems/minimum-common-value/) | Easy | 2/10 | 58.0% | [ ] |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | 3/10 | 54.8% | [ ] |
| 360 | [Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array/) :lock: | Medium | 5/10 | 58.1% | [ ] |
| 1868 | [Product of Two Run-Length Encoded Arrays](https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/) :lock: | Medium | 6/10 | 59.6% | [ ] |

## opposite_ends_pair_sum

**What it is** — Place one pointer at the start and one at the end of a sorted array; move them inward based on whether their sum is too small or too large. This gives O(n) pair finding instead of O(n²) brute force. Recognize it whenever a problem involves finding pairs (or counting them) whose sum satisfies a condition in a sorted array.

**Common steps**
1. Sort the array if it is not already sorted.
2. Initialize `left = 0` and `right = len - 1`.
3. Compute the sum (or relevant expression) of `arr[left]` and `arr[right]`.
4. If the sum equals the target, record the pair and move both pointers inward.
5. If the sum is too small, advance `left` to increase the sum.
6. If the sum is too large, retreat `right` to decrease the sum. Repeat until `left >= right`.

**Key variations**
- Exact target vs. counting pairs below/above a threshold — adjust the condition for when to count and which pointer to move.
- Maximize/minimize the pair sum — stop as soon as you find the optimum rather than exhausting all pairs.
- Two separate arrays — convert to a difference problem and use binary search, or use a similar two-pointer sweep after combining (Count Pairs in Two Arrays).
- Counting valid triangles — fix one side and use two pointers on the remaining sorted elements (Valid Triangle Number).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2824 | [Count Pairs Whose Sum is Less than Target](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/) | Easy | 2/10 | 87.7% | [ ] |
| 3194 | [Minimum Average of Smallest and Largest Elements](https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/) | Easy | 2/10 | 85.3% | [ ] |
| 2562 | [Find the Array Concatenation Value](https://leetcode.com/problems/find-the-array-concatenation-value/) | Easy | 2/10 | 72.0% | [ ] |
| 1099 | [Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/) :lock: | Easy | 2/10 | 62.1% | [ ] |
| 2465 | [Number of Distinct Averages](https://leetcode.com/problems/number-of-distinct-averages/) | Easy | 2/10 | 58.9% | [ ] |
| 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | 3/10 | 65.0% | [x] |
| 1237 | [Find Positive Integer Solution for a Given Equation](https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/) | Medium | 4/10 | 70.0% | [ ] |
| 1679 | [Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | Medium | 4/10 | 57.0% | [ ] |
| 633 | [Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/) | Medium | 4/10 | 36.8% | [ ] |
| 1885 | [Count Pairs in Two Arrays](https://leetcode.com/problems/count-pairs-in-two-arrays/) :lock: | Medium | 5/10 | 60.3% | [ ] |
| 611 | [Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/) | Medium | 5/10 | 56.9% | [ ] |
| 2563 | [Count the Number of Fair Pairs](https://leetcode.com/problems/count-the-number-of-fair-pairs/) | Medium | 5/10 | 52.7% | [ ] |

## string_matching

**What it is** — Two pointers advance through one or two strings simultaneously, character by character, to verify alignment, detect divergence, or locate the first mismatch. Recognize it when a problem asks whether two strings match under some transformation rule (skipping characters, handling long-presses, comparing versions, etc.) and a single linear scan suffices.

**Common steps**
1. Initialize one pointer per string (or one at each end of a single string).
2. At each step, determine whether the current character should be consumed or skipped (e.g., skip backspaces, skip non-letters, parse a version segment).
3. When both characters are "ready," compare them; on mismatch, return the result immediately.
4. Advance one or both pointers depending on which string's character was consumed.
5. After the main loop, check whether both strings are fully consumed (if lengths must match).

**Key variations**
- Skip-character rules — backspace (#), non-letters, non-vowels: advance the relevant pointer past the skipped character before comparing.
- Version/token parsing — consume a full integer or word segment at each step rather than a single character.
- One pointer per string from opposite directions — compare from both ends (First Matching Character From Both Ends).
- Divergence with one allowed fix — continue after a mismatch by trying to skip one character in one of the strings (One Edit Distance, Long Pressed Name).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3884 | [First Matching Character From Both Ends](https://leetcode.com/problems/first-matching-character-from-both-ends/) | Easy | 1/10 | 81.8% | [ ] |
| 2109 | [Adding Spaces to a String](https://leetcode.com/problems/adding-spaces-to-a-string/) | Medium | 3/10 | 71.8% | [ ] |
| 1826 | [Faulty Sensor](https://leetcode.com/problems/faulty-sensor/) :lock: | Easy | 3/10 | 50.5% | [ ] |
| 844 | [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/) | Easy | 3/10 | 49.9% | [ ] |
| 408 | [Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/) :lock: | Easy | 3/10 | 37.0% | [ ] |
| 696 | [Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/) | Easy | 4/10 | 70.4% | [ ] |
| 3460 | [Longest Common Prefix After at Most One Removal](https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/) :lock: | Medium | 4/10 | 67.4% | [ ] |
| 925 | [Long Pressed Name](https://leetcode.com/problems/long-pressed-name/) | Easy | 4/10 | 32.9% | [ ] |
| 2337 | [Move Pieces to Obtain a String](https://leetcode.com/problems/move-pieces-to-obtain-a-string/) | Medium | 5/10 | 56.6% | [ ] |
| 1813 | [Sentence Similarity III](https://leetcode.com/problems/sentence-similarity-iii/) | Medium | 5/10 | 48.4% | [ ] |
| 809 | [Expressive Words](https://leetcode.com/problems/expressive-words/) | Medium | 5/10 | 46.8% | [ ] |
| 165 | [Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/) | Medium | 5/10 | 46.4% | [ ] |
| 161 | [One Edit Distance](https://leetcode.com/problems/one-edit-distance/) :lock: | Medium | 5/10 | 34.6% | [ ] |
| 777 | [Swap Adjacent in LR String](https://leetcode.com/problems/swap-adjacent-in-lr-string/) | Medium | 6/10 | 38.1% | [ ] |

## subsequence_matching

**What it is** — A slow pointer walks through the candidate subsequence while a fast pointer scans the source string; every time the characters match, both pointers advance, otherwise only the source pointer advances. Recognize it when a problem asks whether one string can be "embedded" inside another by deleting characters without reordering them.

**Common steps**
1. Initialize `i = 0` (pointer into the subsequence) and `j = 0` (pointer into the source).
2. While both pointers are in bounds, compare `sub[i]` with `src[j]`.
3. If they match, advance both `i` and `j`.
4. If they do not match, advance only `j`.
5. After the loop, check whether `i` reached the end of the subsequence — if yes, it is a valid subsequence.
6. For "smallest valid sequence" variants, scan from the right simultaneously to track the last unmatched character.

**Key variations**
- Binary check (is it a subsequence?) vs. counting how many characters remain unmatched.
- Greedy character assignment — match as early as possible (leftmost greedy) or as late as possible depending on the objective.
- Multiple pattern matching — for each candidate pattern, run the subsequence check independently (Camelcase Matching).
- Forming an array subsequence — treat subarrays as atomic units and match them one at a time (Form Array by Concatenating Subarrays).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 392 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Easy | 2/10 | 49.0% | [ ] |
| 2486 | [Append Characters to String to Make Subsequence](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/) | Medium | 3/10 | 73.0% | [ ] |
| 2825 | [Make String a Subsequence Using Cyclic Increments](https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/) | Medium | 4/10 | 65.7% | [ ] |
| 1023 | [Camelcase Matching](https://leetcode.com/problems/camelcase-matching/) | Medium | 4/10 | 65.3% | [ ] |
| 1764 | [Form Array by Concatenating Subarrays of Another Array](https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/) | Medium | 5/10 | 54.8% | [ ] |
| 3302 | [Find the Lexicographically Smallest Valid Sequence](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/) | Medium | 7/10 | 21.9% | [ ] |

## subarray_count_with_constraint

**What it is** — Two pointers define the boundaries of a subarray or index window, and you count or find subarrays/index pairs that satisfy a constraint on values, distances, or structure. Recognize it when you need to enumerate subarrays where a property (max, min, distance between indices) falls within a range, and a brute-force O(n²) scan is too slow.

**Common steps**
1. Sort the array if the constraint is on values and order does not matter.
2. Fix one endpoint (or use a left pointer) and expand or shrink a right pointer.
3. When the constraint is satisfied, count all valid subarrays rooted at the current left (often `right - left + 1`) and advance left.
4. When the constraint is violated, advance right (or shrink the window from the left).
5. For "bounded maximum" style problems, use the formula: count(max <= upper) - count(max <= lower - 1).
6. Accumulate or track the best result across all window positions.

**Key variations**
- Index-distance constraints — both the index gap and the value difference must be bounded (Find Indices With Index and Value Difference).
- Mountain subarray — the window must first strictly increase then strictly decrease (Longest Mountain in Array).
- Subsequence counting — sort first, then use two pointers from opposite ends to count valid pairs (Number of Subsequences That Satisfy the Given Sum Condition).
- Incremovable subarrays — find the longest sorted prefix and suffix, then count removable middle segments with two pointers.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2200 | [Find All K-Distant Indices in an Array](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/) | Easy | 2/10 | 77.3% | [ ] |
| 2903 | [Find Indices With Index and Value Difference I](https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/) | Easy | 3/10 | 60.3% | [ ] |
| 2511 | [Maximum Enemy Forts That Can Be Captured](https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/) | Easy | 3/10 | 41.3% | [ ] |
| 2970 | [Count the Number of Incremovable Subarrays I](https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/) | Easy | 4/10 | 56.5% | [ ] |
| 845 | [Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/) | Medium | 5/10 | 42.1% | [ ] |
| 2905 | [Find Indices With Index and Value Difference II](https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/) | Medium | 5/10 | 32.7% | [ ] |
| 795 | [Number of Subarrays with Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/) | Medium | 6/10 | 54.9% | [ ] |
| 1498 | [Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/) | Medium | 6/10 | 49.2% | [ ] |
| 2972 | [Count the Number of Incremovable Subarrays II](https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-ii/) | Hard | 7/10 | 40.1% | [ ] |

## interval_intersection

**What it is** — Two pointers each track the current interval from two separate sorted interval lists; at each step you check for overlap, record any intersection, and advance the pointer whose interval ends first. Recognize it when you have two lists of non-overlapping sorted intervals and need to find their common regions or schedule conflicts.

**Common steps**
1. Initialize `i = 0` and `j = 0` as pointers into the two interval lists.
2. At each step, compute the intersection: `start = max(A[i][0], B[j][0])`, `end = min(A[i][1], B[j][1])`.
3. If `start <= end`, a valid intersection exists — record it.
4. Advance the pointer whose interval ends earlier (`A[i][1] < B[j][1]` → advance `i`, else advance `j`).
5. Repeat until one list is exhausted.

**Key variations**
- Recording all intersections vs. finding the first available common slot of minimum duration (Meeting Scheduler).
- Handling open vs. closed interval boundaries — adjust the `start <= end` check accordingly.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 986 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Medium | 5/10 | 73.0% | [ ] |
| 1229 | [Meeting Scheduler](https://leetcode.com/problems/meeting-scheduler/) :lock: | Medium | 5/10 | 55.2% | [ ] |

## palindrome_check

**What it is** — Two pointers start at opposite ends of a string (or array) and march toward the center, comparing characters at each step to verify or construct a palindrome. Recognize it when a problem involves checking symmetry, making a string palindromic with minimal changes, or splitting a string into palindromic parts.

**Common steps**
1. Initialize `left = 0` and `right = len - 1`.
2. Skip non-alphanumeric characters if the problem requires it (Valid Palindrome).
3. Compare `s[left]` and `s[right]`; if they differ, decide whether the problem allows fixes (swap, skip, or return false immediately).
4. Advance `left` and retreat `right`.
5. If one mismatch is allowed, recurse or branch on skipping `left` vs. skipping `right` and check both sub-problems.
6. Return true if the pointers meet or cross without unresolvable mismatches.

**Key variations**
- Strict check vs. one-deletion allowed (Valid Palindrome II) vs. k-deletions allowed.
- Constructing the lexicographically smallest palindrome — replace mismatched characters with the smaller of the two.
- Chunked palindrome decomposition — match prefixes and suffixes greedily, then recurse on the remaining middle.
- Cross-string palindrome — interleave halves of two different strings to form a palindrome (Split Two Strings to Make Palindrome).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2697 | [Lexicographically Smallest Palindrome](https://leetcode.com/problems/lexicographically-smallest-palindrome/) | Easy | 2/10 | 81.4% | [ ] |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | 2/10 | 53.2% | [x] |
| 246 | [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) :lock: | Easy | 2/10 | 47.5% | [ ] |
| 2330 | [Valid Palindrome IV](https://leetcode.com/problems/valid-palindrome-iv/) :lock: | Medium | 3/10 | 75.6% | [ ] |
| 680 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | 3/10 | 44.2% | [ ] |
| 2422 | [Merge Operations to Turn Array Into a Palindrome](https://leetcode.com/problems/merge-operations-to-turn-array-into-a-palindrome/) :lock: | Medium | 6/10 | 68.9% | [ ] |
| 1616 | [Split Two Strings to Make Palindrome](https://leetcode.com/problems/split-two-strings-to-make-palindrome/) | Medium | 7/10 | 32.2% | [ ] |
| 3844 | [Longest Almost-Palindromic Substring](https://leetcode.com/problems/longest-almost-palindromic-substring/) | Medium | 7/10 | 22.5% | [ ] |
| 1147 | [Longest Chunked Palindrome Decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/) | Hard | 8/10 | 58.9% | [ ] |
| 1842 | [Next Palindrome Using Same Digits](https://leetcode.com/problems/next-palindrome-using-same-digits/) :lock: | Hard | 8/10 | 54.3% | [ ] |
| 2193 | [Minimum Number of Moves to Make Palindrome](https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/) | Hard | 8/10 | 52.8% | [ ] |

## greedy_matching

**What it is** — Sort both sequences and use two pointers to greedily pair or match elements from each, always choosing the best available partner for the current element without reconsidering earlier decisions. Recognize it when a problem asks you to maximize matches, minimize a max/min pair value, or assign elements from one group to another under some ordering constraint.

**Common steps**
1. Sort both arrays (or the single array) in ascending or descending order depending on the objective.
2. Initialize `left` and `right` pointers (often one per array, or one at each end of a single array).
3. Compare the elements at the two pointers; apply the greedy condition to decide whether a match is made.
4. If a match is made, advance both pointers and record the result.
5. If no match is possible, advance the pointer that can never be matched at this step (e.g., the weaker player who cannot beat any remaining trainer).
6. Repeat until one pointer is exhausted.

**Key variations**
- Minimize the maximum pair sum — sort ascending, pair smallest with largest (opposite ends).
- Maximize the number of matches — greedily pair the smallest feasible element from one list with the smallest element from the other that satisfies the constraint.
- Celebrity / elimination — use two pointers to eliminate candidates in O(n) then verify the survivor.
- Finding an offset — try all candidate offsets (brute force outer loop) and use two pointers for inner verification (Recover the Original Array).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1877 | [Minimize Maximum Pair Sum in Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) | Medium | 4/10 | 83.3% | [ ] |
| 2410 | [Maximum Matching of Players With Trainers](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/) | Medium | 4/10 | 75.3% | [ ] |
| 2491 | [Divide Players Into Teams of Equal Skill](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/) | Medium | 4/10 | 68.9% | [ ] |
| 2592 | [Maximize Greatness of an Array](https://leetcode.com/problems/maximize-greatness-of-an-array/) | Medium | 4/10 | 61.6% | [ ] |
| 1855 | [Maximum Distance Between a Pair of Values](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/) | Medium | 4/10 | 61.4% | [ ] |
| 1471 | [The k Strongest Values in an Array](https://leetcode.com/problems/the-k-strongest-values-in-an-array/) | Medium | 5/10 | 62.7% | [ ] |
| 1989 | [Maximum Number of People That Can Be Caught in Tag](https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/) :lock: | Medium | 5/10 | 49.4% | [ ] |
| 2105 | [Watering Plants II](https://leetcode.com/problems/watering-plants-ii/) | Medium | 5/10 | 48.7% | [ ] |
| 2576 | [Find the Maximum Number of Marked Indices](https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/) | Medium | 5/10 | 41.3% | [ ] |
| 277 | [Find the Celebrity](https://leetcode.com/problems/find-the-celebrity/) :lock: | Medium | 6/10 | 49.0% | [ ] |
| 3132 | [Find the Integer Added to Array II](https://leetcode.com/problems/find-the-integer-added-to-array-ii/) | Medium | 6/10 | 32.9% | [ ] |
| 3814 | [Maximum Capacity Within Budget](https://leetcode.com/problems/maximum-capacity-within-budget/) | Medium | 7/10 | 20.3% | [ ] |
| 2122 | [Recover the Original Array](https://leetcode.com/problems/recover-the-original-array/) | Hard | 8/10 | 41.5% | [ ] |
| 1163 | [Last Substring in Lexicographical Order](https://leetcode.com/problems/last-substring-in-lexicographical-order/) | Hard | 8/10 | 35.0% | [ ] |

## sequence_generation

**What it is** — Two pointers cooperate to build or simulate a sequence incrementally, where one pointer reads from an already-generated portion of the output to determine the next value to write. Recognize it when the sequence is self-referential (each new element depends on previously generated elements) or when simulating a physical process that propagates from both ends inward.

**Common steps**
1. Initialize a "read" pointer and a "write" pointer within the same output array (or separate input/output).
2. At each step, use the value at the read pointer (and possibly surrounding context) to determine the next element(s) to append at the write pointer.
3. Advance the read pointer after consuming its value, and advance the write pointer after each element is written.
4. Continue until the write pointer reaches the required length or a termination condition is met.
5. For simulation problems (Push Dominoes), use a separate pass in each direction, accumulating forces or distances before combining.

**Key variations**
- Self-referential generation — the sequence describes itself (Magical String uses the sequence to determine run lengths).
- Next permutation style — scan from the right to find the first descending pair, then swap and reverse the suffix (Next Greater Element III).
- Physics simulation — propagate left-to-right and right-to-left forces, then take the dominant force at each position (Push Dominoes).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 556 | [Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) | Medium | 5/10 | 35.3% | [ ] |
| 838 | [Push Dominoes](https://leetcode.com/problems/push-dominoes/) | Medium | 6/10 | 63.0% | [ ] |
| 481 | [Magical String](https://leetcode.com/problems/magical-string/) | Medium | 6/10 | 55.1% | [ ] |

## k_sum

**What it is** — Reduce a k-sum problem to a two-sum problem by fixing k-2 elements with nested loops, then applying the opposite-ends two-pointer technique on the remaining sorted subarray. Recognize it whenever a problem asks for all unique tuples (triplets, quadruplets) that sum to a target in an array.

**Common steps**
1. Sort the array.
2. Use k-2 nested loops to fix the first k-2 elements; skip duplicates at each loop level by checking `nums[i] == nums[i-1]`.
3. After fixing the outer elements, set `left` to the index after the last fixed element and `right` to the last index.
4. Apply the two-sum opposite-ends logic: if the current sum equals the target, record the tuple and advance both pointers past duplicates; if too small, advance `left`; if too large, retreat `right`.
5. Continue until `left >= right`, then move to the next iteration of the outer loops.

**Key variations**
- Exact target (3Sum, 4Sum) vs. closest sum (3Sum Closest) vs. count of tuples below target (3Sum Smaller).
- Closest sum — track the running minimum of `abs(sum - target)` and update the best candidate instead of recording exact matches.
- Count below target — when `sum < target`, all pairs with the current left are valid, so add `right - left` to the count and advance `left`.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 259 | [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) :lock: | Medium | 5/10 | 51.4% | [ ] |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Medium | 6/10 | 48.5% | [ ] |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Medium | 6/10 | 39.0% | [x] |
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | Medium | 7/10 | 40.6% | [ ] |

## cycle_detection

**What it is** — Floyd's tortoise-and-hare algorithm uses a slow pointer that moves one step at a time and a fast pointer that moves two steps; if a cycle exists, they are guaranteed to meet inside it. Recognize it when a problem involves detecting a repeated value or loop in a sequence that can be modeled as a linked-list-style traversal (index as next pointer).

**Common steps**
1. Model the problem as a function `f(x)` where following `x -> f(x)` repeatedly will eventually cycle (e.g., array value as the next index).
2. Initialize `slow = f(start)` and `fast = f(f(start))`.
3. Advance `slow` by one step and `fast` by two steps until they meet — this confirms a cycle exists.
4. To find the cycle entry point, reset one pointer to `start` and move both one step at a time; they will meet at the cycle entrance.
5. The value at the meeting point is the duplicate / start of the cycle.

**Key variations**
- Finding the duplicate number — the array values are indices, making it a direct application of Floyd's algorithm (Find the Duplicate Number).
- Circular array loop — the cycle must be all-positive or all-negative steps and longer than one element; requires careful handling of the direction constraint (Circular Array Loop).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | 6/10 | 64.3% | [x] |
| 457 | [Circular Array Loop](https://leetcode.com/problems/circular-array-loop/) | Medium | 7/10 | 37.3% | [ ] |

## opposite_ends_optimization

**What it is** — Two pointers start at opposite ends of an array and converge inward, making a greedy decision at each step about which pointer to move based on which side currently limits the objective. Recognize it when you need to maximize or compute an area/capacity/score that depends on the minimum (or maximum) of two boundary values, and moving the larger boundary inward can never improve the result.

**Common steps**
1. Initialize `left = 0` and `right = len - 1`.
2. Compute the current objective value using both boundary elements (e.g., area = `min(height[left], height[right]) * (right - left)`).
3. Update the running answer if the current value is better.
4. Move the pointer at the shorter (limiting) boundary inward — moving the taller boundary can only decrease or maintain the width without increasing the height cap.
5. Repeat until `left >= right`.

**Key variations**
- Container with most water — width shrinks by 1 each step; always move the shorter wall inward.
- Trapping rain water — track `left_max` and `right_max` running maxima; the trapped water at each position equals `max - current_height` on the side with the lower maximum.
- Subarray with score constraint — fix one end and binary-search or two-pointer the other end to maintain a constraint on the minimum value within the window (Maximum Score of a Good Subarray).
- Maximum product of endpoints — consider both ascending and descending orderings, as the optimal product may come from two large positives or two large-magnitude negatives.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | 5/10 | 60.0% | [x] |
| 3584 | [Maximum Product of First and Last Elements of a Subsequence](https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/) | Medium | 6/10 | 31.5% | [ ] |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | 8/10 | 67.3% | [ ] |
| 1793 | [Maximum Score of a Good Subarray](https://leetcode.com/problems/maximum-score-of-a-good-subarray/) | Hard | 8/10 | 64.2% | [ ] |
