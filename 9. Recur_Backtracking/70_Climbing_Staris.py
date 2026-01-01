#Return n steps to reach the top
#Suppose we have i-2, i-1, i position
#if we want to reach i we can from i -2 or i -2
# => stepto (i) = stepto (i-1) + stepto(i-2)    feel like fibonacy 1 1 2 
class Solution:
    #B1: Tao mot so nho
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        #B2. Kiem tra co trong memo chua:
        if n in self.memo:
            return self.memo[n]
        
        #B3. Recur:
        if n <= 1:          #Base case: 1 1 ; Chuoi: 1 1 2 3
            return 1
        else:   #Vua de duy vua them vao bo nho
            res = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.memo[n] = res
            return res