class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        
        total_freq = freq1 + freq2
        min_fruit = min(min(basket1), min(basket2))
        
        for fruit in total_freq:
            if total_freq[fruit] % 2 != 0:
                return -1
        
        surplus1 = []
        surplus2 = []
        
        for fruit in total_freq:
            diff = freq1[fruit] - freq2[fruit]
            if diff > 0:
                surplus1 += [fruit] * (diff // 2)
            elif diff < 0:
                surplus2 += [fruit] * ((-diff) // 2)
        
        surplus1.sort()
        surplus2.sort(reverse=True)
        
        cost = 0
        for a, b in zip(surplus1, surplus2):
            cost += min(a, b, 2 * min_fruit)
        
        return cost
