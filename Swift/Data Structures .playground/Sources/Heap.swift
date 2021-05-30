import Foundation

public class Heap{
    
    var vals : [Int]
    
    public init(vals : [Int] ) {
        self.vals = vals;
        for i in (0..<Int(self.vals.count / 2)).reversed() {
            self.heapify(i: i)
        }
        
    }
    public func pop() -> Int {
        let item = self.vals[0] ;
        self.delete(num : item)
        return item;
    }
    
    public func peek() -> Int {
        return self.vals[0]
    }
    func heapify(i : Int) {
                
        var largest = i;
        var left = (2 * i) + 1;
        var right = (2 * i) + 2;
        
        if left < self.vals.count && self.vals[left] > self.vals[largest] {
            largest = left;
        }
        if right < self.vals.count && self.vals[right] > self.vals[largest] {
            largest = right
        }
        
        if largest != i {
            var temp = self.vals[i]
            self.vals[i] = self.vals[largest]
            self.vals[largest] = temp
            self.heapify(i: largest)
        }
        
    }
    
    public func insert(num : Int) {
        if self.vals.count == 0  {
            self.vals.append(num)
        }
        else {
            self.vals.append(num);
            for i in (0..<Int(self.vals.count / 2)).reversed() {
                self.heapify(i: i)
            }
        }
    }
    
    func delete(num : Int) {
        var i = 0 ;
        while i < self.vals.count {
            if self.vals[i] == num {
                break
            }
        }
        var temp = self.vals[i]
        self.vals[i] = self.vals[self.vals.count-1]
        self.vals[self.vals.count-1] = temp
        self.vals.removeLast()
        
        for i in (0..<Int(self.vals.count / 2)).reversed() {
            self.heapify(i: i)
            
        }
        
        
    }
    public func isEmpty() -> Bool {
        return self.vals.count == 0
    }
}
