# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]

max_profit = 0

for i in range(len(prices)-1):
    for j in range(i+1, len(prices)):
        profit = prices[j] - prices[i]
        # check if the profit is greater than max_profit
        if profit>max_profit:
            max_profit = profit

        # check all loops
        print(f'{prices[i]}-{prices[j]}= {profit}')

                   
print(max_profit)
