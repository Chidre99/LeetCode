# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order_traversal(node: Optional[TreeNode]):
            if not node:
                return []
            # Traverse left subtree, then the node, then the right subtree
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        # Perform an in-order traversal and get the k-th smallest element
        in_order = in_order_traversal(root)
        return in_order[k - 1]
