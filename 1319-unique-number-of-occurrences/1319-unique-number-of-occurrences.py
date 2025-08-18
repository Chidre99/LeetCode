class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence = {}

        for num in arr:
            occurrence[num] = occurrence.get(num,0) + 1

        counts = occurrence.values()
        if len(counts) == len(set(counts)):
            return True
        return False
