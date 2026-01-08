class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        res = nums1[0]*nums2[0]

        n = len(nums1)
        m = len(nums2)

        listt = [[-float("inf")]*(m+1) for _ in range(n+1)]

        for j in range(m):
            for i in range(n):
                listt[i+1][j+1] = max(nums1[i] * nums2[j],
                listt[i][j] + nums1[i] * nums2[j],
                listt[i][j+1],
                listt[i+1][j])

            
        return listt[n][m]