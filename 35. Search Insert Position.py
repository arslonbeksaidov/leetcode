from typing import List


class Solution:
    def binarySearch(self, array, left, right, x):

        if right >= left:
            mid = right + left
            mid = mid // 2
            if array[mid] == x:
                return mid
            elif array[mid] > x:
                return self.binarySearch(array, left, mid - 1, x)
            else:
                return self.binarySearch(array, mid + 1, right, x)
        else:
            return left

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)


solution = Solution()
print(solution.searchInsert([1, 3, 5, 6], 2))
