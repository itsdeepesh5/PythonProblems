class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        current_node= head
        prev=None
        next_node=None
        #1->2->3->4->5        
        while current_node is not None:
            #print(current_node.val, current_node.next.val)
            next_node= current_node.next # 2, 3  4 5, None
            if prev is None:
                current_node.next = None  #1.next= None
            else:
                current_node.next= prev #1 ,2, 3, 4
            
            prev= current_node   #1 2 3, 4
            current_node= next_node #2 3 4, 5
           
        head= current_node
        
        return prev

    def reverseList(self, head: 'ListNode') -> 'ListNode':
        
        if head is None:
            return head
        
        if head.next is None:
            return head
        
        rev= self.reverseList(head.next)
        next_node= head.next
        next_node.next= head
        head.next= None
        
        return rev
