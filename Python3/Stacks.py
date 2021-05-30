class Stack :
    def __init__(self) :
        self._vals = [] ;
        self._size = 0 ;
    
    def push(self, val) :
        self._vals.append(val)
    def pop(self) :
        return self._vals.pop();
    
    def isEmpty(self) :
        return self_size == 0 ;


    def peek(self) :
        return self._vals[-1] ;
    def printStack(self):
        print(self._vals)
stack = Stack();
stack.push(10);
stack.push(12)
stack.push(15)
stack.pop()
stack.push(13)
stack.push(9)
stack.pop()
stack.printStack()
