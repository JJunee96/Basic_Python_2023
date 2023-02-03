# 파일 읽어오기
file = open('./day05/sample01.txt', 'r' , encoding= 'UTF-8')

while True:
    text = file.readline()

    if not text: break

    print(text)

file.close()        # 파일을 오픈하면 반드시 클로우즈를 해야합니다!!!! 
                    # 파이썬은 덜 엄격해서 안해도 가능하나 다른 그 어떤곳에서든 뭔갈 열었다면 닫아주는건 필수
                    