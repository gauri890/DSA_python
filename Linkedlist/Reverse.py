class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node

    #Iterative way Time Complexity: O(n) Auxiliary Space: O(1)
    def reverse(self):
        prev = None
        curr = self.head
        while (curr is not None):
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
        self.head = prev

    #Recursive way
    def reverseUtil(self,curr,prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next1 = curr.next 
        curr.next = prev
        self.reverseUtil(next1,curr)

    def Rreverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)
        pass
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
    llist.append(1)

    llist.printList()
    llist.reverse()
    print('')
    llist.printList()
    print('\n','Recursive way')
    llist.Rreverse()
    llist.printList()