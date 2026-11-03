class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getK(A, B, k):
            if len(A) > len(B):
                B, A = A, B
            if not A:
                return B[k-1]
            if k == 1:
                return min(A[0], B[0])
            
            i = int(min(len(A), k // 2))
            j = int(min(len(B), k // 2))
            
            if A[i-1] <= B[j-1]:
                return getK(A[i:], B, k - i)
            else:
                return getK(A, B[j:], k - j)
        
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return getK(nums1, nums2, int((total + 1) / 2))
        else:
            return (getK(nums1, nums2, int(total / 2)) + getK(nums1, nums2, int(total / 2 + 1))) / 2