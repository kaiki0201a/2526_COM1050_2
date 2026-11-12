#Ý tưởng: Nếu ta có số các số âm là chẵn -> ta có thể biến tất cả về số dương
#Nếu lẻ thì ta sẽ chỉ có biến biến về có duy nhất một số âm
#Việc của ta là đếm số âm, và số có trị tuyệt đối bé nhất

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])  #Cow
        m = len(matrix)     #Row

        res = 0
        min_va = abs(matrix[0][0])
        count = 0

        #Đếm số âm, tìm số bé nhất, tính tổng max
        for i in range(m):
            for j in range(n):
                k = matrix[i][j]
                if matrix[i][j] < 0:
                    count += 1
                min_va = min(min_va, abs(k))
                res += abs(matrix[i][j])

        #Kiểm tra và trừ cho số có abs bé nhất nếu số số âm là lẻ
        if count % 2 == 0:
            return res
        else:
            return res - 2* min_va