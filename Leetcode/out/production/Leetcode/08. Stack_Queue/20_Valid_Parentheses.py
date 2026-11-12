def isValid(s: str) -> bool:
    
    listt = []  #Stack
    set_open = ("(", "[", "{")  #Check set

    for i in s:

        #Neu i la ngoac mo:
        if i in set_open:
            listt.append(i)
        
        #Neu i la ngoac dong
        else:

            #Neu len(listt) > 0: truoc do ton tai ngoac mo / return False
            if len(listt) > 0:

                #Neu no la ngoac cung loai:
                if (listt[-1] == "(" and i == ")") or (listt[-1] == "[" and i == "]") or (listt[-1] == "{" and i == "}"):
                    listt.pop()
                
                else:
                    return False
            
            else: return False
    
    #Neu no triet tieu het
    return True if len(listt) == 0 else False