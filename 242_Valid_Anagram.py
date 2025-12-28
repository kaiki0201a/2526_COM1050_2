def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    #Dem tung str
    for i in range(len(s)):
        #Lenh get giong nhu hoi xem co key s[i] khong
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        #Kiem tra xem co cung ki tu- so luong ki tu khong
        if countS[c] != countT.get(c, 0):
            return False
        
    return True