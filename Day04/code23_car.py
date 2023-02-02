import os
import code
# 자동차 클래스
class Car:
    __number = '68서 6131'          # 이 변수를 함부로 수정불가하게 하려면 변수앞 __ 를 붙이면 됨   

    def get_number(self) -> str:
        return self.__number

    # 클래스 외부에선 변경X, 멤버함수로는 내부를 조작O
    def set_number(self, number):
        self.__number = number

    def __init__(self, number = '54라 9538') -> None:
        print('__init__')
        self.__number = number

    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls)     # 부모클래스(상속)

    def __str__(self) -> str:
        return f'차번호는 {self.__number}'

yourcar = Car('88호 3741')
print(yourcar)
yourcar.__number = '12라 1242'  # 외부에서는 멤버변수에 접근불가
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('22오 1231')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제차는 요, 아이오닉이고, 번호가 {mycar.get_number()}')

mycar.__number = '132거 8874'
print(mycar.get_number())

