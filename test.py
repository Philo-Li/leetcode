class Solution(object):
    def gridTrading(self, low, high, nowPrice, gridNums, balance, leverage, volatility):
        """
        type low: int
        type high: int
        type nowPrice: int
        type gridNums: int
        type balance: int
        type leverage: int
        type votality: float
        """
        inteval = (high - low) // gridNums
        oneShot = balance / gridNums * leverage
        longPosition = list(range(low, nowPrice, inteval))
        shortPosition = list(range(nowPrice, high, inteval))
        print("做多网格：", longPosition)
        print("做空网格：", shortPosition)
        print("单次购买量", oneShot)
        buyETH , newBalance = 0.0 , 0.0
        for i in range(volatility):
            for j in range(i):
                newBalance -= buyETH * inteval
            buyETH += oneShot / (nowPrice - i * volatility)
        newPrice = nowPrice * ( 1 - 1.0 * volatility / 100)
        print("ETH", buyETH, "new price", newPrice)
        print("亏损（浮亏）", newBalance, "账户余额", balance)
        print("爆仓？", balance + newBalance <= 0)
        
        
        return balance

if __name__ == '__main__':
    solution = Solution()
    # print(solution.gridTrading(1000, 3009, 1768, 120, 640, 100, 7))
    # print(solution.gridTrading(1000, 3009, 1768, 120, 640, 100, 11))
    # print(solution.gridTrading(1000, 3009, 1768, 120, 640, 20, 12))
    # print(solution.gridTrading(1000, 3009, 1768, 120, 640, 1, 30))
    # print(solution.gridTrading(1000, 3009, 1768, 120, 6000, 1, 30))
    print(solution.gridTrading(1200, 2200, 1761, 60, 640, 100, 6))
    print(solution.gridTrading(1673, 1850, 1761, 25, 660, 100, 6))



