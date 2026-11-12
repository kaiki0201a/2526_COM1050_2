class Solution:
    def myAtoi(self, s: str) -> int:
        #Xoa white space
        s = s.lstrip()
        if len(s) == 0:
            return 0
        #Kiem tra ki tu dau
        sw = ""
        if s[0] == "-":
            sw = "-"
            s = s[1:]
        elif s[0] == "+":
            sw = ""
            s = s[1:]
        elif ("0" > s[0]) or s[0] > "9":
            return 0

        #Loai bo chu so 0 dung dau
        n = len(s)
        i = 0
        while i < n:
            if s[i] == "0":
                i+= 1
            else:
                s = s[i:]
                break
        
        #Xet cac phan tu dung sau:
        n2 = len(s)
        j = 0
        while j < n2:
            if "0" <= s[j] <= "9":
                j += 1
            else:   #while s[j] is not digit
                s = s[:j]
                break
        if len(s) > 0:
            s = sw + s
            if int(s) >= 2**31 -1:
                return 2**31 -1
            elif int(s) <= (-2)**31:
                return (-2)**31
            else:
                return int(s)
        else:
            return 0

