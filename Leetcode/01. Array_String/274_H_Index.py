class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        n = len(citations)

        for idx in range(n-1, -1, -1):  #Luu do dai

            i = n - idx - 1
            if citations[i] >= idx:
                return idx
p1 = Solution()
print(p1.hIndex([3]))