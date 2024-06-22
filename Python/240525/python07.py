a = 5
b = 6
sum = a + b
print(sum)
a = 7   # 변수 a의 값 변경 : 5 -> 7
print(sum, a, b)
sum = a + b # 변경된 a의 값과 b의 덧셈연산
print(sum)
print()

int_a = int("10")
float_a = float("23.4")
str_int = str(10)
str_float = str(12.4)
print(int_a, float_a, str_int, str_float)
print(str_int + str_float)  # 문자열 덧셈 가능 => 문자열이 붙여서 출력 (1012.4 (O) / 22.4 (X))
# print(str_int + int_a)  # 파이썬은 문자열과 정수간의 덧셈이 불가능 => 에러로 출력 (TypeError: can only concatenate str (not "int") to str)