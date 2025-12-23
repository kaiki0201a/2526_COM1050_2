class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        s_find = False

        while low <= high:
            mid = (low + high)//2
            guess = nums[mid]

            if guess == target:
                s_find = True
                return mid
            if guess < target:
                low = mid + 1
            else:
                high = mid -1
        if s_find == False:
            if high < 0:
                return 0
            elif nums[high] > target:
                return high
            else: return high + 1