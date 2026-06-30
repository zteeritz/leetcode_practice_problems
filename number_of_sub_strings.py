class Solution:
    def num_of_strings_slinding_window(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0}
        left = 0
        answer = 0

        for right in range(len(s)):
            count[s[right]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                answer += len(s) - right

                count[s[left]] -= 1
                left += 1

        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.num_of_strings_slinding_window("abcabc"))