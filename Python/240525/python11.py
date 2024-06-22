a = 7
b = 5
c = 9

if a < b :  # true이면 A가 작음
    if a < c :  # a가 가장 작음
        if b < c :  # a < b < c
            print(a, b, c)
        else :  # a < c < b
            print(a, c, b)
    else : # a<b, c<a, c<a<b // c가 가장 작음
        print(c, a, b)
else : # b<c, c<a, b<c<a // b가 가장 작음
    print(b, c, a)

print()

door_key = '108동 키'
door_num = 112

if door_key == '108동 키' or door_num == 111 :
    print("둘 중 하나만 맞으면 들어간다.")

if door_key == '108동 키' and door_num == 111 :
    print("둘 다 맞으면 들어간다.")

