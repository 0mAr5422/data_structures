class Node  :
    def __init__(self,val , right = None , left = None , bf = 0) :
        self.val = val;
        self.right = right;
        self.left = left;
        self.bf = bf

    
class AVL:
    def __init__(self , root ) :
        self.root = root;
    
    def getHeight(self, root) :
        if not root :
            return 0 ;
        return max(self.getHeight(root.left) , self.getHeight(root.right)) + 1

    def rightRotate(self, root) :
        y = root.left;
        t = y.right;
        y.right = root;
        root.left = t;
        root.bf = self.getHeight(root.left) - self.getHeight(root.right);
        y.bf = self.getHeight(y.left) - self.getHeight(y.right);

        return y

    def leftRotate(self, root) :
        y = root.right;
        t = y.left;
        y.left=root;
        root.right = t;

        root.bf = self.getHeight(root.left) - self.getHeight(root.right);
        y.bf = self.getHeight(y.left) - self.getHeight(y.right);

        return y

    def successor(self, root) :
        if not root :
            return None ;
        if root.left :
            return self.successor(root.left);
        else :
            return root;


    def insert(self , newNode) :
        def ins(root , newNode) :
            if not root :
                return newNode
            if newNode.val >= root.val :
                root.right = ins(root.right , newNode);
            else :
                root.left = ins(root.left , newNode);
            
            root.bf = self.getHeight(root.left) - self.getHeight(root.right);

            if root.bf > 1 :
                if newNode.val < root.left.val :
                    return self.rightRotate(root);
                else :
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root);
                
            if root.bf < -1 :
                if newNode.val > root.right.val :
                    return self.leftRotate(root);
                else :
                    root.right = self.rightRotate(root.right);
                    return self.leftRotate(root);



            return root;
        self.root = ins(self.root , newNode)


    def delete(self , val) :
        def dell(root , val) :
            if not root :
                return None ;
            if root.val == val :
                if not root.left and not root.right :
                    root = None ;
                elif root.left and root.right :
                    s = self.successor(root.right);
                    s.val ,root.val = root.val , s.val ;
                    root.right = dell(root.right , s.val);
                    
                elif root.left :
                    root = root.left;
                else :
                    root = root.right;
            elif val >= root.val :
                root.right = dell(root.right , val);
            else :
                root.left = dell(root.left , val);
            if not root:
                return root
            root.bf = self.getHeight(root.left) - self.getHeight(root.right)

            if root.bf > 1 :
                if root.left and root.left.bf >= 0 :
                    return self.rightRotate(root)
                else :
                    root.left = self.leftRotate(root.left)
                    return self.rightRotate(root)
            if root.bf < -1 :
                if root.right and root.right.bf >= 0 :
                    return self.leftRotate(root);
                else :
                    root.right = self.rightRotate(root.right);
                    return self.leftRotate(root)
            return root;
        self.root = dell(self.root , val)
    

    def printAVL(self) :
        values = [];
        def dfs(root) :
            nonlocal values;
            if not root:
                return;
            dfs(root.left)
            values.append((root.val , root.balanceFactor))
            dfs(root.right)
        dfs(self.root)
        print(values)

    def print2(self) :
        def bfs(root) :
            q = [[0 , root]]
            answer = [];
            while q :
                temp = q.pop(0);
                level = temp[0]
                tree = temp[1]
            
                if not answer :
                    answer.append([level , tree.val])
                else :
                    if level > answer[-1][0] :
                        answer.append([level,tree.val])
                    else :
                        answer[-1].append(tree.val);
                if tree.left:
                    q.append([level+1 , tree.left]);
                if tree.right :
                    q.append([level+1 , tree.right]);
            for i in range(len(answer)) :
                answer[i].pop(0);
            print(answer);
        bfs(self.root)


nums = [13, 52, 9, 21, 61, 8, 11]
avl = AVL(Node(33))
for i in nums :
    avl.insert(Node(i))

avl.insert(Node(10))
avl.insert(Node(41))
avl.insert(Node(15))
avl.insert(Node(22))
avl.insert(Node(43))
avl.insert(Node(12))
avl.insert(Node(60))





avl.delete(15)
avl.delete(43)
avl.delete(8)

avl.print2()




