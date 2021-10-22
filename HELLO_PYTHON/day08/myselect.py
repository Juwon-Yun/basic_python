import pymysql
#
# host = "127.0.0.1"
# port = "3305"
# db = "python"
# user = "root"
# password = "python"


conn = pymysql.connect(host="127.0.0.1", user="root", password="python", db="python",port=3305 , charset="utf8")

try:
    curs = conn.cursor()
    sql = "select * from emp"
    curs.execute(sql)
    
    #투플 작은배열 => ()
    rows = curs.fetchall()
    
    for row in rows:
        print(row)
finally:
    curs.close()
    conn.close()