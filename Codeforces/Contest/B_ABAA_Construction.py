t = int(input())

"""
- n chan thi a,b luon ton tai
- n le thi hoac a,a hoac b,b
- ? thi danh gia chi so dung sau
"""
for _ in range(t):
    n = int(input())
    s = input()
    T = []
    for j in range(n):
        if j % 2 == 0:
            T.append("a")
        else:
            T.append("b")
    l = n
    left, right = 0, n-1

    sw = True
    if n % 2 == 0:
        choose = True
    else:
        choose = False

    for i in range(n):
        if not choose:
            if s[i] == T[left]:
                left += 1
            elif s[i] == T[right]:
                right -= 1
            elif s[i] == "?":
                if i < n-1:
                    if s[i+1] == T[left]:
                        right -= 1
                    elif s[i+1] == T[right]:
                        left += 1
                    else:
                        left += 1
            else:
                sw = False
                print("NO")
                break
        else:
            if s[i] == T[left]:
                left += 1
            elif s[i] == T[right]:
                right -= 1
            else:
                if i < n-1:
                    if s[i+1] == T[left]:
                        right -= 1
                    elif s[i+1] == T[right]:
                        left += 1
                    else:
                        left += 1
        choose = not choose
    if sw:
        print("YES")
        
        
        


    