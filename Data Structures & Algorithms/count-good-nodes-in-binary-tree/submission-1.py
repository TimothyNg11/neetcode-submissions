# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([[root, root.val]])
        total = 0

        while queue:
            node, maxVal = queue.popleft()
            newMax = maxVal
            if node.val >= maxVal:
                total += 1
                newMax = node.val
            if node.left:
                queue.append([node.left, newMax])
            if node.right:
                queue.append([node.right, newMax])
        
        return total
            

                



        