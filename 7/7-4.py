class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def cla(s):
    for i in s:
        if i!=s[0]:
            return "F"
    if s[0]=="0":
        return "B"
    if s[0]=="1":
        return "I"
def build_tree(s):
    if not s:
        return None
    l=len(s)//2
    root=TreeNode(cla(s))
    if l!=0:
        root.left=build_tree(s[:l])
        root.right=build_tree(s[l:])
    return root
def postorder(root):
    ans=[]
    if root:
        ans.extend(postorder(root.left))
        ans.extend(postorder(root.right))
        ans.append(root.val)
    return ans
n=int(input())
s=input().strip()
root=build_tree(s)
ans=postorder(root)
print("".join(ans))