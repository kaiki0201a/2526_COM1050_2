#Input:
"""
- So the bai, va so tren cac the bai
"""
#Output:
"""
- Diem cua moi nguoi tren mot hang
- Moi luot thi nguoi choi luon chon la lon hon tu ben trai ngoai cung hoac ben phai ngoai cung
"""

n = int(input())
arr = list(map(int, input().split()))

Sereja, Dima = 0, 0
left, right = 0, len(arr) - 1

sw = True

while left <= right:

    if arr[left] > arr[right]:
        Choose= arr[left]
        left += 1
    else:
        Choose = arr[right]
        right -= 1
    
    if sw:
        Sereja += Choose
    else:
        Dima += Choose

    sw = not sw
    
print(Sereja, Dima)



