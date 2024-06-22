# 파이썬 시작코드
# 주석 추가
# 화면에 "hello world" 찍기
print("hello world")
print("Hochan Kim")
print(50)
print() # 값이 없으면 줄을 변경한다
print(1,2,3,4, "홍길동")


# 본인 이름찍기
# 주석
# 문자열조작

print('안녕')   # 문자열 표시할때, '' 또는 ""를 사용한다.
print("let's go")
# print('let's go') # 에러코드, 같은 따옴표는 한 번만 쓸 수 있다.

# 이스케이프 문자 - 특수문자 표시방법
# \" \' : 문법으로 사용되지 않고 문자 '' 나 ""로 사용됨
# print("그가 "let's go" 라고 말했다.")  
print("그가 \"let\'s go\" 라고 말했다.")
print()
# \n : newline 줄바꿈
print(" 그가\n \"let\'s go\" \n라고 말했다.") 
print()
# \t : tab사용
print(" 그가\n \"let\'s go\" \n라고 말\t했\t다.") 
print()
# \\ : 사선 하나 출력
print(" \\그가\n \"let\'s go\" \n라고 말\t했\t다.\\")
print("\\")
print("""
      안녕하세요
      안녕하세요
      안녕하세요
      안녕하세요""")
print("=================================")
# \ 사용 : 맨 위 줄바꿈 효과 사라짐
print("""\
      안녕하세요
      안녕하세요\
      안녕하세요
      안녕하세요""")