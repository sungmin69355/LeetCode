class Solution:
    def intToRoman(self, num: int) -> str:
        chars =  {1000:'M',900:'CM',500:'D',400:'CD',100:'C',
				90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
            
        roman = ''
            
        for rn in chars:    
            while rn <= num:
                roman += chars[rn]
                num -= rn
        return roman