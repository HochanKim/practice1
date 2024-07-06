# import my_module    # 'my_module' 기능 가져오기

# print(my_module.greet("Alice")) # 출력 : Hello, Alice!
# print(my_module.add(3, 5))      # 출력 : 8
# print(my_module.PI)             # 출력 : 3.141592


# from my_module import greet, add, PI    # 'my_module'에서 특정 메소드만 가져오기

# print(greet("Alice")) # 출력 : Hello, Alice!
# print(add(7, 7))      # 출력 : 14
# print(PI)             # 출력 : 3.141592


import my_module as my    # 'my_module'의 별칭 붙이기

# 별칭으로 메소드를 호출
print(my.greet("Alice")) # 출력 : Hello, Alice!
print(my.add(15, 15))      # 출력 : 30
print(my.PI)             # 출력 : 3.141592
