#Use sliding window
#Use set to check

class Solution:
    def lengOftheLongestSubstring(self, s: str) -> int:
        left = 0
        sett = set()    #Check base
        n = len(s)
        longest = 0

        #right runs from 0 -> n-1
        for right in range(1,n):
            #Shift left to the right if s[right] in set
            while s[right] in sett:
                set.remove(s[left])
                left += 1
                
            sett.add(s[right])
            size = right - left + 1
            longest = max(longest, size)
        return longest
    
