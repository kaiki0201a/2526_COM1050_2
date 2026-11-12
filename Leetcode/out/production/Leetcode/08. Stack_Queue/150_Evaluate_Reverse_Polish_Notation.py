def evalRPN( tokens: List[str]) -> int:
    stack = []

    for i in tokens:
        
        if i.lstrip("-").isdigit():
            stack.append(i)
        elif len(stack) >= 2:
            a1 = int(stack.pop())
            a2 = int(stack.pop())
            if i == "+":
                a = a1 + a2
            elif i == "-":
                a = a2 - a1
            elif i == "*":
                a = a1 * a2
            elif i == "/":

                #Phai xu ly voi phan am:
                #C1
                """
                a = int(a2) // int(a1)
                a3 = abs(int(a2)) // abs(int(a1))
                if a < 0:
                    a = -a3
                """
                #C2:
                a = int(a2/a1)
                
                
            stack.append(a)
        print("Check :", stack)
        
    return stack[-1]
print(evalRPN(["4","-2","/","2","-3","-","-"]))