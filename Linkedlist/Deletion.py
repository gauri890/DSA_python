class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,new_data):
        new_node = Node(new_data)
        #new_node.next = None

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while(temp.next):
            temp = temp.next 
        
        temp.next = new_node

    def delAtbeg(self):
        self.head = self.head.next 

    def delAtend(self):
        temp = self.head
        while(temp.next.next):
            temp = temp.next 

        temp.next = None
    
    def delAt(self,find):
        temp = self.head

        while(temp.next):
            if find == temp.next.data:
                break
            else:
                temp = temp.next
            
        temp.next = temp.next.next

    def printList(self):
        temp = self.head

        while(temp):
            print(temp.data,end = " ")
            temp = temp.next 


if __name__ == "__main__":

    llist = linkedlist()

    llist.append(6)
    llist.append(5)
    llist.append(4)
    llist.append(3)
    llist.append(2)
    llist.append(10)

    llist.printList()
    
    llist.delAtbeg()
    llist.delAtend()

    print("")
    llist.printList()
    llist.delAt(4)

    print("")
    llist.printList()

   