거듭제곱

def power(x,y):
	result=1
	for i in range(y):
		result = result *x
	return result

>>> power(5,7)
78125



소수인지 아닌지 판별

def is_prime(n):
	for i in range(2,n):
		if(n%i==0):
			return False
	return True




모든 소수출력


def is_prime1(n):
	for i in range(3,101):
		if is_prime(i):
			print(i)



랜덤 값 출력
            >>> import random
>>> random.radrange(2)

>>> random.randint(0,100)

randint 는 100 하면 100까지 나오고
첫시작 숫자와 끝 숫자를 입력해야 한다 .


radrange(2)
는 숫자 하나만 입력해도되고 끝 숫자는 안나온다.



mutable : tuple . list
변하는 값

immutable : string , 2 ,3 4, 등의 숫자
변하지 않는 값


>>> aaa=5
>>> id(aaa)
6584104
>>> aaa=6
>>> id(aaa)
6584092
>>> aaa=aaa+7
>>> aaa
13
>>> id(aaa)
6584008
>>> id(13)
6584008
>>> id(6)


주소값 같다  immutable : string , 2 ,3 4, 등의 숫자이기 떄문이다.


>>> bbb=[1,2,3,4]
>>> id(bbb)
48919336
>>> bbb[0]=10
>>> bbb
[10, 2, 3, 4]
>>> id(bbb)
48919336

mutable : tuple . list
변하는 값은
