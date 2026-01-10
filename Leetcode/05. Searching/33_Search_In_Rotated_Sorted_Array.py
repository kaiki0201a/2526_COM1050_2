def search( nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    ch0 = nums[-1]
    if ch0 == target:
        return 0

    while left <= right:
        mid = (left + right )//2
        guess  = nums[mid]
        print("CHECK :", left, right , mid)
        if guess == target:
            return mid

        elif guess > target:
            if guess > ch0 :
                #TH1: guess > target > ch0
                if target > ch0:
                    right = mid- 1
                #TH2: target < ch0, guess > ch0
                else:
                    left = mid + 1
                #TH3: target < guess < ch0
            else:
                right = mid - 1
        else:   #guess < target

            #TH1: target > guess > ch0
            if guess > ch0: #target > guess > ch0
                left = mid + 1

            else: 
                #TH2: guess < ch0, target > ch0
                if target > ch0:
                    right = mid - 1
                #TH3: guess < ch0, target < ch0?
                else:
                    left = mid + 1
    return -1
print(search([1,3], 3))