import sys 
import collections
class Graph :

    def __init__(self) :
        self.d = collections.defaultdict(list);

    def add(self , first , second) : 
        self.d[first].append(second);
       

    def remove(self , first , second) :
        self.d[first].remove(second);
    
    def dfs(self , node , g) :
        visited = collections.defaultdict(bool) ;
        stack = [];
        def d(node) :
            nonlocal visited ;
            nonlocal stack;
            nonlocal g;
            visited[node] = True ;
            if g[node] == [] :
                stack.append(node);
                return True

            for i in g[node] :
                if visited[i] :
                    continue;
                d(i);
            stack.append(node)
            
            return False
        
        d(node);
        return stack;
    def dfs2(self, node , g , visited) :
        comp = [];
        def d2(node ) :
            nonlocal g ;
            nonlocal visited;
            nonlocal comp;

            
            visited[node] = True;
            comp.append(node)
            for i in g[node] :
                if not visited[i] :
                    d2(i );
            return comp

        return d2(node)
        


    def rev(self) :
        newD = collections.defaultdict(list);
        for i in self.d :
            for j in self.d[i] :
                newD[j].append(i);
        return newD

    def findStronglyConnectedComponents(self ) :
        stack = self.dfs(0 , self.d) ;
        reversedStack = self.rev();
        visited = collections.defaultdict(bool)
        components = [];
        while stack :
            node = stack.pop();
            if visited[node]:
                
                continue;
            components.append(self.dfs2(node , reversedStack , visited));

        print(components)


graph = Graph();
graph.add(0 , 1);
graph.add(1,2);
graph.add(2,3);
graph.add(3,0);
        
graph.add(2 , 4);
graph.add(4,5);
graph.add(5,6);
graph.add(6,7);
        
graph.add(6 , 4);

graph.findStronglyConnectedComponents()
    
