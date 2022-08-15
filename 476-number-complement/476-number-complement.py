class Solution:
    def findComplement(self, num: int) -> int:
        a = str(format(num, 'b'))
        
        result = ['0','b']
        for i in a:
            if i == '0':
                result.append('1')
            else:
                result.append('0')
        
        return int("".join(result), 2)