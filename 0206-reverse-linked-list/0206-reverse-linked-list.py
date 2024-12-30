# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize variables
        prev = None  # This will become the new head of the reversed list
        curr = head  # Start with the current node as the head of the list

        while curr:
            next_node = curr.next  # Store the next node
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move the 'prev' pointer to the current node
            curr = next_node       # Move to the next node in the list

        # At the end, 'prev' will be the new head of the reversed list
        return prev
