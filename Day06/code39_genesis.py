# Car클래스를 상속한 제네시스 클래스
from code38_Car import Car

# Child Class
class Genesis(Car):
    def __init__(self, name, color, plate_number, product_year) -> None:
        super().__init__()

        self.__name = name
        self.__color = color
        self.__plate_number = plate_number
        self.__product_year = product_year
        print(f'{self.__name} 인스턴스 생성!') 


    def set_name(self, name):                       # 부모가 없음. 자식 클래스에서 새로 생성
        self.__name = name
    
    def get_name(self):                             # 부모 클래스 name 재정의
        return self.__name

    def run(self):                                  # 부모 클래스의 run 재정의
        return f'{self.__name}이(가) 달립니다.'     

    def stop(self): 
        return f'{self.__name}이(가) 멈춥니다.'

gv80 = Genesis('팔공이', 'black', '233오 1232', 2022)
# gv80.set_name('팔공이')
print(f'이차의 이름은 {gv80.get_name()}입니다.')
print(gv80.run())
print(gv80.stop())
