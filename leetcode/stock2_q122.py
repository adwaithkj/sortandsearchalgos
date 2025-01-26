class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        x=0
        y=0
        b=0
        s=0
        sum1=0
        for i in range(len(prices)):
            if i==0:
                b=prices[i]
                s=prices[i]
            else:
                if prices[i]<b:
                    # sum1+=s-b
                    b=prices[i]
                    x=i
                    s=prices[i]
                    y=i
                elif prices[i]>b:
                    sum1+=prices[i]-b
                    b=prices[i]
                    x=i
                    s=prices[i]
                    y=i

        return sum1
                    

        