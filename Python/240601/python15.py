# 리스트(list) : 여러개의 값을 하나의 변수에 저장, 연속된 데이터 (파이썬에서 '배열(array)'의 역할, 파이썬에는 배열이 존재하지 않는다.)
# 리스트 생성 방법
my_list = []    # 다음줄에 my_list.append()를 사용할 수 있다.
# 한 줄에 my_list와 my_list.append()를 같이 사용시 에러

# 초기값을 가지고 리스트 생성
my_list = [1, 2, 3]
my_list = [1, 2, 3, 4, 5]   # 리스트 초기화는 되도록 처음에 한 번만 사용 권고

print(my_list)
print()

# 리스트 읽어오기
print(my_list[2])
print(my_list[-1])
print(my_list[0])
print(my_list[3])
print(my_list[-3])
print()

# 리스트 수정하기
# 3을 30으로 변경하기
my_list[2] = 30
my_list[3] = 40

print(my_list)
print()

# 리스트 추가하기
# append() : 리스트 마지막에 추가
my_list.append(6)
my_list.append(77)
my_list.append(8)
print(my_list)
print()

# insert(인덱스, 값) : 리스트에 데이터 
my_list.insert(0, 10)   # [10, 1, 2, 30, 40, 5, 6, 77, 8]
print(my_list)
print()

# extend() : 다른 리스트 추가
o_list = [6, 5, 4]
my_list.extend(o_list)
print(my_list)
print()

# remove(데이터) : list에 들어간 데이터를 삭제
my_list.remove(10)
print(my_list)
print()

# 같은 데이터가 들어 있으면 첫 번째 찾은 값을 1개만 삭제
my_list.remove(5)
print(my_list)  # [1, 2, 30, 40, '5', 6, 77, 8, 6, 5, 4] => 왼쪽에서 순서대로 읽다가 첫 번째 '5'를 제거 => [1, 2, 30, 40, 6, 77, 8, 6, 5, 4]
print()

# pop(인덱스)
returnValue = my_list.pop(1)    # 특정 인덱스의 요소를 제거
# returnValue = my_list.pop()    # 인덱스를 지정하지 않으면 마지막 데이터를 제거  
print(returnValue)              # 제거한 데이터를 리턴
print()

# clear() : 리스트 데이터를 모두 삭제
my_list.clear()
print(my_list)
print()

# 슬라이싱을 이용해서 데이터 추출
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:5])     # 2번째부터 5번째 미만(2번째부터 4번째까지) 데이터를 추출
print(my_list[:5])      # 0번째부터 5번째 미만(0번째부터 4번째까지) 데이터를 추출
print(my_list[3:])      # 3번째부터 끝번째까지 데이터를 추출
print(my_list[::-1])    # 기존 리스트의 데이터를 역순으로 출력
print()

# index(데이터) : 리스트 안에 있는 데이터의 인덱스를 리턴한다.
my_list = [10, 1, 2, 8, 9, 3]
my_index = my_list.index(3)
print(my_index)     # 리스트 안에 있는 '3'이 존재하는 인덱스 번호가 나온다 / 리스트에 해당 데이터가 없으면 error
print()

# count(데이터) : 특정 데이터의 개수를 출력
my_list = [10, 1, 2, 8, 9, 3, 10, 10, 9, 1, 1, 1, 1]

my_count = my_list.count(10)
print(my_count)

my_count = my_list.count(1)
print(my_count)

my_count = my_list.count(2)
print(my_count)

my_count = my_list.count(9)
print(my_count)
print()

# sort() : 해당 리스트 자체를 정렬해주는 기능
my_list.sort()
print(my_list)  # [1, 1, 1, 1, 1, 2, 3, 8, 9, 9, 10, 10, 10]
my_list.sort(reverse=True)
print(my_list)  # [10, 10, 10, 9, 9, 8, 3, 2, 1, 1, 1, 1, 1] => 'reverse=True'로 큰 수에서 작은 수로 정렬 (오름차순 정렬)
print()

# sorted : 새로운 정렬된 리스트를 반환합니다. 원본 리스트는 변경되지 않습니다.
sorted_list = sorted(my_list)
print(sorted_list)
print()

# 리스트 결합
list1 = [1,2,3]
list2 = [4,5,6]

add_list = list1 + list2
print(add_list)
