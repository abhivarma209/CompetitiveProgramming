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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* curr=new ListNode(0);
        ListNode* res=curr;
        int carry=0;
        while(carry || (l1||l2)){
            int res=0;
            if(l1){
                res+=l1->val;
                l1=l1->next;
            }
            if(l2){
                res+=l2->val;
                l2=l2->next;
            }
            res+=carry;
            ListNode* y= new ListNode(res%10);
            curr->next=y;
            curr=y;
            carry=res/10;
            
            
        }
        return res->next;
    }
};