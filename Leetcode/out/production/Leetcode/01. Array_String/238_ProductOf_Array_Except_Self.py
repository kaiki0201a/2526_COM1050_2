#Y tuong: tinh tich truoc va tich sau roi nhan lai
"""
#       1   2   3   4
pre  1  1   2   6   24
post    24  24  12   4   1
res     24  12  8   6
#Lam nhu nay rat ton bo nho 
Thay vao day :
prefix = 1 -> 1 -> 2 -> 6
postfix = 24 <- 12 <- 4 -< 1

"""
#C1: Ton bo nho:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*(len(nums) + 1)

        for i in range(len(nums)):
            pre[i+1] = pre[i]*nums[i]
        
        post = [1]* (len(nums)+1)
        for i in range(len(nums)-1, -1,-1):
            post[i] = post[i+1]*nums[i]
        
        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = pre[i]*post[i+1]

        return res            
#C2: Clean bo nho
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]* len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

p1 = Solution2()
print(p1.productExceptSelf([1,2,3,4]))
