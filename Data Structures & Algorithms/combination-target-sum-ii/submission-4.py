class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicate values at the same level
                if candidates[i] > remaining:
                    break     # sorted, so nothing further can fit
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res