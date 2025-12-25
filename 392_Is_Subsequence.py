class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        m = len(s)
        
        for i in t:
            if j < m:
                if i == s[j]:
                    j += 1

        if j == m:
            return True
        else: 
            return False
                


        
        
        