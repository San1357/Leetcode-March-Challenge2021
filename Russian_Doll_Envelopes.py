'''Problem : Russian Doll Envelopes '''

#CODE :

class Solution(object):
    def longestIncreasingSubseqLength(self, nums):
        
        LISlist = [] 
        for num in nums:
            pos = bisect_left( LISlist, num )
            if pos == len(LISlist):
                LISlist.append( num )
            else:
                LISlist[ pos ] = num

        return len(LISlist)

    def maxEnvelopes(self, envelopes):
        
        sortedEnvelopes = sorted( envelopes, key=lambda coord: (coord[0],-coord[1]) )

        return self.longestIncreasingSubseqLength( y for x,y in sortedEnvelopes )
