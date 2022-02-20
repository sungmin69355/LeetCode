class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = nums1 +nums2
        if len(result) ==0:
            return 
        if len(result) == 1:
            return float(result[0])
        result.sort()
        result_len = len(result)
        if result_len%2 == 0:
            a = result[math.floor(result_len/2)]+result[math.floor(result_len/2)-1]
            return float(a/2)
        else:
            return float(result[math.floor(result_len/2)])