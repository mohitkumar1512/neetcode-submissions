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
        if (!head) return nullptr;

        int l = len(head);
        int toRemove = l - n;
        if (toRemove <= 0){
            return head->next ? head->next : nullptr;
        }
        ListNode* prev = head;
        ListNode* curr = head;
        while (toRemove){
            prev = curr;
            curr = curr->next;
            toRemove -= 1;
        }
        prev -> next = curr->next;
        return head;

    }
    int len(ListNode* head){
        int ret = 0;
        while(head){
            ret += 1;
            head = head->next;
        }
        return ret;
    }
};
