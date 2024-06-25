# Assignment #3: March月考

Updated 1537 GMT+8 March 6, 2024

2024 spring, Complied by ==同学的姓名、院系==

罗瑞哲 生命科学学院

**说明：**

1）The complete process to learn DSA from scratch can be broken into 4 parts:
- Learn about Time and Space complexities
- Learn the basics of individual Data Structures
- Learn the basics of Algorithms
- Practice Problems on DSA

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



**编程环境**

==（请改为同学的操作系统、编程环境等）==

操作系统：Windows 10

Python编程环境：Spyder IDE 5.2.2, PyCharm 2023.1.4 (Professional Edition)

C/C++编程环境：Mac terminal vi (version 9.0.1424), g++/gcc (Apple clang version 14.0.3, clang-1403.0.22.14.1)



## 1. 题目

**02945: 拦截导弹**

http://cs101.openjudge.cn/practice/02945/



思路：



##### 代码

```python
# 
k=int(input())
l=list(map(int,input().split()))
dp=[0]*k
for i in range(k-1,-1,-1):
    maxn=1
    for j in range(k-1,i,-1):
        if l[i]>=l[j] and dp[j]+1>maxn:
            maxn=dp[j]+1
    dp[i]=maxn
print(max(dp))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240312213632660](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240312213632660.png)



**04147:汉诺塔问题(Tower of Hanoi)**

http://cs101.openjudge.cn/practice/04147



思路：



##### 代码

```python
# 
def moveOne(numDisk : int, init : str, desti : str):
    print("{}:{}->{}".format(numDisk, init, desti))
def move(numDisks : int, init : str, temp : str, desti : str):
    if numDisks == 1:
        moveOne(1, init, desti)
    else:
        move(numDisks-1, init, desti, temp) 
        moveOne(numDisks, init, desti)
        move(numDisks-1, temp, init, desti)

n, a, b, c = input().split()
move(int(n), a, b, c)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240312211551576](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240312211551576.png)



**03253: 约瑟夫问题No.2**

http://cs101.openjudge.cn/practice/03253



思路：



##### 代码

```python
# 
while True:
    n, p, m = map(int, input().split())
    if {n,p,m} == {0}:
        break
    monkey = [i for i in range(1, n+1)]
    for _ in range(p-1):
        tmp = monkey.pop(0)
        monkey.append(tmp)

    index = 0
    ans = []
    while len(monkey) != 1:
        temp = monkey.pop(0)
        index += 1
        if index == m:
            index = 0
            ans.append(temp)
            continue
        monkey.append(temp)

    ans.extend(monkey)

    print(','.join(map(str, ans)))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240312211805378](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240312211805378.png)



**21554:排队做实验 (greedy)v0.2**

http://cs101.openjudge.cn/practice/21554



思路：



##### 代码

```python
# 
n=int(input())
lst=list(map(int,input().split()))
dic={}
nums=[]
t=0
for i in range(n):
    dic[i+1]=lst[i]
lst.sort()
for i in range(n):
    t+=(n-i-1)*lst[i]
    for k,v in dic.items():
        if lst[i]==v:
            nums.append(str(k))
            dic[k]=None
t/=n
print(" ".join(nums))
print("%.2f"%t)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240312200704277](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240312200704277.png)



**19963:买学区房**

http://cs101.openjudge.cn/practice/19963



思路：



##### 代码

```python
# 
n = int(input())

pairs = [i[1:-1] for i in input().split()]
distances = [ sum(map(int,i.split(','))) for i in pairs]

prices = [int(x) for x in input().split()]

# ratio = distance/price
r = []
for i in range(n):
    r.append(distances[i]/prices[i])


H = zip(r,prices)
H = sorted(H, key=lambda x: (-x[0],x[1]))

#print(H)

prices.sort()    
r.sort()

import math
if n%2 == 0:
    rank = int(n/2)
    price_sq = (prices[rank-1] + prices[rank])/2
    r_sq = (r[rank-1] + r[rank])/2
else:
    rank = math.ceil(n/2)
    price_sq = prices[rank-1]
    r_sq = r[rank-1]
    
cnt = 0
for h in H:
    if h[0]>r_sq and h[1]<price_sq:
        cnt += 1 
    
print(cnt)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240312212240201](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240312212240201.png)



**27300: 模型整理**

http://cs101.openjudge.cn/practice/27300



思路：



##### 代码

```python
# 
from collections import defaultdict

n = int(input())
d = defaultdict(list)
for _ in range(n):
    name, para = input().split('-')
    if para[-1]=='M':
        d[name].append((para, float(para[:-1])/1000) )
    else:
        d[name].append((para, float(para[:-1])))


sd = sorted(d)
for k in sd:
    paras = sorted(d[k],key=lambda x: x[1])
    value = ', '.join([i[0] for i in paras])
    print(f'{k}: {value}')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240312212010938](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20240312212010938.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“2024spring每日选做”、CF、LeetCode、洛谷等网站题目。==

这周别的作业有点多，有些题来不及做了，只好抄题解，我下周挤出时间把这些题复盘一下。



