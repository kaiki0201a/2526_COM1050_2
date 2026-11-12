n, m = map(int, input().split())

dictt_hs = {}

dictt_day = {}

for i in range(m):  #day thu i
    a, b = map(int, input().split())


#Tao dictt dem day
    if a in dictt_hs:
        dictt_hs[a] += 1
    else: 
        dictt_hs[a] = 1
    if b in dictt_hs:
        dictt_hs[b] += 1
    else:
        dictt_hs[b] = 1

#Tao dictt noi hoc sinh
    if a in dictt_day:
        dictt_day[a].append(b)
    else:
        dictt_day[a] = [b]
    if b in dictt_day:
        dictt_day[b].append(a)
    else:
        dictt_day[b] = [a]

res = 0
sw = True

while sw:
    lis = []

    count = 0
    for i in dictt_hs:
        if dictt_hs[i] == 1:
            lis.append(i)
            if dictt_hs[dictt_day[i][0]] != 1 and dictt_hs[dictt_day[i][0]] > 0:
                lis.append((dictt_day[i][0]))
            if dictt_hs[dictt_day[i][0]] == 1:
                dictt_hs[dictt_day[i][0]] = 0
            try:
                dictt_day(dictt_day[i][0]).remove([i])
            except:
                continue
            
            count = 1
    print(lis)
    if count == 0:
        sw = False
    if len(lis) > 0:
        res += 1
    if len(lis) > 0:
        for i in lis:
            dictt_hs[i] -= 1
    else:
        break
print(res)
        

    






        

        


