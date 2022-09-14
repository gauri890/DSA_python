class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init(self):
        self.head = None
    
    def push(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def detectloop(self):
        s1 = set()
        temp = self.head
        while(temp):

            if (temp in s):
                return True
            
            s1.add(temp)
            temp = temp.next 

        return False
    
    def loopcount(self):
        slow = self.head
        fast = self.head
        flag = 0

        while( slow and fast and fast.next.next and slow.next and fast.next):
            if slow == fast and flag != 0:
                count = 1
                slow = slow.next
                while(slow != fast):
                    slow = slow.next
                    count += 1
                    
                return count

            slow = slow.next
            fast = fast.next.next 
            flag = 1
        return 0


    
    def printlist(self):
        temp = self.head
        while(temp.next):
            print(temp.data, end = " ")
            temp = temp.next

llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.head.next.next.next.next.next = llist.head

if(llist.detectloop()):
    print("Loop Found")
else:
    print("No Loop")
