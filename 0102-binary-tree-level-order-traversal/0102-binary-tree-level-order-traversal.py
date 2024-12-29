# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # If the tree is empty, return an empty list
        
        result = []  # To store the values of nodes at each level
        queue = deque([root])  # Initialize a queue with the root node
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level = []  # To store the values of nodes at the current level
            
            for _ in range(level_size):
                node = queue.popleft()  # Remove the node from the front of the queue
                level.append(node.val)  # Add its value to the current level
                
                # Add the left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)  # Add the current level to the result
        
        return result
