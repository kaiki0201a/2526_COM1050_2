#Khi gap gia lon hon thi ban luon
#Cap nhat lai gia mua neu da ban hoac gap gia mua thap hon

def maxProfit(prices: List[int]) -> int:
    buy_on = 0
    profit = 0

    for sell_on in range(len(prices)):

        if prices[sell_on] > prices[buy_on]:
            profit = profit + prices[sell_on] - prices[buy_on]
            print("CHECK: ",prices[sell_on], prices[buy_on])

        #Cap nhat gia mua (always)
        buy_on = sell_on
        
    return profit
print(maxProfit([7,1,5,3,6,4]))