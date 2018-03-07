
def create():
       stack = []
       return stack
def isEmpty(stack):
       return len(stack)==0
def push(stack,value):
       stack.append(value)
       return stack
def pop(stack):
       if(isEmpty(stack)):
              return "Empty"
       stack.pop()
       

if __name__ == "__main__":
       stack = create()
     
       push(stack,1)
       push(stack,2)
       print(stack)
       pop(stack)
       print(stack)
              
