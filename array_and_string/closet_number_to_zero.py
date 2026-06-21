class Solution:

    def find_closest_number(self, nums: list[int]) -> int:
        closet = nums[0]
        for num in nums:
            if abs(num) < abs(closet):
                closet = num
            elif abs(num) == abs(closet) and num > closet:
                closet = num
        return closet


if __name__ == '__main__':
    print(Solution().find_closest_number([-4, -2, 1, 4, 8]))
