class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        # Initialize variables
        dq = deque()  # Stores indices of elements in the current window
        result = []   # Stores the maximums of each window
        
        for i in range(len(nums)):
            # Remove indices that are out of the window's range
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove indices of elements smaller than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add the current index
            dq.append(i)
            
            # Add the maximum of the current window to the result
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
