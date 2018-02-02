class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(reversed(s.split()))




class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rstring = []
        stack = []
        for idx, ch in enumerate(reversed(s)):
            if ch == " ":
                flag = False
                while len(stack) > 0:
                    flag = True
                    rstring.append(stack.pop())
                if flag:
                    rstring.append(" ")
            else:
                stack.append(ch)
                
        while len(stack) > 0:
            rstring.append(stack.pop())
            
        if len(rstring) > 0 and rstring[-1] == " ":
            rstring = rstring[:-1]
                
        return "".join(rstring)
            
            