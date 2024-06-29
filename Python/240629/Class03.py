# 클래스에서 인스턴스 필드
# 인스턴스 필드를 조작하는 함수, 인스턴스 메소드

# 파이썬 => 크롤링, 혼자 공부하는 머신러닝+딥러닝, 장고(Django), DB 

# 클래스 선언
class Dog :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def bark(self) :
        return f"{self.name} says woof!"
    
    def birthday(self) :
        self.age += 1
        return self.age
    
    def celebrate_birthday(self) :
        new_age = self.birthday()
        return f"{self.name} is now {new_age} year old"

# 인스턴스화
my_dog = Dog("happy", 10)
print(my_dog.bark())
print(my_dog.celebrate_birthday())