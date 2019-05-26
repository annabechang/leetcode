"""
155. Min Stack

Easy

1741

180

Favorite

Share
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

"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        cur_min = self.getMin()
        if cur_min == None or x < cur_min:
            cur_min = x
        self.s.append((x,cur_min))
        
    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        if not self.s:
            return None
        return self.s[-1][0]

    def getMin(self) -> int:
        if not self.s:
            return None
        return self.s[-1][1]

    # let's say it's push (-2, 0, -3)
    #our stack will look like this:
    #[(-2,-2),(0,-2),(-3,-3)]
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
"""
Success
Details 
Runtime: 56 ms, faster than 94.40% of Python3 online submissions for Min Stack.
Memory Usage: 16.9 MB, less than 16.51% of Python3 online submissions for Min Stack.

"""

