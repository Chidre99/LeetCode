class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element
        freq_map = Counter(nums)
        
        # Use a heap to get the k most frequent elements
        return [item for item, _ in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]
