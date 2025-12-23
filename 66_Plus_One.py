class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        if digits[n] < 9:
            digits[n] += 1
            return digits
        else:
            count = 1
            while n-1 >=0:
                if digits[n-1] == 9:
                    count += 1
                    n -= 1
                else: break
            if count == len(digits):
                digits = [1] + [0]*(len(digits))
            else:
                digits[n-1] += 1
                digits[n:] = [0]*count
            return digits