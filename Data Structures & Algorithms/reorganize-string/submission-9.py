class Solution:
    def reorganizeString(self, s: str) -> str:
        dct = {}
        for char in s:
            dct[char] = dct.get(char, 0) + 1
        total = len(s)
        heap = []
        for key, num in dct.items():
            if total % 2:
                if num > ((total // 2) + 1):
                    return ''
            else:
                if num > ((total // 2)):
                    return ''

            heapq.heappush(heap, (-num, key))
        res = ''
        counter = 0
        prev = ''
        while counter < len(s):
            tup = heapq.heappop(heap)
            val, key = -tup[0], tup[1]
            res = res + key
            val -= 1
            if prev != '':
                heapq.heappush(heap, prev)
            prev = (-val, key)
            counter += 1
        
        return res

        