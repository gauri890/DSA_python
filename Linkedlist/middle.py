class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class Linkedlist:
    def __init__(self):
        print('start')
        self.head = None
    
    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while(temp.next):
            temp = temp.next
        
        temp.next = new_node
    
    def length(self):
        len = 0
        temp = self.head
        while(temp):
            len += 1
            temp = temp.next
        
        return len
    
    def middle(self,len):
        slow = self.head
        fast = self.head

        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next 
        
        if len % 2 == 1:
            print(slow.data)
        else:
            print(slow.next.data)



    def printList(self):
        temp = self.head

        while(temp):
            print(temp.data , end = " ")
            temp = temp.next

if __name__ == '__main__':

    llist = Linkedlist()

    llist.append(6)
    llist.append(5)
    llist.append(4)
    llist.append(3)
    llist.append(2)
    #llist.append(1)

    llist.printList()

    len = llist.length()
    print('')
    print(len,end ='\n')
    llist.middle(len)

