# Arrays & Hashing

## Key Concepts

- Hash maps give O(1) lookup — use them to avoid nested loops
- When you need to check "have I seen this before?" → hashmap/set
- Frequency counting with dictionaries
- Trading space for time: O(n) space to get from O(n²) to O(n) time

## Common Patterns

1. **Two-pass with hashmap**: Build a map first, then query it
2. **Single-pass with hashmap**: Check and insert in one loop
3. **Frequency count**: Count occurrences, then use the counts
4. **Index mapping**: Map values to indices for O(1) access

## Problems

| # | Problem | Difficulty | Status |
|---|---------|-----------|--------|
| 1 | Two Sum | Easy | ⬜ |
| 49 | Group Anagrams | Medium | ⬜ |
| 217 | Contains Duplicate | Easy | ⬜ |
| 242 | Valid Anagram | Easy | ⬜ |
| 347 | Top K Frequent Elements | Medium | ⬜ |
| 128 | Longest Consecutive Sequence | Medium | ⬜ |
| 238 | Product of Array Except Self | Medium | ⬜ |
| 36 | Valid Sudoku | Medium | ⬜ |
| 271 | Encode and Decode Strings | Medium | ⬜ |
