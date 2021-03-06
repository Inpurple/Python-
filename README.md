Python 语法总结 
====

### 1.Python continue 语句
continue 语句跳出本次循环，而break跳出整个循环。 
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue 语句用在while和for循环中。

### 2.	带索引的列表迭代 enumerate() 
列表：<br>  
```python
teams=["Parkers","49ers","Ravens","Patriots"]
for index,team in enumerate(teams):
    print(index,team)
```
    0 Parkers
    1 49ers
    2 Ravens
    3 Patriots
 
字典：对键和值都进行遍历<br>  
如果只需要值，可以使用d.values()，如果想获取所有的键则可以使用d.keys()。
如果想获取键和值d.items方法会将键-值对作为二维元组返回，for循环的一大好处就是可以循环中使用序列解包。

```python
d={
name1: "pythontab",
name2: ".",
name3: "com"
}
for key, value in d.items():
    print (key, ' value : ', value)
```
    name1 value : pythontab<br>  
    name2 value : .<br> 
    name3 value : com<br> 

### 3.	Python标准库网址
https://docs.python.org/zh-cn/3/library/index.html 

### 4.	Python中的浅拷贝和深拷贝<br> 
Python的切片操作是是浅拷贝<br> 
#### 浅拷贝
```python
import copy
a = [1, 2, 3, [5, 6]]
b = copy.copy(a)
print b
```
    [1, 2, 3, [5, 6]]
```python
a[3].append('c')
print b
```
    [1, 2, 3, [5, 6, 'c']]
#### 深拷贝
```python
a = [1, 2, 3, [5, 6]]
b = copy.deepcopy(a)
a[3].append('c')
print b
```
    [1, 2, 3, [5, 6]]
拷贝即是开辟一块新的内存空间，把被拷贝对象中的值复制过去。而浅拷贝并没有为子对象[5,6]开辟一块新的内存空间，而仅仅是实现对a中[5，6]的引用。所以改变a中[5，6]的值，b中的值也会发生变化。深拷贝则是为子对象也开辟了一块新空间。所以改变a中[5, 6]的值，并不影响b

### 5.	python根据某个值获得一维列表和二维列表的索引值

```python
L1 = [1,2,3,4,5,6,7,8,9,10]  #一维列表  

L2 = [[1,1],[2,2],[3,3],[4,4],[5,5]]  #二维列表  

def getOneDimensionListIndex(L,value):  
"""获得一维列表某个值的索引值"""  
index = L.index(value)  
return index  


def getTwoDimensionListIndex(L,value):  
"""获得二维列表某个值的一维索引值 
思想：先选出包含value值的一维列表，然后判断此一维列表在二维列表中的索引 
"""  
data = [data for data in L if data[0]==value] #data=[(53, 1016.1)]  
index = L.index(data[0])  
return index

#获得二维列表某个值的一维索引值的另一种方法
def getTwoDimensionListIndex(L,value):  
    """获得二维列表某个值的一维索引值的另一种方法"""  
    for i in range(len(L)):  
        for j in range(len(L[i])):  
            if L[i][j] == value  
            index = i 
```
s.index(x[, i[, j]])	x 在 s 中首次出现项的索引号（索引号在 i 或其后且在 j 之前）

### 6.Python 没有 switch / case 语句
不同于我用过的其它编程语言，Python 没有 switch / case 语句。为了实现它，我们可以使用字典映射：

### 7.	Python中可以当做key值的数据类型：
所有python自带类型中，除了list、dict、set和内部至少带有上述三种类型之一的tuple之外，其余的对象都能当key

### 8.	可变类型和不可变类型
不可变对象：该对象所指定内存中的值不可以被改变，在改变某个对象的值的时候，由于其内存中的值不可以被改变，所以，会把原来的值复制一份再进行改变，这样就会计算机会开辟一段新的内存空间来存储新的值，python 不可变对象有 int str float number,tuple,None<br>  

可变对象：该对象所指定的内存地址上面的值可以被改变，变量被改变后，其所指向的内存地址上面的值，直接被改变，没有发生复制行为，也没有发生开辟新的内存地址行为。python可变对象有，列表，字典，set集合

### 9.	Python中在列表索引超出范围(这里：’’)时获得默认值。
我如何做到这一点？在Python的“请求宽恕，不允许”的精神，这里有一种方法：<br> 
try:
    b = a[4]
except IndexError:
    b = ''
    
### 10.	python中关于str与list的元素替换

字符串替换str.replace()方法
python中的replace()方法是把字符串中的old字符串替换成new的字符串，如果指定替换次数max,则按照替换次数进行替换<br> 
str.replace(old,new,count=0)----但是并未改变str<br> 
old：字符串替换前的字符 <br> 
new：字符串替换后的字符 <br> 
count：替换的次数，默认为0，不填表示全局替换<br> 

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:

        
        print(s.replace(s[0],"_"))
        print(s)
```
standout:<br> 
_eetcode<br> 
leetcode

列表替换直接用索引赋值法

### 11.	字典序的理解
设想一本英语字典里的单词，何者在前何者在后？<br> 
显然的做法是先按照第一个字母、以 a、b、c……z 的顺序排列；如果第一个字母一样，那么比较第二个、第三个乃至后面的字母。如果比到最后两个单词不一样长（比如，sigh 和 sight），那么把短者排在前。<br>
通过这种方法，我们可以给本来不相关的单词强行规定出一个顺序。“单词”可以看作是“字母”的字符串，而把这一点推而广之就可以认为是给对应位置元素所属集合分别相同的各个有序多元组规定顺序。
### 12.	python 字符相减得到数字
python中没有字符之间的直接相减运算，但可以通过ord()函数实现 
ord()函数主要用来返回对应字符的ascii码
```python
ord('9')-ord('0')
```
    9
### 13.	如何删除二维数组的列
```python
import numpy as np
A = np.delete(A, 1, 0)  # delete second row of A
B = np.delete(B, 2, 0)  # delete third row of B
C = np.delete(C, 1, 1)  # delete second column of C
```
According to numpy's documentation page, the parameters for numpy.delete are as follow:
numpy.delete(arr, obj, axis=None)
* arr refers to the input array,
* obj refers to which sub-arrays (e.g. column/row no. or slice of the array) and
* axis refers to either column wise (axis = 1) or row-wise (axis = 0) delete operation.

### 14.	SET的用法
python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.

#### set方法对list去重：
1.set(某list) 返回字典，也许和原来的列表顺序不一样。

python 使用set对列表去重后，保持原来列表的顺序排列
```python
testlist = ['cc', 'bbbb', 'afa', 'sss', 'bbbb', 'cc', 'shafa']
set2list = list(set(testlist))
print set2list
set2list.sort(key = testlist.index) 
print set2list    
```
运行结果：

['cc', 'shafa', 'bbbb', 'afa', 'sss']<br> 
['cc', 'bbbb', 'afa', 'sss', 'shafa']



#### set的创建：
集合(set)
a.set是一个无序不重复的序列

b.可以用 { } 或者 set( ) 函数创建集合

c.集合存放不可变类型（字符串、数字、元组）

　　注意：创建一个空集合必须用 set( ) 而不是 { } ，因为 { } 是用来创建一个空字典 


 
#### Python Set add()方法
add() 方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。
语法
add()方法语法：set.add(elmnt)

### 15.	超出索引的返回值
pattern="b"<br>
print(pattern[1:])—""<br>
print(pattern[1])---提示超出索引<br>

pattern=["b"]<br>
print(pattern[1:])—[]<br>
print(pattern[1])---提示超出索引
### 16.python list中方法的时间复杂度
#### list
|Operation|Big-O Efficiency|
|:---|:---|
|index [] | O(1)|
|index assignment | O(1)|
|append | O(1)|
pop() | O(1)
pop(i) | O(n)
insert(i,item) | O(n)
del operator | O(n)
iteration | O(n)
contains (in) | O(n)
get slice [x:y] | O(k)
del slice | O(n)
set slice | O(n+k)
reverse | O(n)
concatenate | O(k)
sort | O(n log n)
multiply | O(nk)

#### dic

|操作|平均情况|最坏情况|
|:---|:---|:---|
|复制|O(n)|O(n)|
|取元素|O(1)|O(n)|
|更改元素|O(1)|O(n)|
|删除元素|O(1)|O(n)|
|遍历|O(n)|O(n)|

#### set
|操作|平均情况|最坏情况|
|:---|:---|:---|
x in s|O(1)|O(n)
并集|s|t|O(len(s)+len(t))	 
交集|s&t|O(min(len(s), len(t))|O(len(s) * len(t))
差集|s-t|O(len(s))	 
s.difference_update(t)|O(len(t))	 
对称差集 s^t|O(len(s))|O(len(s) * len(t))
s.symmetric_difference_update(t)|O(len(t))|O(len(t) * len(s))

### 17. python ‘//’ 取整，‘%’ 取余
2/2   除法（用于py3，py2中需要将除数转化为浮点型）<br>  
1.0<br>  
2//2  取整<br>  
1<br>  
1/2   除法<br>  
0.5<br>  
1//2  取整<br>  
0<br>  
3//2  取整<br>  
1<br>  
3%2  取余<br>  
1<br>  
4%2  取余<br>  
0<br>  

### 18.list与str的转换
对python 字符串中指定位置的字符做修改操作：<br>  
```python
str = list(str)
str [0] = 'p'
str = '.join(str)
```
### 19. Python 字符串大小写转换
以下代码演示了如何将字符串转换为大写字母，或者将字符串转为小写字母等：
```Python
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 
```

### 20.Python中可以用如下方式表示正负无穷：

float("inf")<br>  
float("-inf")

### 21.Python split()方法
Python 字符串 Python 字符串

#### 描述
Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串

#### 语法
split() 方法语法：
```python
str.split(str="", num=string.count(str)).
```
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。<br> 
num -- 分割次数。默认为 -1, 即分隔所有。<br> 
返回值:返回分割后的字符串列表。

### 22.解决报错RecursionError: maximum recursion depth exceeded in comparison
发现python默认的递归深度是很有限的（默认是1000），因此当递归深度超过999的样子，就会引发这样的一个异常。
解决<br> 
可以修改递归深度的值，让它变大大一点
```python
import sys   
sys.setrecursionlimit(100000) #例如这里设置为十万  
```
结语<br> 
这个解决方法并不治本，还需要在代码上进行优化。我出现这个错误的原因是忽略了对爬取页面的异常值处理，在增加判断之后，递归深度一般达不到python的默认限制。

### 23.Python 排序---sort与sorted学习
当我们从数据库中获取一写数据后，一般对于列表的排序是经常会遇到的问题，今天总结一下python对于列表list排序的常用方法：
#### 第一种：内建方法list.sort()可以直接对列表进行排序
用法：
```python
list.sort(func=None, key=None, reverse=False(or True))
```
对于reverse这个bool类型参数，当reverse=False时：为正向排序；当reverse=True时：为方向排序。默认为False。
执行完后会改变原来的list，如果你不需要原来的list，这种效率稍微高点为了避免混乱，其会返回none
例如：
```python
list = [2,8,4,6,9,1,3]
list.sort()
print(list)
```
    [1, 2, 3, 4, 6, 8, 9]+
#### 第二种：内建函数sorted()<br>
这个和第一种的差别之处在于：
sorted()不会改变原来的list，而是会返回一个新的已经排序好的list<br>
list.sort()方法仅仅被list所定义，sorted()可用于任何一个可迭代对象<br>
用法：
```python
sorted(list)
```

该函数也含有reverse这个bool类型的参数，当reverse=False时：为正向排序(从小到大)；当reverse=True时：为反向排序(从大到小)。当然默认为False。
执行完后会有返回一个新排序好的list
例如：

>>> list = [2,8,4,1,5,7,3]
>>> other = sorted(list)
>>> other
[1, 2, 3, 4, 5, 7, 8]

### 24.反转部分列表
#### 方法1：切片法
```python
a = [1,2,3,4,5]
a[0:3] = a[2::-1]   #work! 参数略复杂，[]中第一个参数是要反转的最后一个数的index，比如这里要翻转前三个数字 1 2 3，
               #那么第一个参数就是3的index，所以这里是2，第二个参数是要反转的第一个数的index，如果从第一个数开始那么可以省略
               #最后一个参数是-1，表示反序
print(a)
>>[3, 2, 1, 4, 5]
```
#### 方法2：list.reverse()
list.reverse()：是python中列表的一个内置方法（也就是说，在字典，字符串或者元组中，是没有这个内置方法的），用于列表中数据的反转；
exp：
```python
lista = [1, 2, 3, 4]
lista.reverse()
print(lista)
```
1
2
3
    打印结果：[4, 3, 2, 1]

其实，lista.reverse() 这一步操作的返回值是一个None，其作用的结果，需要通过打印被作用的列表才可以查看出具体的效果。

#### 方法3：reversed()：
而reversed()是python自带的一个方法，准确说，应该是一个类；<br>
关于reversed()官方解释：

>reversed(sequence) -> reverse iterator over values of the sequence
>Return a reverse iterator

translate it :
>reversed（sequence） - >反转迭代器的序列值
>返回反向迭代器

也就是说，在经过reversed()的作用之后，返回的是一个把序列值经过反转之后的迭代器，所以，需要通过遍历，或者List,或者next()等方法，获取作用后的值；

下面通过几个案例进行说明：
1.列表的反转：
```python
bb = [1,3,5,7]
print(list(reversed(bb)))
```
1
2
    打印结果：[7, 5, 3, 1]

### 25.dic.get()方法
get() 方法语法：

D.get(key[,default=None])
参数<br>
key -- 字典中要查找的键。<br>
default -- 可选参数，如果指定键的值不存在时，返回该值，默认为 None。<br>
返回值<br>
返回指定键的值，如果指定键的值不在字典中返回指定值，默认为 None。

### 26.python 中 None，空字符串，空列表的区别：
#### 1.区别:数据类型
在python中是没有NULL的，取而代之的是None，它的含义是为空，但要注意和空列表与空字符串的区别，None的类型是Nonetype,""的类型是string，[]的类型是list.<br>
None≠[]≠""
#### 2.共同点：判断皆为False
```python
type(None)
>>><class 'NoneType'>
```
python是把0，空字符串‘ ’和None都看作False，把其他数值和非空字符串都看作True

### 27.Python中if else简写出现"SyntaxError: can't assign to conditional expression"错误的解决方法将else后的“p1=”去掉

Re:SyntaxError: can't assign to conditional expression

原因在于，expression是表达式，就是加减乘除等各种运算符号联接起来的式子，是可以被求值的代码。Statement不总有值

### 28.队列，其实就是一个先进先出的线性表，只能在队首执行删除操作，在队尾执行插入操作。
用列表表示队列，可以用append()方法实现在队尾插入元素，用pop(0)方法实现在队首删除元素

### 29.python中的count()函数
#### 1.string 中 某字符 的次数
```python
str.count(sub, start= 0,end=len(string))
```
|Args|Annotations|
|:---|:---|
|sub|搜索的子字符串|
|start|字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。|
|end|字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。|
#### 2.list 中 某元素 的次数
```python
list.count(obj)
```
|Args|Annotations|
|:---|:---|
|obj|搜索的list|

### 30.关于python列表(list)切片[start:stop:step]的理解 

列表切片的语法
```python
1 names=["bbguo","bbliang","bbxi","bbwang","bbbo","bbya","bbyi","bbqing"]
2 print(a[0:3:2])  #切片格式 变量名[start:stop:step]，3个参数分别是切片的起始下标，停止下标和步长。
```

理解:

#### 1.切片的step的值是正还是负，决定切片的方向：
##### 1.1 即step为正数时（step>0），代表从左往右切片，即start下标值小于stop下标值，比如上面的列表，
```python
1 names=["bbguo","bbliang","bbxi","bbwang","bbbo","bbya","bbyi","bbqing"]
2 print(names[1:5:2]) #step为2，大于0,从左往右切，从start开始（含start的值"bbliang"），stop结束（不含stop的值"bbya"）,语法逻辑要求start须小于stop才会认为语法正确，并执行切片操作，这里start=1,stop=5,start<stop,
3 ['bbliang', 'bbwang'] #输出结果
```
##### 1.2 当step为负数时（step<0），代表从右往左切片，即start下标值需要大于stop下标值，编译器才可以判断并执行切片操作。
``` python
1 names=["bbguo","bbliang","bbxi","bbwang","bbbo","bbya","bbyi","bbqing"]
2 print(names[5:1:-2]) #step为-2，小于0,从右往左执行切片，从start开始（含start的值“bbya”），stop结束（不含stop的值"bbliang"）,语法逻辑要求start须大于stop，编译器才会认为语法正确执行切片操作，这里start=5,stop=1,start>stop, 
3  ['bbya', 'bbwang'] #输出结果
```
#### 2、start、stop、step 为空值时的理解，空值得理解
##### 2.1 start的空值，即start的第一个值，当step为正的时候，start的空值为下标0,stop的空值为下标7，这里这个例子就是：names[0] ；当step为负的时候，start的空值代表下标7，stop的空值代表下标0，列表的最后一个数据，即names[leng-1]， 即star和stop的空值代表列表的头和尾，依据step的是正还是负来颠倒，例子：<br>  
step为1时：<br>  
```python
1 names=["bbguo","bbliang","bbxi","bbwang","bbbo","bbya","bbyi","bbqing"]
2 print(names[::1]) #start为0，stop 为lenth（注意不是7，因为包含bbqing）
3 ['bbguo', 'bbliang', 'bbxi', 'bbwang', 'bbbo', 'bbya', 'bbyi', 'bbqing'] #输出结果
```
 
step为-1时：<br>  
```python
1 names=["bbguo","bbliang","bbxi","bbwang","bbbo","bbya","bbyi","bbqing"]
2 print(names[::-1]) #start 为 lenth(注意不是7，包含bbqing)，stop为0
3 ['bbqing', 'bbyi', 'bbya', 'bbbo', 'bbwang', 'bbxi', 'bbliang', 'bbguo'] #输出结果
```
##### 2.2 step的空值代表默认1。
 
#### 3、列表下标，以及切片时start,stop的负值的理解：
##### 3.1 首先列表下标为负值时，即代表从列表右边数起来倒数第几个元素，比如names[-1]即代表，names这个列表右边第一个元素。例子如下：
```python
1 names=["bbguo","bbliang","bbxi","bbwang","bbbo","bbya","bbyi","bbqing"]
2 print (names[-1]) #-1下标代表列表的倒数第一个元素，即右边第一个元素
3 bbqing  #输出结果
```
同理可以推出names[-2],names[-3]
##### 3.2 切片的start和stop为负值时，无论step是正还是负，start和stop的负值都代表的是列表从左到右的倒数第几个元素。也就是说比如无论names[-1::1]、names[-1::-1]，names[:-1:1]、names[:-1:-1]，names[start]或者names[stop]的-1代表的都是names.这个列表中倒数第一个数据（bbqing），step正负这里只是用来判断切片的方向，继而查看切片的start和stop按照step的方向，是否有数据可以切片。当step>0时,比如step=1，由于names[-1::1]的start 位置以及是右边的倒数第一个数据了，即这个列表的最后一个数据，所以按照step正数向右切片，所以stop的空值也是这个数据，所以根据切片包含start的逻辑，而stop空值右包含最后一个数据，所以names[-1::1]输出结果将为bbqing。
　　　　
```python
1 names=["bbguo","bbliang","bbxi","bbwang","bbbo","bbya","bbyi","bbqing"]
2 print (names[-1::1])
3 ['bbqing'] #输出结果
```
##### 3.3 当step为正，代表切片方向从左往右，如果切片的范围区间不正确，没有数据，输出结果将为空值。举例如下：
```python
1 names=["bbguo","bbliang","bbxi","bbwang","bbbo","bbya","bbyi","bbqing"]
2 print(names[-4:5:-1]) #step-1,即代表从右往左切片，start值为-4，即右边倒数第四个数据（bbbo）,stop为5，即左边数起第小标5的数据(bbya),从bbo开始，bbya结束，不符合-1从右往左切片的方向要求，所以切片区间内没有值，输出空值。
3 [] 输出结果
 ```
综上所有实验数据得出的结论主要有一下3点：<br>  
python的列表切片<br>  
1、方向由step确定，step为正时，从左往右切片，step为负时，从右往左切片。<br>  
2、start和stop的正值代表列表下标，负值代表列表从左往右数起，倒数第几个数据。<br>  
3、start和stop的空值分别代表列表的头尾的最后一个数据，至于start和stop空值的时候代表的是列表的头还是尾，由step的正负值决定，即由step确定列表切片的方向后决定。当step为正时，即代表从左往右切片，则start的空值代表左边的开头，stop的空值代表右边的结尾。当step为负值时，即代表从右往左切片，则start的空值代表右边的开头，stop的空值代表左边的结尾。当step为负时，start的空值代表
 
### 29.Python isdigit()函数的使用方法 

#### 29.1检测字符串中是否由“正数字”组成。<br>  ---正整数还是正数有待确认
语法使用：str.isdigit()<br>  
如果字符串中至少有一个字符串并且所有的字符由数字组成，那么将返回True，否则返回False。

#### 29.2检测字符串中是否由“数字”组成。<br>  ----包括正负

正则表达式法：
```python
 num = '-10'
 import re
 if re.match(r'^-?(\.\d+|\d+(\.\d+)?)', num)：
     print(num是整数)
 else:
     print(num不是整数)
```

更Pythonic的方法：
```python
 num = '-10'
 if num.lstrip('-').isdigit():
     print(num是整数)
 else:
     print(num不是整数)
 ```
 
### 30.dict()函数的使用方法 
作用：dict() 函数用于创建一个字典。返回一个字典。<br>
语法：<br>
```python
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
```
参数说明：
**kwargs -- 关键字<br>
mapping -- 元素的容器。<br>
iterable -- 可迭代对象<br>
实例：
```python
1 >>>dict()                        # 创建空字典
2 {}
3 >>> dict(a='a', b='b', t='t')     # 传入关键字
4 {'a': 'a', 'b': 'b', 't': 't'}
5 >>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
6 {'three': 3, 'two': 2, 'one': 1} 
7 >>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
8 {'three': 3, 'two': 2, 'one': 1}
9 >>>
```
### 30.Python3 字典 items() 方法

描述:Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
### 31.lambda表达式
lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
lambda就是用来定义一个匿名函数的，如果还要给他绑定一个名字的话，就会显得有点画蛇添足，通常是直接使用lambda函数。如下所示：
```python
add = lambda x, y : x+y
add(1,2)  # 结果为3
```

### 32. python位运算
Python位运算符
按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：


&:按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
|:按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
^:按位异或运算符：当两对应的二进位相异时，结果为1 
~:按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1

以下实例演示了Python所有位运算符的操作：
```python
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b;        # 12 = 0000 1100
print "1 - c 的值为：", c
 
c = a | b;        # 61 = 0011 1101 
print "2 - c 的值为：", c
 
c = a ^ b;        # 49 = 0011 0001
print "3 - c 的值为：", c
 
c = ~a;           # -61 = 1100 0011
print "4 - c 的值为：", c
 
c = a << 2;       # 240 = 1111 0000
print "5 - c 的值为：", c
 
c = a >> 2;       # 15 = 0000 1111
print "6 - c 的值为：", c
以上实例输出结果：
1 - c 的值为： 12
2 - c 的值为： 61
3 - c 的值为： 49
4 - c 的值为： -61
5 - c 的值为： 240
6 - c 的值为： 15
```
### 33. python 计数器（counter）

Counter是对字典类型的补充，用于追踪值的出现次数。

ps：具备字典的所有功能 + 自己的功能

 

把我写入的元素出现的多少次都计算出来
```python
import collections

# 创建一个Counter对象
obj = collections.Counter(‘ddccbbqqaaa‘)
print(obj)

```


Counter({‘a‘: 3, ‘d‘: 2, ‘c‘: 2, ‘b‘: 2, ‘q‘: 2})#把我写入的元素出现的多少次都计算出来


### 34.python常见报错: IndentationError: unindent does not match any outer indentation level----
检查包括注释在内，是否所有的都缩进在同一位置

![image](https://github.com/Inpurple/Python-/blob/master/Python_sytax_attach/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190813162754.png)


### 35.Python判断字符串是否为字母或者数字

```python
str_1 = "123"
str_2 = "Abc"
str_3 = "123Abc"

#用isdigit函数判断是否数字
print(str_1.isdigit())
Ture
print(str_2.isdigit())
False
print(str_3.isdigit())
False

#用isalpha判断是否字母
print(str_1.isalpha())    
False
print(str_2.isalpha())
Ture    
print(str_3.isalpha())    
False

#isalnum判断是否数字和字母的组合
print(str_1.isalnum())    
Ture
print(str_2.isalnum())
Ture
print(str_1.isalnum())    
Ture
注意：如果字符串中含有除了字母或者数字之外的字符，比如空格，也会返回False
```

### 36.遗留问题：列表反转，lis[::-1],冒号的默认值是啥？

顾头不顾尾

使用range()生成器时，如果冒号前面没写的话，代表从0开始取元素<br> 
使用range()生成器时，如果冒号后面没写的话，代表取到最后的元素<br> 
如果冒号前后都没写的话，代表取全部<br> 
如果步长是正数的话，就从前往后开始取值；<br> 
如果步长是负数的话，就从后往前开始取值，类似于reverse()<br> 

切片应该类似
   
