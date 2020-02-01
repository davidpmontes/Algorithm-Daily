# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.output = []
        self.answer = float("inf")
        def inOrderTraversal(root):
            if root == None:
                return
            
            inOrderTraversal(root.left)
            self.output.append(root.val)
            inOrderTraversal(root.right)
            
            return
        
        inOrderTraversal(root)
        
        for i in range(1, len(self.output)):
            absoluteDif = self.output[i] - self.output[i - 1]
            if absoluteDif < self.answer:
                self.answer = absoluteDif
        
        return self.answer
