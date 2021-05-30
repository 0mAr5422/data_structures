import Foundation

public class TreeNode {
    
    var val : Int ;
    var left : TreeNode? = nil
    var right : TreeNode? = nil
    
    public init(val : Int ) {
        self.val = val;
    }
    
    
}


public class BinarySearchTree {
    public var root : TreeNode ;
    var values : [Int] = [];
    
    public init(root : TreeNode ) {
        self.root  = root;
        
    }
    deinit {
        
    }
    
    public func search(val:Int) -> Bool {
        func search(root : TreeNode? , val : Int) -> Bool {
            if root == nil {
                return true;
            }
            if self.root.val == val {
                return true;
                
            }
            if val > self.root.val {
                return search(root : root!.right , val : val)
                
            }
            else {
                return search(root: root!.left, val: val)
                
            }
        }
        return search(root: self.root, val: val)
         
    }
    
    
        
   public func insert(root : TreeNode? , newNode : TreeNode?) {
        if root == nil || newNode == nil {
            return ;
            
        }
        if newNode!.val > root!.val {
            if root!.right == nil {
                root!.right = newNode
                return;
                
            }
            else {
                insert(root: root?.right , newNode: newNode)
            }
        }
        else {
            if root!.left == nil {
                root!.left = newNode
                return
            }
            else {
                insert(root: root?.left, newNode: newNode)
            }
        }
    }
        
        
        
    
    
    public func delete(val : Int) -> TreeNode? {
        
        if self.root.val == val {
            if (self.root.right != nil) {
                let temp = self.root.left
                self.root = self.root.right!
                insert(root: self.root, newNode: temp)
                return self.root
                
            }
            if (self.root.left != nil ){
                let temp = self.root.right
                self.root = self.root.left!;
                insert(root: self.root, newNode: temp)
                return self.root
            }
            
            else {
                return nil
            }
        }
        
        func dell(root : TreeNode? , val : Int) {
            if root == nil {
                return;
            }
            if val > root!.val {
                if root!.right != nil{
                    if val == root?.right?.val {
                        if root?.right?.right != nil {
                            let temp = root?.right?.left;
                            root?.right = root?.right?.right
                            insert(root: root?.right, newNode: temp)
                            return
                        }
                        if root!.right?.left != nil {
                            let temp = root!.right!.right;
                            root?.right = root?.right?.left
                            insert(root: root?.right, newNode: temp)
                            return
                        }
                        else {
                            root?.right = nil
                        }
                    }
                    else {
                        dell(root: root?.right, val: val)
                    }
                }
            }
            else {
                if root?.left != nil {
                    if root?.left?.val == val {
                        if root?.left?.left != nil {
                            let temp = root?.left?.right
                            root?.left = root?.left?.left
                            insert(root: root?.left, newNode: temp)
                            return
                        }
                        if root!.left!.right != nil {
                            let temp = root?.left?.left
                            root?.left = root?.left?.right
                            insert(root: root?.left, newNode: temp)
                            return
                        }
                        else {
                            root?.left = nil
                        }
                    }
                    else {
                        dell(root: root?.left, val: val)
                    }
                }
            }
            
            
            
        }
        dell(root: self.root, val: val)
        
        return self.root
        
    }
    
    
    public func printBST() {
        
        self.values = [];
        func dfs(root : TreeNode?) {
            if root == nil {
                return ;
            }
            dfs(root: root?.left)
            self.values.append(root!.val)
            dfs(root: root?.right)
        
        }
        dfs(root: self.root)
        print(self.values)
        print("-----------------------------")
    }
    
}
