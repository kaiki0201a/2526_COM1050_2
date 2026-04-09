class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        resa, resb, resc = [0], [0], [0]
        res2a, res2b, res2c = [0], [0], [0]

        for i in s:
            if i == "a":
                resa.append(resa[-1]+1)
            else:
                resa.append(resa[-1])
            if i == "b":
                resb.append(resb[-1]+1)
            else:
                resb.append(resb[-1])
            if i == "c":
                resc.append(resc[-1]+1)
            else:
                resc.append(resc[-1])
        s = s[::-1]
        for i in s:
            if i == "a":
                res2a.append(res2a[-1]+1)
            else:
                res2a.append(res2a[-1])
            if i == "b":
                res2b.append(res2b[-1]+1)
            else:
                res2b.append(res2b[-1])
            if i == "c":
                res2c.append(res2c[-1]+1)
            else:
                res2c.append(res2c[-1])
        res2a = res2a[::-1]
        res2b = res2b[::-1]
        res2c = res2c[::-1]
        print(resa)
        print(res2a)
        print(resb)
        print(res2b)
        print(resc)
        print(res2c)
        
p1 = Solution()
print(p1.longestBalanced("aabcc"))