class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track numbers seen in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                # Check row
                if num in rows[r]:
                    return False
                rows[r].add(num)
                
                # Check column
                if num in cols[c]:
                    return False
                cols[c].add(num)
                
                # Check sub-box
                box_index = (r // 3) * 3 + (c // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        return True
