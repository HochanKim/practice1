# 클래스 기본구조
# 키워드는 class를 사용한다.
# class 클래스이름 :
#       클래스와 관련된 코드 기술
#       pass

# 클래스 인스턴스화 하는 방법
#   인스턴스 변수 선언 = 클래스 이름()


# # 클래스 선언
# class Dog :
#     pass

# # 인스턴스화
# dog1 = Dog()
# dog2 = Dog()

# '초기화 메소드'에서 클래스가 가지고 있는 데이터를 초기화 한다. (생성자)
# '__init__'

# 클래스 선언 (클래스명 'Dog')
class Dog :
    # 초기화 메소드
    def __init__(self, name, age) :
        self.name = name
        self.age = age

# 인스턴스화
my_dog = Dog("happy", 5)
print("애완견 이름 : "+my_dog.name)
print("애완견 나이 : "+str(my_dog.age))

my_dog.name = "Lucky"
my_dog.age = 6
print("애완견 이름 : "+my_dog.name)
print("애완견 나이 : "+str(my_dog.age))
print()

your_dog = Dog("hello", 3)
print("애완견 이름 : "+your_dog.name)
print("애완견 나이 : "+str(your_dog.age))