class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        
        prev_idx = -1
        for idx, num in enumerate(nums):
            if num != val:
                prev_idx += 1
                nums[prev_idx] = num
                
        return prev_idx + 1