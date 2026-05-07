# Sliding Window

## Key Concepts

- Maintain a window (subarray/substring) that expands or shrinks
- Avoids recomputing from scratch — just add/remove elements at edges
- Fixed-size window vs. dynamic window (expand right, shrink left)

## Common Patterns

1. **Fixed window**: Window of size k, slide one element at a time
2. **Dynamic window**: Expand until invalid, then shrink until valid again
3. **Frequency map in window**: Track character/element counts within window

## Problems

| # | Problem | Difficulty | Status |
|---|---------|-----------|--------|
| 121 | Best Time to Buy and Sell Stock | Easy | ⬜ |
| 3 | Longest Substring Without Repeating Characters | Medium | ⬜ |
| 424 | Longest Repeating Character Replacement | Medium | ⬜ |
| 567 | Permutation in String | Medium | ⬜ |
| 76 | Minimum Window Substring | Hard | ⬜ |
