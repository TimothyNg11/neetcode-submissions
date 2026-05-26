# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.string = ""
        def bfs(curr):
            if not curr:
                self.string += '#'
                return
            queue = deque([curr])
            while queue:
                node = queue.popleft()
                self.string = self.string + str(node.val) + ','
                if node.left:
                    queue.append(node.left)
                if not node.left and node.val != '@':
                    queue.append(TreeNode('@'))
                if node.right:
                    queue.append(node.right)
                if not node.right and node.val != '@':
                    queue.append(TreeNode('@'))
        
        bfs(root)
        return self.string
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        temp = TreeNode()
        if data == '#':
            return temp.left
        
        def buildTree(data):
            lst = data.split(',')
            queue = deque([TreeNode(lst[0])])
            i = 1

            while queue and i < len(lst):
                node = queue.popleft()
                if i < len(lst) and node.val != '@':
                    node.left = TreeNode(lst[i])
                    queue.append(node.left)
                i += 1
                if i < len(lst) and node.val != '@':
                    node.right = TreeNode(lst[i])
                    queue.append(node.right)
                i += 1
            
            return root

        return buildTree(data)
