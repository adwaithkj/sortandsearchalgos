class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        tg=0
        start=0
        remaining=0
        for i in range(len(cost)):
            tg+=gas[i]-cost[i]
            remaining+=gas[i]-cost[i]

            if remaining<0:
                start=i+1
                remaining=0

        if tg<0:
            return -1
        else:
            return start
        return -1
        