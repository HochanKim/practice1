# if문 : 조건문을 가지고 여러 코드 블럭 중 하나의 코드 블럭 실행
# if, if else, elif
# 양수, 음수, 0인지 출력하는 프로그램

# if
a = 10
if a > 0 :
    print("변수 a는 양수")
if a == 0 :
    print("변수 a는 0")
if a < 0 : 
    print("변수 a는 음수")

# if else
if a > 0 :
    print("if else a는 양수")
else :
    if a == 0 :
        print("if else a는 0")
    
    else :
        print("if else a는 음수")

#elif
if a > 0 :
    print("else if a는 양수")
elif a == 0 :
    print("else if a는 0")
else :
    print("else if a는 0")

print()

# 성적 평균 총합 구하기
kor = 60
math = 70
eng = 80
sum = kor + math + eng
avg = sum / 3
print(f"국어는 {kor}, 수학은 {math}, 영어는 {eng}... 총합은 {sum}... 평균은 {avg}") # 파이선 문자 포맷(format)