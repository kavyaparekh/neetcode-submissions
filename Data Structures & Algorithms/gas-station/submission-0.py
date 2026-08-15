class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totGas = 0
        totCost = 0
        start = 0
        currGas = 0
        for i in range(len(gas)):
            totGas += gas[i]
        for i in range(len(cost)):
            totCost += cost[i]
        if totGas < totCost:
            return -1
        elif totGas >= totCost:
            for i in range(len(gas)):
                currGas += (gas[i] - cost[i])
                if currGas < 0:
                    start = i+1
                    currGas = 0
        return start
