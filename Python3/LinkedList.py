class Node :
    def __init__(self,val , next = None , prev = None) :
        self.val = val ;
        self.next = next ;
        self.prev = prev;



class LinkedList :
    def __init__(self , node : Node) :
        self.head = node;
        self.tail = node;
        self.size = 0 ;
    def printList(self) :
        l = [];
        temp = self.head;
        while temp :
            l.append([temp.prev.val if temp.prev else None , temp.val , temp.next.val if temp.next else None])
            temp = temp.next;
        print(l)

    def addToEnd(self, val) :
        newNode = Node(val) ;
        temp = self.tail;
        temp.next = newNode;
        newNode.prev = temp;
        self.tail = newNode
        return ;

    def addToHead(self, val) :
        newNode = Node(val) ;
        newNode.next = self.head;
        self.head.prev = newNode;
        self.head = newNode;


linkedList = LinkedList(Node(5))

linkedList.addToHead(12)
linkedList.addToHead(24)
linkedList.addToEnd(25)
linkedList.addToEnd(36)



def merge(head , head2) :
    
    answer = Node(0);
    temp = answer
    
    while head and head2 :
        if head.val <= head2.val :
            temp.next = Node(head.val)
            head = head.next
            temp = temp.next;
        else :
            temp.next = Node(head2.val)
            head2 = head2.next;
            temp = temp.next;
    while head :
        temp.next = Node(head.val)
        temp = temp.next
        head = head.next;
    while head2 :
        temp.next = Node(head2.val)
        temp = temp.next;
        head2 = head2.next;
    
    return answer.next





head = (Node(10))
head2 = (Node(13))
head.next = Node(14)

head = merge(head , head2)

temp = head;
l = []
while temp :
    l.append(temp.val)
    temp = temp.next;

print(l)