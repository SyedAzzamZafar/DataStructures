def insertNodeAtPosition(head, data, position):
    newnode = SinglyLinkedListNode(data)
    i=0
    cur=head
    while i!=position-1:
        cur=cur.next
        i+=1
    newnode.next=cur.next
    cur.next=newnode
    return head
