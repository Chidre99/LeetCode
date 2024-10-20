/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 
// Definition for singly-linked list.
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    // Create a dummy node to act as the start of the merged list
    struct ListNode dummy;
    struct ListNode* tail = &dummy; // Tail always points to the last node of the merged list
    dummy.next = NULL; // Initializing the dummy next pointer

    // While both lists are not empty, compare and link nodes
    while (list1 != NULL && list2 != NULL) {
        if (list1->val < list2->val) {
            tail->next = list1; // Attach the smaller node to the merged list
            list1 = list1->next; // Move the pointer to the next node in list1
        } else {
            tail->next = list2; // Attach the smaller node to the merged list
            list2 = list2->next; // Move the pointer to the next node in list2
        }
        tail = tail->next; // Move the tail pointer
    }

    // At this point, one of the lists is exhausted. Attach the remaining nodes of the other list.
    if (list1 != NULL) {
        tail->next = list1;
    } else {
        tail->next = list2;
    }

    // Return the next node of the dummy (the head of the merged list)
    return dummy.next;
}
