/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* prev = NULL; // This will be the new tail of the list, so it initially points to NULL.
    struct ListNode* curr = head; // Current node we're processing.

    while (curr != NULL) {
        struct ListNode* nextTemp = curr->next; // Temporarily store the next node.
        curr->next = prev;                      // Reverse the current node's pointer.
        prev = curr;                            // Move 'prev' one step forward (to the current node).
        curr = nextTemp;                        // Move 'curr' one step forward (to the next node).
    }

    return prev; // At the end, 'prev' will be the new head of the reversed list.
}
