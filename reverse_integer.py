class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        neg_flag = False
        if x < 0:
            neg_flag = True
            x *= -1
        while x!=0:
            dig = x % 10
            reverse = reverse * 10 + dig
            x = x / 10
        if neg_flag == True:
            reverse *= -1
        if reverse < -2147483648 or reverse > 2147483647:
            return 0
        return reverse
        

class Solution(object):
    def reverse(self, x):
        s = cmp(x, 0)
        r = int(`s*x`[::-1])
        return s*r * (r < 2**31)