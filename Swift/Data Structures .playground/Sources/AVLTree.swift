import Foundation


public class AVLNode {
        
    var val : Int ;
    var left : AVLNode?
    var right : AVLNode?
    var bf : Int = 0;
    
    public init(val : Int ) {
        self.val = val;
    }
    
        
}


public class AVLTree {
    var root : AVLNode?;
    
    
    public init(root : AVLNode?) {
        self.root = root ;
    }
    
    
    func findSuccessor(root : inout AVLNode?) -> AVLNode? {
        if root == nil {
            return root;
        }
        if root?.left != nil {
            return findSuccessor(root: &(root!.left))
        }
        else {
            return root
        }
    }
    
    
    public func printBST() {
        var answer : [[Int]] = [];
        
        var q : [(Int , AVLNode?)] = [(0 , self.root)]
        while q.count > 0 {
            let temp = q.removeFirst()
            let level = temp.0
            let tree = temp.1
            if answer.count == 0 {
                answer.append([level , tree!.val])
            }
            else {
                if level > answer.last![0] {
                    answer.append([level , tree!.val])
                }
                else {
                    answer[answer.count-1].append(tree!.val)
                }
                
            }
            if tree!.left != nil {
                q.append((level+1 , tree!.left))
            }
            if tree!.right != nil {
                q.append((level + 1 , tree!.right))
            }
        }
        
        for i in 0..<answer.count {
            answer[i].removeFirst()
        }
        print(answer)
    }
    
    func getHeight(root : AVLNode?) -> Int {
        func height(root: AVLNode?) -> Int {
            if root == nil {
                return 0
            }
            return 1 + max(height(root: root!.left) , height(root: root!.right))
        }
        
        return height(root: root)
    }
    
    func leftRotate(root : inout AVLNode) -> AVLNode? {
        var y = root.right;
        var temp = y?.left;
        y?.left = root;
        root.right = temp
        root.bf = self.getHeight(root: root.left) - self.getHeight(root: root.right)
        y!.bf = self.getHeight(root: y?.left) - self.getHeight(root: y?.right)
        
        return y
    }
    
    
    func rightRotate(root : inout AVLNode) -> AVLNode? {
        var y = root.left;
        var temp = y?.right
        y?.right = root
        root.left = temp
        
        root.bf = self.getHeight(root: root.left) - self.getHeight(root: root.right)
        y!.bf = self.getHeight(root: y?.left) - self.getHeight(root: y?.right)
        return y
    }
    
    
    public func insert(newNode : AVLNode) {
        
        func ins(root :  inout AVLNode? , newNode : AVLNode) -> AVLNode?  {
            if root == nil {
                return newNode
            }
            if newNode.val > root!.val {
                root!.right = ins(root: &root!.right, newNode: newNode)
                
            }
            else {
                root!.left = ins(root: &root!.left, newNode: newNode)
            }
            root?.bf = self.getHeight(root: root?.left) - self.getHeight(root: root?.right)
            
            if root!.bf > 1 {
                if newNode.val < root!.left!.val {
                    return self.rightRotate(root: &root! )
                }
                else {
                    root!.left = self.leftRotate(root: &(root!.left)!)
                    return self.rightRotate(root: &root!)
                }
                
            }
            
            if root!.bf < -1 {
                if newNode.val > root!.right!.val {
                    return self.leftRotate(root: &root!)
                }
                else {
                    root?.right = self.rightRotate(root: &(root!.right)!)
                    return self.leftRotate(root: &root!)
                }
                
            }
            
            
            return root
            
        }
        
        self.root = ins(root: &self.root, newNode: newNode)!
        
        
        
        
    }
    
    public func delete(val : Int) {
        
        func dell(root : inout AVLNode? , val : Int) -> AVLNode?{
            
            if root == nil {
                return nil;
            }
            
            if root!.val == val {
                if root?.left == nil && root?.right == nil {
                    return nil
                }
                
                else if root?.right != nil && root?.left != nil {
                    var temp = self.findSuccessor(root: &(root!.right))
                    
                    var temp2 = root?.val
                    root?.val = temp!.val
                    temp!.val = temp2!
                    
                    root?.right = dell(root: &(root!.right), val: temp!.val)
                    return root
                }
                else {
                    if root?.right != nil {
                        root = root?.right
                        
                    }
                    else {
                        root = root?.left
                    }
                    return root
                }
                
                
            }
            else if val > root!.val {
                root?.right = dell(root: &(root!.right), val: val)
            }
            else {
                root?.left = dell(root: &root!.left, val: val)
            }
            
            root?.bf = self.getHeight(root: root?.left) - self.getHeight(root: root?.right)
            
            if root!.bf > 1 {
                if (root?.left!.bf)! >= 0 {
                    return self.rightRotate(root: &(root)!)
                }
                else {
                    root!.left = self.leftRotate(root: &(root!.left)!)
                    return self.rightRotate(root: &(root)!)
                }
            }
            if root!.bf < -1 {
                if (root?.right!.bf)! <= 0 {
                    return self.leftRotate(root: &(root)!)
                }
                else {
                    root!.right = self.rightRotate(root: &(root!.right)!)
                    return self.leftRotate(root: &(root)!)
                }
            }
            
            return root
        }
        
        self.root = dell(root: &self.root, val: val)!
        
    }
}
