# LeetCode Practice Problems

Python solutions for LeetCode problems, organized by topic and problem-solving technique.

## Current Status

- Total solution files: 17
- Topic folders: 6
- Standalone problem files in repo root: 0
- Utility / starter file in repo root: 1 (`main.py`)

## Repository Layout

```text
leetcode/
├── main.py
├── README.md
├── array_and_string/
│   ├── closet_number_to_zero.py
│   ├── length_of_the_last_word.py
│   ├── longest_common_prefix.py
│   ├── max_profit.py
│   ├── maximum_sub_array.py
│   ├── merge_alternatively.py
│   ├── number_of_strings_as_sub_string.py
│   ├── roman_to_integer.py
│   └── summary_range.py
├── dynamic_programming/
│   └── fibonacci.py
├── hashmap_and_set/
│   ├── is_anagram.py
│   ├── jewels_and_stones.py
│   ├── maximum_number_of_balloon.py
│   └── ransom_note.py
├── math/
│   └── revert_integer.py
├── sliding_window/
│   └── number_of_sub_strings.py
└── stack/
    └── valid_parentheses.py
```

## Solved Problems

### Array and String

| File | Problem |
| --- | --- |
| `array_and_string/merge_alternatively.py` | Merge Strings Alternately |
| `array_and_string/summary_range.py` | Summary Ranges |
| `array_and_string/longest_common_prefix.py` | Longest Common Prefix |
| `array_and_string/roman_to_integer.py` | Roman to Integer |
| `array_and_string/length_of_the_last_word.py` | Length of Last Word |
| `array_and_string/max_profit.py` | Best Time to Buy and Sell Stock |
| `array_and_string/maximum_sub_array.py` | Maximum Subarray |
| `array_and_string/closet_number_to_zero.py` | Find Closest Number to Zero |
| `array_and_string/number_of_strings_as_sub_string.py` | Number of Strings That Appear as Substrings in Word |

### Hashmap and Set

| File | Problem |
| --- | --- |
| `hashmap_and_set/is_anagram.py` | Valid Anagram |
| `hashmap_and_set/ransom_note.py` | Ransom Note |
| `hashmap_and_set/jewels_and_stones.py` | Jewels and Stones |
| `hashmap_and_set/maximum_number_of_balloon.py` | Maximum Number of Balloons |

### Dynamic Programming

| File | Problem |
| --- | --- |
| `dynamic_programming/fibonacci.py` | Fibonacci Number |

### Math

| File | Problem |
| --- | --- |
| `math/revert_integer.py` | Reverse Integer |

### Sliding Window

| File | Problem |
| --- | --- |
| `sliding_window/number_of_sub_strings.py` | Number of Substrings Containing All Three Characters |

### Stack

| File | Problem |
| --- | --- |
| `stack/valid_parentheses.py` | Valid Parentheses |

## How to Run

Run any file directly with Python:

```bash
python3 array_and_string/max_profit.py
python3 math/revert_integer.py
python3 sliding_window/number_of_sub_strings.py
```

Most files include a small `if __name__ == '__main__':` block with sample input/output for quick checking.

## Notes

- Solutions are written in Python.
- Problem files are now organized into topic folders instead of living in the repo root.
- `main.py` is still the default starter file and is not part of the solution set.
- Some filenames still reflect work-in-progress naming and can be cleaned up later.

## Next Cleanup Opportunities

- Rename `math/revert_integer.py` to `math/reverse_integer.py`.
- Rename `array_and_string/closet_number_to_zero.py` to `array_and_string/closest_number_to_zero.py`.
- Rename `sliding_window/number_of_sub_strings.py` to a clearer name such as `number_of_substrings_containing_all_three_characters.py`.
