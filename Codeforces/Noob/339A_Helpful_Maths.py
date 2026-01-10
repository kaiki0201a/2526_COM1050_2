
s = input()
s = s.split("+")

s.sort()
s_new = ""
for i in s:
    s_new += i + "+"
s_new = s_new.rstrip("+")

print(s_new)