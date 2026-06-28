# LeetCode Practice Problems

Python solutions for LeetCode problems, organized mostly by topic.

## Current Status

- Total solution files: 11
- Topic folders: 2
- Standalone problem files in repo root: 2
- Utility / starter file in repo root: 1 (`main.py`)

## Repository Layout

```text
leetcode/
├── main.py
├── README.md
├── length_of_the_last_word.py
├── revert_integer.py
├── array_and_string/
│   ├── closet_number_to_zero.py
│   ├── longest_common_prefix.py
│   ├── max_profit.py
│   ├── merge_alternatively.py
│   ├── roman_to_integer.py
│   └── summary_range.py
└── hashmap_and_set/
    ├── is_anagram.py
    ├── jewels_and_stones.py
    └── ransom_note.py
```

## Solved Problems

### Root

| File | Problem |
| --- | --- |
| `revert_integer.py` | Reverse Integer |
| `length_of_the_last_word.py` | Length of Last Word |

### Array and String

| File | Problem |
| --- | --- |
| `array_and_string/merge_alternatively.py` | Merge Strings Alternately |
| `array_and_string/summary_range.py` | Summary Ranges |
| `array_and_string/longest_common_prefix.py` | Longest Common Prefix |
| `array_and_string/roman_to_integer.py` | Roman to Integer |
| `array_and_string/max_profit.py` | Best Time to Buy and Sell Stock |
| `array_and_string/closet_number_to_zero.py` | Find Closest Number to Zero |

### Hashmap and Set

| File | Problem |
| --- | --- |
| `hashmap_and_set/is_anagram.py` | Valid Anagram |
| `hashmap_and_set/ransom_note.py` | Ransom Note |
| `hashmap_and_set/jewels_and_stones.py` | Jewels and Stones |

## How to Run

Run any file directly with Python:

```bash
python3 array_and_string/max_profit.py
python3 hashmap_and_set/ransom_note.py
python3 length_of_the_last_word.py
```

Most files include a small `if __name__ == '__main__':` block with sample input/output for quick checking.

## Notes

- Solutions are currently written in Python.
- Most problems are grouped by topic, but a couple still live in the repo root.
- `main.py` is still the default starter file and is not part of the solution set.
- Some filenames reflect work-in-progress naming and may be cleaned up later.

## Next Cleanup Opportunities

- Move the root-level problem files into topic folders for consistency.
- Rename `revert_integer.py` to `reverse_integer.py`.
- Rename `closet_number_to_zero.py` to `closest_number_to_zero.py`.
