class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #co dinh 1
        n = len(nums)

        nums.sort()
        res = []
        sett = set()

        print(nums)

        i = 0
        while i < n-3:
            if i > 0:
                if nums[i] == nums[i-1]:
                    i += 1
                    continue
            j = i + 1
            while j < n-2:
                if nums[j] == nums[j-1] and j-1 != i:
                    j += 1
                    continue
                k = j + 1
                h = n - 1
                while k < h:
                    if nums[i] + nums[j] + nums[k] + nums[h] > target:
                        h -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[h] < target:
                        k += 1
                    else:
                        if not res:                
                            res.append([nums[i], nums[j], nums[k], nums[h]])
                        elif [nums[i], nums[j], nums[k], nums[h]] != res[-1]:
                            res.append([nums[i], nums[j], nums[k], nums[h]])
                        h -= 1
                j += 1
            i += 1
                      
        return res   
p1 = Solution()
print(p1.fourSum([1,0,-1,0,-2,2], 0))