def deleteNode(head, position):
    i=0
    cur=head
    if position==0:
        head=head.next
        return head
    else:
        #reaching positon with 2 pointers:previous & cur(tobedeleted)
        while i!=position-1:
            cur=cur.next
            i+=1
        previous=cur
        cur=previous.next
        #deletion
        previous.next=cur.next
    
        del cur
        return head
    
    