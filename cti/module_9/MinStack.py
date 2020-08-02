
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.


** repl.it unit test **

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 93, in test_case1
    self.assertEquals(minStack.getMin(), -2)
AssertionError: -3 != -2

Traceback (most recent call last):
  File "/home/runner/unit_tests.py", line 67, in test_allMins
    self.assertEquals(minStack.getMin(), 1)
AssertionError: 0 != 1


'''


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = list()
        self.min = float('inf')

        return

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if x < self.min:
            self.min = x

        # return

    def pop(self):
        """
        :rtype: None
        """
        popped = self.data.pop()
        if popped == self.min:
            self.min = min(self.data)
        return popped

    def top(self):
        """
        :rtype: int
        """
        peek = self.data[-1]

        return peek
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


