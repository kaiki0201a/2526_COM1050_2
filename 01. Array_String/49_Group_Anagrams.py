#Ta se tao mot dictt de luu cac ki tu la anagram bang cach sap xep key lai

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dictt = {}


        for i in strs:
            
            #Check xem sau khi sap xep thi thuoc nhom nao
            s = sorted(i)
            s = "".join(s)

            #Join vao
            if s in dictt:
                dictt[s].append(i)
            else:
                dictt[s] = [i]

        #Lay value ra va cho vao mot list
        return list(dictt.values())