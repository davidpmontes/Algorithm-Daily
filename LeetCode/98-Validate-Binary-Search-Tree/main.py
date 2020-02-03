# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(root, minLeft, maxRight):
            if root == None:
                return True
            
            if root.left:
                if root.left.val >= root.val or root.left.val <= minLeft:
                    return False
            
            if root.right:
                if root.right.val <= root.val or root.right.val >= maxRight:
                    return False
            
            return helper(root.left, minLeft, root.val) and helper(root.right, root.val, maxRight)
        
        return helper(root, float("-inf"), float("inf"))
