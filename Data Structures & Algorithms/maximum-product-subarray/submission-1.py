class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = nums[0]
        curMin, curMax = 1, 1
        for num in nums:
            x, y = curMax * num, curMin * num
            curMax = max(x, y, num)
            curMin = min(x, y, num)
            product = max(product, curMax)
        
        return product

        