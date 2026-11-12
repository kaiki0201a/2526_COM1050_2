#Y tuong: dung mang 2 chieu
"""
Gia su dp[i][j] la gia tri toi thieu can xoa cua s1[i:] va s2[j:]

-
Neu s1[i] = s2[j] => khong can xoa gi ca, lay cai doi dien cua duoi
Neu s1[i] != s2[j] cai nao nho hon thi xoa
"""
class Solution():
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        # Tạo bảng DP kích thước (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        #Neu s1 het: chi phi la tong s2
        for i in range(n-1, -1,-1):
                dp[m][i] = dp[m][i+1] + ord(s2[i])

        #Neu s2 het: chi phi la tong s1
        for i in range(m-1, -1, -1):
                dp[i][n] = dp[i+1][n] + ord(s1[i])

        for i in range(m-1, -1, -1):
                
            for j in range(n-1, -1, -1):
                   
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    mo1 = dp[i][j+1] + ord(s2[j])
                    mo2 = dp[i+1][j] + ord(s1[i])

                    dp[i][j] = min(mo1, mo2)

        return dp[0][0]

#C2: Tuong tu nhung theo chieu nguoc lai: de hon
class Solution2():
    def mini(self, s1, s2) -> int:
          
        total = 0
        for i in s1:
            total += ord(i)
        for i in s2:
             total += ord(i)

        m = len(s1)
        n = len(s2)

        dp = [[0]* (m+1) for _ in range(n+1)]

        for i in range(1, m+1):
             
            for j in range(1, n+1):
                
                #Bang nhau thi them
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return total - 2*dp[n][m]
                
p1 = Solution2()
print(p1.mini("sea", "eat"))