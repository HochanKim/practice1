# 상속
class Animal :
    def speak(self) :
        return "I make a sound"
    
my_animal = Animal()
print(my_animal.speak())

# speak, eat 기능있는 강아지 클래스
# class Dog :
#     def speak(self) :
#         return "I make a sound"
#     def eat(self) :
#         return "I am eating"

class Dog(Animal) :     # 클래스 'Animal'의 상속을 받은 클래스 'Dog'
    def eat(self) :
        return "I am eating"

my_dog = Dog()
print(my_dog.eat())
print(my_dog.speak())