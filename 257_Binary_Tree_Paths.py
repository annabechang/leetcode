"""
257. Binary Tree Paths
Easy
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# dfs + stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        stack = [(root,"")]
        res = []
        #res = result
        
        if not root:
            return []
        
        while stack:
            node, string = stack.pop()
            
            if not node.left and not node.right:
                res.append(string + str(node.val))

            if node.left:
                stack.append((node.left, string + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, string + str(node.val) + "->"))
        return res
"""
Success
Details 
Runtime: 40 ms, faster than 59.60% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.9 MB, less than 6.33% of Python3 online submissions for Binary Tree Paths.
"""
#dfs recursively
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        
        def help(root, curr):
            if root == None:
                return
            # if it's a leaf. update result list + current value
            # change it to string because root value is an intiter 
            if root.left == None and root.right == None:
                res.append(curr + str(root.val))
            else:
                help(root.left, curr + str(root.val) + '->')
                help(root.right, curr + str(root.val) + '->')
        
        help(root, '')
        return res
"""
Success
Details 
Runtime: 36 ms, faster than 85.94% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 13.6 MB, less than 6.33% of Python3 online submissions for Binary Tree Paths.
"""
#bfs + queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        res, queue  = [], collections.deque([(root, "")])
        while queue:
            node, cur = queue.popleft()
            
            if not node.left and not node.right:
                res.append(cur + str(node.val))
            if node.left:
                queue.append((node.left, cur + str(node.val) + "->"))
            if node.right:
                queue.append((node.right, cur + str(node.val) + "->"))
        return res
"""
Success
Details 
Runtime: 40 ms, faster than 59.60% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14 MB, less than 6.33% of Python3 online submissions for Binary Tree Paths.

"""
