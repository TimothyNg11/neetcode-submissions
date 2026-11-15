class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        dct = {'W': 0, 'B': 0}
        res = float('inf')
        for r, color in enumerate(blocks):
            dct[color] = dct.get(color, 0) + 1
            if (r - l + 1) > k:
                dct[blocks[l]] -= 1
                l += 1
            if (r - l + 1) == k:
                res = min(res, dct['W'])
        
        return res
            

        