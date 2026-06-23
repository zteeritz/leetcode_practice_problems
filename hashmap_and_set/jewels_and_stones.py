class Solution:
    def num_jewels_in_stones(self, jewels: str, stones: str) -> int:
        # O(n^2)
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1

        return count

    def num_jewels_in_stones_2(self, jewels: str, stones: str) -> int:
        jewels_map = {}
        for j in jewels:
            jewels_map[j] = 0

        for stone in stones:
            if jewels_map.get(stone) is not None:
                jewels_map[stone] += 1

        sum = 0
        for j in jewels_map:
            sum += jewels_map[j]

        return sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.num_jewels_in_stones_2("aA", "aAAbbbb"))
    print(solution.num_jewels_in_stones_2("z", "ZZ"))