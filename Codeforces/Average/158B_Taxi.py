#Cho n nhom di taxi, moi nhom max 4 dua, xe max 4 cho, tinh so xe sao cho cac thanh vien deu di chung

s = int(input())
listt = list(map(int, input().split()))

taxi = 0
dictt = {1: 0, 2: 0, 3: 0, 4: 0}
for i in listt:
    dictt[i] += 1

#Xe 4 thi chi co the di le
taxi += dictt[4]

#Xe 3 so luon di voi xe 1 de toi uu
taxi += dictt[3]
if dictt[1] >= dictt[3]:
    dictt[1] = dictt[1] - dictt[3]
else:
    dictt[1] = 0
#Xe 2 se di voi xe 2 de toi uu
taxi += dictt[2] // 2

#Neu xe 2 con hoac xe 1 con
if dictt[2] % 2 != 0:
    if dictt[1] <= 2:
        taxi += 1
        dictt[1] = -1
    else:
        taxi += 1
        dictt[1] -= 2
    
if dictt[1] % 4 != 0 and dictt[1] > 0:
    taxi += dictt[1]//4 + 1
elif dictt[1] % 4 == 0 and dictt[1] > 0:
    taxi += dictt[1]//4

print(taxi)


