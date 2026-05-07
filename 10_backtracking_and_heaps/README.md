# Backtracking & Heaps

## Key Concepts — Backtracking

- Explore all possibilities via recursion, undo choices that don't work
- Template: choose → explore → unchoose
- Prune early to avoid unnecessary work

## Key Concepts — Heaps

- Priority queue: efficiently get min/max element
- Use for "top K", "K-th largest", or streaming median problems
- Python: `heapq` (min-heap by default, negate for max-heap)

## Common Patterns

1. **Subsets/Combinations**: Generate all subsets or combinations of size k
2. **Permutations**: Generate all orderings
3. **Constraint satisfaction**: Place items with rules (N-Queens, Sudoku)
4. **Top K**: Push to heap, maintain size k

## Problems

| # | Problem | Difficulty | Status |
|---|---------|-----------|--------|
| 78 | Subsets | Medium | ⬜ |
| 39 | Combination Sum | Medium | ⬜ |
| 46 | Permutations | Medium | ⬜ |
| 90 | Subsets II | Medium | ⬜ |
| 40 | Combination Sum II | Medium | ⬜ |
| 79 | Word Search | Medium | ⬜ |
| 131 | Palindrome Partitioning | Medium | ⬜ |
| 51 | N-Queens | Hard | ⬜ |
| 295 | Find Median from Data Stream | Hard | ⬜ |
| 355 | Design Twitter | Medium | ⬜ |
| 621 | Task Scheduler | Medium | ⬜ |
| 973 | K Closest Points to Origin | Medium | ⬜ |
