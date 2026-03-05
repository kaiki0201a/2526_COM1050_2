#Tim vi tri sai it hon//

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        K_chan, K_le = 0, 0
        M_chan, M_le = 0, 0

        for i in range(n):
            if s[i] == "0":
                if i % 2 == 0:
                    K_chan += 1
                else:
                    K_le += 1
            else:
                if i % 2 == 0:
                    M_chan += 1
                else:
                    M_le += 1

        if M_chan + K_le > M_le + K_chan:
            return M_le + K_chan
        else:
            return M_chan + K_le