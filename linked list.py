class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self,newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self,previousNode,newData):
        if previousNode is None:
            print("it is the last element")
            #return
        newNode = Node(newData)
        newNode.next = previousNode.next
        previousNode.next = newNode

    def append(self,newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = newNode

    def deleteNode(self,key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
        while temp is not None:
            if temp.data == key:
                break
            
            prev = temp
            #print(prev)
            temp = temp.next
            print(temp)
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def pop(self):
        temp = self.head
        if temp is None:
            print("list is empty")
        else:
            self.head = temp.next
            temp = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

        
if __name__ == "__main__":
    llist = LinkedList()
    """llist.push(2)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    #llist.printList()
    #llist.insertAfter(llist.head.next,8)
    #llist.append(9)
    
    #llist.printList()
    #llist.deleteNode(2)"""
    llist.push(32)
    llist.push(33)
    llist.printList()
    
    llist.pop()
    print("not")
    llist.printList()
