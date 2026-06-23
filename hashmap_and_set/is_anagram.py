
class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        # TODO: "a" and "ab"
        s_set = set(s)
        t_set = set(t)
        diff = s_set.difference(t_set)
        return len(diff) == 0

