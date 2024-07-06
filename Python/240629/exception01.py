# 예외처리
# 프로그램에 문제가 발생했을때 종료되지 않고 프로그램을 계속 진행하기 위해서 사용한다.

# try :
#     result = 10/0
# except ZeroDivisionError :
#     print("0으로 나눌수 없다.")

# print("종료")

# 예외처리 문법
# try 블록 : 오류가 발생할 수 있는 코드를 포함
# except 블록 : try 블록에서 예외가 발생했을때 실행할 코드를 포함
# else 블록 : 예외가 발생하지 않았을때 실행할 코드
# finally 블록 : 항상 실행되는 코드

try :
    number = int(input("숫자를 입력하세요 : "))
    result = 100 / number
except ValueError :
    print("유효한 숫자를 입력해야 합니다.")
except ZeroDivisionError :
    print("0으로 나눌 수 없습니다.")
else :
    print("결과 :",result)
finally :
    print("자원 반납")

print("프로그램 종료")