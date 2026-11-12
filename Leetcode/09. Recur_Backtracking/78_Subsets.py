class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            
            # Don't pick nums[i]
            backtrack(i+1)

            # Pich nums[i]

            sol.append(nums[i])
            backtrack(i+1)

            sol.pop()
        
        backtrack(0)

        return res

p1 = Solution()
print(p1.subsets([1,2,3]))