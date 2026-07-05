class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        res_str = ""
        is_minus = False
        for i in range(len(x_str) - 1, -1, -1):
            if x_str[i] == '-':
                is_minus = True
                continue
            res_str += x_str[i]

        if is_minus:
            res = -1 * int(res_str)
        else:
            res = int(res_str)

        if res < -(2 ** 31) or res > (2 ** 31):
            return 0

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(-123))
    print(solution.reverse(120))
