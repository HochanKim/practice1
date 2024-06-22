# 컴퓨터가 1~100 사이에 랜덤수를 생성해서 사용자가 맞추는 게임
import random
com_input = random.randint(1,100)  # 컴퓨터가 입력한 임의의 수
count = 0

while count < 10 :  # 10번 이하로 제한
    count = count + 1   # 1부터 10까지 회수 출력
    user_input = (int(input("입력회수 : "+ str(count) +"회, 1부터 100까지 생각한 수를 입력하세요 : ")))    # 사용자가 입력한 임의의 수
    if com_input == user_input :
        print("맞췄습니다. 축하합니다~!")
        break
    elif com_input > user_input :
        print("컴퓨터가 입력한 수보다 작습니다.")
        print()
    else :
        print("컴퓨터가 입력한 수보다 큽니다.")
        print()

print("컴퓨터 :",com_input,"사용자 :",user_input)
