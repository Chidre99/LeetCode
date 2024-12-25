class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:  # Use `<=` to ensure all elements are checked
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid  # Found the target
            
            # Determine which side is sorted
            if nums[low] <= nums[mid]:  # Left half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Target is in the left sorted half
                else:
                    low = mid + 1  # Target is in the right half
            else:  # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1  # Target is in the right sorted half
                else:
                    high = mid - 1  # Target is in the left half
        
        return -1  # Target not found
