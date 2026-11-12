class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtracking(i):
            if i == n:
                res.append(sol[:])
                return

            # Dont pick nums[i]
            backtracking(i+1)

            # Pick nums[i]
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

        backtracking(0)

        return res
p1 = Solution()
print(p1.subsets([1,2,3]))