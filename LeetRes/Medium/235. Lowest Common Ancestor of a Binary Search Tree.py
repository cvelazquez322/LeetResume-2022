# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def helper(root, a, path, rlist):
    path += str(root.val) + ','
    if root == a:
        rlist.append(path)
    if root.left:
        helper(root.left, a, path, rlist)
    if root.right:
        helper(root.right, a, path, rlist)
    return rlist
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return 0
        ppath = helper(root, p, '', [])[0].split(',')
        ppath.pop()
        #print(ppath)
        qpath = helper(root, q, '', [])[0].split(',')
        qpath.pop()
        #print(qpath)
        curr = None
        for i in range(min(len(ppath), len(qpath))):
            if ppath[i] == qpath[i]:
                curr = ppath[i]
            else:
                return TreeNode(int(curr))
                    return TreeNode(int(curr))