#Giai bang hash map
#Gia tri= key, index = value
def twoSum(nums: List[int], target: int) -> List[int]:
    dictt = {}  #Luu gia tri va de tim kiem O(1)

    for i, j in enumerate(nums):    #i: index, j: value

        another = target - j
        #Kiem tra trong dictt co another chua
        if another in dictt:
            return [dictt[another], i]
        else:
            dictt[j] = i
            
