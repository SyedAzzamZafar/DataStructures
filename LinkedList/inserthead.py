def insertNodeAtHead(llist, data):
    # Write your code here
    newnode=SinglyLinkedListNode(data)
    if llist is None:
        llist=newnode
        return llist
    else:
        ghead=llist
        newnode.next=ghead
        nhead=newnode
        return nhead
