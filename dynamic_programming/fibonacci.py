class Solution:
    # brute-force
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)

    # top-down memorization
    def fib_top_down_memo(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def dp(x: int) -> int:
            if x in memo:
                return memo[x]

            memo[x] = dp(x - 1) + dp(x - 2)
            return memo[x]

        return dp(n)

    # bottom-up
    def fib_bottom_up_memo(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        arr_ans = [0, 1]
        for i in range(2, n + 1):
            arr_ans.append(arr_ans[i - 1] + arr_ans[i - 2])

        return arr_ans[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(5))
    print(sol.fib(4))
    print(sol.fib(3))
    print()

    print(sol.fib_top_down_memo(5))
    print(sol.fib_top_down_memo(4))
    print(sol.fib_top_down_memo(3))
    print()

    print(sol.fib_bottom_up_memo(5))
    print(sol.fib_bottom_up_memo(4))
    print(sol.fib_bottom_up_memo(3))
