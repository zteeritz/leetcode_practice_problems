import math
from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        min_price = math.pow(10, 4)
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == '__main__':
    print(Solution().max_profit([7, 1, 5, 3, 6, 4]))