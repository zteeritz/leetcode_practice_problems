from typing import List


class Solution:
    def summary_range(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")
                start = end
                end = num

        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{end}")

        return ranges

    def summary_range2(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]
            while i < len(nums) - 1 and nums[i + 1] == nums[i] + 1:
                i += 1

            if start != nums[i]:
                ans.append(str(start) + "->" + str(nums[i]))
            else:
                ans.append(str(start))

            i += 1

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.summary_range2([0, 1, 2, 4, 5, 7]))  # Output: ["0->2", "4->5", "7"]
    print(solution.summary_range([0, 2, 3, 4, 6, 8, 9]))  # Output: ["0", "2->4", "6", "8->9"]
    print(solution.summary_range([]))  # Output: []
    print(solution.summary_range([-1]))  # Output: ["-1"]
    print(solution.summary_range([0]))  # Output: ["0"]
