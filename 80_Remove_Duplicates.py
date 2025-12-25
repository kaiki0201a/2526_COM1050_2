class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        n = len(nums)
        if n <= 2:
            return n

        left = 0    #Update where postion will be need to fill
        i = 1   # 1-> n-1
        count = 1   #Check number, so that just duplicate can be add
        while i < n:
            if nums[i] != nums[left]:
                left += 1
                nums[left] = nums[i]
                count = 1   #reset count
            elif count == 1:    #when count = 1: add (just one time)
                left += 1
                nums[left] = nums[i]
                count = 2

            i += 1
        return left + 1

                


        
        