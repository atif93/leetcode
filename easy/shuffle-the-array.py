class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new_nums = []
        for i in range(n):
            new_nums.append(nums[i])
            new_nums.append(nums[n+i])
        return new_nums