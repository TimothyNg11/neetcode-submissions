class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        target = (m + n) // 2

        arr = []
        x = 0
        y = 0
        for i in range(target + 1):
            if y >= n or (x < m and nums1[x] < nums2[y]):
                arr.append(nums1[x])
                x += 1
            else:
                arr.append(nums2[y])
                y += 1

        if (m + n) % 2 == 1:
            return arr[-1]
        else:
            return (arr[-2] + arr[-1]) / 2