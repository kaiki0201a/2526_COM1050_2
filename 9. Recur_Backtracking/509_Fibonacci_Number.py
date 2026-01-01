#Fib: 0 1 1 2

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        else:
            return self.fib(n-1) + self.fib(n-2)
p1 = Solution()
print(p1.fib(2))