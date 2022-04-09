class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = Counter(list(set(nums1)) + list(set(nums2)))
        result = []
        
        for key, value in temp.items():
            if value>=2:
                result.append(key)
        
        return result