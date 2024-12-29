# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # Initialize max_sum to negative infinity
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # Base case: the contribution of a null node is 0
            
            # Compute the maximum path sum for the left and right subtrees
            # If the subtree contributes negatively, we take 0 (ignore the subtree)
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Compute the price of the current path: node value + left + right
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum sum if the current path sum is greater
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the node's maximum gain if used as part of its parent's path
            return node.val + max(left_gain, right_gain)
        
        dfs(root)  # Start DFS traversal from the root
        return self.max_sum