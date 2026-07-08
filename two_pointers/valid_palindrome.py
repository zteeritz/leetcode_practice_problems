class Solution:
    def valid_palindrome(self, s: str) -> bool:
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
        return filtered == filtered[::-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.valid_palindrome("A man, a plan, a canal: Panama"))