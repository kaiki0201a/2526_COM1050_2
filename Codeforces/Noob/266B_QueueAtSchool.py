#Y tuong: dung con tro de duyet, neu swap roi thi cur += 2, khong thi cur += 1

child, time = map(int, input().split())

qu = input()    #0 -> child - 1
qu = list(qu)   #chuyen doi str -> list tung ki tu

while time >0:

    cur = 1

    sw = True   #Check xem co swap hay khong

    while cur < child:
        
        #Swap
        if qu[cur] == "G" and qu[cur-1] == "B":
            qu[cur], qu[cur-1] = qu[cur-1], qu[cur]
            cur += 2
            sw = False
        else:
            cur += 1
    
    if sw:
        break

    time -= 1
    
qu = "".join(qu)
print(qu)

        





