"""
225. Implement Stack using Queues
Easy

348

434

Favorite

Share
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

"""
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queues = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queues.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queues.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queues[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queues == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
"""
Success
Details 
Runtime: 32 ms, faster than 86.02% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 13.2 MB, less than 52.57% of Python3 online submissions for Implement Stack using Queues.

"""

from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queues = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queues.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        return self.queues.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
  
        return self.queues[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queues) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
"""
Success
Details 
Runtime: 32 ms, faster than 86.02% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 13.3 MB, less than 20.05% of Python3 online submissions for Implement Stack using Queues.
"""
