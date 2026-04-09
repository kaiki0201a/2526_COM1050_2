from collections import deque
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        res = deque()
        res.append(nums[0])
        n = len(nums)

        i = 1
        cur = float("inf")
        if n <= 1:
            return 0

        while i < n:
            if len(res) < k:
                res.append(nums[i])
            else:

                cur = min(res[-1] - res[0], cur)
                print(res, cur)
                res.popleft()
                res.append(nums[i])

            i += 1
        cur = min(res[-1] - res[0], cur)     
        return cur

p1 = Solution()
print(p1.minimumDifference([87063,61094,44530,21297,95857,93551,9918], 6))