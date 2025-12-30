
def wordPattern( pattern: str, s: str) -> bool:
    s = s.split()
    if len(s) != len(pattern):
        return False

    pa_word = {}#Luu pattern
    word = {}   #Luu string

    n = len(s)
        
    for i in range(n):
        #Check tung tu trong pattern, dictt la pa_word
        if pattern[i] not in pa_word:
            pa_word[pattern[i]] = s[i]
        else:
            if s[i] != pa_word[pattern[i]]:
                return False
        
        #Check tung tu trong s, dictt la word
        if s[i] not in word:
            word[s[i]] = pattern[i]
        else:
            if pattern[i] != word[s[i]]:
                return False 

    return True    
print(wordPattern("abba", "dog cat cat dog"))       