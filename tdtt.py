#1
"""
x = range (3, 20, 2)
for i, n in enumerate(x):
    print(i,n)
for i, n in enumerate(x):
    if i % 2 ==0:
        print(i, n)
    elif i % 3 ==0:
        print(i, -n)
    else:
        print( " Okii ")
"""
#2
"""
def one_to_n(n):
    out = [ ] #tao mang out rong
    for i in range(1, n+1):
        out.append(str(i)) # ep kieu va them i vao out
    print(" ",join(out)) # them vao " " xen cac cac phan tu cua mang out
one_to_n(10)
"""
#3

def only(nums):
    return [x * 2 for x in nums if (x %2) ==0] # lay cac gia tri x nhan 2 khi x chay trong vong lap va thoa man x chia het cho 2
print(only([1,2,3,4,5,6]))
