import pandas as pd

excel_file_path="cricketer_data.xlsx"
df = pd.read_excel(excel_file_path, 'Raw Data')
print("Welcome to Cricketer Detail Getter Applicaton")
cricketer_name = input("Enter Cricket Name: ")

cricketer_details=df.loc[df['Name'] == cricketer_name ]

if not cricketer_details.empty:
    print(cricketer_details)
else:
    print("Details not found. Please try another name.")
