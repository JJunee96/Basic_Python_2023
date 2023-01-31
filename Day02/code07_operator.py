# 연산자
# 할당연산
# 2 = 1 (X)
val = 1

# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(10 * 10)
print(1024 / 2) # 소수나누기
print(1024 // 2) # 정수나누기 = 몫
print(6 // 3) 
print(6 % 3) # 나머지

# print(6 / 0) # 무한대는 오류! 컴퓨터는 무한대를 표현할 방법이 읎어요!
# print(6 // 0) # 같은 내용!!!

print(2 ** 10) # 제곱 표현

# 문자열연산
first = 'Hello'
second = 'World'
print(first + second)
print(first + ' ' + second) # 중간 공백 넣을시 표현
print(first, second) # 애는 개별로 나오는것임으로 다른 개념

print(first * 4)

# 문자열 길이 : len
print(len(first)) 
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
# print(first[5]) 5번은 없으므로 에러!

# 파이썬에서 인덱스 찾는 특이한 방법
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[0:4]+'년' +current[5:7]+ '월' +
current[8:10]+ '일' +
current[11:13]+ '시' +
current[14:16] + '분' + current[17:] + '초')

print(current[-19:-15])

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7 

print(que)

que.append(10)    # append 제일 뒤에 값 추가
print(que)

que.insert(3, 99) # insert(원하는위치, 변경값)
print(que)

que.remove(10)    # remove 원하는값 삭제
print(que)


# tup = (1, 2, 3, 4, 5)   이런거 안됨
# tup[1] = 9
# print(tup[1])

# 문자열 == 문자 리스트
title = 'Python'
print(title)

# title[0] = 'p'   문자열에서는 값 변경 불가!
print('p' + title[1:])

# 일반적인 문자형 리스트
text = ['p','y','t','h','o','n']
print(text)
text[0] = 'P'
print(text)

# 문자열 포맷팅
print("I'm so happy {0} you, {1}!!".format(2, 'Hey')) #{순서}  .format(순서에 맞게 넣을값)
# 최신식 문자열 포맷팅
preword = 2
sayHello = 'Hey'
print(f"I'm so happy {preword} you, {sayHello}!!") # f <- 포맷팅 하겠다는 표시, {} 안에 내용 바로 입력

pi = 3.141592
print(f'파이는 {pi} 입니다.')
print(f'파이는 {pi:0.2f} 입니다.') # {pi:0.2f} 소숫점 2자리까지 표현
print(f'파이는 {pi:10.3f} 입니다.') # {pi:10.3f} 정수 10자리와 소숫점 3자리까지 표현

# 문자열을 특정문자로 자르기
full_name = 'WonJune MG. Cho'
vals = full_name.split() # 기본은 공백
print(type(vals))
print(vals)

vals = full_name.split('.') # .으로 지정
print(vals)

print(full_name.replace('WonJune MG.', 'Ashely')) # replace : 원래있던 문자중 일부분 바꾸기

# 문자열 공백 없애기
hi = '         Hello~ Bye         '
print(hi.lstrip() + '|') # 왼쪽 공백 제거
print(hi.rstrip() + '|') # 오른쪽 공백 제거
print(hi.strip()  + '|')  # 양쪽 공백 제거

# 문자열에서 값을 찾기
print(full_name.index('G')) # 입력값에 해당하는 값 번호찾기
# print(full_name.index('Z'))  없는건 에러!

print(full_name.find('Z')) # index와 같은 값 번호 찾기, 없는 값은 -1로 표시됨

# 찾는 단어의 갯수
print(full_name.count('u'))

# 모든 단어를 대문자/소문자로 변경
print(full_name.upper()) # 대문자
print(full_name.lower()) # 소문자


# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)