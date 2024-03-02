import pandas as pd ## default class for all data frame operations...
from sqlite3 import connect

conn = connect("student_db.db")
curr = conn.cursor()

table_name = ['jobsd','table1','table2','table3']
file_name = [r'C:\NonWAR\Names.xlsx','C:\data2.xlsx','C:\data2.xlsx']

#curr.execute('CREATE TABLE IF NOT EXISTS jobsd (JOBNAME TEXT)')
data = pd.read_excel(file_name[1])
#data.to_sql('jobsd', conn, if_exists='replace')
data.to_sql(table_name[0], conn, if_exists='replace')
curr.execute('''SELECT * FROM jobsd''')

for record in curr.fetchall():
    print(record)
conn.commit()
