class Solution:
    """
    @param: prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        if prices == []:
            return 0
        a = list()
        a.append(prices[0])
        
        for x in range(1, len(prices)-1):
            if prices[x] < prices[x + 1] and prices[x - 1] > prices[x]:
                a.append(prices[x])
            if prices[x] > prices[x + 1] and prices[x - 1] < prices[x]:
                a.append(prices[x])
                
        a.append(prices[len(prices) - 1])
        total = 0
        for n in range(0, len(a)):
            max = a[n]
            for m in range(n, len(a)):
                if a[m] > max:
                    max = a[m]
            if total < max - a[n]:
                total = max - a[n]
        return total


s = Solution()
s.maxProfit([2, 1, 2, 0, 1])
