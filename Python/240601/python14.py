import random   # random 기능 가져오기

# 컴퓨터와 가위바위보 하기
# random.randint()    # 0=< x < 1 사이의 무작위의 실수 선별
# random.randint(0, 2)    # 0, 1, 2 중 무작위 선별
# 0 = 가위, 1 = 바위, 2 = 보
comInput = random.randint(0, 2)
userInput = input("가위, 바위, 보 중 하나 입력 : ")
# result = "무승부"   # 같은 수가 나올시 변수값 result에 "무승부" 대입 (디폴트값)
if comInput == 0 :
    comInput = "가위"
elif comInput == 1 :
    comInput = "바위"
else :
    comInput = "보"

# 승패 확인
if comInput == "가위" :
    if userInput == "바위" :
        result = "User 승"
    elif userInput == "보" :
        result = "컴퓨터 승"
    else :
        result = "무승부"

if comInput == "바위" :
    if userInput == "보" :
        result = "User 승"
    elif userInput == "가위" :
        result = "컴퓨터 승"
    else :
        result = "무승부"
        
if comInput == "보" :
    if userInput == "가위" :
        result = "User 승"
    elif userInput == "바위" :
        result = "컴퓨터 승"
    else :
        result = "무승부"

# 최종출력
print(f"컴퓨터 : {comInput} / User : {userInput} / 승패 : {result}")