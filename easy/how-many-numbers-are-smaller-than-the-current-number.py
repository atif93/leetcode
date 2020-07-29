class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        ranks = []
        for num in nums:
            rank = 0
            for i in range(num):
                if i in freq:
                    rank += freq[i]
            ranks.append(rank)
        return ranks