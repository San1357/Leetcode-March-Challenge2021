'''Problem : Binary Tree With Factor '''

#CODE : 

class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        dp = {}
        for i, a in enumerate(A):
            dp[a] = 1
            for j in range(i):
                if a % A[j] == 0 and a / A[j] in dp:
                    dp[a] += dp[A[j]] * dp[a / A[j]]
        return sum(dp.values()) % (10**9 + 7)
