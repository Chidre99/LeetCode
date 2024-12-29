# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []  # If the tree is empty, return an empty list
        
        result = []  # To store the rightmost node at each level
        queue = deque([root])  # Initialize a queue with the root node
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            
            for i in range(level_size):
                node = queue.popleft()  # Remove the node from the front of the queue
                
                # If this is the last node in the current level, add its value to the result
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add the left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
