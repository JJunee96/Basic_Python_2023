# 함수
# 함수 정의
def add(x, y):     
    result = x + y
    return result  # 계산값을 result에 담은채로 호출한 곳으로 다시 점프

def sub(x, y):
    result = x - y
    return result

def mul(x, y):
    result = x * y
    return result

def div(x, y):
    result = x // y
    return result

# 함수호출
val = add(1024, 5) # 함수 정의한 곳으로 점프

# 출력
print(val)

val = sub(1024, 1000)
print(val)

val = mul(512, 2)
print(val)

val = div(108, 10)
print(val)