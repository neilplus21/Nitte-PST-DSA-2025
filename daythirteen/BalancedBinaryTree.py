class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def balanced_binary_tree(root):
    is_valid = True
    def depth(node):
        nonlocal is_valid
        if node is None: return 0
        left_depth = depth(node.left)
        right_depth = depth(node.right)
        if abs(left_depth-right_depth)>1: is_valid = False
        return max(left_depth,right_depth) + 1
    depth(root)
    return is_valid
def construct_tree(arr,i=0):
    if i>=len(arr) or arr[i] is None: return None
    parent = TreeNode(arr[i])
    parent.left = construct_tree(arr,i*2+1)
    parent.right = construct_tree(arr,i*2+2)
    return parent

print(balanced_binary_tree(construct_tree( [3,9,20,None,None,15,7])))
print(balanced_binary_tree(construct_tree([1,2,2,3,3,None,None,4,4])))  
print(balanced_binary_tree(construct_tree([])))  
print(balanced_binary_tree(construct_tree([1,2,None,None,3,4])))
     


        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class Solution:
#     def check(self,node):
#         if not node: return 0  # height 0
#         left = self.check(node.left)
#         if left == -1: return -1  # not balanced
#         right = self.check(node.right)
#         if right == -1: return -1
#         if abs(left - right) > 1: return -1  # unbalanced tree
#         print(1+max(left,right),left,right)
#         return 1 + max(left, right)  # return height
# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3, TreeNode(6), TreeNode(7))
# print(Solution().check(root) != -1)
# '''
#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7
# '''
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(4)
# print(Solution().check(root) != -1)
# '''
#         1
#        /
#       2
#      /
#     3
#    /
#   4
# '''