"""
- Toán
Để tìm một số có đúng đúng4 ước thì số đó phải thuộc một trong hai dạng sau:sau
1. Dạng tích của hai số nguyên tố khác nhau: n = p x q
2. Dạng lập phương của một số nguyên tố
- Theo code:
1. Các ước thường đi theo cặp
"""



#C1. Chưa dùng AI chỉ dùng hint
#Ý tưởng: từ 2-> căn n thì n chia hết cho đúng 1 số:i
# Từ căn n -> n thì n chia hết cho đúng 1 số là j = n/i

def sumFourDivisors( nums: List[int]) -> int:

    res = 0
    for i in nums:
        count = 0   
        uoc = 0

        #Đếm số < căn n
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                count += 1
                uoc = j

        #Check số > căn n
        if count == 1:
            k = i // uoc

            if uoc * k == i and k > int(i**0.5):
                res = res + uoc + k + 1 + i  
    return res
#C2.
#Các ước thường đi theo cặp trừ số chính phương hoặc tương tự
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0   #Biến lưu result

        for num in nums:
            divisors = set()

            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:    #Neu chia het, i la uoc va n/i la uoc
                    divisors.add(i)
                    divisors.add(num//i)    #No tu xu ly TH so chinh phuong

                    if len(divisors) > 4:
                        break    #Khong co so nao co 4 uoc, chuyen qua xet so khac
                
            if len(divisors) == 4:
                total_sum += sum(divisors)

        return total_sum
    
#C3. Hoi kho hieu: Kỹ thuật sàng(Sieve Approach)
# Ý tưởng: thay vì cầm từng số lên và kiểm tra xem có bao nhiêu ước thì ta sẽ lập một cái bảng thật lớn và điền số ước cho tất cả các số cùng một lúc


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        #B1: Chuẩn bị bảng
        m = max(nums)
        divs = [0 for i in range(m+1)]
        sums = [0 for i in range(m+1)]

        #B2: Thuật toán Sàng(Core Logic)
        for i in range(1, m+1, 1):      #Kiểm tra xem i có phải là ước không
            for j in range(i, m+1, i):  # j là bội của j, lọc các số là bội của j và cộng thêm 1 vào div, i vào sum
                divs[j] += 1
                sums[j] += i

        res = 0
        for i in nums:
            if divs[i] == 4:
                res += sums[i]

        return res


