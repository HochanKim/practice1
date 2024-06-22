import openpyxl
# openpyxl01.py
# 엑셀 조작하는 라이브러리 openpyxl
# pip install openpyxl

# 새로운 엑셀파일 생성
wb = openpyxl.Workbook()

# 현재 활성화된 시트 선택
ws = wb.active

# 시트 이름 바꾸기
ws.title = "자동화"

wb.save('첫번째파일.xlsx')
