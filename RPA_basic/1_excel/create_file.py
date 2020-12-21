from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "yongsheet"
wb.save("sample.xlsx")
wb.close()