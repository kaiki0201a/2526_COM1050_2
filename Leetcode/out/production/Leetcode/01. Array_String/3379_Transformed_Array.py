
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n

        for i in range(n):

            if nums[i] == 0:
                res[i] = nums[i]
            elif nums[i] > 0:
                gap = nums[i] % n

                if i + gap > n-1:
                    res[i] = nums[i+gap - (n-1) -1]
                else:
                    res[i] = nums[i+gap]
            else:
                gap = abs(nums[i]) % n
                if i - gap < 0:
                    res[i] = nums[n-1 - (gap - i - 1)]
                else:
                    res[i] = nums[i - gap]
                    
        return res