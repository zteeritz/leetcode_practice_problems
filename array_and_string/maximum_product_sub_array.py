from typing import List


class Solution:
    def max_product_sub_array(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        cur_max = nums[0]
        cur_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(cur_max * nums[i], nums[i])
            cur_min = min(cur_min * nums[i], nums[i])
            answer = max(answer, cur_max)

        return answer


if __name__ == '__main__':
    sol = Solution()
    # print(sol.max_product_sub_array([-2, 0, -1]))
    # print(sol.max_product_sub_array([5, 4, -1, 7, 8]))
    print(sol.max_product_sub_array([2, 3, -2, 4]))
