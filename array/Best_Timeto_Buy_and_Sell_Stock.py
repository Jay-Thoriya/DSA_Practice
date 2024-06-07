# Input: prices[] = {7, 1, 5, 3, 6, 4}
# Output: 5
# Explanation:
# The lowest price of the stock is on the 2nd day, i.e. price = 1. Starting from the 2nd day, the highest price of the stock is witnessed on the 5th day, i.e. price = 6. 
# Therefore, maximum possible profit = 6 – 1 = 5. 

# Input: prices[] = {7, 6, 4, 3, 1} 
# Output: 0
# Explanation: Since the array is in decreasing order, no possible way exists to solve the problem.

# complexity O(n^2)
def chkStockPrice(a):
    minPrice = a[0]
    maxPrice = 0
    for i in range(1,len(a)):
        if(minPrice+1> a[i]):
            minPrice = a[i]
            if(len(a)-1==i):
                return 0
    for j in range(a[minPrice]+1,len(a)):
        if(maxPrice < a[j]):
            maxPrice = a[j]
    return maxPrice - minPrice


# complexity O(n)
def maxProfit(prices, n):
    buy = prices[0] # buy = 7
    max_profit = 0
    for i in range(1, n):

        # Checking for lower buy value
        if (buy > prices[i]): 
            buy = prices[i]

        # Checking for higher profit
        elif (prices[i] - buy > max_profit):
            max_profit = prices[i] - buy
    return max_profit


# Driver code
if __name__ == '__main__':
                    
    prices = [7, 1, 5, 6, 4]
    n = len(prices)
    max_profit = maxProfit(prices, n)
    print(max_profit)
    print(chkStockPrice(prices))