# 다형성 : 일반 객체지향언어에서 부모를 이용해서 자식을 사용하는 의미

class Animal :
    def speak(self) :
        return "Animal"
    
class Dog(Animal) :
    def speak(self) :
        return "woof!"
    
class Cat(Animal) :
    def speak(self) :
        return "Meow!"

# 인스턴스 = 생성자
animal = Animal() 
dog = Dog()
cat = Cat()

animals = [animal, dog, cat]
for animal in animals :
    print(animal.speak())