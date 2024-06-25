class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def buildtree(inorder,postorder):
    if not inorder or not postorder:
        return None
    root_val=postorder.pop()
    root=TreeNode(root_val)
    root_index=inorder.index(root_val)
    root.right=buildtree(inorder[root_index+1:],postorder)
    root.left=buildtree(inorder[:root_index],postorder)
    return root
def preorder(root):
    ans=[]
    if root:
        ans.append(root.val)
        ans.extend(preorder(root.left))
        ans.extend(preorder(root.right))
    return ans
inorder=input().strip()
postorder=input().strip()
root=buildtree(list(inorder),list(postorder))
print("".join(preorder(root)))