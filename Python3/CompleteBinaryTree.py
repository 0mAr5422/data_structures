import sys
import collections

class Node :
    def __init__(self, val , left = None , right = None) :
        self.val = val ;
        self.right = right;
        self.left = left;
    

class CompleteBinaryTree :
    def __init__(self, root) :
        self.root = root ;
    def isFull(self ,root) :
        if not root :
            return True ;
        return self.noden(root.left ) == self.noden(root.right)
        
    def isComplete(self , root) :
        if not root :
            return True;
        if root.left and root.right :
            return (self.isComplete(root.left) and self.isComplete(root.right)) ;
        if not root.left and not root.right :
            return True;
        return False
    
    def getHeight(self , root):
        if not root :
            return 0;
        return 1 + max(self.getHeight(root.left) , self.getHeight(root.right))

    def insert(self, newNode) :

        def dfs(root , newNode):
            if not root :
                return root ;
            if not root.left :
                root.left = newNode
                return root;
            if not root.right :
                root.right = newNode
                return root
            l = self.isComplete(root.left)
            r = self.isComplete(root.right) ;
            lh = self.isFull(root.left)
            rh = self.isFull(root.right)
            
            
            if l and r and lh and rh :
                if self.getHeight(root.left) > self.getHeight(root.right) :
                    root.right = dfs(root.right , newNode);
                else :
                    root.left = dfs(root.left , newNode);
                
                return root

            if not l :
                root.left = dfs(root.left , newNode);
                return root;
            elif l and r :
                if not lh  :
                    root.left = dfs(root.left , newNode);
                    return root ;
                if not rh :
                    root.right = dfs(root.right , newNode);
                    return root;
                root.left = dfs(root.left , newNode);
                return root;
            elif not r :
                root.right = dfs(root.right , newNode);
                return root;
            
            
            return root
            
        self.root = dfs(self.root , newNode)

    def print2(self) :
        def bfs(root) :
            q = [[0 , root]]
            answer = collections.defaultdict(list)
            while q :
                temp = q.pop(0);
                level = temp[0]
                tree = temp[1]
                if not tree :
                    answer[level].append(None)
                    continue
            
                answer[level].append(tree.val)
                
                q.append([level+1 , tree.left]);
                
                q.append([level+1 , tree.right]);
            
            return answer;
        answer = (bfs(self.root))
   
        print(answer)
        # l = [];
        # for i in answer :
        #     for j in answer[i] :
        #         if not j :
        #             continue
        #         l.append(j)
        # print(l)




# cpt = CompleteBinaryTree(Node(3))
# nums = [9 , 2 , 1, 4 , 5, 12, 24, 45 , 444 , 43, 96, 88, 59, 40, 38, 77, 16, 27, 60, 95, 35, 32, 23, 100]
# for i in nums :
#     cpt.insert(Node(i))

# cpt.print2()


