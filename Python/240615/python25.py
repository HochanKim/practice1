import openpyxl
import openpyxl.workbook
wb = openpyxl.Workbook()
ws = wb.create_chartsheet('2030.01')

# 전체 시트 출력
print(wb.sheetnames)

# 시트 삭제
del wb['Sheet']

wb.save('두번째파일.xlsx')

# 엑셀 파일을 잘못 읽어오면 열어서 다시 저장하고 닫은 다음에 다시 시작