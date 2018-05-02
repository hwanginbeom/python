>>> def myfunc(x):
	x=4
	print(x)


>>> x=5
>>> x
5
>>> myfunc(x)
4


x=5는 전역변수

함수 안에 있는 x=4는 지역 변수

우선순위는 지역변수에 먼저 있다.  함수는 스택에 저장된다. 그래서 함수가 살아 있을 동안에만 쓰여진다.

전역변수는 함수를 닫지 않는 한 계속 살아있다.


a=3 , b=4

sum(a,b)

def sum(x,y) 여기에 a와 b 를 넣으면 주소 값이 들어간다.
x=5
y=6

-> a= 3 , b =4
이유는 ?

이 id 값은 a 와 x 의 값은 다르게 나타나진다.

정리하자면 sum(x,y) 까지는 주소 값이 들어간다.

하지만 x 와 y값은 주소값이 아닌 그냥 값이 들어가고 이 주소는 a 와 b와

다른 주소를 가지게 된다.


mutable = list

immutable = string , int, tuple

>>> aaa="hi"
>>> id(aaa)
49127456
>>> aaa+="good"
>>> aaa
'higood'
>>> id(aaa)
55434432

string으로 할 경우 immutalbe 이라 주소 값에 저장이 되는게 아니라 새로운 주소값에

저장을하고


>>>
>>> aaa=[1,2,3,4]
>>> id(aaa)
57973736
>>> aaa+=[5,6]
>>> aaa
[1, 2, 3, 4, 5, 6]
>>> id(aaa)
57973736


list 에 저장을 할경우 mutable 값이라 주소값에 저장이 된다.

aaa += 3
aaa=aaa+3    // 주소값이 바뀐다.
이건 다르다. 주소 값이 달라진다.


>>> def sub():
	s="바나나"
	print(s)


>>> sub()
바나나
>>> s
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s
NameError: name 's' is not defined

s는 sub안에 만 있는 지역변수이기 떄문에다.




>>> def sub():
	print(ss)


>>> ss="배"
>>> sub()
배




>>> def sub():
	print(s)
	s="바나나"
	print(s)


>>> sub()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    sub()
  File "<pyshell#4>", line 2, in sub
    print(s)
UnboundLocalError: local variable 's' referenced before assignment


>>> s="사과"
>>> s
'사과'


>>> sub()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sub()
  File "<pyshell#4>", line 2, in sub
    print(s)
UnboundLocalError: local variable 's' referenced before assignment


같은 함수에 지역변수와 전역변수를 같은 이름으로 하지 않는다.

함수내부에서 전역변수를 쓰기 위해서는 global 을 사용한다

>>> def sub():
	global s
	print(s)
	s="바나나"
	print(s)


>>> s="사과"
>>> sub()
사과
바나나

>>> print(s)
바나나


@주소확인 (list)

>>> sub(list)
>>> print(list)
[1, 2, 3, 4, 4, 5]
>>> def sub(mylist):
	mylist+=[4,5]
	print(id(mylist))

>>> aaa=[10,20]
>>> id(aaa)
2804912
>>> sub(aaa)
2804912
>>> aaa
[10, 20, 4, 5]

주소가 같다.


@주소확인(string)

>>> aaa=[10,20]
>>> id(aaa)
2804912
>>> sub(aaa)
2804912
>>> aaa
[10, 20, 4, 5]
>>>
>>>
>>>
>>> def myfunc(my):
	my+="123"
	print(id(my))


>>> aaa="hi good"
>>> id(aaa)
54260416
>>> myfunc(aaa)
54241824

주소가 다르다.




@모듈
>>> import math

>>> math.ceil(3.5)
4
>>> math.floor(3.5)
3
>>> math.ceil(-2.7)
-2
>>> math.floor(-2.7)
-3


@모듈만들기


def add(x,y):
    return x+y


def sub(x,y):
    return x-y

    print("연산 프로그랩입니다.")
    print("더하기와 빼기가 있슴")

    print("3더하기 4는" ,add(3,4))
    print("3뺴기 4는" ,sub(3,4))

연산 프로그랩입니다.
더하기와 빼기가 있슴
3더하기 4는 7
3뺴기 4는 -1

import mymath 하면 print 부분이 나온다. 이걸 안보게 하기 위해
if __name__=="__main__":
    이 부분을 넣는다.



def add(x,y):
    return x+y


def sub(x,y):
    return x-y

if __name__=="__main__":  // 이부분을 넣으면 import 할 때 다른 부분들이 안나온다.
    print("연산 프로그랩입니다.")
    print("더하기와 빼기가 있슴")

    print("3더하기 4는" ,add(3,4))
    print("3뺴기 4는" ,sub(3,4))


>>> import mymath



모듈(help)

import math
help(math)

file - >  class broowesr
해서 모듈이름을 검색하면 사용법을 알수있따 .




@사칙연산


def add(x,y):
    return x+y


def sub(x,y):
    return x-y

def div(x,y):
    return x/y

def mul(x,y):
    return x*y

if __name__=="__main__":
    print("연산 프로그랩입니다.")
    print("더하기와 빼기가 있슴")

    print("3더하기 4는" ,add(3,4))
    print("3뺴기 4는" ,sub(3,4))



@람다식

>>> aaa=lambda x,y:x+y
>>> aaa(3,4)
7


>>> L=[lambda x: x**2 , lambda x: x**3, lambda x: x**4]
>>> L[0]
<function <lambda> at 0x033A7E40>
>>> L[0](3)
9
>>> L[1](2)
8
>>> L[2](3)
81
>>>
>>> for x in L:
	print(x(3))


9
27
81
