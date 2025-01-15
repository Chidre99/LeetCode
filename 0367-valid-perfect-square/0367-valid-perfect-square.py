class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i, j = 0, num
        while i <= j:
            mid = (i + j) // 2
            curr = mid * mid  
            if curr == num:  
                return True
            elif curr < num:  
                i = mid + 1
            else: 
                j = mid - 1
        return False  