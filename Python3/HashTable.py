import sys
import math

class HashTable:
    def __init__(self, size) :
        self.size = size ;
        self.vals = [None for i in range(self.size)];

    def hash(self,key) :
        A = (math.sqrt(5) - 1 ) / 2 

        return math.floor(self.size * ((key * A) % 1));
    
    def add(self, key , val):
        hashedKey = self.hash(key)
        self.vals[hashedKey] = val;
        return True
    
    def delete(self, key) :
        hashedKey = self.hash(key)
        self.vals[hashedKey] = None;
    
    def get(self,key) :
        hashedKey = self.hash(key)
        if self.vals[hashedKey] == None:
            return False;
        else :
            return self.vals[hashedKey];
    

table = HashTable(10);

table.add(123, "apple")
table.add(432, "mango")
table.add(213, "banana")
table.add(654, "guava")

print(table.vals)

table.delete(123)

print(table.vals)