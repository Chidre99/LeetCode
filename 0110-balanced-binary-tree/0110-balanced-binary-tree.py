class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # Base case: the height of an empty subtree is 0
            
            # Recursively calculate the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # If any subtree is unbalanced, propagate -1 up the recursion
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the current subtree
            return 1 + max(left_height, right_height)
        
        # Start the recursion and check if the result is -1 (unbalanced)
        return height(root) != -1
