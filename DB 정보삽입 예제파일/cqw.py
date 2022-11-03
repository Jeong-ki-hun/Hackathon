import psycopg2
import datetime
import time


con = psycopg2.connect(host='rosie.db.elephantsql.com',dbname="mkzljolf", user="mkzljolf", password="y8SJDcZX-NC4_i13HjH2CunYCnWMbNiC",port=5432)

cur = con.cursor()
# for i in range(100):
#     time.sleep(0.1)
#     now = datetime.datetime.now()

#     print(now)


for i in range(100,300):
    time.sleep(3)
    now = datetime.datetime.now()
    all = [i,now]
    sql = sql = "INSERT INTO ob_question (question_text, pub_date) VALUES(%s,%s)"
    cur.execute(sql, all)
    con.commit()