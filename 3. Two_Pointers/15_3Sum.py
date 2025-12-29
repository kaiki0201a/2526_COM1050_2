def threeSum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    set1 = set()
    
    print("CHECK nums: ",nums)
    #Fix 1 value, x will be fix
    for i, x in enumerate(nums):
        print(x, x not in set1)
        if x not in set1:
            target = 0 - x

            #We will use two point to find y,z
            l = i + 1
            r = len(nums) - 1
            if l < len(nums):
                print("L :",nums[l])
                print("R: ",nums[r])

            while l < r:        
                if nums[l] + nums[r] == target:
                    res.append([x, nums[l], nums[r]])
                    if nums[l] == x or nums[r] == x:
                        break
                    print("CHECK KQ: ",res)
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
            set1.add(x)
        print(f"CHECK set: {set1}, check x: {x}")

    return res
print("KET QUA :",threeSum([0,0,0,0]))