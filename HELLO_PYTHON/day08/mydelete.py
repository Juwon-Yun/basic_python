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
    
    sql = """update emp set emp_name = '6',
            tel = '6',
            address = '6'
            where emp_id = '12' """
    
    result = curs.execute(sql)
    
    print(result)
finally:
    conn.commit()
    curs.close()    
    conn.close()
    
