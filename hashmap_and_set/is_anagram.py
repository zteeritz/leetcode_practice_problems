class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        s_map = self.create_map(s)
        t_map = self.create_map(t)
        return s_map == t_map

    def create_map(self, s: str) -> dict[str, int]:
        map = {}
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

        return map

if __name__ == '__main__':
    sol = Solution()
    print(sol.is_anagram("leetcode", "leetcode"))