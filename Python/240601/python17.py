# 증감식
sum = 0
i = 5
while i < 30 :
    sum = sum + i
    print(sum, i)
    i = i + 1
print(sum)
print()

# continue, break
for i in range(10) :
    if i == 3 :
        continue    # '3'을 제외하고 10까지 수가 계속 출력
    print(i)
print()

for i in range(10) :
    if i == 7 :
        break       # '7'에 도달하면 while문 종료
    print(i)
print()

while True :
    name = input("이름입력, 종료를 원하면 quit 입력 : ")
    if name == 'quit' :
        break   # 'quit'를 입력하면 while문 종료
    print(name+"님 반갑습니다.")
print("이름입력 종료")
print()