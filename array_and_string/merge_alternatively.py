class Solution:
    def merge_alternatively(self, word1: str, word2: str) -> str:
        result = ""

        i = 0
        while i < len(word1):
            if i < len(word2):
                result += word1[i] + word2[i]
            else:
                result += word1[i]

            i += 1

        if len(word2) > len(word1):
            while i < len(word2):
                result += word2[i]
                i += 1
                
        return result


if __name__ == '__main__':
    print(Solution().merge_alternatively("ab", "pqrs"))
