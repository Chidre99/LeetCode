class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True  # An empty tree is always a subtree
        if not root:
            return False  # A non-empty tree cannot be a subtree of an empty tree
        
        # Check if the current trees are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True  # Both trees are empty
        if not p or not q or p.val != q.val:
            return False  # One tree is empty or values differ
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
