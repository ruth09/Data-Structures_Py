class Node:
       def __init__ (self,data):
              self.data = data
              self.next = None

class CircularLinkedList:
       def __init__(self):
              self.head = None

       def push(self,newNode):

              #creating the node 
              node = Node(newNode)
              temp = self.head

              #setting the next with the head 
              node.next = self.head

              #if the node is not empty push the node in the beggininig
              if self.head is not None :
                     #iterate the loop until the head node when the node.next is sel.head stop iterating .
                     while temp.next != self.head:
                            temp = temp.next
                     temp.next = node
              else:
                     node.next = node

              #assign the head to the begining
              self.head = node

       def printCircular(self):
              temp = self.head
              if self.head is not None:
                   while(True):
                       print (temp.data)
                       temp = temp.next
                       if (temp == self.head):
                           break
              
if __name__ == "__main__":
       cir = CircularLinkedList()
       cir.push(3)
       cir.push(2)
       cir.push(1)
       cir.printCircular()
       
