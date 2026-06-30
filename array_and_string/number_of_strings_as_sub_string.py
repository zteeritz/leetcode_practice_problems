from typing import List


class Solution:
    def num_of_strings(self, patterns: List[str], word: str) -> int:
        count = 0
        for p in patterns:
            if p in word:
                count += 1

        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.num_of_strings(["a","abc","bc","d"], "abc"))
    print(solution.num_of_strings(["a","a","a","a"], "a"))
    print(solution.num_of_strings(["a","a","a"], "ab"))