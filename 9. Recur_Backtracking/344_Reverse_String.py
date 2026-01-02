#Đảo ngược chuỗi
#1. Decomposition
"""
- Vấn đề lớn: Đảo ngược cả một mảng s từ đầu đến cuối
- Chia nhỏ: muốn đảo ngược ta đảo phần tử đầu và phần cuối
- Phần còn lại: sau khi đổi 2 đầu ta lại làm với mảng bên trong
"""
#2. Pattern Recognition
"""
- Thao tác lặp đi lặp lại: lấy thằng [0] đổi chỗ với thằng [n-1]
- Sau đó thu hẹp đến khi gặp nhau

"""

#C1. Two point
class Solution:
    def ReverseString(self, s):
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return s

#C2: Recursive
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left >= right:
                return s
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right -1)

        helper(0, len(s) - 1
