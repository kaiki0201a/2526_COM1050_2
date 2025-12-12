#BT5: Dem so 0 tan cung cua n giai thua
def dem_so(n):
    ans = 0
    while n >= 5:
        n //=5
        ans += n
    return ans
n = int(input())
print(f"So 0 tan cung trong {n}! la: ",dem_0(n))
