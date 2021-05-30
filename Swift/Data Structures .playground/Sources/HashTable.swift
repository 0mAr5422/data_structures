import Foundation


public class HashTable {
    
    var size : Int;
    var vals : [Any?]!
    
    public init(size : Int) {
        self.size = size ;
        self.vals = [];
        for i in 0...self.size{
            self.vals.append(nil)
        }
    }
    
    private func hash(key : Int) -> Double {
        let A = (sqrt(5) - 1) / 2 ;
        let hashedKey = Double(self.size) * ((Double(key) * A).truncatingRemainder(dividingBy: Double(1)))
        return floor(hashedKey)
    }
    
    public func add(key : Int , val : Any)  {
        let hashedKey = Int(self.hash(key: key))
        self.vals[hashedKey] = val;
        
    }
    
    
    public func delete(key : Int) {
        let hashedKey = Int(self.hash(key: key))
        self.vals[hashedKey] = nil
        
    }
    
    public func get(key: Int) -> Any {
        let hashedKey = Int(self.hash(key: key))
        if self.vals[hashedKey] == nil {
            return -1
        }
        return self.vals[hashedKey]!
    }
    
    public func printt() {
        print(self.vals)
    }
    
}
