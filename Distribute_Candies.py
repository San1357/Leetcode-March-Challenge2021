'''Problem: Distribute Candies '''

#CODE :

class Solution:
    def distributeCandies(self, candy):
        
        total = len(candy)
        max = total // 2
        candy = set(candy)
        diff = len(candy)
        if diff > max :
            return max
        else:
            return diff 
        return min(len(candy)//2, len(set(candy)))
        
        
