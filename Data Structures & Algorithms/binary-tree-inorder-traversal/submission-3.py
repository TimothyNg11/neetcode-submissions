# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def dfs(head):
            if not head:
                return
            
            dfs(head.left)
            self.res.append(head.val)
            dfs(head.right)
        
        dfs(root)
        return self.res
        