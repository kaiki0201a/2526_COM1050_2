class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        total, min_len = 0, n

        while r < n:
            total += nums[r]
            
            while total >= target:

                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l += 1

            r += 1
        
        if l == 0:
            return 0
        else:
            return min_len