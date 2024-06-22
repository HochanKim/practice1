# "안녕하세요"를 10번 출력하세요
for i in range(10) :
    print("안녕하세요")
print()

# 1~10까지 출력 , 출력한 순의 총합 출력
for i in range(1, 11) : # 1 이상 11 미만의 수 출력 -> 1 ~ 10
    print(i)
print()
sum = 0     # 더하고자 하는 값을 초기화
for x in range(1, 11) :
    sum = sum + x
print("1부터 10까지의 합 :",sum)
print()

# 4~20까지 출력 , 출력한 순의 총합 출력
for i in range(4, 21) : # 4 이상 21 미만의 수 출력 -> 4 ~ 20
    print(i)
print()
sum = 0
for i in range(0, 17) : # 0 이상 17 미만의 수 출력 -> 0 ~ 16
    sum = sum + (i + 4) # (i + 4) => 0+4 ~ 16+4 값이 반복적으로 대입
print("4부터 20까지의 합 :",sum)
print()

# 5~29까지 출력 , 출력한 순의 총합 출력
for i in range(5, 30) : # 5 이상 30 미만의 수 출력 -> 5 ~ 29
    print(i)
print()
sum = 0
for i in range(0, 25) : # 0 이상 25 미만의 수 출력 -> 0 ~ 24
    sum = sum + (i + 5) # (i + 5) => 0+5 ~ 24+5 값이 반복적으로 대입
print("5부터 29까지의 합 :",sum)
print()

# 4~15까지 수중 4부터 3씩 증가한 수 출력
for i in range(4, 16, 3) :  # 4부터 15까지 수에서 3씩 증가하는 수
    print(i)
print()

# “안녕하세요”를 10번 찍어 보자. 
count = 0
while count < 10 :
    count = count + 1
    print("안녕하세요")
print()

# 0~9까지 찍어보자.
count = -1
while count < 9 :
    count = count + 1
    print(count)
print()

# 3~10까지찍어 보자.
count = 2
while count < 10 :
    count = count + 1
    print(count)
print()

# 1~10의 합을 구해보자.
num = 0
sum = 0
while num < 10 :
    num = num + 1
    sum = sum + num
print(sum)
print()

# i=i+5 변환식을 사용해서 10~100사이의 i값을 출력해 보자.
for i in range(5, 96) : 
    i = i + 5
    print(i)
print()