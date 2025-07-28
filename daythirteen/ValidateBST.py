class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def validate(self,node, min_val=float('-inf'), max_val=float('inf')):
        if not node: return True
        if not (min_val < node.val < max_val): return False
        return (self.validate(node.left, min_val, node.val) and
                self.validate(node.right, node.val, max_val))
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(Solution().validate(root))  # True
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(Solution().validate(root))  # False