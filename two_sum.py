class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for idx, num in enumerate(nums):
            if num in index:
                break
            index[target - num] = idx
        return [index[num], idx]