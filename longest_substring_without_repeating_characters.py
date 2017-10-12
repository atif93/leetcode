class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = set()
        maxlength = 0
        curlength = 0
        start = 0
        i = 0
        while i < len(s):
            if s[i] not in alpha:
                alpha.add(s[i])
                curlength += 1
            else:
                start = s.find(s[i], start) + 1
                alpha = set(s[start:i])
                curlength = i - start
                i -= 1
            if maxlength < curlength:
                maxlength = curlength
            i += 1
            
        return maxlength
                
            