#Fib: 0 1 1 2

class Solution:
    #B1. Tao mot cai so tay:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        #B2. Kiem tra co trong memo chua
        if n in self.memo:
            return self.memo[n]
        
        #B3. Neu khong co thi de quy de tinh
        else:
            if n <= 1:      #Base case
                return n

            else:   #Vua de quy vua luu lai vao self.memo
                res = self.fib(n-1) + self.fib(n-2)
                self.memo[n] = res
                return res
p1 = Solution()
print(p1.fib(2))