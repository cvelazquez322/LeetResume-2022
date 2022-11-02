# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.internalArray = self.inorder(root, [])
    def inorder(self, root, rlist):
        if root.left:
            self.inorder(root.left, rlist)
        rlist.append(root.val)
        if root.right:
            self.inorder(root.right, rlist)
        return rlist
    def next(self) -> int:
        #print(self.internalArray, 1)
        return self.internalArray.pop(0)
            def hasNext(self) -> bool:
        #print(self.internalArray, 2)
        return bool(self.internalArray)
        # Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()