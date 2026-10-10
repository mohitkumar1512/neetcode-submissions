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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* rightNode = nullptr;
        ListNode* rightNodeNext = nullptr;
        
        ListNode* head_copy = head;
        for (int i = 0; i < right; i++){
            rightNode = head_copy;
            head_copy = head_copy->next;
        }
        rightNodeNext = rightNode->next;
        head_copy = head;
        
        ListNode* leftNode = head_copy;
        ListNode* leftNodePrev = nullptr;
        ListNode* leftNodeCopy = nullptr;
        head_copy = head_copy->next;
        for (int i = 1; i < left; i++){
            leftNodePrev = leftNode;
            leftNode = head_copy;
            head_copy = head_copy->next;
        }
        leftNodeCopy = leftNode;
        ListNode* pre = leftNodePrev;
        while (leftNode != rightNodeNext){
            ListNode* leftNext = leftNode->next;
            leftNode->next = leftNodePrev;
            leftNodePrev = leftNode;
            leftNode = leftNext;
        }
    
        leftNodeCopy->next = rightNodeNext;
        if (pre) pre->next = leftNodePrev;   // node(1)->next = node(4) 
        return (left == 1) ? leftNodePrev : head;
    }

};