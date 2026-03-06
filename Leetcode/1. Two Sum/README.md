## LeetCode 1: Two Sum

This folder contains two Python implementations of the classic Two Sum problem.

Problem statement:

Given an array `nums` and an integer `target`, return the indices of two numbers such that they add up to `target`.

## Files

- `Two Sum(One pass).py`
- `Two Sum(Two pass).py`

## 1) One-pass hash map approach

File: `Two Sum(One pass).py`

Idea:
- Iterate through the list once.
- For each number, compute `target - current`.
- If that complement is already in the dictionary, return/store both indices.
- Otherwise store current number and index in dictionary.

Time complexity: `O(n)`
Space complexity: `O(n)`

## 2) Two-pass style approach

File: `Two Sum(Two pass).py`

Idea:
- First pass: build dictionary of value to index.
- Second pass: search complement for each value.

Time complexity: `O(n)`
Space complexity: `O(n)`

## Run

From this folder:

```bash
python "Two Sum(One pass).py"
python "Two Sum(Two pass).py"
```

## Note

These scripts currently use hardcoded sample arrays and print index pairs as output.

