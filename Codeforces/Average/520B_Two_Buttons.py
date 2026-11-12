"""
Neu tu duy greedy bình thường cứ nhân 2 lên rồi cuối cùng trừ đi phần dư tốn step
- Ta sẽ suy từ m - n rồi trừ đi phần dư thì hợp lý hơn
- Với m chẵn thì ta chia 2
- Với m lẻ thì ta cộng 1, khi đó n sẽ -1 
"""
n, m = map(int, input().split())    #So ban dau, so muc tieu

#Tu duy nguoc di tim m - n
step = 0

while m > n:

    if m % 2 != 0:
        step += 1
        m += 1
        continue
    m = m // 2
    step += 1

print(step + abs(n-m))
