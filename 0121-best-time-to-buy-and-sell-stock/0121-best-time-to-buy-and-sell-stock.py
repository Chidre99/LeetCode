class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables
        min_price = float('inf')  # Smallest possible price
        max_profit = 0            # Maximum profit
        
        # Traverse the prices
        for price in prices:
            # Update minimum price if a lower price is found
            if price < min_price:
                min_price = price
            # Calculate potential profit
            profit = price - min_price
            # Update max profit if the potential profit is larger
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
