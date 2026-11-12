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

#C2.Boyer-Moore VOTING
#Noob
def MajorityElement(nums: List[int]) -> int:
    res = nums[0]
    count = 1
    for i in nums[1:]:
        count += (1 if i == res else -1)
        if count == 0:
            res, count = i, 1
    return res

#Pro: Phần tử chiếm đa số luôn triệt tiêu được hết các phần tử còn lại
def MajorityElement2(nums: List[int]) -> int:
    res = count = 0

    for i in nums:
        # Khi count = 0: triệt tiêu hết thì số i này sẽ là đa số( tính từ 0->i)
        if count == 0: res = i

        #Update số lượng, thêm hoặc triệt tiêu
        count += (1 if i == res else -1)
        
    return res
        
        
