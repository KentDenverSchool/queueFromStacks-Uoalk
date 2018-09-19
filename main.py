#Author: Grant Fitez
#Date:9/13/18
#Purpose: This lab is intended to practice the implementation of the queue data structure using stacks
class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer
    def getData(self):#returns data object
        return(self.data)
    def changeData(self, newData):#changes data to newData
        self.data = newData
    def addPoint(self, newNode):#adds newNode to the end of the pointer array
        self.pointer.append(newNode)
    def addPointAtIndex(self, newNode, index):#adds newNode to the end of the pointer array
        self.pointer[index] = newNode
    def rmPoint(self, index):#removes pointer at index in array
        if(index < len(self.pointer)):
            del self.pointer[index]
    def setPoint(self, index, node):#sets pointer at index in array
        self.pointer[index] = node
    def getNode(self, index):#returns pointer at index
        if(index < len(self.pointer)):
            return self.pointer[index]
    def pointerCount(self):
        return len(self.pointer)
    def __repr__(self):
        left = 'None'
        if self.pointer[0] != None:
            left = self.pointer[0].data
        right = 'None'
        if len(self.pointer) > 2 and self.pointer[1] != None:
            right = self.pointer[1].data
        return "{data:"+str(self.data)+", pointers:"+str(self.pointerCount())+", Left Pointer:"+str(left)+" Right Pointer:"+str(right)+"}";


class Stack:
    def __init__(self):
        self.firstNode=None;
    def pop(self):
        node=self.peak();
        if(self.getSecondToTop()==None):
            self.firstNode=None
        else:
            self.getSecondToTop().rmPoint(0)
        return node
    def push(self,data):
        if(self.firstNode==None):
            self.firstNode=Node(data, [])
        else:
            node=Node(data,[])
            self.getTop().addPoint(node)
    def peak(self):
        if(self.getTop()==None):
            return None
        return self.getTop().getData();
    def getTop(self):
        node=self.firstNode;
        if(node==None):
            return None
        while(node.pointerCount()>0):
            node=node.getNode(0)
        return node
    def getSecondToTop(self):
        before=None;
        node=self.firstNode;
        if(node==None):
            return None
        while(node.pointerCount()>0):
            before=node
            node=node.getNode(0)
        return before
    def isEmpty(self):
        if self.firstNode==None:
            return True
        return False
    def size(self):
        count =1;
        node=self.firstNode;
        if(node==None):
            return 0
        while(node.pointerCount()>0):
            node=node.getNode(0)
            count+=1
        return count
    def __repr__(self):
        return self.getTop().getData()


class QueueFromStacks:
    def __init__(self):
        self.inbox=Stack()
        self.outbox=Stack()
    def enqueue(self, e):
        self.inbox.push(e)
    def dequeue(self):
        el=self.peek()
        self.outbox.pop()
        return el
    def isEmpty(self):
        return self.inbox.isEmpty() and self.outbox.isEmpty()
    def size(self):
        return self.inbox.size() + self.outbox.size()
    def peek(self):
        if self.outbox.size()==0:
            transfer=self.inbox.pop()
            while transfer!=None:
                self.outbox.push(transfer)
                transfer=self.inbox.pop()
        return self.outbox.peak()


print("Create queue and add 'test'. Then peak and then deenqueue:")
s=QueueFromStacks()
print("is empty:"+str(s.isEmpty()))
s.enqueue("test")
print("is empty:"+str(s.isEmpty()))
print(s.peek())
print(s.dequeue())


print("\ndeenqueue and peak an empty stack:")
print(s.dequeue())
print(s.peek())

print("\nAdd three elements and then deenqueue all of them:")
s.enqueue("first")
s.enqueue("second")
s.enqueue("third")
print("size:"+str(s.size()))
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
print(s.dequeue())
