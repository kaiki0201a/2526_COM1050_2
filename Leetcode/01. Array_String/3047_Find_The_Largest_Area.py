class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        
        n = len(bottomLeft)
        res = 0
        for i in range(n):     #HCN i

            for j in range(i+1,n):  #HCN i+1 - > n-1

                if not ((bottomLeft[i][1] >= topRight[j][1]) or (bottomLeft[j][0] >= topRight[i][0]) or (bottomLeft[i][0] >= topRight[j][0]) or (bottomLeft[j][1] >= topRight[i][1])):
                    
                    diem1 = max(bottomLeft[i][0], bottomLeft[j][0])
                    diem2 = min(topRight[i][0], topRight[j][0])
                    canh1 = diem2 -diem1

                    diem3 = max(bottomLeft[i][1], bottomLeft[j][1])
                    diem4 = min(topRight[i][1], topRight[j][1])

                    print("CHECK", i, j, diem1, diem3)

                    canh2 = diem4- diem3
                    canh = min(canh1, canh2)

                    res = max(res, canh**2)


        return res

p1 = Solution()
print(p1.largestSquareArea([[1,1],[2,2],[3,1]],[[3,3],[4,4],[6,6]] ))