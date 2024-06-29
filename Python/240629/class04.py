# 클래스               : 관련있는 코드들을 묶어서 관리하는 프로그램
# 인스턴스 필드        : 인스턴스화 했을때 인스턴스의 데이터를 저장하는 공간 (클래스 안에 선언된 변수)
# 인스턴스 메소드      : 인스턴스 필드를 조작하는 함수
# 생성자              : 인스턴스 필드를 초기화하는데 사용
# 클래스 필드         : 인스턴스를 대표하는 데이터 
# 클래스 메소드       : 클래스 필드들을 조작하는 함수

class Rectangle :
    total_count = 0

    @staticmethod
    def class_info() :
        print("이 클래스는 사각형 관련 정보를 담는 클래스이다.")
    
    @classmethod
    def get_total_count(cls) :
        my_str=f"현재 total_count : ${cls.total_count}"
        return my_str

    total_count = 0
    def __init__(self, width, height) :
        Rectangle.total_count = Rectangle.total_count+1
        self.height = height
        self.width = width

    def print_info(self) : 
        print(self.width)
        print(self.height)
        print(Rectangle.total_count)
        
print(Rectangle.get_total_count())

# 클래스 메소드, 클래스 필드들을 조작할때
# 메소드에 @classmethod를 상단에 기술
# 매개변수로 cls 변수를 사용한다.

# 정적 메소드 호출
# 클래스 필드와 인스턴스 필드 모두 관련이 없는 메소드 제작시 사용
# 메소드 위에 @staticmethod를 기술

Rectangle.class_info()



# width1 = 5  
# height1 = 10 
# def cal_ractangle1() :
#     global width1
#     global height1
#     return width1*2 + height1*2

# # def print_total() : 
# #     print (total_count)

# print(cal_ractangle1())  # 사각형 둘레 출력
# print()

# width2 = 12 
# height2 = 16 
# def cal_ractangle2() :
#     global width2
#     global height2
#     return width2*2 + height2*2

# # def print_total() : 
# #     print (total_count)

# print(cal_ractangle1())  # 사각형 둘레 출력
# print(cal_ractangle2())  # 사각형 둘레 출력
# print()


# class Rectangle :
#     total_count = 0
#     def __init__(self, width, height) :
#         Rectangle.total_count = Rectangle.total_count+1
#         self.height = height
#         self.width = width

#     def print_info(self) : 
#         print(self.width)
#         print(self.height)
#         print(Rectangle.total_count)
#         print()

# rect1 = Rectangle(5, 4)
# rect2 = Rectangle(7, 10)
# rect1.print_info()
# rect2.print_info()
# print()

# Rectangle.total_count = 20
# rect1.height = 10
# rect2.height = 20
# rect1.print_info()
# rect2.print_info()




