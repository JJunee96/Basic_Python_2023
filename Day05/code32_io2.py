# 다중입력
# x, y = input('두 영단어를 입력하세요. : ').split(',')  # split() 공백을 자르기

# print(x)
# print(y)

# 완전 다중입력(갯수가 몇개든지 상관없음)
inputs = list(map(str, input('단어를 입력하세요 : ').split()))  # map은 리스트 형식으로 받아옴(?) 그래서 앞에 list 형식으로 바꿔주기
                                                                # map(자료형 형식, 함수)
print(inputs)

inputs = list(map(int, input('정수를 입력하세요 : ').split()))

print(inputs)