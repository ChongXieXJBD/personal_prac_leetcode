class Node:
    def __init__(self,val):
        
        self.__value = val;

        self.__next = None;

    def getData(self):
        return self.__value;

    def setData(self,new_val):
        self.__value = new_val;

    def setNext(self, nextNode):
        self.__next
        
