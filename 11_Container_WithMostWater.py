#The area belong on width and min(height)
#we use two points from [0] and [-1]
#We will shilft left or right which is smaller ,
# because when we shilft it into, the width will be smaller
#then we need the higher of min(height)


#C1: Easy to understand
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = (right-left)* min(height[left], height[right])

        if len(height) <= 2:
            return min(height)

        #Viec di chuyen left, right vao trong se lam giam width khi do can tim min(heith[left], heith[right]) lon hon
        while left < right:

            if height[left] < height[right]:
                left += 1
                width = right - left
                hi = min(height[left], height[right])
                max_water = max(max_water, width*hi)
            else:
                right -= 1
                width = right - left
                hi = min(height[left], height[right])
                max_water = max(max_water, width*hi)

        return max_water

#Cleaner
def maxArea( height: List[int]) -> int:
    res = 0
    l ,r = 0, len(height) - 1

    while l < r:
        area = (r -l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res
            










