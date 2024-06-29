# 클래스
# 객체 형태의 개발을 위한 틀, 설계도 (파이썬은 객체 지향 언어)
# 객체 : 식별 가능한 모든것
# 인스턴스 : 클래스를 사용가능한 상태
# 클래스 : 관련있는 코드를 묶을때 사용
# 함수, 메소드는 비슷한 의미인데 객체 안에 있으면 메소드
# 객체와 관련없이 동작하면 함수


# # 사각형 둘레를 구하는 파이썬 프로그램을 함수로 구현해보자
# width = 10  # 너비
# height = 15 #  높이

# # 파이썬 함수 (사각형 둘레 공식)
# def cal_ractangle() :
#     global width
#     global height
#     return width*2 + height*2

# print(cal_ractangle())  # 사각형 둘레 출력
# print()


# # 새로운 사각형 계산
# width1 = 5  
# height1 = 10 
# def cal_ractangle1() :
#     global width1
#     global height1
#     return width1*2 + height1*2
# print(cal_ractangle())  # 사각형 둘레 출력
# print(cal_ractangle1())  # 사각형 둘레 출력
# print()

# # 새로운 사각형 계산
# width2 = 12 
# height2 = 16 
# def cal_ractangle2() :
#     global width2
#     global height2
#     return width2*2 + height2*2
# print(cal_ractangle())  # 사각형 둘레 출력
# print(cal_ractangle1())  # 사각형 둘레 출력
# print(cal_ractangle2())  # 사각형 둘레 출력


# 클래스 구현
class Rectangle : 
    def __init__(self) :
        self.width = 0
        self.height = 0
    def setdata(self, width, height) :
        self.width = width
        self.height = height
    def calculator(self) :
        result = self.width*2 + self.height*2
        return result

rect = Rectangle()  # 인스턴스화된 변수 rect
rect.setdata(5, 5)
print(rect.calculator())

rect = Rectangle()  # 인스턴스화된 변수 rect
rect.setdata(10, 15)
print(rect.calculator())