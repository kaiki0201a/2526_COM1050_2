class Solution:
    def simplifyPath(self, path: str) -> str:
        
        #Tach ra va loai bo / thua
        path = path.split("/")
        stack = []

        i = 0
        while i < len(path):

            if path[i] == "." or path[i] == "":     #Khong lam gi ca
                i += 1
                
            elif path[i] == "..":   # Xoa cai gan nhat vi ..: thu muc cha
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(path[i])

            i += 1
        stack = "/" + "/".join(stack)

        return stack



