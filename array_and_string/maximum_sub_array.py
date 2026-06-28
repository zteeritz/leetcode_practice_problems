from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        cur_index = 1
        cur_max = nums[0]
        cur_sum = nums[0]

        while cur_index <= len(nums) - 1:
            if cur_sum < 0:
                cur_sum = nums[cur_index]
            else:
                cur_sum += nums[cur_index]

            cur_max = max(cur_max, cur_sum)
            cur_index += 1

        return cur_max

if __name__ == '__main__':
    sol = Solution()
    print(sol.max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
    print(sol.max_sub_array([5,4,-1,7,8]))