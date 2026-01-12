#Vasya has recently learned to type. Determine whether Vasya managed to say hello by given word s.
#We will deleted some word and result is "hello" -> yes. ex: ahhellllooou

#Y tuong dung two point de tim tung chu trong hello

form = "hello"

s = input()

j = 0   #index 0 of form to find h

for i in s:
    if i == form[j]:
        j += 1

    if j == len(form):  #Khi tim duoc ki tu cuoi => j = len(form) -1 + 1 = len(form)
        break
    

if j == len(form):
    print("YES")
else:
    print("NO")

