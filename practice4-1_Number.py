
# 모두의 연구소, 토요일 스터디 Jump to Python - Study 1st, Sangwoo Ji
# 자료형
# 숫자형 Number - 정수형 Integer

#-----------------------------------------------------------
#실제 사용되고 있는 부동 소수점 방식은 대부분 IEEE 754 표준을 따른다.
# 이 규격에서는 실수를 32비트로 처리하는 단정밀도(single precision)에서는
# 부호 1비트, 지수부 8비트, 가수부 23비트를 사용하며, 64비트로 처리하는
# 배정밀도(double precision)에서는 부호 1비트, 지수부 11비트, 가수부 52비트를 사용한다.
# 4배정도(quadruple precision)에서는
# 128비트로 부호 1비트, 지수부 15비트, 가수부 112비트를 사용한다.[4]
# https://ko.wikipedia.org/wiki/IEEE_754
# - IEEE 754는 전기 전자 기술자 협회(IEEE)에서 개발한 컴퓨터에서 부동소수점을 표현하는 가장 널리 쓰이는 표준이다.
# ±0 등의 수와 무한, NaN 등의 기호를 표시하는 법과 이러한 수에 대한 연산을 정의하고 있다.
#  가장 최신 버전인 IEEE 754-2008은 IEEE 754-1985와
   # IEEE 754-1997을 대부분 포함한다.
# 실수 계산의 정확성 : decimal — Decimal fixed point and floating point arithmetic
# The decimal module provides support for fast correctly-rounded decimal floating point arithmetic. It offers several advantages over the float datatype:

#-----------------------------------------------------------
from decimal import *
getcontext().prec = 6   # 소수점 6자리까지
Decimal(1) / Decimal(7)
Decimal('0.142857')  # 소수점 6자리까지 정확한 실수를 표시함

getcontext().prec = 28  # 소수점 28자리까지
Decimal(1) / Decimal(7)
Decimal('0.1428571428571428571428571429')  # 소수점 28자리까지 정확한 실수를 표시함

getcontext().prec = 7
k=Decimal(34) / Decimal(7)  # 4.857142857142857142857142857
print('print k=',k)

m=Decimal(0.3)+Decimal(0.1)+Decimal(0.1)  # decimal : 오류 발생함, Decimal 써야함.
print(m)  # 0.3000000000000000166533453694

getcontext().prec = 1     # 소수점 1자리 숫자 연산
p=Decimal(0.1)+Decimal(0.1)+Decimal(0.1)
print('소수점 1자리 숫자 연산',p)    # 0.3

getcontext().prec = 6     # 소수점 6자리 숫자 연산
q=Decimal(0.1)+Decimal(0.1)+Decimal(0.1)
print('소수점 6자리 숫자 연산',q)     # 0.300000

#-----------------------------------------------------------
# 숫자형 8진수(Octal)

a8 = 0o177   # 8진수를 만들기 위해서는 숫자가 0o 또는 0O(숫자 0 + 알파벳 o 또는 대문자 O)으로 시작하면 된다
b8 = 0o177

z8 = a8 + b8
print(z8)  # 254
print('숫자형 8진수(Octal) z8=',z8)  # 177 + 177, 254 (Decimal 표현됨), 원래값은 376

# 16진수(Hexadecimal) 16진수를 만들기 위해서는 숫자가 0x로 시작하면 된다.
a16 = 0x8ff
b16 = 0xABC
z16 = a16 + b16
print('숫자형 16진수(hex) z16=',z16)  # 5051, 13bb가 정확한 값인데..(5051 : 10진수 표현됨)

# 복소수 (Complex number)
ac1 = 1+2j
bc1 = 3-4J
zc1 = ac1 + bc1
print('숫자형 복소수 (Complex number) zc1=',zc1)  # zc1= (4-2j)
abs(zc1)
print('복소수 절대값', abs(zc1))

# 자료형
# 숫자형 Number - 정수형 Integer
a = 123
b = -1
c = a + b
print(c)
print('print(c)=',c)

# 숫자형 Number - 실수형 Floating-Point
d = 1.2
e = -3.14
f = d - e
print('print(f)=',f)

# 숫자형 Number - 실수형 Floating-Point 소수점 표현방식이다
g = 4.24E10
h = 4.24e-10
print('print(g)=',g,'print(h)=',h)

# 숫자형 Number - 정수형과 실수형의 차이점
i = 0.3+0.3+0.3
print(i)   # 0.8999999999999999

j = 0.1+0.1+0.1
print(j)  # 0.30000000000000004


# 숫자 연산

# 프로그래밍을 한번도 해 본적이 없는 독자라도 사칙연산(+, -, *, /)은 알고 있을 것이다.
# 파이썬 역시 계산기와 마찬가지로 아래의 연산자를 이용하여 사칙연산을 수행한다.

a = 3444
b = 3777
c = a + b
print('print(a)=',a)
print('print(b)=',b)
print('print(c=a+b)=',c)

d = 3
e = 3
f = d**e
print('print(f)=',f)

"""
dev
"""

#  % : 나머지 값을 반환하는 연산자이다.
#
#

j = 32
k = 3
i = j % k
print ('%:나머지 값을 반환하는 연산자',i)

l = 7
m = 4
n = l / m
print(n)  # / : 일반적인 나눈값

p = 7
q = 4
r = 7 // 4
print('print r=7 // 4 나누기값중 소수점 자리를 버리는 연산',r)  # 나누기값중 소수점 자리를 버리는 연산
