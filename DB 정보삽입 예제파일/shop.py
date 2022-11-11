import psycopg2

index = [1, 2, 3, 4]
name = ['서울쭈꾸미', '어나더쭈꾸미', '레전드쭈꾸미', '하하쭈꾸미']
link = ['seoul', 'another', 'legend', 'haha']
text = ['서울에서 제일 맛있는 쭈꾸미집으로...', '서울에서 두번째로 맛있는 쭈꾸미 집으로...', '서울에서 세번째로 맛있는 쭈꾸미 집으로...', '가수 하하가 운영하는 쭈꾸미 집으로...']
status = ['혼잡', '주의', '여유', '여유']
image = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2PEmk8XMQeqxjL8STsmlRtgj_B8faavDiSQ&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQP7aADT-4ylAOZvA0MmckYogjGB2KXPcRO1Q&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxe8NPjwBIWJVdkW9iKp6oaWL3Duh2GZJQCA&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEzdkc1EWiAFJtVPqEL3ApgEbf54NL7hiFEA&usqp=CAU']

con = psycopg2.connect(host='rosie.db.elephantsql.com',dbname="mkzljolf", user="mkzljolf", password="y8SJDcZX-NC4_i13HjH2CunYCnWMbNiC",port=5432)

cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS shop_list")
cur.execute("""CREATE TABLE shop_list (
                id INT NOT NULL PRIMARY KEY,
                name VARCHAR(255),
                link VARCHAR(255),
                text VARCHAR(255),
                status VARCHAR(255),
                image_url VARCHAR(1000))""")
for i in range(len(index)):
    cur.execute("INSERT INTO shop_list (id, name, link, text, status, image_url) VALUES (%s, %s, %s, %s, %s, %s)", (index[i], name[i], link[i], text[i], status[i], image[i]))

con.commit()
cur.close()
con.close()