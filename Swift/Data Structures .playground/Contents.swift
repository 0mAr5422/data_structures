import Foundation


// ----------------------------------Linked List ----------------------------//
//var linkedList = LinkedList(head : Node(val : 5))
//
//linkedList.addToHead(val : 12)
//linkedList.addToHead(val : 24)
//linkedList.addToEnd(val : 25)
//linkedList.addToEnd(val : 36)
//linkedList.printList()
//


// ----------------------------------Stacks----------------------------//

//
//var stack = Stack();
//stack.push(val: 10);
//stack.push(val: 12)
//stack.push(val: 15)
//stack.pop()
//stack.push(val : 13)
//stack.push(val : 9)
//stack.pop()
//stack.printStack()

// ----------------------------------Queues----------------------------//


//
//var queue = Queue(maxSize : 10) ;
//queue.enqueue(val: 12);
//queue.enqueue(val: 11)
//queue.deque()
//queue.enqueue(val: 12)
//queue.deque()
//queue.printQueue()
//



// ----------------------------------Binary Search Trees----------------------------//

//
//
//var bst = BinarySearchTree(root: TreeNode(val: 5))
//bst.insert(root: bst.root, newNode: TreeNode(val: 12))
//bst.insert(root: bst.root, newNode: TreeNode(val: 6))
//bst.insert(root: bst.root, newNode: TreeNode(val: 3))
//bst.insert(root: bst.root, newNode: TreeNode(val: 7))
//bst.insert(root: bst.root, newNode: TreeNode(val: 2))
//bst.insert(root: bst.root, newNode: TreeNode(val: 13))
//bst.insert(root: bst.root, newNode: TreeNode(val: 15))
//bst.insert(root: bst.root, newNode: TreeNode(val: 14))
//
//bst.printBST()
//
//bst.delete(val : 5)
//
//bst.printBST()
//
//
//
// ----------------------------------Self-Balancing (AVL) Binary Search Trees----------------------------//
//
//
//var avl = AVLTree(root: AVLNode(val: 33))
//var nums = [13, 52, 9, 21, 61, 8, 11]
//
//for i in nums {
//    avl.insert(newNode: AVLNode(val: i))
//
//
//}
//
//
//avl.insert(newNode: AVLNode(val: 10))
//avl.insert(newNode: AVLNode(val: 41))
//avl.insert(newNode: AVLNode(val: 15))
//avl.insert(newNode: AVLNode(val: 22))
//avl.insert(newNode: AVLNode(val: 43))
//avl.insert(newNode: AVLNode(val: 12))
//avl.insert(newNode: AVLNode(val: 60))
//
//
//
//avl.delete(val:15)
//avl.delete(val:43)
//avl.delete(val:8)
//
//avl.printBST()

// ----------------------------------Heap----------------------------//

var nums = [3 , 9 , 2, 1 ,4 , 5]
var heap = Heap(vals: nums)



while heap.isEmpty() != true {
    print(heap.pop())
}
   

