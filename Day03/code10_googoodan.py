# 구구단 프로그램
for x in range(2, 10):
    print(f'{x}단 시작 ======')
    for y in range(1, 10):
        print(f'{x} X {y} = {x*y:>2}',end =', ') # {x*y:>2} 두자리로 만들어서 오른쪽 정렬
    print() # for문 종료할때 써줘야하는 구문


