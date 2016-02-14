

# 모두의 연구소, 토요일 스터디 Jump to Python - Study 1st, Sangwoo Ji

#  튜플 (tuple)
# 리스트의 항목 값은 변화가 가능하고 튜플의 항목 값은 변화가 불가능하다.
# 튜플을 사용해야 할 것이다. 이와는 반대로 수시로 그 값을 변화시켜야 할 경우라면
# 리스트를 사용해야 한다.
# 실제 프로그램에서는 평균적으로 튜플보다는 리스트를 훨씬 많이 쓰게 된다.

t1 = (1, 2, 'a', 'b')

t1[0]
t1[3]
print("튜플 데이터 출력 t1 = (1, 2, 'a', 'b')")
print("튜플 데이터 출력", t1[0])
print("튜플 데이터 출력", t1[3])

t3 =t1*2
print(t3)  # t1 정보가 반복 2번되는 것

t5 =t1*4
print(' t1 정보가 반복 2번되는 것',t5)


abb = [1,2,3,7,8,8,10]
print(abb.index(3))
print(abb.index(7),abb.index(10))


ap=[1,2,3]
ap.pop()
print(ap)

ap.pop(1)
print(ap)


ac=[1,2,3,1,1,3,4,1]
ac.count(1)
print(ac)
print(ac.count(1))

aex=[1,2,3]
aex.extend([444, 5555, 5555,3838, 39328, 1, 1, 311 ])
print(aex)

sat= [890, 5555, 5555,3838, 39328, 1, 1, 311 ]

sun = aex + sat
print('sun=',sun)

sunta =  [1,2,sat]
print(sunta)


t1 = (1, 2, 'a', 'b')

t1[0]
t1[3]
print("튜플 데이터 출력 t1 = (1, 2, 'a', 'b')")
print("튜플 데이터 출력", t1[0])
print("튜플 데이터 출력", t1[3])

t2=(3,4)

t3=t1 + t2
print(t3)

t2=t1+t2
print('t2=',t2)

t2.extend[1]
print('x',t2)

del t2[5]
print('t22=',t2)
