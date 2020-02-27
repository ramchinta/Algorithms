'''Given a Binary Search Tree (BST),
convert it to a Greater Tree such that every key of the original BST is changed to the original key plus
sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.cursum = 0
    def convertBST(root):
        if not root:
            return None
        if root.right:
            self.convertBST(root.right)
        self.cursum+=root.val
        root.val=self.cursum
        if root.left:
            self.convertBST(root.left)
        return root

print(Solution.convertBST([5,2,13]))
#[18,20,13]