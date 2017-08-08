class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i, ch in enumerate(s):
            if i < len(s) - 1  and dict_num[s[i + 1]] > dict_num[ch]:
                ans -= dict_num[ch]    
            else:
                ans += dict_num[ch]
        return ans