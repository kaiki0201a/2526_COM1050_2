#Danh gia S = 3p - 2q voi p giam va q giam

t = int(input())
for _ in range(t):
    p, q = map(int, input().split())

    if q > p and 3*p >= 2*q:
        print("Bob")
    else:
        print("Alice")



