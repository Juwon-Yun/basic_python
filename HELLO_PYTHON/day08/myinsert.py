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
    
    sql = """insert into emp values(%s,%s,%s,%s)"""
    
    result = curs.execute(sql, ('12','12','12','12'))
    
    print(result)
finally:
    conn.commit()
    curs.close()    
    conn.close()
    
