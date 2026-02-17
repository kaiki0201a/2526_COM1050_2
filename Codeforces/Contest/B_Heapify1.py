#Hint:  Cac so o 1, 2, 4, 8... se doi cho duoc cho nhau tuy y
"""
Docstring for B_Heapify1
- 1 2 4 8 ...
- 3 6 12 ...
- 5 10 20 ...
- 7 14 ...
- 9 18...
- 11...
- Chỉ cần chung phần lẻ gốc thì luôn swap được một cách tuỳ ý
"""

t = int(input())

#Hàm lấy phần lẻ gốc
def get(x):
    while x % 2 == 0:
        x //= 2
    return x
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    # 1 <= i <= n/2
    arr = [0] + arr
    n += 1

    sw = True
    for i in range(1, n):
        if get(arr[i]) != get(i):
            sw = False
            break
    if sw:
        print("YES")
    else:
        print("NO")





    
