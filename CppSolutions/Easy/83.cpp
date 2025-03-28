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
        ListNode* deleteDuplicates(ListNode* head) {
            ListNode* act = head;
            while (act != nullptr && act->next != nullptr){
                if (act->val == act->next->val ){
                    ListNode* temp = act->next;
                    act->next = temp->next;
                    delete temp;
                }else{
                    act = act->next;
                }
            }
            return head;
        }
    };