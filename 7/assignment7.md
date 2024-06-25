# Assignment #7: April 月考

Updated 1557 GMT+8 Apr 3, 2024

2024 spring, Complied by ==同学的姓名、院系==

罗瑞哲 生命科学学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 10

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

### 27706: 逐词倒放

http://cs101.openjudge.cn/practice/27706/



思路：



代码

```python
# 
s=list(map(str,input().split()))
s.reverse()
print(" ".join(s))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240406171703647](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240406171703647.png)



### 27951: 机器翻译

http://cs101.openjudge.cn/practice/27951/



思路：



代码

```python
# 
m,n=map(int,input().split())
words=list(map(int,input().split()))
queue=[]
ans=0
for num in words:
    if num not in queue:
        queue.append(num)
        ans+=1
        if len(queue)==m+1:
            queue.pop(0)
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240406173320694](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240406173320694.png)



### 27932: Less or Equal

http://cs101.openjudge.cn/practice/27932/



思路：



代码

```python
# 
n,k=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
if k==0:
    print(nums[0]-1 if nums[0]>1 else -1)
else:
    if k<n and nums[k-1]==nums[k]:
        print(-1)
    else:
        print(nums[k-1])
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240406175643750](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240406175643750.png)



### 27948: FBI树

http://cs101.openjudge.cn/practice/27948/



思路：



代码

```python
# 
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
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240406215551256](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240406215551256.png)



### 27925: 小组队列

http://cs101.openjudge.cn/practice/27925/



思路：



代码

```python
# 
from collections import deque
t=int(input())
grp={}
for i in range(t):
    grp[i]=list(map(str,input().split()))
queue=deque()
group_queue={i:deque() for i in range(t)}
while True:
    s=list(map(str,input().split()))
    if s==["STOP"]:
        break
    elif s[0]=="ENQUEUE":
        p=s[1]
        for i in range(t):
            if p in grp[i]:
                group_queue[i].append(p)
                if i not in queue:
                    queue.append(i)
                break
    else:
        group=queue[0]
        print(group_queue[group].popleft())
        if not group_queue[group]:
            queue.popleft()

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240406223600508](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240406223600508.png)



### 27928: 遍历树

http://cs101.openjudge.cn/practice/27928/



思路：



代码

```python
# 
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
def traverse_print(root, nodes):
    if root.children == []:
        print(root.value)
        return
    pac = {root.value: root}
    for child in root.children:
        pac[child] = nodes[child]
    for value in sorted(pac.keys()):
        if value in root.children:
            traverse_print(pac[value], nodes)
        else:
            print(root.value)
n = int(input())
nodes = {}
children_list = []
for i in range(n):
    info = list(map(int, input().split()))
    nodes[info[0]] = TreeNode(info[0])
    for child_value in info[1:]:
        nodes[info[0]].children.append(child_value)
        children_list.append(child_value)
root = nodes[[value for value in nodes.keys() if value not in children_list][0]]
traverse_print(root, nodes)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240407180059227](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240407180059227.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

这次作业难度不大，挺好的。



