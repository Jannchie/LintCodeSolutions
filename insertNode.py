
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None



class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root == None:
            root = node
        if node.val < root.val:
            if root.left == None:
                root.left = node
            self.insertNode(root.left,node)
        if node.val > root.val:
            if root.right == None:
                root.right = node
            self.insertNode(root.right,node)
        return root

s = Solution()
a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)
a.left = b
s.insertNode(a,c)