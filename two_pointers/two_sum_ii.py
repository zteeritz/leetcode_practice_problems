from typing import List


class Solution:
    def two_sum_time_exceed(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [numbers[i], numbers[j]]

        return []

    def two_sum_binary_search(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            need = target - numbers[i]

            left = i + 1
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == need:
                    return [i + 1, mid + 1]
                elif numbers[mid] < need:
                    left = mid + 1
                else:
                    right = mid - 1

        return []

    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            if s < target:
                left += 1
            else:
                right -= 1

        return []


if __name__ == '__main__':
    solution = Solution()
    print(solution.two_sum_binary_search([2, 7, 11, 15], 9))
