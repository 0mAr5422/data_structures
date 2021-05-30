import Foundation

public class Node {
    var val : Int ;
    var next : Node? = nil ;
    var prev : Node? = nil ;

    public init(val : Int) {
        self.val = val;
        
    }
}

public class LinkedList {
    var head : Node?;
    var tail : Node?;
    public init(head : Node) {
        self.head = head;
        self.tail = head;
        
    }
    
    public func printList() {
        var l : [[Any]] = [];
        var temp = self.head;
        while temp != nil {
            var inner : [Any] = [];
            if let prev = temp!.prev?.val {
                inner.append(prev)
            }else {inner.append("None")}
            inner.append(temp!.val)
            if let next = temp!.next?.val {
                inner.append(next)
            }else {inner.append("None")}
            temp = temp!.next
            l.append(inner)
        }
        
        print(l)
    }
    public func addToHead(val : Int) {
        var newNode : Node = Node(val: val)
        self.head!.prev = newNode
        newNode.next = self.head;
        self.head = newNode
    }
    public func addToEnd(val : Int) {
        var newNode : Node = Node(val: val)
        self.tail!.next = newNode;
        newNode.prev = self.tail
        self.tail = newNode
    }
    
}
