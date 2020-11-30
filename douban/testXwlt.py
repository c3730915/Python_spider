import xlwt
workbook = xlwt.Workbook(encoding="utf-8") #Create workbook object
worksheet = workbook.add_sheet("sheet1") #Create work sheet
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j)


