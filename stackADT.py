# Complete implementation of a stack ADT
class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
        
    def push(self, item):
        self.items.insert(0, item) # Top is at the beginning. O(n) time
        # self.items.append(item) # Top is at the end of the list. O(1) time

    def pop(self):
        return self.items.pop(0) # Top is at the beginning. O(n) time
        # return self.items.pop() # Top is at the end of the list. O(1) time

    def peek(self):
        return self.items[0] # Top is at the beginning.
        # return self.items[len(self.items)-1] # Top is at the end of the list.
    def size(self):
        return len(self.items)
    
if __name__ == "__main__":  
    s = Stack()
    s.push('hello')
    s.push('true')
    print(s.pop())
