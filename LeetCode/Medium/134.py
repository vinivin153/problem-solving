class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        idx = 0
        total_gas = 0
        current_gas = 0

        for i in range(n):
            get_gas = gas[i] - cost[i]
            total_gas += get_gas
            current_gas += get_gas

            if current_gas < 0:
                idx = i + 1
                current_gas = 0
            
        if total_gas < 0:
            return -1
        else:
            return idx