## - code to create a new excel file
##from openpyxl import Workbook
##wb = Workbook()
##ws = wb.active
##ws['A1'] = 'Hello'
##wb.save('sample.xlsx')

##from openpyxl import load_workbook
##wb = load_workbook('sample.xlsx')
##ws = wb.active
##print(ws['A1'].value)

import pandas as pd
#import cx_Oracle
import os
from datetime import datetime
from sqlite3 import connect
conn = connect("student_db.db")
curr = conn.cursor()
curr.execute('CREATE TABLE IF NOT EXISTS students (Name TEXT, Marks NUMBER, Rank NUMBER)')
data = {
    'Name': ['David', 'Emily', 'Harry'],
    'Marks': [84, 63, 92],
    'Rank': [2, 3, 1]
}
df = pd.DataFrame(data)
print(df)
df.to_sql('students', conn, if_exists='replace')
curr.execute('''SELECT * FROM students''')
for record in curr.fetchall():
    print(record)
# commit the query
conn.commit()
lt = ['C:\data.xlsx' , 'C:\data1.xlsx', 'C:\data2.xlsx' ]
k = -1
#pt = 'C:\data.xlsx'
for i in lt:
    print("value of k is" , k)
    k = k + 1
    data = pd.read_excel(lt[k])
    print(data)
#con = cx_Oracle.connect('FINDATARPT/admed@FNRP1DEV')
#cursor = con.cursor()
#print(data)
#TODAY = datetime.now()
#DIR = os.path.dirname(os.path.abspath(__file__))
#print(TODAY)
#print(DIR)