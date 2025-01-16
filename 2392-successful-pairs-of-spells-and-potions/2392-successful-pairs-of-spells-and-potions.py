from typing import List
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort() 
        result = []
        n = len(potions)
        
        for spell in spells:
            min_potion = (success + spell - 1) // spell  
            index = bisect_left(potions, min_potion)
            result.append(n - index)
        
        return result
