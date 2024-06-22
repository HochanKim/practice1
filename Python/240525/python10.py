import datetime

now = datetime.datetime.now()

if now.hour < 12 :
    print("현재시간은 {}시로 오전입니다.".format(now.hour))
    print(f"현재시간은 {now.hour}시로 오전입니다.")     # f => '.format'을 의미
if now.hour >= 12 :
    print("현재시간은 {}시로 오후입니다.".format(now.hour))
    print(f"현재시간은 {now.hour}시로 오후입니다.")     # f => '.format'을 의미
print()

number = int(input("숫자를 입력하세요 : "))
if number % 2 == 0 :
    print("짝수")
if number % 2 == 1 :
    print("홀수")
print()    

# 파이썬에서 if-else 구문 (조건문)
pick_number = int(input("당신이 생각한 숫자를 여기에 입력하세요 => "))

if pick_number % 2 == 0 :
    # 입력한 숫자가 짝수일 경우
    print("당신이 생각한 숫자는 짝수입니다.")
else : 
    # 입력한 숫자가 홀수일 경우
    print("당신이 생각한 숫자는 홀수입니다.")
print()

# elif 구문
# 세 가지 이상의 조건을 설정한 구문에서 사용된다.
now = datetime.datetime.now()   # 현재의 날짜/시간을 구하기
month = now.month   # 구한 값을 변수명 'month'에 저장한다.

# 조건문으로 계절을 확인합니다.
if 3 <= month <= 5 :
    print("현재는 봄입니다.")
elif 6 <= month <= 8 :
    print("현재는 여름입니다.") 
elif 9 <= month <= 11 :
    print("현재는 가을입니다.") 
else :
    print("현재는 겨울입니다.") 
print()