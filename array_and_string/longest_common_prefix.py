from typing import List

class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        i = 0
        min_length = min(len(s) for s in strs)
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1

        return strs[0][:i] # slice notation that gets characters from index 0 up to (but not including) index i


if __name__ == '__main__':
    solution = Solution()
    print(solution.longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
    print(solution.longest_common_prefix(["dog", "race", "car"]))