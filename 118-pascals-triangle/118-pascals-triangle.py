class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums = []
        result = []
        for i in range(numRows):
            if i ==0:
                result.append([1])
            elif i ==1:
                result.append([1,1])
            else:
                for j in range(i+1):
                    if j == 0 or j == i:
                        nums.append(1)
                    else:
                        nums.append(result[i-1][j-1]+result[i-1][j])
                result.append(nums)
                nums = []
            
        return result