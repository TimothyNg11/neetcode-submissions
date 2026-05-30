class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            lst = [x for x in nums[i:i+k+1]]
            if len(lst) == len(set(lst))+1:
                return True
            
        return False
        