class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def findlong(a: List[int]) -> int:
            sett = set(a)

            res = 0

            for i in sett:
                if i -1 not in sett:

                    j = i
                    while j in sett:
                        j += 1
                    
                    res = max(res, j - i)

            return res

        h = min(findlong(hBars),findlong(vBars))
        return (h+1)**2