class StackNode:
       def __init__(self,data):
              self.data = data
              self.next = None

class Stack:
       def __init__(self):
              self.head = None
       def push(self,data):
              newNode = StackNode(data)
              newNode.next = self.head
              self.head = newNode
              print("{0} is pushed".format(data))
       def isEmpty(self):
              return True if self.head is None else False
       def pop(self):
              if(self.isEmpty()):
                     return "empty"
              temp = self.head
              self.head = self.head.next
              return temp.data
       def peek(self):
              if (self.isEmpty()):
                     return "empty"
              temp = self.head
              return temp.data
              
if __name__ == "__main__":
       stack = Stack()
       stack.push(2)
       stack.push(3)
       print(stack.peek())
       print(stack.pop())
       print(stack.peek())
       print(stack.pop())
       print(stack.peek())
       
              
