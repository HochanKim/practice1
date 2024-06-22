print('*', end = ' ')   # 엔터 없이 별
print(' ', end = ' ')   # 엔터 없이 공백 출력
print()     # 엔터사용
print('**', end = ' ')   # 엔터 없이 별
print(' ', end = ' ')   # 엔터 없이 공백 출력
print()     # 엔터사용
print('***', end = ' ')   # 엔터 없이 별
print(' ', end = ' ')   # 엔터 없이 공백 출력
print()     # 엔터사용
print('****', end = ' ')   # 엔터 없이 별
print(' ', end = ' ')   # 엔터 없이 공백 출력
print()     # 엔터사용
print('*****', end = ' ')   # 엔터 없이 별
print(' ', end = ' ')   # 엔터 없이 공백 출력
print()     # 엔터사용

print()

print('', end = ' ')   # 엔터 없이 별
print('*', end = ' ')   # 엔터 없이 별
print('*', end = ' ')   # 엔터 없이 별
print('*', end = ' ')   # 엔터 없이 별
print('', end = ' ')   # 엔터 없이 별
print()


print('*', end = ' ')   # 엔터 없이 별
print('*', end = ' ')   # 엔터 없이 별
print('*', end = ' ')   # 엔터 없이 별
print('*', end = ' ')   # 엔터 없이 별
print()

print()


# *를 가로로 출력
print('*', end = ' ')   
print('*', end = ' ')   
print('*', end = ' ')   
print('*', end = ' ')
print('*', end = ' ')
print()

count = 5
for i in range(count) :
    print('*', end = ' ')
print()

# *를 세로로 출력
print('*', end = ' ')
print()
print('*', end = ' ')
print()  
print('*', end = ' ')
print()  
print('*', end = ' ')
print()
print('*', end = ' ')
print()
print()

for i in range(count) :
    print('*', end = ' ')
print()
print()

for i in range(count) :
    for j in range(count-i-1) :
        print(' ', end = ' ')
    for j in range(i + 1) :
        print("*", end = ' ')
    print()