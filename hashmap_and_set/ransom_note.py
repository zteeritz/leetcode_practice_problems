from collections import deque, Counter


class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        magazine_deq = deque(magazine)
        for char in ransom_note:
            if char not in magazine_deq:
                return False
            else:
                magazine_deq.remove(char)

        return True

    def can_construct_counter(self, ransom_note: str, magazine: str) -> bool:
        if len(ransom_note) < len(magazine):
            return False

        freq = Counter(magazine)
        for char in ransom_note:
            if freq[char] == 0:
                return False
            freq[char] -= 1

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.can_construct(ransom_note="aa", magazine="ab"))
