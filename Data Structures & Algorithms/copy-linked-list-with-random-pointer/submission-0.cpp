/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head == nullptr) return nullptr;

        Node* curr = head;

        //Pass1: interleave copied nodes
        while(curr!=nullptr){
            Node* copy = new Node(curr->val);//creates a node (copy) with the same value as the current original node
            copy->next = curr->next;//point the copy's next to whatever the og node was pointing to
            curr->next = copy;//insert the copie node immediately after the og node (A->A'->B->B')
            curr = copy->next;//move curr ptr fwd to the next og node(skip the copy)
        }
        //current pass result: A->A'->B->B'->C->C'
        //A.random = C

        //Pass2: assign random pointers for copies
        curr = head;//curr=A
        while(curr != nullptr){
            if(curr->random != nullptr){//check if og node has a random pointer
                //curr->random = C, curr->next=A', curr->random->next=C'
                curr->next->random = curr->random->next;
                //copy node's random = copy of curr->random 
                //now A'.random=C'
            }
            curr = curr->next->next;//move to the next og node    
        }   //curr = B

        //Pass 3: Separate og list and copied list
        curr = head; //curr = A
        Node* copyHead = head->next;//copyhead = A->next = A'
        while(curr!=nullptr){
            Node* copy = curr->next; // get copied node next to og node
            curr->next = copy->next;//restroing og list
            //A->next = A'->next = B
            if(copy->next !=nullptr){
                copy->next = copy->next->next;//link copy to next xopy node
                //A'->next = A'->next->next = B'
            }
            curr = curr->next;
            //curr = B
        }
        return copyHead;
    }
};