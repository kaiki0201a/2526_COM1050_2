#C1. Sort: Kha Noob
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        nums = list(set(nums))
        nums.sort()

        res, cur_res = 0, 1

        sw = True
        i = 1

        while i < len(nums):
            sw = False

            if nums[i] == nums[i-1] + 1:
                cur_res += 1
            else:
                cur_res = 1
            res = max(res, cur_res)

            i+=1
        
        if sw:
            return len(nums)
        else:
            return res
    
p1 = Solution()
print(p1.longestConsecutive([100,4,200,1,3,2]))

#C2:
#Y tuong: 
"""
- Tìm điểm bắt đầu
+ Nếu nó là điểm bắt đầu -> tìm điểm tiếp theo 
+ Nếu không: skip
=> Tránh việc xét trùng lặp liên tục vd như 1234 rồi lai 234
"""

class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)

        res = 0
        for i in nums:  #for i in sett is better =))))
            
            #Check xem co hay khong
            if i - 1 not in sett:

                j = i
                while j in sett:    #Tim so tiep theo
                    j += 1
                
                res = max(res, j - i)   #Cap nhat res
        
        return res

