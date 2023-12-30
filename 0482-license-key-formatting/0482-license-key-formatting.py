class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        strStemp = s.replace('-','').upper()
        result = ''
        slSize = int(len(strStemp)%k)
        
        if(slSize != 0):
            s = strStemp[:slSize]
            strStemp = strStemp[slSize:]
            result+=s
            if(len(strStemp)>=k):
                result+='-'
        
        for i in range(int(len(strStemp)/k)):
            result+=strStemp[i*k:(i*k)+k]
            if((i*k)+k != len(strStemp)):
                  result+='-'           

        
        return result
        