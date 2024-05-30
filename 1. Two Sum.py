class Solution(object):
    def twoSum(self, nums, target):
        for index in range(0, len(nums)):
            for z_index in range(index+1,len(nums)):
                if nums[index] + nums[z_index] == target:
                    return [index,z_index]




ans = Solution().twoSum([3, 2, 3], 6)
print(ans)