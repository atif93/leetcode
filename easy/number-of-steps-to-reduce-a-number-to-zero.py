class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num != 0:
            steps += 1
            if num%2 != 0:
                num -= 1
            else:
                num /= 2
        return steps