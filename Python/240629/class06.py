class Animal :
    def __init__(self, name) :
        self.name = name
    def speak(self) :
        print(f"{self.name}가(이) 소리를 냅니다.")
    def info(self) :
        print(f"현재 객체는 {self.name}입니다.")

animal = Animal("백구")
animal.speak()
animal.info()
print(animal.speak())
print(animal.info())

class Dog(Animal) :
    def speak(self):
        print("멍 멍멍!")
    def eat(self, *args) :
        if(len(args) == 1) :
            print(f"{self.name}이 {args[0]}를 먹습니다.")
        if(len(args) == 2) :
            print(f"{self.name}이 {args[0]}와 {args[1]} 먹습니다.")

# 강아지 클래스는 기존 Animal이 가지고 있는 기능을 모두 가지고 있다.
# 추가적으로 변형되어 speak 메소드랑 새로운 eat 메소드를 가지고 있다.

my_dog = Dog("꽃잎")
my_dog.eat("뼈다귀")
my_dog.eat("뼈다귀", "사료")
my_dog.speak()  # 오버라이드
my_dog.info()