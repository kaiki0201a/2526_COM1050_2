#Xoa nguyen am va chen dau . truoc phu am, output toan so thuong

s = input()
s = s.lower()
sett = {"u", "e", "o", "a", "i", "y"}

s = list(s)

s_new = ""
for i in s:
    if i not in sett:
        s_new += "." + i
print(s_new)