class Solution:
    def valid_palindrome(self, s: str) -> bool:
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
        return filtered == filtered[::-1]

    def valid_palindrome_two_pointers(self, s: str) -> bool:
        # this still creates a filtered string O(n) space wasted
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())

        left = 0
        right = len(filtered) - 1

        while left <= right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1

        return True

    def valid_palindrome_three_pointers_fixed(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            # compare only when both are alphanumeric
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.valid_palindrome("A man, a plan, a canal: Panama"))
    print(solution.valid_palindrome_three_pointers_fixed("A man, a plan, a canal: Panama"))