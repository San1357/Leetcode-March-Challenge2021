'''Problem : ADD ONE ROW TO TREE '''

#CODE :

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, root)
        
        queue = deque([root])
        while d-2:
            m=len(queue)
            while m:
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                m -= 1
            d -= 1
        
        while queue:
            node = queue.popleft()
            if node:
                node.left = TreeNode(v, node.left)    
                node.right = TreeNode(v, None, node.right)
        
        return root
        
