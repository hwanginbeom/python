@짝수 더하기
sum = 0

for i in range ( 0 ,101 , 2):
    sum= sum+i


print(sum);


@공백 활용하기
>>> for x in "abcdef":
	print(x)


a
b
c
d
e
f
>>> for x in "abcdef":
	print(x, end = "")


abcdef
>>> for x in "abcdef":
	print(x, end = "/")


a/b/c/d/e/f/
>>>

@factorial

sum = 1
for i in range(10 ,0 , -1 ):
    sum=i*sum

print(sum)



sum = 1
for i in range(1 , 11 ):
    sum=i*sum

print(sum)


import math
math.factorial(10)



@함수만들기

>>> def myfact(n):
	fact=1
	for x in range(1,n+1):
		fact=fact*x
	return fact

>>> myfact(10)
3628800


@거북이로 그림그리기
import turtle

t=turtle.Turtle()
t.shape("turtle")
t.speed(0)

t.color("red")
angle=60
for x in range(0,6 ):
    t.forward(200)
    t.left(angle)



@원하는 각형 그리기

import turtle as t

n=int(input("몇 각형을 그리기를 원합니까?"))

for x in range(0,n):
    t.forward(100)    //길이
    t.left(360/n)     //각도


@거북이로 사각형 3개 20도 기울어서 그리기

import turtle as t

for j in range(100):
    t.left(20)
    for i in range(4):

        t.forward(100)
        t.left(90)
