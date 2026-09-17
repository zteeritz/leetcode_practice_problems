

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1 or num_rows >= len(s):
            return s

        rows = [""] * num_rows
        row = 0
        direction = 1

        for char in s:
            rows[row] += char

            if row == 0:
                direction = 1
            elif row == num_rows - 1:
                direction = -1

            row += direction
        return "".join(rows)

if __name__ == '__main__':
    sol = Solution()
    # print(sol.convert("A", 1))
    # print(sol.convert("AA", 2))
    print(sol.convert("PAYPALISHIRING", 3))
    print(sol.convert("PAYPALISHIRING", 4))
