import time
# 함수 
# 복잡한 코드가 반복적으로 사용될때, 함수를 이용해서 간단하게 사용할 수 있다.

# 함수는 선언부와 호출부가 있다. (ex. 선언부 => f(x) = 2x + 3 // 호출부 => f(2) = 7)
# 파이썬의 함수 키워드는 'def'

# 파이썬 함수 실행 코드
# def 함수이름(매개변수, ... )
#     실행코드
#     실행코드
#     [return 반환할 값]

# def 함수정의를 위한 키워드
# 함수이름 : 여러개의 함수를 구분하는 용도로 사용한다.
# 실행코드 : 함수가 호출되었을때 실질적으로 실행되는 코드
# 매개변수 : 함수가 실행될때 추가로 전달해야 하는 데이터
# return : 함수가 실행된 후에 반환되는 값 

def greet() : # 함수이름 = greet()
    # 함수로 저장한 실행코드
    print("안녕하세요")
    print("저는 홍길동입니다")
    print("만나서 반갑습니다")

greet() # 만든 함수 호출
print()

def greet(name, age) : # 함수이름 = greet(), (매개변수) = name, age
    # 함수로 저장한 실행코드
    print("안녕하세요")
    print(f"저는 {name}입니다")     # 실행코드 안에 매개변수 넣음
    print(f"나이는 {age}세 입니다")    # 실행코드 안에 매개변수 넣음
    print("만나서 반갑습니다")

# 함수 이름은 식별자라서 모두 달라야 하는데
# 함수 이름이 같아도 매개변수가 다르면 함수를 만들수 있다. (오버로드)

greet("홍길동", 25)    # 문자열 "홍길동"이 매개변수 'name'에 대입하고 출력함
print()
greet("김길동", 30)  # 문자열 "김길동", 정수 '30'이 각각 매개변수에 대입해서 출력
print()


def returnGreet(name) :
    greet = f"{name}님, 안녕하세요"
    return greet
get_value = returnGreet("홍길동")    # 매개변수에 "홍길동" 대입
print(get_value)
print()

# 두 수를 더해서 리턴하는 함수
def add(a, b) :
    sum = a + b
    return sum
print(add(4, 5))
result = add(6, 7)
print(result)
print()

# 두 수를 입력받아 큰 수를 리턴하는 함수
def max_value (a, b) :
    if a > b :
        return a
    if b > a :
        return b
print(max_value(17, 16))
print()


# 두 수를 입력받아 사이에 있는 수를 모두 더한 값을 리턴하는 함수
def sum_between(a, b) :
    # a와 b 중, 큰 수를 b에 넣는 작업
    if a > b :
        a, b = b, a
    sum = 0
    for i in range(a, b+1) :
        sum += i
    return sum
print(sum_between(1, 10))
print()

# 이름과 횟수를 입력받아 횟수만큼 이름을 출력하는 함수를 만들어보자
def print_name(name, number) :
    for i in range(number) :
        print(name)
    return(print_name)
print_name("홍길동", 10)
print()
print_name("홍철수", 5)
print()

# 두 숫자와 연산기호를 입력받아 연산결과를 생성해주는 함수를 만들어보자
# 풀이 버전
def calc(a, b, oper) :  
    if oper == "+" : 
        print(a+b)

    if oper == "-" : 
        print(a-b)

    if oper == "*" : 
        print(a*b)

    if oper == "/" : 
        print(a/b)
        
    return(calc)
calc(15, 3, "+")
calc(15, 3, "-")
calc(9, 9, "*")
calc(15, 3, "/")
print()

# 답변 버전
def calculator(num1, operator, num2) :
    return_value = 0    # 반환받을 값 생성 및 초기화

    if (operator == "+") :
        return_value = num1+num2
    elif (operator == "-") :
        return_value = num1-num2
    elif (operator == "*") :
        return_value = num1*num2
    elif (operator == "/") :
        return_value = num1/num2

    return return_value
print(calculator(15, "+", 15))
print(calculator(15, "-", 10))
print(calculator(15, "*", 8))
print(calculator(15, "/", 15))
print()

# 하나의 수를 입력받아 짝수인지 홀수인지 확인하는 함수를 만들어보자
def isEven (num) :
    if num % 2 == 0 :
        return True
    else :
        return False
if isEven(10) :
    print("\"짝수\"입니다.")
else :
    print("\"홀수\"입니다.")

time.sleep(5)