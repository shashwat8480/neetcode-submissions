# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        
        result = [] 
        q = deque() 
        q.append(root)

        while q: 
            rightmost = None 
            n = len(q)
            
            for i in range(n): 
                node = q.popleft() 
                rightmost = node.val 

                if node.left: 
                    q.append(node.left)
                
                if node.right: 
                    q.append(node.right)
            
            result.append(rightmost)
        
        return result

       

        