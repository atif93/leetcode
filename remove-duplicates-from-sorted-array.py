class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        
        prev = nums[0]
        prev_idx = 0
        for idx, num in enumerate(nums[1:]):
            if num != prev:
                prev_idx += 1
                nums[prev_idx] = num
                prev = num
                
        return prev_idx + 1