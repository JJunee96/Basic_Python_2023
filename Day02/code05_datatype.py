# 자료형
# None 값이 없는 값
None
print(None)
print(0 == None)
print('' == None)

# 숫자형
val = 3
print(type(val)) # type() 변수의 자료형을 나타내주는 함수

val = 3.14
print(type(val)) 

val = 'Hello'
print(type(val)) 

val = 0b1010
print(type(val)) 

val = 12.23412352524324
print(type(val))

val = 4_520_000 #통화 단위 천당 구분자 '_' 사용가능(콘솔에는 표시 안됨)
print(val)

val = 3_099.99
print(val)

# 문자열
val = 'Life is short, You need Python'
print(val)
print(type(val))

val = 'Hello\nWorld!' # \ = 이스케이프 문자, 탈출시켜주는 문자 
print(val)
val = 'Hell\tWorld!'  
print(val) 
val = 'Hell\t\bWorld!'  # \n = 엔터 \t = 탭 \b = 백스페이스
print(val) 

val = '''Life is short,
You need Python'''     # 홑따옴표 3개씩 쓰면 문장으로 사용가능

print(val)

val = "Hi, I'm 'JJunee'"
print(val)
val = 'Hi, I\'m \'JJunee\''
print(val)

# 불린형 or 불형
참 = True
거짓 = False
print(type(거짓))

print(1 + 1 == 1)

# 거짓이라는 False 값 변수가 참인가?
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(2)) # 1이외의 값은 True라고 하지마세요!


