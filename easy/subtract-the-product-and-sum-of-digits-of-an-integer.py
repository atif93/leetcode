class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod = 1
        summ = 0
        while n > 0:
            dig = n % 10
            n /= 10
            prod *= dig
            summ += dig
        return prod - summ