class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxc = max(candies)
        for i, c in enumerate(candies):
            if c + extraCandies >= maxc:
                candies[i] = True
            else:
                candies[i] = False
        return candies