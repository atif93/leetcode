class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)/2):
            sublist = [nums[2*i+1]] * nums[2*i]
            res.extend(sublist)
        return res