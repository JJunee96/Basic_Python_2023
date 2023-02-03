# 예외처리
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:                    # 예외오류 생길것 같은 부분에 지정
    x, y = input('두 수를 입력하세요 : ').split()
    x = int(x)
    y = int(y)
except Exception as e:  # 예외오류 발생시 처리되는 부분
    print(e)
    exit()          # 입력에서 예외 에러시 예외처리 후 진행시키면 안되므로 종료 시키기

# 원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지마세요')
#     exit()

print('계산 테스트')
try:
    print(div(x, y))                # 예외가 발생하면 비정상적종료가 발생 = 발생지점이후로 처리하지않고 끝내버림
# except ZeroDivisionError as e:    # 사용자가 필요로 할때만 지정해서 사용
#     print('0으로 나누면 안됩니다!')
except Exception as e:              # 예외 메세지를 띄우기 위한 작업, Exception은 제일 부모이기때문에 예외오류 처리메세지들중 가장 마지막에 작성해야함
    print(e)
finally:                            # 마지막에 무조건 실행!
    print('계산은 계속됩니다!!')    


print(add(x, y))
print(mul(x, y))

# 예외가 많으면 사용자가 신뢰하지 않음(사용하지않음)