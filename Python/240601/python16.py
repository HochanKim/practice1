# 반복문 (list 이용방법)
my_list = [1, 2, 3]
for item in my_list :       # 리스트 변수 my_list 안에 있는 자료들을 item으로 대입 후 반복(for문 선언)
    my_item = item + 10     # 리스트 변수 내 자료들을 대입받은 변수 item을 10과 덧셈한 값을 반복 출력
    print(my_item)
print()

# 반복문 (range 이용방법)
for item in range(10) :     # 0 이상 10 미만의 수, 0부터 9까지 반복하는 범위 설정
    if item % 2 == 0 :
        print(f"{item}은 짝수이다.")
    else : 
        print(f"{item}은 홀수이다.")
print()

my_list = []
for item in range(5, 10) :   # 5 이상 10 미만의 수, 5부터 9까지 반복하는 범위 설정
    my_list.append(item)     # list의 끝에 수를 입력하는 반복
    print(my_list)
print()

my_list = []
for item in range(5, 16, 2) :   # 5 이상 10 미만의 수, 5부터 9까지 2씩 증가하는 수를 반복하는 범위 설정
    my_list.append(item)     # list의 끝에 수를 입력하는 반복
    print(my_list)
print()

new_list = [x+10 for x in my_list]
print(new_list)
print()

# zip() : 여러개의 배열을 묶어서 반복문을 실행
names = ["A", "B", "C"]
ages = [10, 20, 30]
for name, age in zip(names, ages) :
    print(name, age)
print()

# enumerate() : 인덱스랑 데이터를 가져옴
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits) :
    print(index, fruit)
print()

# 딕셔너리 : 키와 값으로 데이터를 저장
my_dic = {}
# 딕셔너리 초기화
my_dic = {
    "name" : "Alice",
    "age" : 30,
    "city" : "new york"
}

print(my_dic)
print()

# 키를 이용해서 값을 읽어오기
print(my_dic["name"])   # 딕셔너리에서 설정한 키 "name"을 불러옴
print(my_dic.get("age"))   # 딕셔너리에서 설정한 키 "age"를 get()으로 불러옴
print(my_dic.get("address"))   # 딕셔너리에서 설정한 키가 없으면 'None'으로 출력됨
print(my_dic.get("address", "invisible"))   # 'None' 대신 다른 값으로 설정해서 출력하는 방법
print()

# 딕셔너리 수정 방법
my_dic["name"] = "new Name"     # 이름 변경 (딕셔너리 키값 변경)
my_dic["email"] = "alice@gmail.com"     # 새 딕셔너리 추가
print(my_dic)
print()

# 딕셔너리 삭제 방법
del my_dic["email"]     # 설정한 키 "email"을 삭제
print(my_dic)
print()

# 딕셔너리 특정키 삭제 후 값 출력
age = my_dic.pop("age")    # 딕셔너리 키 'age'를 삭제
print(age)  # 삭제한 age값 '30'이 리턴
print(my_dic)
print()

# 딕셔너리 키 순회
for key in my_dic :
    print(key)
print()

# 키와 값
for key, value in my_dic.items() :
    print(key, value)   # ex. 'city'(key) 'new york'(value)

value = my_dic.values()
print(value)    # 딕셔너리 키에 대입된 값들을 출력

new_dic = {
    "age" : 22, "city" : "los angeles"
}
my_dic.update(new_dic)  
print(my_dic)