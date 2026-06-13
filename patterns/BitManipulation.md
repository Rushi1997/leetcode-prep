# BitManipulation

131 problems across 14 patterns.

## bit_counting

**What it is** — Bit counting problems revolve around inspecting, tallying, or comparing the individual set bits (1-bits) of integers. You recognize this pattern when a problem asks about the number of 1s in a binary representation, Hamming distance between numbers, popcount-based sorting, or powers of two detection.

**Common steps**
1. Determine whether you need a bit count for one number or across an array.
2. Use `bin(n).count('1')`, `n.bit_count()` (Python 3.10+), or the Brian Kernighan trick (`n & (n-1)` clears the lowest set bit) to count bits efficiently.
3. For powers of two, check `n > 0 and (n & (n-1)) == 0`; for powers of four, add a mask check `n & 0xAAAAAAAA == 0`.
4. When counting bits for all numbers 0..n, use DP: `dp[i] = dp[i >> 1] + (i & 1)` for O(n) time.
5. For Hamming distance between two numbers, XOR them first, then count set bits in the result.
6. Aggregate results (sum, sort key, filter) using the per-number bit counts computed above.

**Key variations**
- Single number: count bits of one integer (Number of 1 Bits, Power of Two).
- Range/array: compute popcount for every element, then sum or sort (Counting Bits, Sort by Bits).
- Pairwise distance: XOR pairs then popcount (Hamming Distance, Total Hamming Distance — process bit-by-bit across all numbers for O(32n)).
- Threshold/condition: filter or combine values based on their bit count meeting some criterion (Sum of Values at Indices With K Set Bits, Prime Number of Set Bits).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3173 | [Bitwise OR of Adjacent Elements](https://leetcode.com/problems/bitwise-or-of-adjacent-elements/) :lock: | Easy | 1/10 | 94.8% | [ ] |
| 2220 | [Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/) | Easy | 1/10 | 87.9% | [ ] |
| 2859 | [Sum of Values at Indices With K Set Bits](https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/) | Easy | 1/10 | 86.1% | [ ] |
| 1342 | [Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) | Easy | 1/10 | 85.8% | [ ] |
| 3688 | [Bitwise OR of Even Numbers in an Array](https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/) | Easy | 1/10 | 85.0% | [ ] |
| 1356 | [Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/) | Easy | 1/10 | 82.3% | [ ] |
| 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | 1/10 | 76.8% | [x] |
| 461 | [Hamming Distance](https://leetcode.com/problems/hamming-distance/) | Easy | 1/10 | 76.8% | [ ] |
| 2595 | [Number of Even and Odd Bits](https://leetcode.com/problems/number-of-even-and-odd-bits/) | Easy | 1/10 | 73.4% | [ ] |
| 2980 | [Check if Bitwise OR Has Trailing Zeros](https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/) | Easy | 1/10 | 71.3% | [ ] |
| 3226 | [Number of Bit Changes to Make Two Integers Equal](https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/) | Easy | 1/10 | 63.5% | [ ] |
| 3199 | [Count Triplets with Even XOR Set Bits I](https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/) :lock: | Easy | 2/10 | 83.2% | [ ] |
| 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | 2/10 | 80.6% | [ ] |
| 762 | [Prime Number of Set Bits in Binary Representation](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/) | Easy | 2/10 | 78.8% | [ ] |
| 2917 | [Find the K-or of an Array](https://leetcode.com/problems/find-the-k-or-of-an-array/) | Easy | 2/10 | 72.8% | [ ] |
| 401 | [Binary Watch](https://leetcode.com/problems/binary-watch/) | Easy | 2/10 | 65.5% | [ ] |
| 342 | [Power of Four](https://leetcode.com/problems/power-of-four/) | Easy | 2/10 | 52.0% | [ ] |
| 231 | [Power of Two](https://leetcode.com/problems/power-of-two/) | Easy | 2/10 | 50.1% | [ ] |
| 3304 | [Find the K-th Character in String Game I](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/) | Easy | 3/10 | 81.6% | [ ] |
| 2275 | [Largest Combination With Bitwise AND Greater Than Zero](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/) | Medium | 4/10 | 80.8% | [ ] |
| 1318 | [Minimum Flips to Make a OR b Equal to c](https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/) | Medium | 4/10 | 72.0% | [ ] |
| 3011 | [Find if Array Can Be Sorted](https://leetcode.com/problems/find-if-array-can-be-sorted/) | Medium | 4/10 | 66.4% | [ ] |
| 2419 | [Longest Subarray With Maximum Bitwise AND](https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/) | Medium | 4/10 | 65.4% | [ ] |
| 3215 | [Count Triplets with Even XOR Set Bits II](https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/) :lock: | Medium | 4/10 | 61.4% | [ ] |
| 477 | [Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/) | Medium | 4/10 | 54.8% | [ ] |
| 3595 | [Once Twice](https://leetcode.com/problems/once-twice/) :lock: | Medium | 5/10 | 75.8% | [ ] |
| 137 | [Single Number II](https://leetcode.com/problems/single-number-ii/) | Medium | 5/10 | 67.0% | [ ] |
| 1558 | [Minimum Numbers of Function Calls to Make Target Array](https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/) | Medium | 5/10 | 62.8% | [ ] |
| 2749 | [Minimum Operations to Make the Integer Zero](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/) | Medium | 5/10 | 58.2% | [ ] |
| 779 | [K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) | Medium | 5/10 | 48.2% | [ ] |
| 2354 | [Number of Excellent Pairs](https://leetcode.com/problems/number-of-excellent-pairs/) | Hard | 7/10 | 49.1% | [ ] |

## xor_tricks

**What it is** — XOR tricks exploit the property that XOR-ing a number with itself produces 0 and XOR-ing with 0 is a no-op, making it ideal for canceling out duplicates or finding missing/unique values. Recognize this pattern when a problem involves finding an element that appears an odd number of times, detecting a missing number, or comparing two collections where most elements cancel.

**Common steps**
1. Identify what should "cancel out" — pairs of equal elements XOR to zero and disappear.
2. XOR all relevant values together; surviving bits represent the answer or the difference.
3. For two unique survivors (Single Number III), isolate a differing bit with `diff & (-diff)`, then split elements into two groups and XOR each group separately.
4. For subset XOR totals, use the math shortcut: each element contributes to exactly half of all subsets, so the total equals `OR_of_all * 2^(n-1)`.
5. Verify edge cases: empty array XORs to 0, single element XORs to itself.

**Key variations**
- Finding the lone unique element among pairs (Single Number, Find the Difference).
- Finding two unique elements among pairs (Single Number III — requires two-pass with bit isolation).
- XOR over all pairs or subarrays (XOR Beauty, Bitwise XOR of All Pairings — use parity of appearances to simplify).
- Constructing a target XOR value with minimum operations (count differing bits).
- Feasibility/equality checks using XOR (Neighboring Bitwise XOR, Apply Bitwise Operations).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1486 | [XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/) | Easy | 1/10 | 87.6% | [ ] |
| 3158 | [Find the XOR of Numbers Which Appear Twice](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/) | Easy | 1/10 | 78.9% | [ ] |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | 1/10 | 77.6% | [x] |
| 389 | [Find the Difference](https://leetcode.com/problems/find-the-difference/) | Easy | 1/10 | 60.3% | [ ] |
| 2932 | [Maximum Strong Pair XOR I](https://leetcode.com/problems/maximum-strong-pair-xor-i/) | Easy | 2/10 | 76.0% | [ ] |
| 1863 | [Sum of All Subset XOR Totals](https://leetcode.com/problems/sum-of-all-subset-xor-totals/) | Easy | 3/10 | 90.1% | [ ] |
| 2997 | [Minimum Number of Operations to Make Array XOR Equal to K](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/) | Medium | 3/10 | 85.4% | [ ] |
| 1506 | [Find Root of N-Ary Tree](https://leetcode.com/problems/find-root-of-n-ary-tree/) :lock: | Medium | 3/10 | 78.6% | [ ] |
| 2317 | [Maximum XOR After Operations ](https://leetcode.com/problems/maximum-xor-after-operations/) | Medium | 4/10 | 79.8% | [ ] |
| 2683 | [Neighboring Bitwise XOR](https://leetcode.com/problems/neighboring-bitwise-xor/) | Medium | 4/10 | 79.8% | [ ] |
| 2527 | [Find Xor-Beauty of Array](https://leetcode.com/problems/find-xor-beauty-of-array/) | Medium | 4/10 | 70.7% | [ ] |
| 2425 | [Bitwise XOR of All Pairings](https://leetcode.com/problems/bitwise-xor-of-all-pairings/) | Medium | 4/10 | 66.9% | [ ] |
| 2546 | [Apply Bitwise Operations to Make Strings Equal](https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/) | Medium | 4/10 | 42.6% | [ ] |
| 260 | [Single Number III](https://leetcode.com/problems/single-number-iii/) | Medium | 5/10 | 70.3% | [ ] |
| 3513 | [Number of Unique XOR Triplets I](https://leetcode.com/problems/number-of-unique-xor-triplets-i/) | Medium | 5/10 | 26.7% | [ ] |
| 2505 | [Bitwise OR of All Subsequence Sums](https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/) :lock: | Medium | 6/10 | 64.0% | [ ] |
| 1835 | [Find XOR Sum of All Pairs Bitwise AND](https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/) | Hard | 6/10 | 62.5% | [ ] |

## bit_manipulation_construction

**What it is** — This pattern involves building or transforming a number by directly manipulating its binary representation — setting, clearing, toggling, or rearranging specific bits. Recognize it when a problem asks you to construct a number with specific bit properties, compute a complement, reverse bits, or minimize/maximize a value by choosing which bits to set.

**Common steps**
1. Identify the bit positions you need to affect (e.g., the highest set bit, all bits, alternating bits).
2. Build a full mask for n bits: `mask = (1 << bit_length) - 1`.
3. Use `n ^ mask` to flip all bits (complement), `n | (1 << k)` to set bit k, `n & ~(1 << k)` to clear bit k, or `n ^ (1 << k)` to toggle bit k.
4. For bit reversal, iterate over each bit position, extract with `(n >> i) & 1`, and place it at the mirrored position.
5. To minimize/maximize a number under bit constraints, greedily assign bits from the most significant position downward.
6. For range-based AND (Bitwise AND of Numbers Range), right-shift both ends until they are equal — the common prefix is the answer.

**Key variations**
- Complement/inversion: flip all bits within the number's own bit length (Number Complement, Complement of Base 10 Integer).
- Bit reversal: mirror all 32 bits (Reverse Bits).
- Base conversion: extract groups of bits and map to characters (Convert to Hexadecimal).
- Greedy bit assignment: choose which bits to keep or set to satisfy a constraint while minimizing/maximizing the result (Minimize XOR, Minimum Array End).
- Range AND: find the common bit prefix of a range (Bitwise AND of Numbers Range).
- Structural properties: detect alternating bits, find binary gaps (Binary Number with Alternating Bits, Binary Gap).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3370 | [Smallest Number With All Set Bits](https://leetcode.com/problems/smallest-number-with-all-set-bits/) | Easy | 1/10 | 80.3% | [ ] |
| 1009 | [Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/) | Easy | 1/10 | 63.4% | [ ] |
| 868 | [Binary Gap](https://leetcode.com/problems/binary-gap/) | Easy | 2/10 | 74.3% | [ ] |
| 476 | [Number Complement](https://leetcode.com/problems/number-complement/) | Easy | 2/10 | 70.4% | [ ] |
| 693 | [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/) | Easy | 2/10 | 69.9% | [ ] |
| 190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | 2/10 | 68.3% | [ ] |
| 405 | [Convert a Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/) | Easy | 2/10 | 54.0% | [ ] |
| 3314 | [Construct the Minimum Bitwise Array I](https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/) | Easy | 3/10 | 85.2% | [ ] |
| 3750 | [Minimum Number of Flips to Reverse Binary String](https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/) | Easy | 3/10 | 76.4% | [ ] |
| 3827 | [Count Monobit Integers](https://leetcode.com/problems/count-monobit-integers/) | Easy | 3/10 | 66.4% | [ ] |
| 3674 | [Minimum Operations to Equalize Array](https://leetcode.com/problems/minimum-operations-to-equalize-array/) | Easy | 3/10 | 60.4% | [ ] |
| 1256 | [Encode Number](https://leetcode.com/problems/encode-number/) :lock: | Medium | 4/10 | 70.3% | [ ] |
| 3125 | [Maximum Number That Makes Result of Bitwise AND Zero](https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/) :lock: | Medium | 4/10 | 69.9% | [ ] |
| 2568 | [Minimum Impossible OR](https://leetcode.com/problems/minimum-impossible-or/) | Medium | 4/10 | 59.0% | [ ] |
| 3315 | [Construct the Minimum Bitwise Array II](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/) | Medium | 5/10 | 66.5% | [ ] |
| 1404 | [Number of Steps to Reduce a Number in Binary Representation to One](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/) | Medium | 5/10 | 63.7% | [ ] |
| 2429 | [Minimize XOR](https://leetcode.com/problems/minimize-xor/) | Medium | 5/10 | 62.4% | [ ] |
| 2571 | [Minimum Operations to Reduce an Integer to 0](https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/) | Medium | 5/10 | 62.2% | [ ] |
| 2438 | [Range Product Queries of Powers](https://leetcode.com/problems/range-product-queries-of-powers/) | Medium | 5/10 | 61.4% | [ ] |
| 201 | [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | Medium | 5/10 | 48.9% | [ ] |
| 2411 | [Smallest Subarrays With Maximum Bitwise OR](https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/) | Medium | 6/10 | 61.9% | [ ] |
| 3133 | [Minimum Array End](https://leetcode.com/problems/minimum-array-end/) | Medium | 6/10 | 55.4% | [ ] |
| 751 | [IP to CIDR](https://leetcode.com/problems/ip-to-cidr/) :lock: | Medium | 6/10 | 53.6% | [ ] |
| 3766 | [Minimum Operations to Make Binary Palindrome](https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/) | Medium | 6/10 | 51.9% | [ ] |
| 3307 | [Find the K-th Character in String Game II](https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/) | Hard | 7/10 | 48.4% | [ ] |

## xor_prefix_sum

**What it is** — XOR prefix sums mirror the classic prefix-sum technique but use XOR instead of addition. Because XOR is its own inverse (`prefix[j] ^ prefix[i] == subarray XOR from i+1 to j`), you can answer range XOR queries in O(1) after O(n) preprocessing. Recognize this pattern when a problem asks for XOR of subarrays, counts of subarrays with a given XOR, or reconstruction of an original array from an encoded XOR sequence.

**Common steps**
1. Build the prefix XOR array: `pre[0] = 0`, `pre[i] = pre[i-1] ^ arr[i-1]`.
2. Answer a range query `[l, r]` as `pre[r+1] ^ pre[l]`.
3. For count-based problems (how many subarrays have XOR equal to k), use a hash map tracking how many times each prefix XOR value has appeared, similar to the two-sum pattern.
4. For reconstruction problems, work backwards: `arr[i] = pre[i] ^ pre[i-1]`.
5. For 2D grids, extend to a 2D prefix XOR table using the inclusion-exclusion principle.

**Key variations**
- Direct range query (XOR Queries of a Subarray — build prefix, answer each query in O(1)).
- Array reconstruction from encoded XOR (Decode XORed Array, Find The Original Array of Prefix Xor).
- Count subarrays/triplets with a specific XOR property (Count Triplets, Count Beautiful Subarrays — use hash map on prefix XORs).
- Maximize/minimize XOR under query constraints (Maximum XOR for Each Query — combine prefix XOR with greedy bit selection).
- 2D prefix XOR (Find Kth Largest XOR Coordinate Value).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1720 | [Decode XORed Array](https://leetcode.com/problems/decode-xored-array/) | Easy | 1/10 | 87.4% | [ ] |
| 2433 | [Find The Original Array of Prefix Xor](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/) | Medium | 3/10 | 88.3% | [ ] |
| 1310 | [XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/) | Medium | 3/10 | 78.1% | [ ] |
| 1829 | [Maximum XOR for Each Query](https://leetcode.com/problems/maximum-xor-for-each-query/) | Medium | 4/10 | 84.7% | [ ] |
| 1442 | [Count Triplets That Can Form Two Arrays of Equal XOR](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/) | Medium | 5/10 | 84.8% | [ ] |
| 1734 | [Decode XORed Permutation](https://leetcode.com/problems/decode-xored-permutation/) | Medium | 5/10 | 66.8% | [ ] |
| 2588 | [Count the Number of Beautiful Subarrays](https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/) | Medium | 5/10 | 54.0% | [ ] |
| 1738 | [Find Kth Largest XOR Coordinate Value](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/) | Medium | 6/10 | 64.3% | [ ] |
| 1177 | [Can Make Palindrome from Substring](https://leetcode.com/problems/can-make-palindrome-from-substring/) | Medium | 6/10 | 41.6% | [ ] |

## interactive_bit_reconstruction

**What it is** — In interactive bit reconstruction problems, you must discover an unknown number by querying an API that reveals information about specific bits — typically whether a particular bit is set. The core idea is to probe each bit position independently, reconstructing the number one bit at a time with at most 30-32 queries (one per bit position).

**Common steps**
1. Identify the bit range: determine how many bits the unknown number can have (usually up to 30 or 46 bits).
2. For each bit position i from 0 to max_bits - 1, query with a power-of-two value `1 << i`.
3. Interpret the response: if the query result indicates the bit is set, include `1 << i` in your answer.
4. Accumulate the result: `answer |= (1 << i)` for each bit confirmed as set.
5. Return the reconstructed number after all queries.

**Key variations**
- 30-bit reconstruction (Guess the Number I — one query per bit, up to 30 queries allowed).
- 46-bit reconstruction (Guess the Number II — number can be larger, requiring careful iteration over more bit positions).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3064 | [Guess the Number Using Bitwise Questions I](https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/) :lock: | Medium | 4/10 | 89.0% | [ ] |
| 3094 | [Guess the Number Using Bitwise Questions II](https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/) :lock: | Medium | 5/10 | 83.0% | [ ] |

## bit_shift_arithmetic

**What it is** — Bit shift arithmetic uses left shifts (`<< k`, equivalent to multiplying by 2^k) and right shifts (`>> k`, equivalent to floor division by 2^k) to perform arithmetic without standard operators, or to efficiently encode numeric relationships in binary. Recognize this pattern when a problem forbids division/multiplication, involves concatenating binary representations, or requires doubling/halving values repeatedly.

**Common steps**
1. Replace multiplication by 2^k with `n << k` and floor division by 2^k with `n >> k`.
2. For addition without `+`, use XOR for the sum bits and AND + left shift for the carry, iterating until there is no carry.
3. For division without operators, find the largest power-of-two multiple of the divisor that fits in the dividend using left shifts, subtract it, and accumulate the quotient.
4. When concatenating binary numbers, compute the current bit length with `n.bit_length()` (or track via shifting), then shift the running result left by that length and OR in the new number.
5. For maximization problems (Maximum OR), try shifting a chosen element left by k positions and greedily confirm it increases the OR of the full array.

**Key variations**
- Arithmetic without operators (Sum of Two Integers — XOR + carry loop; Divide Two Integers — repeated shift-and-subtract).
- Binary string concatenation via shifts (Concatenation of Consecutive Binary Numbers).
- Maximizing OR by shifting one element (Maximum OR — greedy with prefix/suffix OR arrays).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | 4/10 | 55.4% | [ ] |
| 1680 | [Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/) | Medium | 5/10 | 66.6% | [ ] |
| 2680 | [Maximum OR](https://leetcode.com/problems/maximum-or/) | Medium | 5/10 | 43.0% | [ ] |
| 29 | [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/) | Medium | 7/10 | 19.7% | [ ] |

## gray_code

**What it is** — Gray code is a binary numbering scheme where consecutive integers differ by exactly one bit. This pattern appears in problems that require generating a sequence of numbers where adjacent entries have a Hamming distance of 1, or in problems that ask you to count/minimize operations using the structure of Gray code (where each "digit" flips independently as you count).

**Common steps**
1. Recall the formula: the k-th Gray code value is `k ^ (k >> 1)`.
2. To generate all n-bit Gray codes in order, iterate k from 0 to `2^n - 1` and apply the formula.
3. For a circular permutation starting at a given value `start`, generate all Gray codes and XOR each with `start` to rotate the sequence.
4. For inverse problems (given a Gray code value, find its index), use the inverse Gray code formula: `idx = g; idx ^= (idx >> 1); idx ^= (idx >> 2); ...` until stable.
5. For operation-counting problems (Minimum One Bit Operations), recognize that the answer maps to the inverse Gray code index of the target.

**Key variations**
- Generate all n-bit Gray codes in order (Gray Code).
- Circular permutation: shift the standard sequence so it starts at a given value (Circular Permutation in Binary Representation).
- Minimum operations via Gray code inverse: the number of operations to reduce a value to zero equals its inverse Gray code index (Minimum One Bit Operations to Make Integers Zero — Hard).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1238 | [Circular Permutation in Binary Representation](https://leetcode.com/problems/circular-permutation-in-binary-representation/) | Medium | 4/10 | 72.7% | [ ] |
| 89 | [Gray Code](https://leetcode.com/problems/gray-code/) | Medium | 4/10 | 64.8% | [ ] |
| 1611 | [Minimum One Bit Operations to Make Integers Zero](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/) | Hard | 8/10 | 78.4% | [ ] |

## xor_game_theory

**What it is** — XOR game theory problems model two-player combinatorial games using Sprague-Grundy theorem or direct XOR analysis. The key insight is that in Nim-like games, the XOR (nim-sum) of all pile sizes determines the winner: if the XOR is non-zero the first player wins, if zero the second player wins. Recognize this when a problem involves two players taking turns removing elements and you need to determine who wins with optimal play.

**Common steps**
1. Compute the XOR of all relevant values (pile sizes, array elements, etc.).
2. If the XOR is 0, the current player is in a losing position (second player wins); otherwise the current player wins.
3. For array-based variants, also consider parity: if the array length is even, the XOR of all elements will always be 0 after both players play optimally, so the first player wins only if the total XOR is already 0.
4. For Chalkboard XOR Game specifically: the first player wins if the array length is even OR the total XOR is already 0.
5. Verify whether the problem is standard Nim or a variant with restricted moves, as restrictions change the Grundy values.

**Key variations**
- Classic Nim (Game of Nim — XOR all pile sizes; non-zero means first player wins).
- XOR removal game with array parity twist (Chalkboard XOR Game — winning condition involves both XOR and array length parity).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1908 | [Game of Nim](https://leetcode.com/problems/game-of-nim/) :lock: | Medium | 4/10 | 62.9% | [ ] |
| 810 | [Chalkboard XOR Game](https://leetcode.com/problems/chalkboard-xor-game/) | Hard | 7/10 | 66.1% | [ ] |

## bitmask_hashing

**What it is** — Bitmask hashing encodes a set of properties (typically character presence, color flags, or category membership) into a single integer, where each bit represents one property. This lets you compare, combine, or look up sets in O(1) using hash maps keyed by the bitmask. Recognize this pattern when elements have a small set of categorical attributes (26 letters, a few colors, k categories) and you need to count, match, or combine elements sharing those attributes.

**Common steps**
1. Map each property to a bit position (e.g., character `c` maps to bit `ord(c) - ord('a')`).
2. Build a bitmask for each element by OR-ing the bits of all its properties.
3. Store bitmasks in a hash map (value → count, or mask → list of indices) for fast lookup.
4. For matching problems, query the hash map using a transformed mask (e.g., complement, XOR with target).
5. For substring/subarray problems, combine with a prefix approach: maintain a running bitmask and look up previously seen masks.
6. Apply bit tricks to the masks as needed (e.g., `mask & (mask - 1)` to clear the lowest set bit when iterating submasks).

**Key variations**
- Character set encoding (Maximum Product of Word Lengths — encode each word's letters as a 26-bit mask, check `mask1 & mask2 == 0` for no common letters).
- State tracking with bitmask (Rings and Rods, Minimum Operations to Collect Elements — track which items have been seen using a bitmask).
- Prefix bitmask with hash map (Number of Wonderful Substrings — track parity of each character's count; count subarrays with at most one odd-count character).
- Puzzle/word matching (Number of Valid Words for Each Puzzle — enumerate submasks of each puzzle's bitmask).
- Protocol/format validation (UTF-8 Validation — parse leading bits to determine byte sequence length).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2103 | [Rings and Rods](https://leetcode.com/problems/rings-and-rods/) | Easy | 1/10 | 81.5% | [ ] |
| 2869 | [Minimum Operations to Collect Elements](https://leetcode.com/problems/minimum-operations-to-collect-elements/) | Easy | 2/10 | 62.3% | [ ] |
| 2128 | [Remove All Ones With Row and Column Flips](https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/) :lock: | Medium | 5/10 | 76.2% | [ ] |
| 318 | [Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/) | Medium | 5/10 | 61.2% | [ ] |
| 393 | [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/) | Medium | 5/10 | 46.2% | [ ] |
| 2135 | [Count Words Obtained After Adding a Letter](https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/) | Medium | 5/10 | 44.1% | [ ] |
| 1915 | [Number of Wonderful Substrings](https://leetcode.com/problems/number-of-wonderful-substrings/) | Medium | 6/10 | 66.6% | [ ] |
| 2564 | [Substring XOR Queries](https://leetcode.com/problems/substring-xor-queries/) | Medium | 6/10 | 35.6% | [ ] |
| 2857 | [Count Pairs of Points With Distance k](https://leetcode.com/problems/count-pairs-of-points-with-distance-k/) | Medium | 6/10 | 32.9% | [ ] |
| 982 | [Triples with Bitwise AND Equal To Zero](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/) | Hard | 7/10 | 60.0% | [ ] |
| 1178 | [Number of Valid Words for Each Puzzle](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/) | Hard | 7/10 | 47.8% | [ ] |
| 2732 | [Find a Good Subset of the Matrix](https://leetcode.com/problems/find-a-good-subset-of-the-matrix/) | Hard | 7/10 | 46.6% | [ ] |
| 782 | [Transform to Chessboard](https://leetcode.com/problems/transform-to-chessboard/) | Hard | 8/10 | 51.3% | [ ] |
| 1542 | [Find Longest Awesome Substring](https://leetcode.com/problems/find-longest-awesome-substring/) | Hard | 8/10 | 46.8% | [ ] |
| 3670 | [Maximum Product of Two Integers With No Common Bits](https://leetcode.com/problems/maximum-product-of-two-integers-with-no-common-bits/) | Medium | 8/10 | 15.2% | [ ] |

## bitmask_enumeration

**What it is** — Bitmask enumeration uses an integer's bits to represent a subset of a small set (typically n <= 20 elements), then iterates over all 2^n subsets to find the best one. You recognize this pattern when n is small (up to ~20), a problem asks you to try all subsets or all combinations of selections, and checking each subset is efficient.

**Common steps**
1. Confirm n is small enough: 2^n subsets must be feasible (n <= 20 for most problems, n <= 15 for harder checks).
2. Iterate all masks from `0` to `(1 << n) - 1`.
3. For each mask, extract which elements are selected: bit i is selected if `mask & (1 << i) != 0`.
4. Evaluate the subset (compute its score, check validity, etc.) and update the global best.
5. To enumerate only submasks of a given mask efficiently, use `sub = mask; while sub > 0: process(sub); sub = (sub - 1) & mask`.
6. Combine with prefix/suffix precomputation to speed up subset evaluation when possible.

**Key variations**
- Enumerate all subsets of rows/columns to maximize coverage (Maximum Rows Covered by Columns — choose k columns as a bitmask, count rows fully covered).
- Enumerate 3-element subsets via bitmask (Maximum Possible Number by Binary Concatenation).
- Logic/statement consistency checking (Maximum Good People Based on Statements — try each assignment of good/bad people as a bitmask).
- Partition into two subsets with equal product (Partition Array into Two Equal Product Subsets — enumerate which elements go to each half).
- Intersection with a fixed mask to count valid pairings (Number of Unique XOR Triplets).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3309 | [Maximum Possible Number by Binary Concatenation](https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/) | Medium | 4/10 | 65.5% | [ ] |
| 2397 | [Maximum Rows Covered by Columns](https://leetcode.com/problems/maximum-rows-covered-by-columns/) | Medium | 5/10 | 57.9% | [ ] |
| 2212 | [Maximum Points in an Archery Competition](https://leetcode.com/problems/maximum-points-in-an-archery-competition/) | Medium | 6/10 | 51.5% | [ ] |
| 3566 | [Partition Array into Two Equal Product Subsets](https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/) | Medium | 6/10 | 35.2% | [ ] |
| 3514 | [Number of Unique XOR Triplets II](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/) | Medium | 6/10 | 32.5% | [ ] |
| 2151 | [Maximum Good People Based on Statements](https://leetcode.com/problems/maximum-good-people-based-on-statements/) | Hard | 7/10 | 52.4% | [ ] |
| 3644 | [Maximum K to Sort a Permutation](https://leetcode.com/problems/maximum-k-to-sort-a-permutation/) | Medium | 8/10 | 37.4% | [ ] |
| 3757 | [Number of Effective Subsequences](https://leetcode.com/problems/number-of-effective-subsequences/) | Hard | 9/10 | 31.3% | [ ] |
| 3630 | [Partition Array for Maximum XOR and AND](https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/) | Hard | 9/10 | 17.7% | [ ] |

## linear_algebra_xor_basis

**What it is** — A linear XOR basis (also called a linear basis over GF(2)) is a set of at most 30 integers that can represent any value achievable by XOR-ing a subset of the original array. Building this basis using Gaussian elimination lets you quickly determine the maximum XOR achievable, check reachability, or count distinct XOR values. Recognize this pattern when the problem asks for the maximum XOR of any subset, or whether a target XOR is achievable from a collection of numbers.

**Common steps**
1. Initialize an empty basis array of size 30 (one slot per bit position).
2. For each number, attempt to insert it into the basis: for each bit from high to low, if the current bit is set and the basis slot is empty, place the number there and stop; otherwise XOR the number with the basis element at that bit to eliminate the leading bit.
3. After building the basis, to find the maximum XOR value, greedily XOR in each basis element if it increases the current value (from high bit to low bit).
4. To check if a target value is representable, try to reduce it using the basis — if it reduces to 0, it is representable.
5. The number of distinct XOR values achievable is `2^(basis size)`.

**Key variations**
- Maximum XOR of any subsequence (find the max achievable XOR using the greedy basis query).
- Reachability: can we XOR elements to reach a target? (Reduce the target through the basis.)
- Combined with other data structures (Maximum XOR of Subsequences — may involve merging two bases or applying the basis to combined arrays).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3702 | [Longest Subsequence With Non-Zero Bitwise XOR](https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/) | Medium | 6/10 | 37.3% | [ ] |
| 3681 | [Maximum XOR of Subsequences](https://leetcode.com/problems/maximum-xor-of-subsequences/) | Hard | 8/10 | 51.3% | [ ] |

## bitmask_dp

**What it is** — Bitmask DP stores the current "state" of a subset of elements as a bitmask in the DP table, enabling efficient transitions between subsets. It is used when the number of items is small (n <= 20) and the optimal solution depends on which subset has already been processed. Recognize this when a problem involves assigning items to groups, visiting states in order, or tracking which elements have been used, and n is small.

**Common steps**
1. Define `dp[mask]` where each bit of `mask` indicates whether that element has been included/processed.
2. Initialize `dp[0] = base_case` (empty subset).
3. Iterate masks from 0 to `(1 << n) - 1`; for each mask, try adding one more element (bit i not yet in mask) and update `dp[mask | (1 << i)]`.
4. Use precomputed values (e.g., subarray XOR/AND) to make each transition O(1) or O(log n) rather than recomputing from scratch.
5. For OR/AND-based DP (distinct values of OR over subarrays), maintain a set of distinct values reachable at each position — this set has at most O(log(max_val)) distinct entries because each new element can only create O(30) new OR values.
6. Return `dp[(1 << n) - 1]` or the relevant final mask value.

**Key variations**
- BFS with bitmask state (Minimum Flips to Convert Binary Matrix — each matrix state is a bitmask; use BFS to find fewest flips).
- Distinct OR/AND values over subarrays (Bitwise ORs of Subarrays, Number of Subarrays With AND Value of K — the key insight is that distinct OR/AND values per ending index is O(30)).
- Maximum Hamming distance across all bitmask states (Maximum Hamming Distances — DP over complement masks).
- Tracking shrinking sets via AND (Find a Value of a Mysterious Function Closest to Target — AND can only decrease, so distinct AND values per right endpoint is O(30)).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1284 | [Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/) | Hard | 7/10 | 72.5% | [ ] |
| 898 | [Bitwise ORs of Subarrays](https://leetcode.com/problems/bitwise-ors-of-subarrays/) | Medium | 7/10 | 56.9% | [ ] |
| 3141 | [Maximum Hamming Distances](https://leetcode.com/problems/maximum-hamming-distances/) :lock: | Hard | 8/10 | 49.4% | [ ] |
| 1521 | [Find a Value of a Mysterious Function Closest to Target](https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/) | Hard | 8/10 | 47.2% | [ ] |
| 3209 | [Number of Subarrays With AND Value of K](https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/) | Hard | 8/10 | 35.3% | [ ] |
| 3806 | [Maximum Bitwise AND After Increment Operations](https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/) | Hard | 9/10 | 31.7% | [ ] |
| 3435 | [Frequencies of Shortest Supersequences](https://leetcode.com/problems/frequencies-of-shortest-supersequences/) | Hard | 9/10 | 22.3% | [ ] |

## meet_in_the_middle

**What it is** — Meet in the middle splits an exponential search space in half, solves each half independently, then combines the results. For a set of n elements where 2^n is too large to enumerate, split into two halves of n/2 elements each (giving 2^(n/2) subsets per half), enumerate all subsets of each half, then combine using sorting and binary search. Recognize this when n is around 30-40 (too large for full enumeration but 2^(n/2) is manageable) and the problem asks for a subset with a target sum/XOR or closest value.

**Common steps**
1. Split the array into two halves of roughly equal size.
2. Enumerate all 2^(n/2) subsets of each half, computing the target metric (sum, XOR, etc.) for each subset.
3. Sort one half's results.
4. For each subset result from the other half, binary search in the sorted half to find the best complement (exact match, closest value, etc.).
5. Update the global answer based on the combined result.
6. Handle edge cases: empty subsets (value 0), duplicate values in the sorted list, and the constraint that both halves together must respect any global constraint.

**Key variations**
- Closest sum to target (Closest Subsequence Sum — split into halves, sort one half, binary search for complement).
- Minimum sum difference between two partitions (Partition Array Into Two Arrays to Minimize Sum Difference — enumerate all subset sums for each half grouped by size, then pair sizes that add to n/2).
- Minimum removals to achieve a target XOR (Minimum Removals to Achieve Target XOR — use meet-in-the-middle over subsets).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3877 | [Minimum Removals to Achieve Target XOR](https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/) | Medium | 7/10 | 41.7% | [ ] |
| 1755 | [Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/) | Hard | 9/10 | 43.6% | [ ] |
| 2035 | [Partition Array Into Two Arrays to Minimize Sum Difference](https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/) | Hard | 9/10 | 23.4% | [ ] |

## digit_dp_bitmask

**What it is** — Digit DP with bitmask combines digit DP (building a number digit by digit while tracking constraints like "number must be <= N" and "number must have exactly k set bits") with bitmask state to track which digits or bit-pattern constraints have been satisfied so far. Recognize this when a problem asks you to count or find numbers up to a limit satisfying complex binary/digit constraints that can be encoded as a small bitmask of flags.

**Common steps**
1. Define the DP state: `dp[position][tight][bitmask_state]` where `tight` tracks whether the current prefix is still bounded by the limit, and `bitmask_state` encodes the relevant constraint flags.
2. Process digits from the most significant bit/digit to the least significant.
3. At each position, try placing each valid digit (0 or 1 for binary), updating `tight` and `bitmask_state` accordingly.
4. Use memoization over `(position, tight, bitmask_state)` to avoid recomputation.
5. At the base case (all positions filled), check whether `bitmask_state` satisfies the final constraint and return 1 or 0 accordingly.
6. Sum over all valid completions to get the final count.

**Key variations**
- Count integers up to N with exactly k one-bits (Find Nth Smallest Integer With K One Bits — find the n-th such integer rather than count, using binary search + digit DP or direct greedy bit placement).
- Count palindromic numbers in binary with additional digit constraints (Count Binary Palindromic Numbers — must track both the palindrome structure and digit positions as bitmask state).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 3821 | [Find Nth Smallest Integer With K One Bits](https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/) | Hard | 8/10 | 34.8% | [ ] |
| 3677 | [Count Binary Palindromic Numbers](https://leetcode.com/problems/count-binary-palindromic-numbers/) | Hard | 9/10 | 33.8% | [ ] |
