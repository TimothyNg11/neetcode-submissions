# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                result.append('@')
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        
        return ','.join(result)
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        lst = data.split(',')
        root = TreeNode(int(lst[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(lst):
            node = queue.popleft()
            if lst[i] != '@':
                node.left = TreeNode(int(lst[i]))
                queue.append(node.left)
            i += 1
            if i < len(lst) and lst[i] != '@':
                node.right = TreeNode(int(lst[i]))
                queue.append(node.right)
            i += 1
        
        return root
