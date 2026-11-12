from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictt = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        n = len(digits)

        res = deque()

        for i in dictt[digits[0]]:

            res.append(i)
        
        print("CHECK 0", res)

        for i in digits[1:]:    # i day la so

            n = len(res)

            for j in range(n):  # j la so luong tu se lay ra
                b = res.popleft()

                for h in dictt[i]:
                    k = b
                    k = k + h
                    res.append(k)

        print(res)

p1 = Solution()
print(p1.letterCombinations("23"))