//{ Driver Code Starts
//

#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node(int val)
    {
        data=val;
        next=NULL;
    }
};

Node* inputList(int size)
{
    Node *head, *tail;
    int val;
    
    cin>>val;
    head = tail = new Node(val);
    
    while(--size)
    {
        cin>>val;
        tail->next = new Node(val);
        tail = tail->next;
    }
    
    return head;
}

void printList(Node* n)
{
    if(n)
    while(n)
    {
        cout<< n->data << " ";
        n = n->next;
    }
    else cout<< " ";
}


// } Driver Code Ends
/* The structure of the Linked list Node is as follows:

struct Node
{
    int data;
    Node *next;
    Node(int val)
    {
        data=val;
        next=NULL;
    }
};

*/


class Solution
{
    public:
    Node* findIntersection(Node* t1, Node* t2)
    {
       Node* result = nullptr;
        Node* curr = nullptr;

        std::unordered_map<int, int> set;
        while (t1 != nullptr) {
            set[t1->data] = set[t1->data] + 1;
            t1 = t1->next;
        }

        while (t2 != nullptr) {
            if (set.find(t2->data) != set.end() && set[t2->data] > 0) {
                set[t2->data] = set[t2->data] - 1;
                if (result == nullptr) {
                    result = new Node(t2->data);
                    curr = result;
                } else {
                    curr->next = new Node(t2->data);
                    curr = curr->next;
                }
            }
            t2 = t2->next;
        }

        return result;
    }
};



//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	    int n,m;
	    cin>> n >> m;
	    
	    Node* head1 = inputList(n);
	    Node* head2 = inputList(m);
	    
	    Solution ob;
	    Node* result = ob.findIntersection(head1, head2);
	    
	    printList(result);
	    cout<< endl;
	}
	return 0;
}

// } Driver Code Ends