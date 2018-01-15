class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opp = {'{': '}', '}': '{', '(': ')', ')': '(', '[': ']', ']': '['}
        
        stack = []
        
        for ch in s:
            if len(stack) > 0 and stack[len(stack) - 1] == opp[ch]:
                stack.pop()
            else:
                stack.append(ch)
        
        if len(stack) > 0:
            return False
        
        return True