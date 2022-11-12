import psycopg2
import csv
con = psycopg2.connect(host='rajje.db.elephantsql.com',dbname="onjiuvur", user="onjiuvur", password="9MDhITxF84TAukDM1_lqTc9y_Zko7wOx",port=5432)

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS Seoul_table(name VARCHAR(255), x VARCHAR(255),y VARCHAR(255))""")
con.commit()


f = open('/Users/jeong-gihun/Downloads/서울특별시 영등포구_식당기본정보_20220228.csv','r',encoding='cp949')
csvreadr = csv.reader(f)

print(csvreadr)

for row in csvreadr:
    insert = []
    #print(row[1],row[4],row[5])
    insert.append(row[1])
    insert.append(row[4])
    insert.append(row[5])
    #insert.extend([row[1],row[4],row[5]])
    print(insert)
    sql = "INSERT INTO Seoul_table (name, x, y) VALUES(%s,%s,%s)"
    cur.execute(sql,insert)
con.commit()
    






    