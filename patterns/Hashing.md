# Hashing

107 problems across 14 patterns.

## frequency_counting

**What it is:** Frequency counting uses a hash map to tally how many times each element (character, number, word) appears in a collection. You recognize this pattern when a problem asks about duplicates, uniqueness, anagrams, character matching, or "how many of X are there" — anything where the count of each item matters.

**Common steps:**
1. Create an empty hash map (or use a fixed-size array for characters, e.g., `count[26]` for lowercase letters).
2. Iterate through the input and increment `count[element]` for each item seen.
3. If comparing two inputs (e.g., anagram check), build a frequency map for each, then compare them.
4. Iterate through the frequency map to answer the question (sum unique elements, find max frequency, filter by count, etc.).
5. Return the result based on the counts (e.g., return True if all frequencies match, return the element with count == 1, etc.).

**Key variations:**
- Single array/string: count occurrences, then query (Sum of Unique Elements, First Unique Character).
- Two inputs: build a count for each and compare or subtract (Valid Anagram, Ransom Note, Intersection).
- Constrained count: check if one set of counts can satisfy another (Find Words Formed by Characters, Maximum Number of Balloons).
- Sort by frequency: build count map, then sort items by their frequency value (Sort Array by Increasing Frequency, Sort Characters By Frequency).
- Multi-element constraint: find the maximum frequency across multiple character requirements simultaneously (Word Subsets).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1748 | [Sum of Unique Elements](https://leetcode.com/problems/sum-of-unique-elements/) | Easy | 1/10 | 79.9% | [ ] |
| 2357 | [Make Array Zero by Subtracting Equal Amounts](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/) | Easy | 1/10 | 73.8% | [ ] |
| 1133 | [Largest Unique Number](https://leetcode.com/problems/largest-unique-number/) :lock: | Easy | 1/10 | 71.3% | [ ] |
| 383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) | Easy | 1/10 | 65.9% | [ ] |
| 1512 | [Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/) | Easy | 2/10 | 89.8% | [ ] |
| 2965 | [Find Missing and Repeated Values](https://leetcode.com/problems/find-missing-and-repeated-values/) | Easy | 2/10 | 83.2% | [ ] |
| 1636 | [Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/) | Easy | 2/10 | 80.8% | [ ] |
| 2341 | [Maximum Number of Pairs in Array](https://leetcode.com/problems/maximum-number-of-pairs-in-array/) | Easy | 2/10 | 76.1% | [ ] |
| 884 | [Uncommon Words from Two Sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences/) | Easy | 2/10 | 75.7% | [ ] |
| 2283 | [Check if Number Has Equal Digit Count and Digit Value](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/) | Easy | 2/10 | 73.2% | [ ] |
| 1160 | [Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) | Easy | 2/10 | 71.6% | [ ] |
| 266 | [Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) :lock: | Easy | 2/10 | 68.7% | [ ] |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | 2/10 | 68.1% | [ ] |
| 1897 | [Redistribute Characters to Make All Strings Equal](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/) | Easy | 2/10 | 66.9% | [ ] |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | Easy | 2/10 | 65.4% | [ ] |
| 2347 | [Best Poker Hand](https://leetcode.com/problems/best-poker-hand/) | Easy | 2/10 | 61.7% | [ ] |
| 2287 | [Rearrange Characters to Make Target String](https://leetcode.com/problems/rearrange-characters-to-make-target-string/) | Easy | 2/10 | 61.2% | [ ] |
| 1128 | [Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/) | Easy | 2/10 | 60.7% | [ ] |
| 1189 | [Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/) | Easy | 2/10 | 60.2% | [ ] |
| 350 | [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/) | Easy | 2/10 | 59.9% | [ ] |
| 2404 | [Most Frequent Even Element](https://leetcode.com/problems/most-frequent-even-element/) | Easy | 2/10 | 53.6% | [ ] |
| 1198 | [Find Smallest Common Element in All Rows](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/) :lock: | Medium | 3/10 | 76.8% | [ ] |
| 451 | [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | Medium | 3/10 | 75.3% | [ ] |
| 1002 | [Find Common Characters](https://leetcode.com/problems/find-common-characters/) | Easy | 3/10 | 74.7% | [ ] |
| 748 | [Shortest Completing Word](https://leetcode.com/problems/shortest-completing-word/) | Easy | 3/10 | 63.1% | [ ] |
| 819 | [Most Common Word](https://leetcode.com/problems/most-common-word/) | Easy | 3/10 | 45.1% | [ ] |
| 645 | [Set Mismatch](https://leetcode.com/problems/set-mismatch/) | Easy | 3/10 | 43.7% | [ ] |
| 299 | [Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/) | Medium | 4/10 | 52.5% | [ ] |
| 916 | [Word Subsets](https://leetcode.com/problems/word-subsets/) | Medium | 5/10 | 55.9% | [ ] |

## set_lookup

**What it is:** Set lookup uses a hash set to answer membership queries in O(1) time — "have I seen this element before?" or "does this value exist in the collection?" Recognize this pattern when a problem involves checking existence, detecting duplicates, or finding elements that appear in multiple collections, without caring about counts.

**Common steps:**
1. Decide what to store in the set (raw values, transformed values, visited states, etc.).
2. Populate the set by iterating through one input (or build it incrementally as you go).
3. For each element in the second input (or as you scan), check `if element in set`.
4. Take the appropriate action on a hit (increment counter, return True, record the element, etc.).
5. Handle the no-hit case (return False, continue scanning, etc.).

**Key variations:**
- Existence check in one pass: add to set and simultaneously check before adding (Contains Duplicate, First Letter to Appear Twice).
- Cross-collection lookup: build a set from one collection and query it while iterating the other (Jewels and Stones, Intersection of Two Arrays).
- State tracking: encode a state (e.g., coordinate pair, digit-sum) as the set key to detect revisits (Path Crossing, Happy Number).
- Sequence building: use the set to efficiently find sequence starts or extensions (Longest Consecutive Sequence).
- Complement or derived value lookup: check for a mathematically derived value (e.g., `-x` for a given `x`) in the set (Largest Positive Integer That Exists With Its Negative).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 771 | [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/) | Easy | 1/10 | 89.5% | [ ] |
| 1684 | [Count the Number of Consistent Strings](https://leetcode.com/problems/count-the-number-of-consistent-strings/) | Easy | 1/10 | 88.5% | [ ] |
| 1832 | [Check if the Sentence Is Pangram](https://leetcode.com/problems/check-if-the-sentence-is-pangram/) | Easy | 1/10 | 84.2% | [ ] |
| 804 | [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) | Easy | 1/10 | 83.6% | [ ] |
| 2351 | [First Letter to Appear Twice](https://leetcode.com/problems/first-letter-to-appear-twice/) | Easy | 1/10 | 75.0% | [ ] |
| 500 | [Keyboard Row](https://leetcode.com/problems/keyboard-row/) | Easy | 1/10 | 73.8% | [ ] |
| 2309 | [Greatest English Letter in Upper and Lower Case](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/) | Easy | 1/10 | 72.0% | [ ] |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | 1/10 | 64.3% | [ ] |
| 2367 | [Number of Arithmetic Triplets](https://leetcode.com/problems/number-of-arithmetic-triplets/) | Easy | 2/10 | 85.5% | [ ] |
| 349 | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | Easy | 2/10 | 77.7% | [ ] |
| 2441 | [Largest Positive Integer That Exists With Its Negative](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/) | Easy | 2/10 | 74.5% | [ ] |
| 2395 | [Find Subarrays With Equal Sum](https://leetcode.com/problems/find-subarrays-with-equal-sum/) | Easy | 2/10 | 67.0% | [ ] |
| 1496 | [Path Crossing](https://leetcode.com/problems/path-crossing/) | Easy | 2/10 | 62.6% | [ ] |
| 734 | [Sentence Similarity](https://leetcode.com/problems/sentence-similarity/) :lock: | Easy | 2/10 | 44.8% | [ ] |
| 2657 | [Find the Prefix Common Array of Two Arrays](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/) | Medium | 3/10 | 86.9% | [ ] |
| 2442 | [Count Number of Distinct Integers After Reverse Operations](https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/) | Medium | 3/10 | 81.5% | [ ] |
| 202 | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | 3/10 | 59.6% | [ ] |
| 822 | [Card Flipping Game](https://leetcode.com/problems/card-flipping-game/) | Medium | 4/10 | 50.3% | [ ] |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | 5/10 | 47.1% | [x] |
| 2306 | [Naming a Company](https://leetcode.com/problems/naming-a-company/) | Hard | 7/10 | 46.5% | [ ] |

## bijective_mapping

**What it is:** Bijective mapping (also called one-to-one mapping) uses two hash maps simultaneously to enforce that the relationship between two domains is a strict two-way correspondence — every key maps to exactly one value, and every value maps to exactly one key. Recognize this when a problem asks whether two sequences are "structurally identical" or follow the same pattern (isomorphic strings, word patterns, decodings).

**Common steps:**
1. Create two maps: `a_to_b` and `b_to_a` (one for each direction of the mapping).
2. Iterate through both sequences in parallel (element by element).
3. For each pair `(x, y)`, check if `x` is already in `a_to_b`:
   - If yes, verify `a_to_b[x] == y`. If not, return False (conflict).
   - If no, check that `y` is not already in `b_to_a` (would create a many-to-one mapping). If it is, return False.
4. If no conflict, record both `a_to_b[x] = y` and `b_to_a[y] = x`.
5. After the loop, return True.

**Key variations:**
- Decode/translate: apply the mapping to transform one sequence into another (Decode the Message).
- Validate isomorphism: check that two sequences share the exact same structure (Isomorphic Strings, Word Pattern).
- Filter by pattern: find all strings in a list that match a given pattern's structure (Find and Replace Pattern).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2325 | [Decode the Message](https://leetcode.com/problems/decode-the-message/) | Easy | 2/10 | 85.8% | [ ] |
| 205 | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | Easy | 3/10 | 48.3% | [ ] |
| 290 | [Word Pattern](https://leetcode.com/problems/word-pattern/) | Easy | 3/10 | 44.1% | [ ] |
| 890 | [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) | Medium | 4/10 | 77.0% | [ ] |

## index_position_tracking

**What it is:** Index/position tracking stores the index (or position) at which each element was last seen, or first seen, in a hash map. Recognize this when a problem involves finding distances between repeated elements, detecting cycles at positions, or needing to look up "where did I last see this value?" during a single pass.

**Common steps:**
1. Create an empty map: `last_seen = {}` (maps element -> index).
2. Iterate through the input with an index `i`.
3. For each element, check if it already exists in `last_seen`:
   - If yes, compute something using `i - last_seen[element]` (distance, gap, cycle length, etc.).
   - Apply any necessary update (e.g., track the maximum distance found so far).
4. Update `last_seen[element] = i` (store or overwrite with the current index).
5. Return the computed result after the loop.

**Key variations:**
- First vs. last occurrence: store only the first index seen and never overwrite (Largest Substring Between Two Equal Characters).
- Position-to-character keyboard lookup: map characters to fixed positions for cost calculation (Single-Row Keyboard, Alphabet Board Path).
- Cycle/repeat detection in computation: store intermediate states with their index to detect when a cycle begins (Fraction to Recurring Decimal).
- Validation using stored positions: look up stored positions and compare against expected values (Check Distances Between Same Letters).
- Row/column painting: map values to their grid coordinates to track paint progress (First Completely Painted Row or Column).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1165 | [Single-Row Keyboard](https://leetcode.com/problems/single-row-keyboard/) :lock: | Easy | 1/10 | 87.8% | [ ] |
| 760 | [Find Anagram Mappings](https://leetcode.com/problems/find-anagram-mappings/) :lock: | Easy | 1/10 | 84.0% | [ ] |
| 2399 | [Check Distances Between Same Letters](https://leetcode.com/problems/check-distances-between-same-letters/) | Easy | 2/10 | 71.5% | [ ] |
| 1624 | [Largest Substring Between Two Equal Characters](https://leetcode.com/problems/largest-substring-between-two-equal-characters/) | Easy | 2/10 | 68.3% | [ ] |
| 1640 | [Check Array Formation Through Concatenation](https://leetcode.com/problems/check-array-formation-through-concatenation/) | Easy | 3/10 | 57.3% | [ ] |
| 2295 | [Replace Elements in an Array](https://leetcode.com/problems/replace-elements-in-an-array/) | Medium | 4/10 | 59.8% | [ ] |
| 1138 | [Alphabet Board Path](https://leetcode.com/problems/alphabet-board-path/) | Medium | 4/10 | 51.8% | [ ] |
| 1794 | [Count Pairs of Equal Substrings With Minimum Difference](https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/) :lock: | Medium | 5/10 | 64.0% | [ ] |
| 2661 | [First Completely Painted Row or Column](https://leetcode.com/problems/first-completely-painted-row-or-column/) | Medium | 5/10 | 63.9% | [ ] |
| 166 | [Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/) | Medium | 7/10 | 30.9% | [ ] |

## aggregation_with_ranking

**What it is:** Aggregation with ranking uses a hash map to accumulate values (sum, count, set of events) per key, and then identifies the top-ranked key or keys by comparing aggregate values. Recognize this pattern when a problem asks "which entity has the most/highest X?" where data about each entity arrives across multiple entries.

**Common steps:**
1. Create a hash map: `agg = {}` (maps key -> accumulated value).
2. Iterate through the data. For each record, extract the key and the value to aggregate.
3. Update the accumulator: `agg[key] += value` (or `agg[key].add(event)` for unique counts, etc.).
4. After processing all data, scan the map to find the key with the maximum aggregate value.
5. Handle ties as required by the problem (e.g., return all tied keys, choose lexicographically smallest, etc.).

**Key variations:**
- Count events: accumulate a count of occurrences per key (Sender With Largest Word Count).
- Aggregate a numeric value: sum scores or weights per key (Merge Similar Items, Most Popular Video Creator).
- Unique event tracking: store a set per key to count distinct events (Finding the Users Active Minutes).
- Sort output by aggregated value: compute aggregates, then sort the keys by their totals (Sort Features by Popularity).
- Multiple aggregate fields: track both a primary and tiebreaker metric per key simultaneously (Most Popular Video Creator).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2363 | [Merge Similar Items](https://leetcode.com/problems/merge-similar-items/) | Easy | 2/10 | 77.5% | [ ] |
| 1817 | [Finding the Users Active Minutes](https://leetcode.com/problems/finding-the-users-active-minutes/) | Medium | 3/10 | 80.8% | [ ] |
| 2284 | [Sender With Largest Word Count](https://leetcode.com/problems/sender-with-largest-word-count/) | Medium | 3/10 | 59.7% | [ ] |
| 1772 | [Sort Features by Popularity](https://leetcode.com/problems/sort-features-by-popularity/) :lock: | Medium | 4/10 | 66.5% | [ ] |
| 2456 | [Most Popular Video Creator](https://leetcode.com/problems/most-popular-video-creator/) | Medium | 5/10 | 45.3% | [ ] |

## string_canonicalization

**What it is:** String canonicalization converts each string into a standardized "canonical" form (a normalized key) so that strings that are equivalent under some transformation all map to the same key. You then use a set or map keyed by these canonical forms to group or count equivalent strings. Recognize this when a problem asks you to find strings that are "the same" under some rule (same characters, same structure, same pattern).

**Common steps:**
1. Define the transformation rule that produces a canonical key for a string (e.g., sort its characters, extract character set, encode relative character shifts).
2. Create a set or map to store canonical forms.
3. For each string, compute its canonical key using the transformation.
4. Insert the key into the set/map or look it up to find matching groups.
5. Use the set/map contents to answer the question (count groups, count pairs, identify equivalences).

**Key variations:**
- Sorted characters as key: sort the string's characters to group anagrams or similar strings (used heavily in grouping_by_key as well).
- Character set as key: convert a string to a frozenset or sorted unique characters to find strings sharing the same character inventory (Count Pairs Of Similar Strings).
- Positional character set as key: separate even-indexed and odd-indexed characters before sorting (Groups of Special-Equivalent Strings).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2506 | [Count Pairs Of Similar Strings](https://leetcode.com/problems/count-pairs-of-similar-strings/) | Easy | 3/10 | 73.8% | [ ] |
| 893 | [Groups of Special-Equivalent Strings](https://leetcode.com/problems/groups-of-special-equivalent-strings/) | Medium | 4/10 | 73.6% | [ ] |

## two_sum_pair

**What it is:** Two-sum pair uses a hash map to find pairs of elements that satisfy a numeric relationship (sum, difference, product) in a single pass. Instead of checking every pair in O(n^2), you store elements you have already seen and check, for the current element, whether its required "partner" is already in the map. Recognize this when a problem asks for pairs, triplets, or tuples satisfying an equation involving two or more elements.

**Common steps:**
1. Create an empty map: `seen = {}` (maps value -> index or count, depending on the problem).
2. Iterate through the array with index `i` and current element `x`.
3. Compute the required complement: `complement = target - x` (or the appropriate formula).
4. Check if `complement` is in `seen`:
   - If yes, a valid pair is found — record or count it.
5. Add `x` to `seen` (map `x -> i` or increment its count).
6. Return the result after the loop.

**Key variations:**
- Single target sum: find one pair summing to a fixed target (Two Sum).
- Difference k: find pairs with absolute difference equal to k (K-diff Pairs in an Array).
- Multiple targets: check divisibility or power-of-two conditions on the sum (Count Good Meals, Tuple with Same Product).
- Four-number sum: hash sums of pairs from two arrays, then look up complements from the other two (4Sum II).
- Maintain a data structure (add/find API): design a class supporting repeated adds and lookups (Two Sum III).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | 2/10 | 57.4% | [x] |
| 888 | [Fair Candy Swap](https://leetcode.com/problems/fair-candy-swap/) | Easy | 3/10 | 64.9% | [ ] |
| 532 | [K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) | Medium | 4/10 | 45.9% | [ ] |
| 170 | [Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/) :lock: | Easy | 4/10 | 39.1% | [ ] |
| 1726 | [Tuple with Same Product](https://leetcode.com/problems/tuple-with-same-product/) | Medium | 5/10 | 70.1% | [ ] |
| 454 | [4Sum II](https://leetcode.com/problems/4sum-ii/) | Medium | 5/10 | 58.0% | [ ] |
| 1577 | [Number of Ways Where Square of Number Is Equal to Product of Two Numbers](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/) | Medium | 5/10 | 43.4% | [ ] |
| 1711 | [Count Good Meals](https://leetcode.com/problems/count-good-meals/) | Medium | 5/10 | 32.8% | [ ] |

## frequency_of_frequency

**What it is:** Frequency of frequency is a two-level hashing technique: first build a frequency map (element -> count), then build a second map (count -> how many elements have that count). Recognize this pattern when a problem asks whether frequencies are "all equal," "all unique," or can be made so by performing one operation.

**Common steps:**
1. Build the first-level frequency map: `freq[element] = count`.
2. Build the second-level map: `freq_of_freq[count] += 1` by iterating over the values in the first map.
3. Analyze the distribution of frequencies using the second-level map (e.g., check if all values in `freq_of_freq` are 1, or if there is only one distinct frequency).
4. If the problem allows one deletion or modification, enumerate the edge cases where one small change makes the distribution valid.
5. Return True/False or the maximum prefix length based on your analysis.

**Key variations:**
- Uniqueness of occurrences: verify that no two elements share the same count (Unique Number of Occurrences).
- Equivalence under one removal: check whether removing one element from one string makes both strings' frequency multisets equal (Determine if Two Strings Are Close).
- One-character deletion: check if removing a single letter makes all remaining frequencies equal (Remove Letter To Equalize Frequency).
- Maximum valid prefix: find the longest prefix where, after one adjustment, all frequencies become equal (Maximum Equal Frequency — hardest variation).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1207 | [Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/) | Easy | 2/10 | 78.7% | [ ] |
| 1657 | [Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/) | Medium | 4/10 | 54.3% | [ ] |
| 2423 | [Remove Letter To Equalize Frequency](https://leetcode.com/problems/remove-letter-to-equalize-frequency/) | Easy | 4/10 | 19.4% | [ ] |
| 1224 | [Maximum Equal Frequency](https://leetcode.com/problems/maximum-equal-frequency/) | Hard | 8/10 | 38.1% | [ ] |

## grouping_by_key

**What it is:** Grouping by key maps each element to a computed key that captures its equivalence class, then collects all elements sharing the same key into a list or set. Recognize this when a problem asks you to cluster items together based on some shared structural property (same sorted characters, same digit sum, same distance profile).

**Common steps:**
1. Define the key function that captures what makes two elements "equivalent" (e.g., sort the string, compute digit sum, normalize relative character shifts).
2. Create a map: `groups = defaultdict(list)`.
3. For each element, compute its key and append the element to `groups[key]`.
4. After grouping, process each group to answer the question (return groups, count pairs within groups, find the maximum, etc.).
5. When counting pairs within a group of size n, use `n * (n - 1) / 2` if all pairs are valid.

**Key variations:**
- Return all groups: collect and return the lists directly (Group Anagrams, Find Duplicate File in System).
- Count pairs within groups: for each group of size n, count `n*(n-1)/2` pairs (Number of Boomerangs, Count Nice Pairs).
- Find maximum across groups: track the best element within each group during aggregation (Max Sum of a Pair With Equal Sum of Digits).
- Hierarchical or multi-level keys: group by a compound key involving multiple attributes (Analyze User Website Visit Pattern).
- Aggregated counts per group: sum visit counts or scores before comparing groups (Subdomain Visit Count).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 811 | [Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/) | Medium | 3/10 | 77.2% | [ ] |
| 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | 4/10 | 72.5% | [ ] |
| 609 | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) | Medium | 4/10 | 67.5% | [ ] |
| 2342 | [Max Sum of a Pair With Equal Sum of Digits](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) | Medium | 4/10 | 65.9% | [ ] |
| 447 | [Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs/) | Medium | 4/10 | 57.5% | [ ] |
| 1814 | [Count Nice Pairs in an Array](https://leetcode.com/problems/count-nice-pairs-in-an-array/) | Medium | 4/10 | 48.5% | [ ] |
| 249 | [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings/) :lock: | Medium | 5/10 | 67.8% | [ ] |
| 288 | [Unique Word Abbreviation](https://leetcode.com/problems/unique-word-abbreviation/) :lock: | Medium | 5/10 | 27.5% | [ ] |
| 1169 | [Invalid Transactions](https://leetcode.com/problems/invalid-transactions/) | Medium | 6/10 | 32.2% | [ ] |
| 1152 | [Analyze User Website Visit Pattern](https://leetcode.com/problems/analyze-user-website-visit-pattern/) :lock: | Medium | 7/10 | 44.3% | [ ] |

## matrix_set_validation

**What it is:** Matrix set validation uses hash sets (one per row, column, or region) to verify constraints on a 2D grid — typically that no value appears more than once within each unit. Recognize this pattern when a problem involves validating or comparing rows and columns of a matrix, or checking for uniqueness across multiple dimensions simultaneously.

**Common steps:**
1. Identify the units to validate (rows, columns, subgrids, or row-as-string vs column-as-string).
2. Create a set (or map) for each unit: `rows[i]`, `cols[j]`, `boxes[b]`, etc.
3. Iterate over every cell `(i, j)` in the matrix.
4. For the value at `(i, j)`, check membership in all relevant sets. If already present, return False (or record a conflict).
5. If not present, insert the value into all relevant sets and continue.
6. Return True after processing all cells (or the count of valid units / matched pairs).

**Key variations:**
- Multi-dimensional constraint validation: check rows, columns, and subgrids simultaneously (Valid Sudoku).
- Row-to-column string matching: convert rows and columns to canonical strings and count intersections using a map (Equal Row and Column Pairs).
- Sparse matrix optimization: skip zero entries and only hash non-zero positions (Sparse Matrix Multiplication).
- Geometric constraint: verify that points are symmetric about a line using a coordinate set (Line Reflection).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2352 | [Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/) | Medium | 5/10 | 70.9% | [ ] |
| 311 | [Sparse Matrix Multiplication](https://leetcode.com/problems/sparse-matrix-multiplication/) :lock: | Medium | 5/10 | 69.3% | [ ] |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | 5/10 | 64.5% | [ ] |
| 356 | [Line Reflection](https://leetcode.com/problems/line-reflection/) :lock: | Medium | 5/10 | 36.3% | [ ] |

## modular_arithmetic_hash

**What it is:** Modular arithmetic hash uses the remainder (`x % k`) as a hash key to group numbers by their residue class, enabling efficient pair or tuple finding under divisibility constraints. Recognize this when a problem asks about pairs or groups summing to (or differing by) a multiple of some number k.

**Common steps:**
1. Identify the modulus `k` from the problem (e.g., divisible by 60, divisible by k).
2. Create a frequency map: `remainder_count[r]` = how many elements have `element % k == r`.
3. For each element `x`, compute `r = x % k` and its required complement remainder `(k - r) % k`.
4. Check `remainder_count[complement]` to find valid pairings (be careful with `r == 0` and `r == k/2` edge cases where an element pairs with itself).
5. Accumulate the count and return the result.

**Key variations:**
- Pair divisibility: count pairs whose sum is divisible by k, handling the zero and mid-point remainders specially (Pairs of Songs Divisible by 60, Check If Array Pairs Are Divisible by k).
- Group by remainder for sequence targeting: elements with the same remainder under the step size belong to the same "destruction group" (Destroy Sequential Targets).
- Character shift cycles: track how many times each shift distance has been used modulo the alphabet to determine feasibility (Can Convert String in K Moves).
- Three-element combinations: extend the two-sum complement idea to triplets by iterating over pairs and using the map for the third element (3Sum With Multiplicity).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1010 | [Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) | Medium | 4/10 | 53.5% | [ ] |
| 1497 | [Check If Array Pairs Are Divisible by k](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/) | Medium | 5/10 | 46.2% | [ ] |
| 2453 | [Destroy Sequential Targets](https://leetcode.com/problems/destroy-sequential-targets/) | Medium | 5/10 | 42.0% | [ ] |
| 1540 | [Can Convert String in K Moves](https://leetcode.com/problems/can-convert-string-in-k-moves/) | Medium | 5/10 | 37.7% | [ ] |
| 923 | [3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/) | Medium | 6/10 | 46.3% | [ ] |

## prefix_sum_hash

**What it is:** Prefix sum hash combines the prefix sum technique with a hash map to efficiently answer subarray queries. As you scan the array, you maintain a running prefix sum and store previously seen prefix sums in a map. The key insight is that if `prefix[j] - prefix[i] == target`, then the subarray `[i+1..j]` has sum equal to target — and you can check this in O(1) by looking up `prefix[j] - target` in the map. Recognize this when a problem asks about subarrays with a specific sum, equal count of two elements, or divisibility conditions on subarray sums.

**Common steps:**
1. Initialize `prefix_sum = 0` and a map `seen = {0: 1}` (the base case: a prefix sum of 0 exists once before the array starts).
2. Iterate through the array, updating `prefix_sum += element` at each step.
3. Compute the required previous prefix sum: `needed = prefix_sum - target`.
4. Check if `needed` is in `seen`. If yes, add `seen[needed]` to the answer count (or record the index for the longest subarray).
5. Update `seen[prefix_sum] += 1` (or store the earliest index if looking for longest subarray).

**Key variations:**
- Count subarrays with exact sum: accumulate count of subarrays summing to k (standard prefix sum hash).
- Longest subarray with exact sum: store the first index where each prefix sum occurs, not a count (Maximum Size Subarray Sum Equals k).
- Equal count of two values (0s and 1s): remap 0 -> -1, then find subarrays with sum 0 using the same technique (Contiguous Array).
- Divisibility constraint: store `prefix_sum % k` as the key; a repeated remainder means the subarray between is divisible by k (Continuous Subarray Sum).
- Count "bad" pairs using algebra: rearrange the pair condition into a prefix-sum-like formula and use a map to count (Count Number of Bad Pairs).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 2364 | [Count Number of Bad Pairs](https://leetcode.com/problems/count-number-of-bad-pairs/) | Medium | 5/10 | 54.2% | [ ] |
| 325 | [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) :lock: | Medium | 5/10 | 50.9% | [ ] |
| 525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Medium | 6/10 | 51.3% | [ ] |
| 523 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | Medium | 6/10 | 31.3% | [ ] |

## rolling_hash

**What it is:** Rolling hash computes a hash for a fixed-length window over a string or sequence, then updates it incrementally in O(1) as the window slides — rather than recomputing from scratch each time. This lets you compare substrings in O(1) instead of O(length), reducing an O(n * m) brute-force to O(n + m). Recognize this when a problem involves finding matching substrings of a fixed length or detecting near-duplicate windows across a long string.

**Common steps:**
1. Choose a base and a modulus (e.g., base = 31, mod = a large prime) to reduce collision risk.
2. Compute the initial hash for the first window of length `L`.
3. Slide the window one character at a time: `new_hash = (old_hash - outgoing_char * base^(L-1)) * base + incoming_char` (mod modulus).
4. Store hashes of windows from one string in a set.
5. For each window in the second string, check if its hash is in the set (and optionally verify character-by-character to handle collisions).

**Key variations:**
- Single-character difference detection: hash each string with one character deleted (or replaced) and compare hash sets (Strings Differ by One Character).
- Double hashing: use two independent hash functions simultaneously to reduce false positive collision probability.

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 1554 | [Strings Differ by One Character](https://leetcode.com/problems/strings-differ-by-one-character/) :lock: | Medium | 7/10 | 39.9% | [ ] |

## palindrome_hash

**What it is:** Palindrome hash uses hashing to check whether substrings are palindromes in O(1) after O(n) preprocessing, enabling efficient search through exponentially many substring candidates. Recognize this pattern in hard palindrome problems where you must check many substrings for the palindrome property and a naive O(n^2) check per candidate would be too slow.

**Common steps:**
1. Precompute forward and reverse polynomial hashes for the string (and any candidate strings).
2. For a candidate pair of words, determine the split point where one part would need to be a palindrome.
3. Use the precomputed hashes to check in O(1) whether the required substring is a palindrome.
4. Enumerate all candidate pairs (e.g., word + reverse of another word) and validate each using the hash check.
5. Collect all valid pairs and return them.

**Key variations:**
- Concatenation palindrome: check if `word[i] + word[j]` forms a palindrome, which requires one word to be the reverse of a prefix/suffix of the other, with the remainder being a palindrome itself (Palindrome Pairs).

| # | Problem | Difficulty | Score | Acceptance | Status |
|---|---------|------------|-------|------------|--------|
| 336 | [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | Hard | 9/10 | 37.2% | [ ] |
