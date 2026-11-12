#C1: Dung Listt de luu cac vi tri da di den
def canJump(nums: List[int]) -> bool:

    n = len(nums)
    listt = [1] + [0]*(n-1)
    i = 0
    while i < n:
        if nums[i] > 0 and listt[i] == 1:
            for j in range(i,i + nums[i] + 1):
                if j < n:
                    if listt[j] == 0: listt[j] = 1

        i += 1
    
    print(listt)
    if listt[n-1] == 1:
        return True
    else: return False


#C2: Tinh diem cham xa nhat
#No se dung khi tai do nums[i] = 0 ma diem cham cur <= i
def canJumpp( nums: List[int]) -> bool:
    n = len(nums)

    i = 0
    cur = 0

    while i < n-1:

        if i + nums[i] > cur:
            cur = i + nums[i]
        elif nums[i] == 0 and cur <= i:
            return False

        i += 1

    #Di het ma khong gap 0 de return False -> return True
    return True

print(canJumpp([0,2,3]))

#C3.Greedy
#Ta se xet tu cuoi mang -> 0.
def canJumpmp(nums) -> bool:

    goal = len(nums) -1

    for i in range(len(nums)-1, -1, -1):

        #Neu ma no co the cham den goal-> reset goal
        if i + nums[i] >= goal:
            goal = i

    return True if goal == 0 else False