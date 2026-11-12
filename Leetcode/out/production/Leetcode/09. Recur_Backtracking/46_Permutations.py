#Hoan vi

#C1:
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], [-1]*n

        def backtracking(i):
            if i == n:
                res.append(sol[:])
                return

            for j in nums:

                sett = set(sol[:i])

                if j not in sett:

                    sol[i] = j
                    backtracking(i+1)

        backtracking(0)
        return res
    
p1 = Solution()
print(p1.permute([1,2,3]))