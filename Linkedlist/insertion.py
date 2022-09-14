class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self,new_data,find):

        new_node = Node(new_data)

        temp = self.head
        while(temp.next):
            if find == temp.data:
                break
            else:
                temp = temp.next
         
        
        new_node.next = temp.next
        temp.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node

    def printList(self):
        temp = self.head

        while(temp):
            print(temp.data , end = " ")
            temp = temp.next


if __name__=='__main__':
    llist = Linkedlist()

    llist.append(6)
    llist.push(24)
    llist.push(12)
    llist.append(10)
    llist.insertAfter(6,10)

    print("Created linked list is: ")
    llist.printList()

        

