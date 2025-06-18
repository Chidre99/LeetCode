class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        prev = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[prev]:
                if neededTime[prev] < neededTime[i]:
                    total += neededTime[prev]
                    prev = i
                else:
                    total += neededTime[i]
            else:
                prev = i
        return total
