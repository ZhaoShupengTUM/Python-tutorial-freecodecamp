#include<bits/stdc++.h>
using namespace std;
const int N=10010;
struct ListNode
{
    int  m_nKey;
    ListNode* m_pNext;
    ListNode(int x) : m_nKey(x), m_pNext(nullptr){}//初始化
};
int main()
{
    int n,k;
    while(cin>>n)
    {
        ListNode* head = new ListNode(-1);
        ListNode* node = head;
        while(n--)
        { 
            int x;
            cin>>x;
            ListNode* h = new ListNode(x);
            head->m_pNext = h;
            head=head->m_pNext;
        }
        cin>>k;
        if(k==0) 
        {
            cout << 0 << endl;
            continue;
        }
        ListNode *fast=node->m_pNext,*slow=node->m_pNext;
        while(fast && k)
        {
            fast=fast->m_pNext;
            k--;
        } 
        if(k>0) 
        {
            cout<<-1;
            continue;
        }
        while(fast)
        {
              slow=slow->m_pNext;
              fast=fast->m_pNext;
        }     
            
        cout<<slow->m_nKey<<endl;
        
    }
    return 0;
}