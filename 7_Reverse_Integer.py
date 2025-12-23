class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x_s = str(x)
            x_s = x_s[::-1]
        else:
            x_s = str(-x)
            x_s = "-" + x_s[::-1]
        if (-2)**31 <= int(x_s) <= 2**31 -1:
            return int(x_s)
        else:
            return 0
