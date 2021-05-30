import sys ;

class Node :
    def __init__(self , val , left = None , right = None) :
        self.val = val;
        self.right = right;
        self.left = left;
    

class BinarySearchTree :
    def __init__(self, root) :
        self.root = root;
        self.values = []
    def search(self,root , target) :
        if not root :
            return False;
        if root.val == target :
            return True ;
        elif root.val < target :
            return self.search(root.right , target) ;
        else :
            return self.search(root.left , target);
        
    def insert(self , newNode) :
        def ins(root , newNode) :

            if not root or not newNode:
                return ;
            
            if newNode.val >= root.val :
                if root.right :
                    ins(root.right , newNode);
                else :
                    root.right = newNode
                    return ;
                
            else :
                if root.left :
                    ins(root.left , newNode) ;
                
                else :
                    root.left = newNode;
                    return ;
        ins(self.root , newNode)

    def delete(self, val) :
        if val == self.root.val :
            if self.root.right :
                temp = self.root.left;
                self.root = self.root.right;
                self.insert(temp);
                return;
            if self.root.left :
                temp = self.root.right;
                self.root = self.root.left;
                self.insert(temp);
                return
            else :
                self.root = None
                return
        def dell( root , val) :

            if not root :
                return ;
            if val > root.val :
                if root.right:
                    if root.right.val == val :
                        if root.right.right:
                            temp = root.right.left;
                            root.right = root.right.right;
                            self.insert(temp)
                            return
                        if root.right.left :
                            temp = root.right.right;
                            root.right = root.right.left;
                            self.insert(temp)
                            return ;
                        else :
                            root.right = None
                    else :
                        dell(root.right , val)
                else :
                    return ;
            else :
                if root.left :
                    if root.left.val == val :
                        if root.left.left :
                            temp = root.left.right ;
                            root.left = root.left.left;
                            self.insert(temp)
                            return ;
                        if root.left.right :
                            temp = root.left.left;
                            root.left = root.left.right;
                            self.insert(temp)
                            return 
                        else :
                            root.left = None

                    else :
                        dell(root.left , val)

                else :
                    return 

        dell(self.root , val)
        
    def printBST(self) :
        self.values = [];
        def dfs(root) :

            if not root :
                return ;
            dfs(root.left);
            self.values.append(root.val)
            dfs(root.right)
        dfs(self.root)
        print(self.values)
        print("-------------------------------------------")
            
    
bst = BinarySearchTree(Node(5))
bst.insert(Node(12))
bst.insert(Node(6))
bst.insert(Node(3))
bst.insert(Node(7))
bst.insert(Node(2))
bst.insert(Node(13))
bst.insert(Node(15))
bst.insert(Node(14))

bst.printBST()

bst.delete(2)

bst.printBST()






