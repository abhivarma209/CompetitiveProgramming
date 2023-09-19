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
    ListNode* swapPairs(ListNode* head) {
        ListNode* res = new ListNode(0);
        res->next = head;
        ListNode* curr=res;
        while(curr->next && curr->next->next ){
            ListNode* first=curr->next;
            ListNode* second=curr->next->next;
            first->next=second->next;
            curr->next=second;
            second->next=first;
            curr=first;
        }
        return res->next;
    }
};