from sys import maxsize

class Stack:
    def __init__(self, objName):
        self.objName = objName
        print("Name of Stack :",self.objName)
    def createStack(self):
        self.stack = []
        print(self.stack)
        return self
    def isEmpty(self):
        l = len(self.stack)
        print("len : ",l)
        return  l == 0
    def push(self,item):
        self.stack.append(item)
        print("pushed to stack " , item)
        return self.stack
    def Pop(self):
        if (Stack.isEmpty(self)):
            data = str(-maxsize -1)
            print("Empty", data)
            return data #return minus infinite
        #print(" popped from stack", self.stack.pop())
        return True
    def printStack(self):
        for i in self.stack :
            print(i)

stackObj = Stack("deviceStack")
stackObj.createStack()
stackObj.push("device1")
stackObj.push("device2")
stackObj.push("device3")
stackObj.printStack()
stackObj.Pop()
stackObj.printStack()
