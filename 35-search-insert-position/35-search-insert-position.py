class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        i =0 
        j = len(nums)
        
        ##Binary Search Solution
        while(i<j):
            mid = int((i+j)/2)
            calc = nums[mid]
            
            if(target==calc):
                return mid   
            elif(target>calc):
                i = mid+1
            else:
                j = mid
                
        return i
            
            