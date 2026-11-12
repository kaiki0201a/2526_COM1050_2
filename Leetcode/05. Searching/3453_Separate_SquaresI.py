import math
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        min_high = float("inf")
        max_high = -float("inf")
        res = 0

        for i in squares:
            if i[1] < min_high:
                min_high = i[1]
            if i[1] + i[2] > max_high:
                max_high = i[1] + i[2]

        print("CHECK 1: ",min_high, max_high)
        low = min_high
        high = max_high

        while low < high:
            i = (low + high) / 2
            s_tren = 0
            s_duoi = 0

            #j[1] + j[2]: canh tren, j[1]: canh duoi
            #Tinh s_tren, duoi voi moi i
            for j in squares:
                if j[1] + j[2] <= i:
                    print("1", j, i)
                    s_duoi += j[2] ** 2
                elif j[1] >= i:
                    print("2", j, i)
                    s_tren += j[2] ** 2
                else:
                    s_duoi += (i-j[1]) * j[2]
                    s_tren += (j[1]+ j[2]- i) * j[2]
                    print("KQ:", (i-j[1]) * j[2])
                    print((j[1]+ j[2]- i) * j[2])
            if s_duoi > s_tren:
                print("duoi > tren")
                high = i
            elif s_duoi < s_tren:
                
                low = i
                print("tren > duoi")
            elif math.isclose(s_tren, s_duoi, abs_tol=1e-5):
                print("DA THAY")
                break

        sw = True
        h = -float("inf")
        for j in squares:
            if j[1] < i and j[1] + j[2] > i:
                sw = False
            elif j[1] + j[2] < i:
                h = min(j[1] + j[2], i)

        if sw:
            return h
        return i


p1 = Solution()
print(p1.separateSquares([[10,28,4],[15,20,2],[21,30,2],[7,23,4]]))
