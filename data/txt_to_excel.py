import pandas as pd

data = pd.read_csv('info.txt', error_bad_lines=False)
excel_data = data.to_excel('data.xlsx', sheet_name='data')
# print(data)
