# CREATING A LINKED LIST 

class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def __str__(self):
		return str(self.data)

	def next_item(self):
		print("current node")
		print("data of next node: " + str(self.next_node))



# EXAMPLE NODES

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# SETTING POINTERS TO THE FOLLOWING NODE
# **** NOTE THAT THE LAST NODE (node3) DOES NOT HAVE A POINTER MEANING IT IS THE END OF THE LIST

node1.next_node = node2
node2.next_node = node3

# HOW TO SEE THE LIST FORWARD

def print_list(node):
	while node:
		print(node)
		node = node.next_node

#HOW TO SEE THE LIST BACKWARDS
def print_backward(list):
    if list == None: 
    	return
    head = list
    tail = list.next
    print_backward(tail)
    print (head)


# EXAMPLE
print_list(node1)
node1.next_item()

