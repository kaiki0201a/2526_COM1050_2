#C1. Khong toi uu
def Pow(x, n):
    if n == 0:
        return 1
    else:
        if n > 0:
            k = Pow(x, n-1) * x
        else:
            k = Pow(x, n + 1) / x
        return k

#C2. Toi uu
"""
Nhan xet: 
- Khi n mũ chẵn, ta sẽ chia đôi ra 2 phần để tính thay vì tính từng cái
- VD:2^6 -> 2^3 * 2^3 -> 2* 2^2 *2*2^2 -> 2* 2*2 *2*2*2 ->
- Xử lý n < 0: đảo ngược x: x = 1/x, n = -n
- VD 2 ^ -2 : 1/2^2

"""
def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return myPow(1/x, -n)

    if n % 2== 0:
        half = myPow(x, n//2)
        return half * half
    else:
        return x * myPow(x, n-1) 
print(myPow(2,-2))