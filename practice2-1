
# 모두의 연구소, 토요일 스터디 Jump to Python - 2nd, 발표 : Eunseon Jo
# with PyCharm5

# 4.5. 자료형_딕셔너리(Dictionary)
# 자료형(Data type)은 컴퓨터 과학과 프로그래밍 언어에서 정수, 실수 등 여러 종류의 데이터를 식별하는 분류체계입니다.
# 딕셔너리(Dictionary)는 단어 그대로 사전(형)을 만든다고 이해하면 됩니다.
# 같은말로 연관배열(Associative array, Hash) 라고도 불립니다.
# 즉, 자료구조의 하나로 문자열이 아닌 여러 개의 key값에 Data를 짝을 지어 자료를 저장하고, 그 key값으로 해당 배열의 Data값을 찾아 삽입하며, 접근하는 방법입니다.

# Key:Value(왼편의 값:오른편의 값)이며, 한 쌍으로 만드는 자료형입니다.
# 예를 들자면, key값은 'skating'이라면, value값은 '스케이팅'이 될 것입니다.
# 특징은 리스트나 튜플처럼 순차적(sequential)으로 해당 요소 값을 구하지 않고, key값을 통해 value값을 얻어낸다는 점입니다.
# 한마디로 정리하자면, 'skating'이란 단어의 뜻을 찾기 위해 사전의 내용을 순차적으로 모두 검색하는 것이 아닌 'skating'이라는 단어가 있는 곳만을 사전 펼치듯이 펼쳐보는 것입니다.

# 기본 딕셔너리형은 아래와 같습니다.
# {Key1:Value1, Key2:Value2, Key3:Value3 ...}
# 즉, key1,2,3...값과 value1,2,3...값 쌍들을 하나로 묶어주는 '{}'안에 각각의 요소는 key : value 형태로 이루어져 각각 쉼표(', ')로 구분되어 있습니다.

#  * 4.5.1 dic = {'key':'value'} 형 딕셔너리
#  실습1 : "딕셔너리형을 통해 본인 개인정보를 간단하게 직접 기입해서 프린트해봅니다"

dic = {'name':'EunseonJo', 'phone':'01063078282', 'birth': '0809'}
print(dic) # 완료: {'phone': '01000008282', 'birth': '0809', 'name': 'EunseonJo'}, '이름': '조은선', ...형태로 나타납니다.

#  * 4.5.2 a = {숫자 정수: '문자열'} 형 딕셔너리
#  실습2 : "아침 스터디 모임이 10시에 시작하는 의미에서 key 정수값을 10으로 하고,
#          value값은 좋은 아침의 의미로 'Good morning'이란 문자열을 사용해봐요 :D


a = {10: 'Good morning'}
print(a)

# 예제1) 리스트값

b = { 'b': [1,2,3]}
print("'완료: b는 value값에 리스트도 넣을 수 있는 1,2,3 입니다'", a)

# 4.5.3 '사람이름'과 '특기' 딕셔너리
# 위와같이 실습해본 것 외에 딕셔너리는 주로 어떤 것을 표현하는 데 자주 사용될까요?
# 위 dic에서 개인정보를 토대로 실습한 것과 같이 dic 2번째에서는 '사람이름'과 '특기'를 한 쌍으로 만드는 딕셔너리형입니다.
# 예제2)

dic2 = {"김연아":"피겨스케이팅", "박지성":"축구", "귀도":"파이썬", "피카소":"그림"}
print(dic2)

# 파이썬 딕셔너리에서는 위와 같이 한 쌍의 딕셔너리를 표현하는 방법은 간편합니다.
# 다만, 제대로 활용하기 위해서 더 배워볼까요~?

# 4.5.4 Key값을 이용하여 Value값 얻기
# 미국 유명 토크쇼 TBS 코난쇼(Conan Show) 진행자인 코난 오브리언이 한국팬인 '써니 리' 고등학생이 보낸 두 장의 편지를 받고, 한국에 내한하기로 결심했다는데요.
# 학생이 보낸 편지지는 수능 모의고사 답안지였으며, 그 답안지에 펜으로 'TEAM COCO'라고 글자가 마킹되었다고 합니다.
# 그런 의미에서 저는 온라인에서라도 100점 맞고 싶은 마음을 담아 제 닉네임으로 사용해서 grade에 100점을 부여했고요.
# '써니 리'학생의 경우, 모의고사 답안지 제출 대신 편지를 작성했다면, 점수는 0점이였을듯 하여 'sunny'에게는 0점을 부여했습니다.
# 실습3 : '본인이 원하는 점수'는 '본인 이름'을 기입하고, 기대하는 '기대 점수'에는 '본인 닉네임'을 기입해서 실습해봅니다.

grade = {'morin': 100, 'sunny': 0}
print(grade['morin'])

100
print(grade['sunny'])
0
# 4.5.5 딕셔너리 변수[key]값을 넣어 value값 얻어내기
# 자료형 4.3 리스트(List)나 4.4 튜플(Tuple)과 같이 문자열은 요소의 값들을 얻어내기 위해 인덱싱이나 슬라이싱이라는 기법을 사용했지만,
# 딕셔너리는 단 한가지의 방법만 있을 뿐입니다.
# 변수 key값을 이용해서 위 예제를 통해 다시 실습해봅니다.
# 딕셔너리를 만들때
# * 주의해야할 사항은 key는 고유한 값이므로 중복되는 값을 설정해 놓으면 하나를 제외한 나머지의 것들은 무시될 수 있다고 합니다.
# key값이 동일할 경우, value값은 다르더라도 중복되는 key의 값은 무시됩니다.
# 예를 들자면, a = {1:'a', 1:'b'} 일 경우에 print(a)를 한다면, 완료: {1: 'b'}만 나오고, 'a'가 사라지는 경우가 있으니 주의해야 합니다.
# 만약, 동일한 key가 존재한다면 어떤 key에 해당하는 value값을 불러야할지 딕셔너리에서는 알 수 없기 때문입니다.
# 그래서 앞으로는 .py 안에서 abc 알파벳 순으로 겹치지 않는 예제로 진행할 예정입니다.
# 예제3)
c = {1:'d', 2:'e'}
print(c[1])
print(c[2])


c = {1:'d', 2:'e'}
print(c[1])
print(c[2])

# c라는 변수에 {1:'d', 2:'e'}라는 딕셔너리를 대입하였습니다.
# 위의 예에서 보시는 바와 같이 c[1]은 'd'라는 값을 나타내줍니다.
# 다만, 여기에서c[1]이 의미하는 것은 위 리스트나 터플의 a[1]과는 다릅니다.
# 딕셔너리 변수에서 []안의 숫자 1은 몇번째 요소를 뜻하는 것이 아니라 key값에 해당되는 1을 나타냅니다.
# 딕셔너리에서는 리스트나 터플의 인덱싱 방법이 존재하지 않습니다.
# 따라서 c[1]은 딕셔너리 {1:'d', 2:'e'}에서 key값이 1인 것의 value인 'c'를 돌려주게 됩니다. 'e'역시 같습니다.

# 실습4 : 위 4.5.2 에서 했던 실습을 토대로 뒤에 추가로 key 정수값을 스터디가 끝나는 시간인 12시로 하고,
#        value값을 귀한 토요일 오전시간에 스터디하고있는 옆 사람에게 'You did a good job'이라고 이야기해보세요.
#        결국은 본인에게 들려주는 말과도 같으니까요 :D
g = {'10': 'Good morning', '12':'You did a good job'}
print(g)


# 4.5.6 key값과 value값을 뒤집어 놓은 딕셔너리 대입하기
# 예제4) 딕셔너리 중 4.5.5에서 했던 부분을 뒤집어서 대입해봐요.

c = {'d':1, 'e':2}
print(c['d'])
print(c['e'])

# 실습5 : 위에서했던 실습 딕셔너리 중 4.5.1 key값을 이용하여 개별 value값을 얻는 방법을 dic['key']값을 이용해봐요.

dic = {'name':'EunseonJo', 'phone':'01063078282', 'birth': '0809'}

print(dic['name']) # 완료: dic['이름']: 'EunseonJo'로 됩니다.
print(dic['phone'])
print(dic['birth'])

# 4.5.7 딕셔너리 쌍 추가하는 방법
# 딕셔너리 쌍을 추가하는 방법을 key값을 이용해 value를 불러왔던 것처럼 새로운 key값에 value값을 설정하면 바로 딕셔너리에 추가됩니다.
# 예제5) 딕셔너리 쌍 추가하기

c = {1:'d', 2:'e'}
c[3] = 'f'
print(c)
# 완료: {1: 'd', 2: 'e', 3: 'f'}

# 실습6 : 딕셔너리 쌍 추가하기 - 2 / 예제5 딕셔너리에 문자열 추가하는 방법

c['name'] = 'morin'
print(c)
# 완료: {1: 'd', 2: 'e', 3: 'f', 'name': 'morin'} / 위와같이 숫자 알파벳형 딕셔너리에 문자열 추가 가능합니다.

# 예제6) 딕셔너리 쌍 추가하기 - 3 / 리스트값 추가하는 방법
# * 주의사항은 Key값에는 리스트를 쓸 수 없습니다. 하지만, 튜플에서는 key값으로 사용 가능합니다.
# 딕셔너리에서 key값으로 구별 방법은 key가 변하는 값인지 변하지 않는 값인지에 달려 있습니다.
# 리스트를 key 고정값으로 사용한다면, 그 값이 변할 수 있기 때문에 리스트 key로 쓸 수 없습니다.
# ex) a = {[1,2,3] : 'hi'} TypeError
# Value값에는 변하는 값이든 변하지 않는 값이든 관계없이 아무 값이나 넣을 수 있습니다.
# 배열 순서대로, Hash : 단어 매칭, 항상 고정되는 내용, 집합, 배열 형태는 들어가도됨
# 숫자 : 배열과 헷갈릴 수 있어서 그런 부분이래요 :D
# 순서 뒤바뀜(순서 보장x) / => Class 에서 재 확인

c[4] = [1,2,3,4]
print(c)
# 완료: {'name': 'morin', 1: 'd', 2: 'e', 3: 'f', 4: [1, 2, 3, 4]}

# 4.5.8 딕셔너리 쌍 삭제하는 방법
# 실습7 : 딕셔너리 요소 삭제하기
del c[4]
print(c)

# 완료: {1: 'd', 2: 'e', 3: 'f', 'name': 'morin'} / 예제6 리스트값을 delete를 이용해 개별 지움

# 4.5.9 딕셔너리 관련 함수 내 Key값 리스트 만들기(keys)

# 딕셔너리를 자유자재로 사용하기 위해서는 딕셔너리가 자체적으로 가지고 있는 관련 함수들을 사용해보면 됩니다.
# 실습8 : h.keys()값 사용하기

h = {'name':'EunseonJo', 'phone':'01063078282', 'birth': '0809'}

print(h.keys()) # 완료: dict_keys(['birth', 'phone', 'name'])
# h.keys()는 딕셔너리 h의 key값 만을 모아서 dict_keys 객체로 보여줍니다.

# 예제7) h.values()값 사용하기
print(h.values())
# h.values()는 딕셔너리 h의 values값 만을 모아서 dict_values 객체로 보여줍니다.

# dict_keys 객체는 리스트를 사용하는 것과 차이가 없습니다.(* 리스트 고유의 메소드인 append, insert, pop, remove, sort 등의 메소드를 수행할 수 없습니다)

# 실습9 :
for h in h.keys():
    print(h)
# 완료: (각 한줄씩) name, birth, phone
# for 제어문은 반복 구간문입니다.
# h.keys() dic. key고정값을 앞으로 하나씩 추출하는 것입니다.
# 임시값을 가져온 것이며, 순서대로 임의로 넣은 것입니다.
# Tap 지정 엔터 또는 탭 자동 지정된 것과 같습니다.
# h값은 임시 변수값 나타내는 것이래요.

# 예제8) 리스트 list(j.keys())로 변환하기 / dict_keys 객체
# dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 됩니다.

j = {'name':'EunseonJo', 'phone':'01063078282', 'birth': '0809'}
print(list(j.keys()))
# 완료: ['name', 'phone', 'birth']
# 임시변수에서는 내부 리스트 뿌려줌 ()키값과 밸류값 자체 대괄호로 나옴, 자료구조형태는 ()괄호 형태로 알 수 있음.

# 예제9) Value리스트 만들기(values)
# Value값만을 얻고 싶을 때, a.values()처럼 values함수를 사용하면 됩니다.
# dict_values 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용하는 것과 동일하게 사용하면 됩니다.

k = {'name':'EunseonJo', 'phone':'01063078282', 'birth': '0809'}
print(k.values())
# 완료: dict_values(['EunseonJo', '01063078282', '0809'])

# 실습10 : Key, Value 쌍 얻기(items)

l = {'name':'EunseonJo', 'phone':'01063078282', 'birth': '0809'}
print(l.items())
# 완료: dict_items([('phone', '01063078282'), ('birth', '0809'), ('name', 'EunseonJo')])

# 예제10) Key, Value 쌍 모두 지우기(clear)

l.clear()
print(l)
# 완료: {}

# 실습11 : Key값으로 Value값 얻기(get)

m = {'name':'EunseonJo', 'phone':'01063078282', 'birth': '0809'}
print(m.get('name'))
print(m.get('birth'))
print(m.get('phone'))

# 완료: Value값
# get(x) 함수는 x라는 key에 대응하는 value값을 돌려줍니다.
# 주의할 점은 m['no-key']'존재하지 않는 키'값을 가져오려고 할 경우에 key error를 발생시키고, None을 리턴하는 차이가 있습니다.

# 예제11) 해당하는 값 없을 경우, 디폴트하기
# m값에 'food'라는 해당하는 값이 없다면, 디폴드 값인 'bar'를 리턴합니다.

print(m.get('food', 'bar'))

# 해당 key값이 있는지 조사하는 방법(in)
# 실습 12 : 'value' in a

n = {'name':'EunseonJo', 'phone':'01063078282', 'birth': '0809'}
print('name' in n) # 완료: True
print('food' in n) # 완료: False

# '' in n 문자열이 딕셔너리의 key값에 있으면 True, 없으면 False 완료값이 나온다.

# 응용 심화입니다.

# 심화1)
test={1:1, 2:[2,3,"how"], (3,"to"):"study", 4:{5:5}}
print(test) # 결과값은 {1: 1, 2: [2, 3, 'how'], 4: {5: 5}, (3, 'to'): 'study'}

# ex)left:1, center:0, right:2

# 심화2)
myDic={"left":1, "center":0, "right": 2}
print(myDic) # 결과값은 myDic{'right': 2, 'center': 0, 'left': 1}
# 위 출력 결과를 보면, 위와 아래의 입력한 순서가 다른 점을 확인할 수 있습니다.
# 파이썬 사전은 해쉬(hash)를 이용하는 것을 알 수 있습니다.
# 즉, 사전 dic 에 대해서 a라는 키(key)의 값이 b(value)를 지정합니다.

# 심화3)
dic_keys = (['color', 'animal', 'form']) # 방3개 키값, 이름을 dic_keys라는 리스트로 수정.
dic_value1 = (['brown', 'dog', 'heart']) # 튜플 list 2
dic_value2 = (['beige', 'cat', 'star']) #list 3
dic_value3 = (['white', 'bird', 'moon']) #list 3
# 출력결과 color : (yellow, blue) / animal : (cat, dog) / form(heart, star)
# 추후 VALUE값 배열로 개별 지정 가능해서 인덱스나 키값으로 가져갈 수 있습니다.
# 배열 순서가 아니면 딕셔너리 순서가 안되서 있는거 같아요 :D

dic = {} #새로운 사전 dic선언. / 2차 배열 형태 값 개별적으로 가져올 수 있음
for i in range(len(dic_keys)): #키 길이만큼 반복문을 돌면서
     dic[dic_keys[i]] = [dic_value1[i],dic_value2[i],dic_value3[i]] #dic사전에 키값과 나머지값들을 넣고
     print("{0} : ({1}, {2}, {3})".format(dic_keys[i],
     dic[dic_keys[i]][0],dic[dic_keys[i]][1],dic[dic_keys[i]][2])) #출력
# 결과값은
# color : (brown, beige, white)
# animal : (dog, cat, bird)
# form : (heart, star, moon)


# FOR문 IN 집합 RANGE 함수 10 넣었을 경우, 0-9 길이가 몇개있는지 알 수 있게끔
# 배열 형태를 다시 한 번 더 만듬


# 다음은 4.6 집합(Sets)으로 이동해주세요 :D
# practice4-6_.py
