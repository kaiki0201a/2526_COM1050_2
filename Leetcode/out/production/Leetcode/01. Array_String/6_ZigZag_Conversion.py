#Before
class Solution:      
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        n = len(s)
        count = 1
        if numRows == 1 or numRows >= len(s):
            return s

        for i in range(0, n, (numRows - 1)*2):
            res += s[i]
        
        
        while count < numRows - 1 :
            strr = "" + s[count]
            i, j = count, 0     #j luu bien step, i luu gia tri

            while i < n:

                if j % 2 == 0:
                    step = (numRows - count - 1)*2
                    if i+step < n:
                        i += step
                        strr += s[i]
                    else: break
                else:
                    step = (count)*2
                    if i+step < n:
                        i+= step
                        strr += s[i]
                    else: break
                j += 1
            count += 1
            res += strr
        for i in range(numRows -1, n, (numRows - 1)*2):
            res += s[i]

        return res






