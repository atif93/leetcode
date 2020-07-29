class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {'R': 0, 'L': 0}
        balanced = 0
        for ch in s:
            count[ch] += 1
            if count['R'] == count['L']:
                count = {'R': 0, 'L': 0}
                balanced += 1
        return balanced