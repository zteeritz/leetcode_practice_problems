
class Solution:
    def max_number_of_balloons(self, text: str) -> int:
        balloon_map = {}
        balloon_list = ['b', 'a', 'l', 'o', 'n']

        for char in text:
            if char in balloon_list:
                if balloon_map.get(char) is None:
                    balloon_map[char] = 1
                else:
                    balloon_map[char] += 1

        for char in balloon_list:
            if balloon_map.get(char) is None:
                return 0

        count_b = balloon_map['b']
        count_a = balloon_map['a']
        count_l = balloon_map['l']
        count_o = balloon_map['o']
        count_n = balloon_map['n']

        return min(count_a, count_b, count_l // 2, count_o // 2, count_n)

if __name__ == '__main__':
    solution = Solution()
    print(solution.max_number_of_balloons("balloon"))
    print(solution.max_number_of_balloons("loonbalxballpoon"))
    print(solution.max_number_of_balloons("leetcode"))