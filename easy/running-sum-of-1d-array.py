class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums[1:]):
            nums[i+1] += nums[i]
        return nums