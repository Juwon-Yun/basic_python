import pymysql
#
# host = "127.0.0.1"
# port = "3305"
# db = "python"
# user = "root"
# password = "python"


conn = pymysql.connect(host="127.0.0.1", user="root", password="python",
                        db="python",port=3305 , charset="utf8")

try:
    curs = conn.cursor()
    
    sql = """delete from emp where emp_id = %s """
    
    result = curs.execute(sql, ('11'))
    
    print(result)
finally:
    conn.commit()
    curs.close()    
    conn.close()
    
