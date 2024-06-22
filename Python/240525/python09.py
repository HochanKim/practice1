print("if문 시작")
if True :
    print("True 입니다.")
    print("if문 안에 있음")
print("if문 종료")
print()

print("if문 시작")
if False :
    print("True 입니다.")   # False문으로 출력이 안됨
    print("if문 안에 있음")
print("if문 종료")
print()

# 사용자 입력을 받아서 양수, 음수, 0을 출력해보자
number = int(input("정수입력 > "))
if number > 0 : 
    print("양수 입니다.")
if number < 0 : 
    print("음수 입니다.")
if number == 0 : 
    print("0 입니다.")