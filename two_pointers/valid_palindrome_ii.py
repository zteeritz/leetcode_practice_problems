class Solution:
    # should decide immediately at first mismatch and test both branches
    def valid_palindrome_wrong_answer(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        count = 0
        idx = 0
        while left < right:
            if s[left] != s[right]:
                count += 1
                idx = right

            if count > 1:
                return False
            left += 1
            right -= 1

        pop_char = ''.join(char for i, char in enumerate(s) if i != idx)
        left = 0
        right = len(pop_char) - 1
        while left < right:
            if pop_char[left] != pop_char[right]:
                return False
            left += 1
            right -= 1

        return True

    def valid_palindrome(self, s: str) -> bool:
        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # delete left or delete right (only one allowed)
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.valid_palindrome("abca"))
