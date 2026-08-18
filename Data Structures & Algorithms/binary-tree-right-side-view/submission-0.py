class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([[root]])   # list-of-nodes, matching what you append later
        res = []

        while queue:
            group = queue.popleft()
            res.append(group[-1].val)
            level = []
            for node in group:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:              # don't enqueue an empty final level
                queue.append(level)

        return res