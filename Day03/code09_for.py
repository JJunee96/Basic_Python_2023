# for문
arr = [1,2,3,4,5]
sum = 0

for i in arr:
    print(f'{i}')
    sum += i # sum = sum + i

print('합계는',sum)

# 리스트를 편하게 만드는 방법
vals = [i for i in range(1,11)]
print(vals)


# continue / break : 반복문 안에서만 사용 가능 (단독 if문 안에서는 사용 불가)
num = 0
for i in vals:
    num += 1
    if num % 2 == 0:
        continue # 이후의 것을 수행하지 않고 다시 for문으로 올라가는것
        # break # break를 만나면 for문을 완전히 탈출
    else:
        print(num,'번 수는 홀수', i, '입니다')


