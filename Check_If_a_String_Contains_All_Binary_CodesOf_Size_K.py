''' Problem :  Check If A String Contains All Binary Codes Of Size K '''

#CODE :

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        return 2**k <= len(s) and len({s[i:i+k] for i in range(len(s)-k+1)}) == 2**k
    

        
