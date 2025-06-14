class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                left_space = (i == 0) or (flowerbed[i - 1] == 0)
                right_space = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if left_space and right_space:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        
        return count >= n
