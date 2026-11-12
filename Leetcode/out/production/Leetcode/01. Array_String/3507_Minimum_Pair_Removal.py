class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
    
        sw = True
        res = 0

        while sw:

            if len(nums) <= 1:
                return res

            i = 1
            count = 0
            cur, id = float("inf"), 0

            while i < len(nums):
                if nums[i] < nums[i-1] and count == 0:
                    count = 1

                if nums[i] + nums[i-1] < cur:
                    cur = nums[i] + nums[i-1]
                    id = i
                
                i += 1
            
            if count == 0:
                sw = False
                break
            else:
                res += 1
                nums = nums[:id-1] + [cur] + nums[id+1:]

        return res

p1 = Solution()
print(p1.minimumPairRemoval([6,5,4,3,2]))