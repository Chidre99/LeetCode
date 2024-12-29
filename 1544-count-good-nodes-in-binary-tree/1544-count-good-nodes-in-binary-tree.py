class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0  # Base case: no nodes in an empty subtree
            
            # Check if the current node is "good"
            is_good = node.val >= max_val
            count = 1 if is_good else 0
            
            # Update the maximum value for the path to the children
            max_val = max(max_val, node.val)
            
            # Recur for the left and right children
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            
            return count
        
        return dfs(root, root.val)
