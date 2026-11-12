#L[i] la chuoi con tang dai nhat ket thuc tai index i
#Cach 1: O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        L = [1] * n
        res = 1

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    L[i] = max(L[i], L[j]+1)
                if L[i] > res:
                    res = L[i]
        
        return res
#Cach 2: O(nlogn)
#Tails : phan tu nho nhat co do dai k
#Tai moi vi tri tim cai duoi de chen vo, khi do no se thay the duoi cu hoac chen vao cuoi neu > all
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        tails = []

        for i in range(n):
            
            #Tim kiem trong tails vi tri dau tien ">=" nums[i]
            left, right = 0, len(tails) - 1
            pos = len(tails) #mac dinh vi tri chen la cuoi mang

            while left <= right:
                mid = (left + right) // 2

                if tails[mid] >= nums[i]:   #Dau bang o day vi khi bang thi van co the thay the
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if pos == len(tails):
                tails.append(nums[i])
            else:
                tails[pos] = nums[i]
        
        return len(tails)

        