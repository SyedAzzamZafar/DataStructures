def insertNodeAtTail(head, data):
    newnode= SinglyLinkedListNode(data)
    if head:
        cur=head
        while cur.next is not None:
            cur=cur.next
        cur.next=newnode
        cur=newnode
    else:
        head=newnode
    return head
        
    
    