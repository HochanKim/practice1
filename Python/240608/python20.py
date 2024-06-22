# if    양수, 음수, 0을 구분하시오
# if문
print("시작")
a = int(input("정수 입력 >> "))
if a > 0 :
    print("양수")
if a == 0 :
    print("0이다")
if a < 0 :
    print("음수")

print("종료")
print()
# if-else문
if a > 0 :
    print("if else문 양수")
else :
    if a < 0 :
        print("if else문 음수")
    else :
        print("if else문 0과 같다")
print("종료")
print()
# elif문
if a > 0 :
    print("elif 양수")
elif a < 0 :
    print("elif 음수")
else :
    print("elif 0과 같다")
print("종료")
print()

# 반복문
# for문 : 회수가 명확할때, while문 : 회수가 명확하지 않을때
# for 요소 in 시퀀스 :  // 시퀀스 : 반복할 대상

# while문
count = 0   # 선언문
while count < 5 :   # 조건문
    print(count)
    count = count + 1   # 증감문