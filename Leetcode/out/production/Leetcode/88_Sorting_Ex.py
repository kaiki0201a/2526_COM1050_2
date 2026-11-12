def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    h = m + n -1

    while j >= 0 and i >= 0:    #we will stop if 1 or 2 end of element
        if nums2[j] >= nums1[i]:
            nums1[h] = nums2[j]
            j -= 1
        else:
            nums1[h], nums1[i] = nums1[i], nums1[h]
            i -= 1
        h -= 1

    #If j == 0: we have nothing to do 
    #If j > 0: we have some int of nums2 that havent added

    nums1[:j+1] = nums2[:j+1]
    
    return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(nums1,3,nums2,3))