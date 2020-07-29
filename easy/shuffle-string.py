class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        rs = [""]*len(s)
        for ind, i in enumerate(indices):
            rs[i] = s[ind]
        return "".join(rs)