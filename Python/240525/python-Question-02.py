# 입력한 숫자가 10보다 큰 수인지 아닌지 출력하는 코드를 만들어 보자.

number = int(input("숫자를 입력하시오 : "))

if number > 10 :
    print("이 수는 10보다 큽니다.")
else :
    print("이 수는 10보다 작거나 같습니다.")

print()

# 입력 받은 숫자가 양수인지 0인지 음수인지 판단하는 순서도와 프로그램을 만들어 보자.

number = int(input("자연수, 음수, 0 상관없이 당신이 생각한 숫자를 입력하시오 ===> "))

if number > 0 :
    print("당신이 입력한 수는 자연수(양수)입니다.")
elif number == 0 :
    print("당신이 입력한 수는 0입니다.")
else :
    print("당신이 입력한 수는 음수입니다.")

