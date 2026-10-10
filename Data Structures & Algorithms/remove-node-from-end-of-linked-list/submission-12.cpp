/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
    
    ListNode* dummy = new ListNode(0, head); // dummy handles edge case of removing head
    ListNode* left = dummy;
    ListNode* right = head;

    // advance right by n steps
    while (n--) right = right->next;

    // move both until right hits end
    while (right) {
        left = left->next;
        right = right->next;
    }

    // left is now just before the node to remove
    left->next = left->next->next;

    return dummy->next;
    }
};
