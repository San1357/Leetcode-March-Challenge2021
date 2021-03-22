'''Problem : REordered Power Of 2 '''

#CODE :

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """
        :type N: int
        :rtype: bool
        """
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << i))
                   for i in range(31))
        
