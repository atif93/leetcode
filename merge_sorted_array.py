class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]
            
        i = 0
        j = 0
        for k in range(m + n):
            if i < m and (j >= n or nums1[i + n] <= nums2[j]):
                nums1[k] = nums1[i + n]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1