import Foundation

public class Queue {
    
    
    var maxSize : Int;
    var size : Int = 0 ;
    var front = 0 ;
    var rear : Int!
    var vals : [Any?] = [];

    public init(maxSize : Int) {
        self.maxSize = maxSize;
        self.rear = self.maxSize - 1
        self.vals = (0...self.maxSize).map{_ in nil}
        

    }
    
    
    public func isEmpty() -> Bool {
        return self.size == 0
    }
    public func isFull() -> Bool {
        return self.size == self.maxSize;
    }
    
    public func enqueue(val : Int) {
        self.rear = (self.rear + 1 ) % self.maxSize
        self.vals[self.rear] = val ;
        self.size += 1;
        
    }
    public func deque() -> Int {
        let value = self.vals[self.front]
        self.vals[self.front] = nil
        self.front = (self.front + 1) % self.maxSize
        self.size -= 1;
        return value as! Int
    }
    
    
    public func printQueue() {
        print(self.vals , self.size)
    }
}
