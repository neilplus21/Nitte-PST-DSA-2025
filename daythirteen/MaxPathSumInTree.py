class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        def max_gain(node):
            if not node: return 0
            # Recursively get max gain from left and right
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            # Current path sum through the node
            current_sum = node.val + left_gain + right_gain
            # Update global max sum
            self.max_sum = max(self.max_sum, current_sum)
            # Return max gain if continue the same path
            return node.val + max(left_gain, right_gain)
        max_gain(root)
        return self.max_sum
# Step 1: Build your binary tree
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().max_sum(root))

# class TreeNode:
#     def __init__(self,val,left=None,right=None):
#         self.val =val
#         self.left = left
#         self.right = right
#     def __repr__(self):
#         return f"({self.val})"
#     def __str__(self): return str(self.val)+" "+str(self.left.val)+" "+str(self.right.val)
        
        
# def max_path_sum(root:TreeNode):
#     if root is None: return 0
    
#     left_cost = max_path_sum(root.left)
#     right_cost = max_path_sum(root.right)
#     return max(root.val, left_cost, right_cost, left_cost+root.val,right_cost+root.val,
#                left_cost+right_cost+root.val
#                )
    
# def construct_tree(arr,i=0):
#     if i>=len(arr) or arr[i] is None:
#         return None
#     parent = TreeNode(arr[i])
#     parent.left = construct_tree(arr,i*2+1)
#     parent.right = construct_tree(arr,i*2+2)
#     return parent

# print(max_path_sum(construct_tree([1,2,3])))
# print(max_path_sum(construct_tree([-10,9,20,None,None,15,7])))
# root = construct_tree([-10,9,20,None,None,15,7])