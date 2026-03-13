class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs_diff = []
        ans = 0
        for cost in costs:
            diff = cost[0] - cost[1]
            costs_diff.append([cost[0],cost[1],diff])
        
        costs_diff = sorted(costs_diff, key=lambda item: item[2])

        for i in range(len(costs_diff)):
            if i < len(costs_diff)//2:
                ans += costs_diff[i][0]
            else:
                ans += costs_diff[i][1]
        
        return ans