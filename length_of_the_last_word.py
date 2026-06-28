
class Solution:
    def length_of_last_word(self, s: str) -> int:
        words = s.split()
        return len(words[-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.length_of_last_word("Hello World"))
    print(sol.length_of_last_word("   fly me   to   the moon  "))
