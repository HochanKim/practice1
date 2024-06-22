def greet(name, age) :
    return f"안녕, {name}. 당신은 {age}살 입니다."

result = greet("디지몬", 20)
print(result)

result = greet(name = "포켓몬", age = 21)
print(result)
print()

# 가변인자
def add(*args) :
    total = 0
    for num in args :
        total += num
    return total

result = add(1, 2, 3, 4, 5)
print(result)
result = add(3, 4, 5)
print(result)
print()

# 기본값을 가지는 매개변수 선언
def greet(name = "홍길동", age = 10) :
    return f"안녕, {name}. 당신은 {age}살 입니다."
result = greet()
print(result)

result = greet("누구")
print(result)
result = greet(age = 45)
print(result)
print()

# list의 내용을 출력하는 메소드
def my_list(data_list) :
    for i in data_list :
        print(i)

data1 = [1, 2, 3, 4]
my_list(data1)
print()

# 매개변수로 딕셔너리
# 딕셔너리 지정
info={
    'name' : 'Alice',
    'age' : 30
}
def greet(**kwargs) :   # **kwargs => 변수명 'kwargs' : 키워드 인자를 담는 딕셔너리를 의미 ('kwargs'는 keyword arguments의 약자)
    name = kwargs['name']
    age = kwargs['age']
    return f"안녕 {name}, 나이는 {age}"
result = greet(**info)
print(result)
print()

# .get
def greet(**kwargs) :   # **kwargs => 변수명 'kwargs' : 키워드 인자를 담는 딕셔너리를 의미 ('kwargs'는 keyword arguments의 약자)
    name = kwargs.get('name', '아무개')
    age = kwargs.get('age', 40)
    return f"안녕 {name}, 나이는 {age}"
result = greet(name = "홍길동", age = 40)
print(result)
print()

# 여러 개의 값 반환
def min_max(my_list) :
    return min(my_list), max(my_list)
print(min_max([6, 3, 2, 8, 4, 5]))  # (2, 8)
min_value, max_value = min_max({1, 2, 3, 4, 5})    # (1, 5)
print(min_value)
print(max_value)
print()

# list 반환
def equares(numbers) :
    return [n**2 for n in numbers]
result = equares({1,2,3})
print(result)

def person_info(name, age, city) :
    return {"name" : name, "age" : age, "city" : city}  # 딕셔너리 생성 및 반환
info = person_info("김호찬", 30, "인천")    # 반환한 딕셔너리에 list 대입
print(info)
print()

def make_fun() :
    def print_message(x) :
        print(x)
    return print_message
my_func = make_fun()

my_func("hello")