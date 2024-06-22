# 연산자
# 연산자 기호를 사용해서 특정 기능을 표현하는데 사용하는 기호 => '+', '-', '*', '/' 등

# 산술연산자
# +(덧셈), -(뺄셈), *(곱셈), /(나눗셈), //(나눗셈의 몫), %(나눗셈의 나머지), **(거듭제곱, 승수)
# -> 한 개씩 사용해서 출력해보자
print(10 + 3)   # 덧셈 연산 : 13
print(10 - 3)   # 뺄셈 연산 : 7
print(10 * 3)   # 곱셈 연산 : 30
print(10 / 3)   # 나눗셈 연산 : 3.33333 ~
print(10 // 3)  # 나눗셈의 몫 연산 : 3
print(10 % 3)   # 나눗셈의 나머지 연산 : 1
print(10 ** 3)  # 거듭제곱(승수) 연산 : 10의 3제곱 => 10*10*10 == 1000
print()

# 대입연산자 (할당연산자)
# =, +=, *=, %=, == 등
x = 5   # 변수 x에 5를 넣어라
x += 5  # x = x + 5 => 변수 x에 'x + 5'의 연산값을 넣어라
x %= 3  # x = x % 3 => 변수 x에 'x % 3'의 연산값을 넣어라

# 비교연산자
# 크다 ('a' > b), 작다 ('c' < b), 크거나 같다 (>=), 작거나 같다 (<=), 같다 (==), 같지 않다 (!=)
a = 10
b = 3
print(a > b)    # 크다 : True
print(a < b)    # 작다 : False
print(a >= b)   # 크거나 같다 : True
print(a <= b)   # 작거나 같다 : False
print(a == b)   # 같다 : False
print(a != b)   # 같지 않다 : True
print()

# 증감연산자 : 1 더하기 (++) or 1 빼기 (--)
x+=1
x-=1

# 논리연산자 : 두 개의 bool값을 가지고 하나의 결과를 얻을때 사용
# and, or, not // 진리표 참고
x = True
y = False

print(x and y)  # AND : False => 'and'는 둘 다 true일때 true, 나머지는 false
print(x or y)   # OR : True => 'or'는 둘 중 하나만 true이면 true, 둘 다 false일때는 false
print (not x)   # not : False => 부정, true이면 false, false이면 true
print()

# 삼항연산자 => true식 if 조건식 else false식
# (조건식)? true식 : false식 ;
a = 10
b = 20

max_value = a if a > b else b   # a가 b보다 크면 a, 그렇지 않으면 b => true식 : a / if 조건식 : a > b / else false식 : b
print(max_value)    # 결과 : 20