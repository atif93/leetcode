class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        daddr = ""
        for char in address:
            if char == ".":
                daddr += "[.]"
            else:
                daddr += char
        return daddr