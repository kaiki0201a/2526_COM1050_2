#Hint: Neu khong bat dau bang 4/9 hay chon ky hieu toi da tru di gia tri nhap vao
#Them ki hieu vao va tiep tuc lam voi phan du
#Neu bat dau = 4/9, lay ra luon

#C1: Noob
class Solution1:
    def intToRoman(self, num: int) -> str:

        s = ""
        if num >= 1000:
            k = num // 1000
            num = num % (k *1000)
            s += k*"M"
        if num >= 100:
            k = num//100
            if k == 4:
                s += "CD"
            elif k == 9:
                s += "CM"
            elif k < 5:
                s += k*"C"
            else:
                s = s + "D" + (k-5)*"C"
            num = num % (k*100)
        if num >= 10:
            k = num//10
            if k == 4:
                s += "XL"
            elif k == 9:
                s += "XC"
            elif k < 5:
                s += k*"X"
            else:
                s = s + "L" + (k-5)*"X"
            num = num % (k*10)
        if num > 0:
            if num == 4:
                s += "IV"
            elif num == 9:
                s += "IX"
            elif num < 5:
                s += num*"I"
            else:
                s = s + "V" + (num-5)*"I"
        
        return s
    
#C2. Clean
class Solution2:
    def intToRoman(self, num: int) -> str:
        #Creating Dict for lookup
        num_map = {
            1: "I",
            5: "V",     4: "IV",
            10: "X",    9: "IX",
            50: "L",    40: "XL",
            100: "C",   90: "XC",
            500: "D",   400: "CD",
            1000 :"M",  900: "CM"
        }

        #result variable
        res = ""
        for n in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
            while n <= num:
                res += num_map[n]
                num -= n
        
        return res
p1 = Solution2()
print(p1.intToRoman(3749))