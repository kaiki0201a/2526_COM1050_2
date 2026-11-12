class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dictt = {5: 0, 10: 0}

        for i in bills:
            if i == 5:
                dictt[5] += 1
            elif i == 10:
                if dictt[5] > 0:
                    dictt[10] += 1
                    dictt[5] -= 1
                else:
                    return False
            else:
                if dictt[5] > 0 and dictt[10] > 0:
                    dictt[5] -= 1
                    dictt[10] -= 1
                elif dictt[5] > 2:
                    dictt[5] -= 3
                else:
                    return False
        
        return True
