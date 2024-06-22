import openpyxl
import random

wb = openpyxl.Workbook()

ws = wb.active

ws.title = "data"

ws.append(['순번', '제품명', '가격', '수량', '합계'])

name_list = ['키보드', '마우스', '모니터', '마이크']

for i in range(random.randint(5, 10)) :
    print(i)    # 데이터 만들어서 넣기
    name = random.choice(name_list)
    print(name)

    if name == "키보드" :
        price = 12000
    elif name == "마우스" :
        price = 4000
    elif name == "모니터" :
        price = 30000
    elif name == "마이크" :
        price = 25000
    ws.append([i+1, name, price, random.randint(1, 5), f'=C{i+2}*D{i+2}'])

wb.save("C업체.xlsx")