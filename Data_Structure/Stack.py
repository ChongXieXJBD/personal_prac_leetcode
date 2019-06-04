# a stack is a kind of data structure which make data allow "First-in, Last-out" law


class Stack(object):
    def __init__(self):
        
        self._arr=[];
        #数组存储栈
        self._top=0;
        #栈顶指针

    def put(self,data):
        
        self._arr.insert(self._top,data);

        self._top+=1;

    def pop(self):
        if self.isEmpty():
            
            raise ValueError("The stack is empty");

        self._top-=1;

        return self._arr.pop(self._top);

    def isEmpty(self):

        if self._top == 0:

            return True;

        else:

            return False;

    def __str__(self):
        #打印方法

        return "Stack(%s)"%self._arr;
            

        

    
        
