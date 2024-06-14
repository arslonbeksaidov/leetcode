from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newList = list(set(nums))
        count = len(newList)
        differ = len(nums) - len(newList)
        for num in range(0, differ):
            newList.append('_')
        print(newList)
        return count

solution = Solution()
dd = solution.removeDuplicates([1,1,2])
print(dd
      )