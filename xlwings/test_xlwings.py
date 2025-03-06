import xlwings as xw

# Connect to active Excel
wb = xw.books.active

# Create a folder if it not exists
if wb is None:
    wb = xw.Book()

sheet = wb.sheets.active

sheet.range("B1").value = "Funcionando!"

