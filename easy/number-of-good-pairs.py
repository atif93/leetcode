class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqs = {}
        good_pairs = 0
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                good_pairs += freqs[num]
                freqs[num] += 1
        return good_pairs