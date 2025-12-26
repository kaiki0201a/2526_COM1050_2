def moveZeroes(nums: List[int]) -> None:

    i = 0  #Store 0
    j = 0   
    n = len(nums)

    while j < n:
        if nums[j] != 0:
            while i < j:
                if nums[i] == 0:
                    break
                i +=1
            nums[j], nums[i] = nums[i], nums[j]
        print("i la:", i)
        print("J la: ", j)
        print(j, nums)

        j += 1

    return nums
print(moveZeroes([0,1,0,3,12]))