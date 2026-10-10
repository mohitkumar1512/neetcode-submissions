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
    void reorderList(ListNode* head) {
        
        // doing this my slow should be at the middle of the entire list. 
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* prev = nullptr;
        ListNode* next = nullptr;
        while (slow != nullptr){
            next = slow->next;
            slow->next = prev;
            prev = slow;
            slow = next;
        }  
        ListNode* start = head;
        ListNode* temp = nullptr;
        ListNode* temp2 = nullptr;
        while (prev->next && start->next){
            temp = start->next;
            temp2 = prev->next;
            
            start->next = prev;
            prev->next = temp;
            
            prev = temp2;
            start = temp;
          
        } 
        
        
    }
};
