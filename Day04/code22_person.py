# 클래스 생성
class Person:           # 클래스 이름만 지정이기 때문에 () 쓰지않음
    name = '익명'       # 속성변수가 곧 글로변변수
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가
    # def __init__(self):
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'X'

    def __init__(self, name = '홍길동', height = 170, gender = 'male') -> None: # 매개변수가 지역변수, 파라미터에 기본값 지정
        self.name = name
        self.height = height
        self.gender = gender 
        

    def walk(self):
        print(f'{self.name}걷습니다.')

    def run(self,option):
        if option == 'Fast':
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!')

    def stop(self):
        print(f'{self.name}멈춥니다.')

    # 2. 생성자외 매직메서드(펑션) __str__
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'

wonjune = Person() # 클래스에서 가져와 만든 객체를 instance, 함수와 같이 호출개념 그래서 () 사용 (객체생성)
# wonjune.name = '조원준'
# wonjune.height = '177'
# wonjune.gender = 'male'
# wonjune.blood_type = 'AB'

print(f'{wonjune.name}의 혈액형은 {wonjune.blood_type}입니다.')

wonjune.walk()
wonjune.run('Fast')

print(wonjune)

# 1. 초기화 후 객체생성
hong = Person()
hong.run('Slow')
print(hong)


print('==============================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리',164,'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)

print(ashely)