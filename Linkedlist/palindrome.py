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
    def palindrome(self):
        temp = self.head
        stack1 = []
        while(temp):
            stack1.append(temp.data)
            temp = temp.next
        
        temp = self.head
        print('')
        while(temp):
            char = stack1.pop()
            print(char,end = ' ')
            if temp.data != char:
                return False
            temp = temp.next
        return True

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
    llist.append(4)
    llist.append(5)
    llist.append(6)

    llist.printList()

    if llist.palindrome():
        print('Palindrome')
    else:
        print('Sorry')