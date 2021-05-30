class Queue :
    def __init__(self,size) :
        self.maxSize = size ;
        self.front = 0 ;
        self.rear = self.maxSize - 1
        self.vals = [None for i in range(self.maxSize)];
        self.size = 0;
    def isEmpty(self) :
        return self.size == 0 ;
    
    def isFull(self) :
        return self.size == self.maxSize;
    
    def enqueue(self, val) :
        
        self.rear = (self.rear + 1) % self.maxSize
        self.vals[self.rear] = val ;
        self.size += 1;

    def deque(self) :
        value = self.vals[self.front] 
        self.vals[self.front] = None
        self.front = (self.front+1) % self.maxSize
        self.size -= 1
        return value 
    

    def printQueue(self) :
        print(self.vals,self.size)


queue = Queue(10) ;
queue.enqueue(12);
queue.enqueue(11)
queue.deque()
queue.enqueue(12)
queue.deque()
queue.printQueue()