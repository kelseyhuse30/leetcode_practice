# This is O(n^2) but it works

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        for i, num in enumerate(nums):
            for j in range(i+1,l):
                if num + nums[j] == target:
                    return [i, j]
