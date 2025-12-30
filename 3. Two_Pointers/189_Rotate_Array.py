def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    
    if n!= 0: k % n

    l, r = 0, n-k-1
    l1, r1 = n-k, n-1

    #Reverse from 0 -> n-k-1: 12345 -> 32145
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    #Reverse from n-k -> n -1: 32145 -> 32154
    while l1 < r1:
        nums[l1], nums[r1] = nums[r1], nums[l1]
        l1 += 1
        r1 -= 1
    #Reverse all again
    l2, r2 = 0, n -1
    while l2 < r2:
        nums[l2], nums[r2] = nums[r2], nums[l2]
        l2 += 1
        r2 -= 1
    return nums
print(rotate([1,2,3,4,5,6,7], 3))

    