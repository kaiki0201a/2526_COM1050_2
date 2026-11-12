class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        hang = [-1]*n   # -1 co nghia la khong thoa man, 1 co nghia la thoa man

        #Tim xem hang nao thoa man, neu thoa man thi vi tri so 1 nam o dau
        for i in range(n):
            count = 0
            for j in range(m):
                if mat[i][j] == 1 and count == 0:
                    count += 1
                    hang[i] = j
                elif mat[i][j] == 1 and count == 1:
                    hang[i] = -1
                    break
        
        #Tim xem cot nao thoa man
        cot = [-1]*m
        for i in range(m):  #i la cot
            count = 0
            for j in range(n):
                if mat[j][i] == 1 and count == 0:
                    count += 1
                    cot[i] = j
                elif mat[j][i] == 1 and count == 1:
                    cot[i] = -1
                    break

        print(hang)
        print(cot)

        res = 0
        for i in range(n):
            if hang[i] != -1:   #Hang thoa man
                if cot[hang[i]] == i:   #Cot thoa man nam dung vi tri
                    res += 1

        return res
        