# 함수
# 함수 정의
# 함수 만드는 방법 4가지
# 1. 파라미터O 리턴O
# 2. 파라미터O 리턴x
# 3. 파라미터X 리턴O
# 4. 파라미터X 리턴X

def add(x, y):     
    result = x + y
    return result

def sub(x, y):
    result = x - y
    print(result)

def mul(x, y):
    result = x * y
    print(result)

def div(x, y):
    result = x // y
    print(result)

def hello():
    print('Hello~!!!')

def hello2():
    msg = 'Hello, hello'
    return msg

# 함수호출
hello()
print(hello2())
print(add(1024, 5))
sub(1024, 1000)
mul(512, 2)
div(108, 10)