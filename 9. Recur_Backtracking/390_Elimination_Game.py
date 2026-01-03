#C1. Tran(Time limit)
def recur(arr: list, j):
    if len(arr) == 1:
        return arr[0]
            
    else:
        if j %2 == 0:
            i  = 0
            while i < len(arr):
                del arr[i]
                i += 1
                print("CHECK: ",arr)
        else:
            i = len(arr)-1
            while i >= 0:
                del arr[i]
                i -= 2
                print("CHECK: ",arr)
        return recur(arr, j+1)

#C2. 
#Y tuong: ta chi quan tam den so dung dau la gi
#Cu moi lan xoa thi step * 2


def Recursivee(head, n, step, i, remain):

    if remain == 1:     #Khi chi con lai 1 so
        return head
    
    #i % 2: xoa tu dau -> cuoi, i /%2 thi xoa tu cuoi -> dau

    #Neu xoa tu dau thi head luon cap nhat
    if i % 2 == 0:
        head = head + step

    #Xoa tu cuoi
    else:
        # Neu con lai chan so thi so dau khong bi xoa, con le thi bi xoa
        if remain %2 != 0:
            head = head + step
            
    step *= 2
    remain = remain //2
    return Recursivee(head, n, step, i+ 1, remain)
print(Recursivee(1,6,1,0,6))
        
    
