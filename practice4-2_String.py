
# 모두의 연구소, 토요일 스터디 Jump to Python - Study 1st, Sangwoo Ji

# 문자열 만드는 방법 4가지

# 위의 예에서는 문자열을 만들 때 이중인용부호(")만을 사용했지만 이 외에도 문자열을 만드는 방법은 세 가지가 더 있다. 파이썬에서 문자열을 만드는 방법은 다음과 같이 네 가지로 구분된다.
#   "Hello World"
# 'Python is fun'
# """Life is too short, You need python"""
# '''Life is too shor, You need python'''

print("Python is favorite food is perl 이중 인용부호")  # " 이중부호 하면 모두 출력이 됨
print('Python is favorite food is perl 단일 인용부호') # ' 단일 인용부호

print("food = 'Python's favorite food is perl' ") # " 내부 ' 단일 인용부호는 이중 부호 이용 출력

print(' "Python is very easy." he says. 이중 인용부호는 단일 인용부호 이용') # 이중인용 부호는 단일 인용부호 이용

food = 'Python\'s favorite food is not perl 역슬래시 이용하는 방법'
say = "\"Python is very not easy.\" he says. 역슬래시 이용 2"
print(food)
print(say)

# 문자열 연산
zd = "python_Satuarday"
zc = zd * 2
print(zc)

# 문자열 인덱싱과 슬라이싱

a = "Life is too short, You need Python"
print (a[3]) # 인덱싱 기능
print ('Life is too short, You need Python 문자열 세번째 인덱스 기능', a[3])
# a[0]: 'L', a[1]: 'i', a[2]: 'f', a[3]: 'e', a[4]: ' ',....
# "파이썬은 0부터 숫자를 센다"
print (a[12], a[-1])

# 마지막의 a[-1]이 뜻하는 것은 뭘까?

bc = a[0] + a[1] + a[2] + a[3]
# 문자열에서 필요한 부분만 뽑아내서 만들어냄, 인덱싱
print('문자열에서 필요한 부분만 뽑아내서 만들어냄, 인덱싱', bc)

t4 = (3, 4)
t5 = (3, 6)
t6 = t4 + t5
print(t6)
