import Foundation

public class Stack {
    var vals : [Int] = [];
    
    var size : Int = 0
    
    public init(){
        self.vals = [];
    }
    
    public func push(val : Int) {
        self.vals.append(val)
        
    }
    public func pop() -> Int {
        return self.vals.removeLast()
    }
    public func isEmpty() -> Bool {
        return self.size == 0
    }
    public func peek() -> Int {
        return self.vals[-1]
    }
    
    public func printStack() {
        print(self.vals)
    }
}
