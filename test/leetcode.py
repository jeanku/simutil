from simutil.Tree import Tree, TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if root is None:
            return root
        def changeleftAndRight(node: TreeNode):
            if node.left is None and node.right is None:
                return
            else:
                node.left, node.right = node.right, node.left
                changeleftAndRight(node.left)
                changeleftAndRight(node.right)
        changeleftAndRight(root.left, root.right)
        return root



t = Tree()
t.construct_tree([9, -42, -42, None, 76, 76, None, None, 13, None, 13])
