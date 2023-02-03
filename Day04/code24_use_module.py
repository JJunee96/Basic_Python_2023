# 모듈사용
import math as m            # 클래스로 안된 모듈
import code22_person as p   # 우리가만든 클래스
from code23_car import Car

print(m.pi)


print(m.tan(0))
print(m.ceil(3.8)) # 올림 = ceil, 내림 = floor
print(2 ** 10)        # 제곱 (정수)
print(m.pow(2, 10)) # 제곱 (소수)

# 모듈은 무조건 클래스로 되어있는건 아님 
# 클래스로 되어있는건 아래처럼 생성자 지정

# 우리가 만든 모듈을 사용
me = p.Person('홍길순', 155, '여성')
print(me)

# 
mycar = Car()
print(mycar)