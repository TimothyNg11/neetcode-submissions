class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sortedNums = sorted(nums)
        self.lst = []

        def recur(nums, target, currList):
            if target == 0:
                self.lst.append(list(currList))
                return
            for i, num in enumerate(nums):
                if num <= target:
                    currList.append(num)
                    recur(nums[i:], target-num, currList)
                    currList.pop()
                else:
                    break


        recur(sortedNums, target, [])

        return self.lst