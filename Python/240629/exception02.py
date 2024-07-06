def handle_exception() :
    try :
        num = int(input("숫자를 입력하세요 : "))
        result = 100 / num
        print(f"결과 : {result}")
        my_list = {1, 2, 3}
        index = int(input("리스트 인덱스를 입력하세요 (0-2) : "))
        print(f"리스트 요소 : {my_list[index]}")

    except ValueError as ve :
        print(f"유효한 숫자를 입력해야 합니다. : {ve}")

    except ZeroDivisionError as zde :
        print(f"0으로 나눌 수 없습니다. : {zde}")

    except IndexError as ie :
        print(f"리스트 인덱스가 잘못되었습니다 : {ie}")

    except Exception as e :
        print(f"알 수 없는 예외가 발생했습니다 : {e}")

    else :
        print("모든 연산이 성공적으로 수행되었습니다.")

    finally :
        print("예외 처리 종료")

# 함수 호출
handle_exception()
