튜플

>>> (1,2,3)
(1, 2, 3)
>>> aaa=(1,2,3)
>>> bbb=(4,5,6)
>>> ccc=aaa+bbb
>>> ccc
(1, 2, 3, 4, 5, 6)
>>> aaa*5
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> a=(1,2,"사과","배")
>>> a
(1, 2, '사과', '배')
>>> len(a)
4

튜플은 변경이 안되고고 리스트는 변경이 가능하다.
()가 튜플 []가 리스트

>>> a=[1,2,3,4]
>>> a[0]=10
>>> a
[10, 2, 3, 4]
>>> b=(1,2,3,4)
>>> b[0]=10
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b[0]=10
TypeError: 'int' object does not support item assignment

>>> for i in [1,2,3,4,5]:
	print(i)


1
2
3
4
5
>>> (1,2,(1,2),3,4)
(1, 2, (1, 2), 3, 4)



>>> max(a)
10
>>> min(a)
2
>>> a
[10, 2, 3, 4]
>>> a[0]
10
>>> a[-1]
4
>>> a[1:4]
[2, 3, 4]

>>> a[:3]
[10, 2, 3]

>>> a[1:]
[2, 3, 4]




>>> a=1,2,3,4

>>> a
(1, 2, 3, 4)

>>> x=1

>>> y=2

>>> x,y=y,x

>>> x
2
>>> y
1

>>> (x,y)=(y,x)

>>> a,b,c=1,2,3


>>> (name,age,major)=("홍길동",18,"컴퓨터")
>>> name
'홍길동'
>>> age
18
>>> major
'컴퓨터'


>>> def mycalc(a,b):
	sumresult=a+b
	subresult=a-b
	return sumresult, subresult

>>> mycalc(10,5)
(15, 5)
>>> sum, sub=mycalc(3,4)
>>> sum
7
>>> sub
-1


두가지 결과 값이 가능하다




>>> a={1,2,3,4}
>>> if 1 in a:
	print("있음")


있음

원소를 꺼내서 맞출수 있다.

>>> for i in a:
	print(i)


1
2
3
4

>>> a={3,5,7,1,2,3}
>>> a
{1, 2, 3, 5, 7}

정렬이되어서 나온다.

>>> set([4,5,6,7])
{4, 5, 6, 7}

집합으로 나온다  집합은 중복을 제거해준다.


>>> for char in set("banana"):
	print(char)


a
b
n
>>> a
{1, 2, 3, 5, 7}
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a[0]
TypeError: 'set' object does not support indexing
>>> a
{1, 2, 3, 5, 7}
>>> a.add(8)
>>> a
{1, 2, 3, 5, 7, 8}


>>> a.update([100,200,300])
>>> a
{1, 2, 3, 100, 5, 7, 8, 200, 300}
>>> a.discard(100)
>>> a
{1, 2, 3, 5, 7, 8, 200, 300}

>>> a.remove(200)
>>> a
{1, 2, 3, 5, 7, 8, 300}
>>> a.clear()
>>> a
set()


부분관계
>>> a={1,2,3}
>>> b={4,5,6}
>>> a==b
False

>>> c={1,2,3}
>>> a==c
True

>>> b={1,2,3,4,5,6}
>>> a<b
True
>>> a>b
False


>>> a.issubset(b)
True
>>> a.issuperset(b)
False

>>> b.issuperset(a)
True

>>> 3 in a
True

>>> a|b
{1, 2, 3, 4, 5, 6}

>>> a&b
{1, 2, 3}

>>> a.union(b)
{1, 2, 3, 4, 5, 6}

>>> a.intersection(b)
{1, 2, 3}

>>> a-b
set()

>>> a
{1, 2, 3}

>>> b
{1, 2, 3, 4, 5, 6}

>>> b-a
{4, 5, 6}

>>> all(a)
True

>>> any(a)
True

>>> a={0,1,2}

>>> all(a)
False

>>> any(a)
True

>>> len(a)
3

>>> max(a)
2

>>> min(a)
0

>>> sorted(a)
[0, 1, 2]



키값
>>> a={1:"갑돌이",2:"갑순이","aaa":"홍길동"}
>>> a[1]
'갑돌이'
>>> a[2]
'갑순이'
>>> a["aaa"]
'홍길동'


>>> student={"kim":2017001, "park":2017002, "Lee":2017003}
>>> student
{'kim': 2017001, 'park': 2017002, 'Lee': 2017003}
>>> student["kim"]
2017001
>>> student["park"]
2017002
>>> student["kim"]=2017005
>>> student
{'kim': 2017005, 'park': 2017002, 'Lee': 2017003}



>>> a={}
>>> a
{}
>>> a=set()
>>> a
set()
>>> a={}
>>> student["choi"]
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    student["choi"]
KeyError: 'choi'
>>> student.get("choi",2017007)
2017007


>>> if "kim" in a:
	print("있음")


>>> if "kim" in student:
	print("있음")


있음
>>> student
{'kim': 2017005, 'park': 2017002, 'Lee': 2017003}
>>> {'kim': 2017005, 'park': 2017002, 'Lee': 2017003}
{'kim': 2017005, 'park': 2017002, 'Lee': 2017003}
>>> student["choi"]=2017004
>>> student
{'kim': 2017005, 'park': 2017002, 'Lee': 2017003, 'choi': 2017004}
>>> student.pop("choi")
2017004
>>> student
{'kim': 2017005, 'park': 2017002, 'Lee': 2017003}
>>> del student["kim"]
>>> student
{'park': 2017002, 'Lee': 2017003}
>>> student.items()
dict_items([('park', 2017002), ('Lee', 2017003)])
>>> for i in student.items():
	print(i)


('park', 2017002)
('Lee', 2017003)



>>> "park" in student
True
>>> "kim" in student
False


>>> a={x:x**3 for x in range(6)}
>>> a
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


>>> a[4]
64

정렬하기 위해서는 리스트로
>>> list(a)
[0, 1, 2, 3, 4, 5]


>>> a
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

>>> sorted(a)
[0, 1, 2, 3, 4, 5]

>>> a.values()
dict_values([0, 1, 8, 27, 64, 125])

>>> sorted(a.values())
[0, 1, 8, 27, 64, 125]


피보나치 수열



재귀함수 일 때 엄청 느리다
>>> def fib(n):
	if n==0:
		return 0
	if n==1 or n==2:
		return 1
	return fib(n-2)+fib(n-1)


테이블을 저장해서 할 때 빨리 된다.
>>> table={0:0 , 1:1}
>>> def fib(n):
	if n not in table:
		value=fib(n-1)+fib(n-2)
		table[n]=value
	return table[n]

>>> fib(50)
12586269025
>>> fib(100)
354224848179261915075



[0]*100 초기화 리스트로 

ㅗ
