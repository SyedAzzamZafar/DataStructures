class node:
	"""class to generate node object"""
	def __init__(self, value=None ):
		#super(Node, self).__init__()
		self.value = value
		self.next = None
		
class sll:
	def __init__(self,head=None):
		"""generate head pointer"""
		self.head = head


	def append(self,data):
		newnode = node(data)
		#print('head')
		if self.head is None:
			self.head=newnode	
			#print('head')
			#print(f'{self.head.value},{self.head.next}\n')	
		else:
			cur = self.head
			while cur.next is not None:
				cur=cur.next
			cur.next=newnode
		cur=newnode
		#print(f'{cur.value},{cur.next}\n')	
	def size(self):
		cur = self.head
		size=1
		while cur.next is not None:
			size+=1
			cur=cur.next

		return(size)
	
	#def delete_list(self):
		if self.head is None:
			return
		else:
			cur=self.head
			self.head = self.head.next
			del cur		
	
	#def head_list(self):
		return(self.head.value)			
	
	def reversePrint(self):
		cur=self.head
		prev=None
		while cur is not None:
			x=cur.next
			cur.next=prev
			prev=cur
			cur=x
		self.head=prev
		return self.head

	def mergelists(self,list):
		



        
	def __str__(self):
		lstr1=''
		if self.head==None:
			return 
		else:
			cur=self.head
			
		
			while cur.next is not None:
				lstr1+=f'{cur.value}->'
				cur=cur.next
			lstr1+=f'{cur.value}->None'
			return(lstr1)
			
			
if __name__ == '__main__':
	mylist = sll()
	
	for value in range(10):
		mylist.append(value)
	#print(mylist.head_list())
	#mylist.delete_list()
	print(mylist)
	mylist.reversePrint()
	print(mylist)
	size=mylist.size()
	print(size)