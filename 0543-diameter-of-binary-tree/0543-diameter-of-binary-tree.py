# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Initialize the diameter
        
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # Base case: the depth of an empty subtree is 0
            
            # Recursively find the depth of left and right subtrees
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            # Update the diameter with the larger path passing through the current node
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the depth of the current node
            return 1 + max(left_depth, right_depth)
        
        depth(root)  # Start recursion from the root
        return self.diameter
