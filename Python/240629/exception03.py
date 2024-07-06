# 주관적 예외처리
class MyCustomError (Exception) :
    pass

a = 10
b = 2
try :
    if b == 2 :
        # raise ValueError("2로 나눌수 없습니다.")
        raise MyCustomError("2로 나눌수 없습니다.")
except MyCustomError as e :
    print(e)
except ValueError as e :
    print(e)