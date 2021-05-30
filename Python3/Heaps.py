import sys ;
import collections
import  CompleteBinaryTree

class Heap :
    def __init__(self , vals) :
        self.vals = vals
        for i in reversed(range( 0 , len(self.vals ) // 2)) :

            self.heapify(i)

    def pop(self) :
        item = self.vals[0] ;
        self.delete(self.vals[0]);
        return item

    def peek(self) :
        return self.vals[0]

    def heapify(self , i) :
        largest = i ;
        left = (2*i )+ 1
        right = (2 * i) + 2;

        if left < len(self.vals) and self.vals[left] > self.vals[largest] :
            largest = left;
        if right < len(self.vals) and self.vals[right] > self.vals[largest] :
            largest = right ;
        
        if largest != i :

            self.vals[i] , self.vals[largest] = self.vals[largest] , self.vals[i]
            self.heapify(largest) 

    def insert(self, val) :
        if not self.vals :

            self.vals.append(val)
        else :
            self.vals.append(val);
            for i in reversed(range(0 , len(self.vals) // 2)):
                self.heapify(i)

    def delete(self, num) :
        size = len(self.vals)
        i = 0
        for i in range(0, size):
            if num == self.vals[i]:
                break
        self.vals[i], self.vals[size-1] = self.vals[size-1], self.vals[i]
        self.vals.pop()
        for i in reversed(range(0 , len(self.vals) // 2)):
            self.heapify(i)


nums = [3 , 9 , 2, 1 ,4 , 5]
heap = Heap(nums)

while heap.vals :
    print(heap.pop())

