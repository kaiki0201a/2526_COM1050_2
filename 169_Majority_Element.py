#C1.
class Solution:
def majorityElement(self, nums: List[int]) -> int:
    count = {}
    res, maxCount = 0, 0    #res: keep track what the max value is, and maxCount of that value

    for n in nums:
        count[n] = 1 + count.get(n, 0)  #if n in count: return n else return default vale

        #Update res
        res = n if count[n] > maxCount else res
        maxCount = count[res]
    return res

#C2.Boyer-Moore
#Noob
def MajorityElement(nums: List[int]) -> int:
    res = nums[0]
    count = 1
    for i in nums[1:]:
        count += (1 if i == res else -1)
        if count == 0:
            res, count = i, 1
    return res

#Pro
def MajorityElement2(nums: List[int]) -> int:
    res = count = 0

    for i in nums:
        if count == 0: res = i

        count += (1 if i == res else -1)
        
    return res
        
        
