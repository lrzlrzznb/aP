class TreeNode:
    def __init__(self,letter):
        self.val=letter
        self.sons=[]
def build_tree(st):
    lst=[]
    node=None
    for i in st:
        if i.isupper():
            node=TreeNode(i)
            if lst:
                lst[-1].sons.append(node)
        elif i=="(":
            if node:
               lst.append(node)
               node=None
        elif i==")":
            if lst:
                node=lst.pop()
    return node
def postorder(node):
    ans=[]
    for son in node.sons:
        ans.extend(postorder(son))
    ans.append(node.val)
    return "".join(ans)
s=input().strip()
ans1=[]
for i in s:
    if i.isupper():
        ans1.append(i)
print("".join(ans1))
root=build_tree(s)
print(postorder(root))
