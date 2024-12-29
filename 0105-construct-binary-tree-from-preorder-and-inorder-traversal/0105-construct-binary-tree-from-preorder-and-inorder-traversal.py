# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None  # Base case: If there are no nodes to process
        
        # The first element of preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder traversal
        root_index_inorder = inorder.index(root_val)
        
        # Split the inorder list into left and right subtrees
        left_inorder = inorder[:root_index_inorder]
        right_inorder = inorder[root_index_inorder + 1:]
        
        # Split the preorder list into left and right subtrees
        left_preorder = preorder[1:1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root