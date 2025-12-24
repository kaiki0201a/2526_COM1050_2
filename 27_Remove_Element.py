class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[first] = nums[i]
                first += 1
        return first

        