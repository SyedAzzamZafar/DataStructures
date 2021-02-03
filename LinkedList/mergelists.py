def mergelists(head1,head2):
    head = None
    cur = head
    

    cur1 = head1
    cur2 = head2
    while cur1 is not None and cur2 is not None:
        if cur1.data<cur2.data:
            newnode = node(cur1.data)
            if head is None:
                head = newnode
                cur = newnode
            else:
                cur.next = newnode
                cur = newnode
            cur1 = cur1.next
        elif cur1.data>cur2.data:
            newnode = node(cur2.data)
            if head is None:
                head = newnode
                cur = newnode
            else:
                cur.next = newnode
                cur = newnode
            cur2 = cur2.next
        else:
            newnode1 = node(cur1.data)
            newnode2 = node(cur2.data)
            if head is None:
                head  =  newnode1
                newnode1.next = newnode2
                cur = newnode2
            else:
                cur.next = newnode1
                cur = newnode1
                cur.next = newnode2
                cur = newnode2
            cur1 = cur1.next
            cur2 = cur2.next
    if cur1:
        while cur1 is not None:
            newnode = node(cur1.data)
            cur.next = newnode
            cur = newnode
            cur1 = cur1.next
    elif cur2:
        while cur2 is not None:
            newnode = node(cur2.data)
            cur.next = newnode
            cur = newnode
            cur2 = cur2.next 
    return head
        
